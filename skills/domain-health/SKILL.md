---
name: domain-health
description: When the user wants to check email deliverability posture, domain authentication, or sending reputation for a domain. Use when the user mentions "domain health," "inbox health," "deliverability," "SPF," "DKIM," "DMARC," "email authentication," "are my emails landing in spam," "can I send from this domain," "is my domain spoofable," "warm up a domain," "check this sending domain," "DMARC rollout," "p=quarantine," "p=reject," "blacklisted," or "email going to spam." Also use before starting cold outbound from any domain, and to score prospect domains for deliverability gaps worth opening a cold email with. For writing the outbound emails themselves, see cold-email. For building the prospect list, see clay-gtm-outbound.
metadata:
  version: 1.0.0
---

# Domain Health

Email authentication and deliverability posture for any domain, using only `dig` and the standard library. No API key, no paid tool, no per-check cost.

The same DNS primitives serve two opposite jobs, which is why they live in one skill:

**Defensive.** Audit a domain you own before you send from it, and before you tighten a DMARC policy. Getting this wrong silently sends your own invoices and password resets to spam.

**Offensive.** Score a prospect's domain to find a real, specific gap worth opening a cold email with.

## When to run it

Before starting outbound from any domain. Before changing a DMARC policy. When email is landing in spam and nobody knows why. When enriching a prospect list with a technical hook. After adding any new sending tool, because that is when sender inventory drifts.

## Modes

**Audit** (default) runs against domains you own.

```bash
python3 scripts/domain_health.py --domain example.com
python3 scripts/domain_health.py --domain example.com --json
python3 scripts/domain_health.py domains.txt
```

**Prospect** produces a CSV for list enrichment, with a `gap` column that is true when the domain's DMARC is missing or monitoring-only.

```bash
python3 scripts/domain_health.py --mode prospect domains.txt > signals.csv
```

**Blacklist** is opt-in via `--blacklist`. See the warning below before using it.

**Mailbox verification** is separate, in `scripts/verify_email.py`. It does MX plus an SMTP probe for a single address. Most networks block outbound port 25, in which case it returns `unknown` rather than guessing.

## What it checks

**MX**, establishing who receives mail for the domain.

**SPF**, including whether more than one record exists (which is a PermError and means SPF fails entirely), the qualifier the record ends in, and the count of DNS-lookup-triggering mechanisms against the limit of ten. Exceeding ten is a common and invisible failure.

**DKIM**, by sweeping a maintained list of per-provider selectors in `scripts/selectors.json`.

**DMARC**, covering policy, the separate subdomain policy, percentage, reporting addresses, and whether those reports go somewhere a human will actually read.

**Sender inventory**, which is the check that matters most and the reason this skill exists. It reads apex verification tokens and sending-subdomain CNAMEs to infer which providers are attached to the domain, then cross-checks each against SPF. This catches a provider verified two years ago, still able to send, never added to SPF, and invisible until the day the policy tightens.

**Maturity signals**, meaning MTA-STS, TLS-RPT and BIMI.

## Honesty constraints

These are load-bearing. Do not relax them, and do not let output phrasing drift past them.

**DKIM absence is never claimed.** Selectors are arbitrary strings and some providers use per-account random ones that cannot be guessed. A sweep that finds nothing means "no key on the selectors tried."

**Verification tokens prove a relationship, not sending.** A token proves the domain was verified with a provider at some point. Treat every inferred sender as a lead to confirm, never a fact. The tool separates mail-relevant signals from non-mail ones (site verification, custom web domains) precisely so the gap list stays worth reading.

**A prospect's primary domain is a proxy.** Teams running cold outbound properly send from a separate domain to protect the primary. Never state a finding about a prospect's primary domain as a confirmed claim about their outbound.

**Blacklist results describe the provider.** For any domain on hosted email, the MX addresses belong to the provider, so a listing reflects their shared infrastructure, not this domain's reputation. This is why the check is gated behind a flag and labelled in the output. Do not report it as the domain's own reputation.

## The DMARC rollout

Never raise a DMARC policy without first completing a sender inventory and reading real aggregate reports. The staged sequence, including how to make reports readable and what to fix before each step, is in `references/dmarc-rollout.md`.

The short version: make reports readable, wait and read them, fix every legitimate sender that is failing, then tighten policy one step at a time. The cost of waiting a month is zero. The cost of guessing wrong is business mail silently going to spam.

## Remediation

Per-provider fixes for each failure mode, covering the records to add and where to find them in each provider's dashboard, are in `references/remediation.md`.

## Turning gaps into outbound

How to convert a prospect's missing or monitoring-only DMARC into a specific, non-generic cold email opener, and the framing rules that keep it honest, are in `references/prospect-scoring.md`.

## Scoring

The audit returns a 0 to 100 readiness score weighted toward what actually blocks a rollout. Treat it as a triage signal for comparing domains, not a precise measurement. The numbered findings beneath it are the real output.

## Related skills

`cold-email` for writing the outbound itself. `clay-gtm-outbound` for building and enriching the prospect list. `seo-audit` for the equivalent audit on the web side.

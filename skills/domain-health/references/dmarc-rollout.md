# DMARC Rollout

Raising a DMARC policy is the only step in email authentication that can break working mail. Every other fix is additive. This one is subtractive: it tells receiving servers to start refusing mail that fails.

The failure mode is specific and nasty. Nothing breaks visibly. Invoices, password resets, and newsletters start landing in spam, and the sender has no signal that it happened.

## The sequence

### Step 1. Make the reports readable

Aggregate reports arrive as gzipped XML. Pointed at a normal mailbox, they are unreadable and in practice go unread, which is why so many domains sit at `p=none` for years.

Point `rua` at a report reader before anything else. Postmark DMARC Digests is free and emails a weekly plain-English summary. dmarcian, EasyDMARC and Valimail have free tiers.

Keep `p=none` during this step. It changes nothing about delivery and cannot break anything.

### Step 2. Read the reports for two to three weeks

This is the step that replaces guessing. The reports name every service sending as the domain and whether each passed SPF and DKIM.

A sender inventory built from DNS (which the audit does) tells you who is *attached* to the domain. Only the reports tell you who is *actually sending*. Both matter, and they answer different questions.

Do not shorten this window. Monthly billing runs, quarterly newsletters and annual renewal notices will not appear in a one-week sample.

### Step 3. Fix every legitimate sender that is failing

For each service in the reports that failed, add its SPF include and its DKIM records. Per-provider instructions are in `remediation.md`.

Watch the SPF lookup count while doing this. The limit is ten, and adding includes is exactly how domains cross it. Crossing it makes SPF fail for everything, which is worse than the problem being solved.

DMARC passes if **either** SPF or DKIM aligns. DKIM is the more robust of the two because it survives forwarding, which strips SPF alignment. A sender with working DKIM is safe even if SPF is imperfect.

### Step 4. Raise to quarantine

Move to `p=quarantine`. Set `sp=` explicitly to match, because the subdomain policy does not inherit from `p=` when `sp=` is present. A record with `p=quarantine; sp=none` leaves every subdomain wide open.

Use `pct=` to ramp if the domain sends high volume: start at `pct=25`, then 50, then 100, watching reports at each step.

### Step 5. Raise to reject

After two more clean weeks at quarantine, move to `p=reject`.

## Reading the record

`p=` is the policy for the domain itself: `none` monitors, `quarantine` sends failures to spam, `reject` refuses them outright.

`sp=` is the policy for subdomains. It does not inherit when explicitly set.

`pct=` is the share of failing mail the policy applies to.

`rua=` receives aggregate reports, which is the useful one. `ruf=` receives forensic reports, which contain message content, are widely unsupported, and carry privacy implications. Most domains should leave `ruf=` off.

`adkim=` and `aspf=` set alignment strictness, relaxed (`r`) or strict (`s`). Relaxed is the right default and allows subdomain alignment.

## What p=none actually means

It means nothing is enforced. Anyone can send mail claiming to be from the domain and receiving servers will deliver it, logging the failure afterwards.

This is worth stating plainly because `p=none` reads like a setting rather than an absence. A domain at `p=none` has DMARC configured and is not protected by it.

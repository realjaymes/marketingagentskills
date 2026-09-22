# Turning Deliverability Gaps into Outbound

A missing or monitoring-only DMARC record is one of the few technical observations that is genuinely specific, verifiable, free to obtain at scale, and relevant to someone whose job includes email.

That makes it a strong cold-email opener and an easy one to get wrong.

## Run it

```bash
python3 scripts/domain_health.py --mode prospect domains.txt > signals.csv
```

The `gap` column is true when DMARC is missing or monitoring-only. Those are the only two states worth opening on. A domain at quarantine or reject has already solved this and saying otherwise destroys credibility in one line.

## The framing rule

**A prospect's primary domain is a proxy, not a read on their outbound.** Teams running cold email properly send from a separate domain specifically to protect the primary. Finding `p=none` on the primary does not mean their outbound is broken. It means the primary is spoofable.

Write the observation as a baseline check, never a confirmed diagnosis. The difference between "your domain can be spoofed" and "your email is broken" is the difference between a credible opener and one that invites a correction.

## What makes it work

Specificity carries it. Naming the actual record state is verifiable in ten seconds and obviously not mail-merged, which is the bar a technical opener has to clear.

The failure mode is that it reads as a vulnerability disclosure from a stranger. Lead with the business consequence, which is that anyone can send mail as their brand, rather than with the acronym.

## What to avoid

Do not manufacture urgency around a condition that has existed for years without incident.

Do not imply a breach, an attack, or that anything has happened. Nothing has.

Do not send this to a security team as a finding. It is not a vulnerability report and will be treated poorly as one.

Do not use it on a domain already at quarantine or reject.

## Segmenting the list

Missing DMARC entirely suggests no one has looked, so the opener can be educational.

Monitoring-only suggests someone configured it and stalled, which is the more interesting segment: they already know what it is, and the useful message is about what blocked the rollout, which is almost always an incomplete sender inventory.

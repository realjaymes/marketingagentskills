# Measurement Example — Zapier

A complete measurement framework worked end to end for Zapier, following the Product Marketing Measurement Framework. Zapier is a no-code automation platform that connects thousands of apps through automated workflows called Zaps. It is product-led SaaS with a free tier and usage-based paid tiers priced on tasks, and its acquisition engine is famous programmatic SEO: a long-tail footprint of "connect App A and App B" pages that captures intent at the exact moment someone wants two tools to talk. The measurement system has to serve the whole self-serve motion, because the same SEO footprint and free tier that acquire users also seed the paid conversions, team plans, and expansion that pay the bills.

Numbers marked _illustrative_ are placeholders for James to replace with live figures. Widely known public facts (Zapier connects thousands of apps) are used with a light note; precise internal figures are not invented.

---

## 0. Foundations

### Business objective to PMM objective mapping

| Company objective | PMM objective | Example metric |
|---|---|---|
| Grow paid revenue | Convert free and task-limited accounts into paid with clear value at the task ceiling | Free-to-paid conversion, paid activation rate |
| Grow acquisition efficiently | Capture integration intent at scale through programmatic SEO and the app directory | Long-tail organic sessions, directory-to-signup rate |
| Expand within accounts | Move accounts from one Zap to many, and from solo to team and company plans | Zaps live per account, team plan adoption, task volume growth |
| Own the automation category | Position as the automation layer for the whole stack, not a set of point integrations | Aided recall, message playback vs Make, n8n, Power Automate |
| Retain paid accounts | Keep automations running reliably so the value never stops | Task success rate, recurring task runs, gross revenue retention |

### North Star

**Active accounts with at least one live Zap running (weekly).** Unique accounts that have a Zap turned on and successfully running tasks in the week.

Why this north star: it proxies delivered value (an automation is live and doing real work, not just a signup), it leads revenue on both sides (a running Zap is what drives task consumption toward the paid ceiling and what makes an account sticky enough to expand), and it is hard to inflate without creating genuine value because a Zap that runs is a Zap that saved someone manual work. A strong alternative north star is **tasks automated per active account**, which more directly tracks the usage that maps to task-based pricing. Active-accounts-with-a-live-Zap is the better single north star because it captures activation and retention in one number, while tasks-per-account becomes the primary expansion input hanging beneath it.

### Metric tree

```
Active accounts with 1+ live Zap running (weekly)
 ├─ Reach into intent ──── long-tail SEO sessions, app directory traffic, partner app referrals
 ├─ Activation depth ───── signup rate, first Zap turned on, first successful task run
 └─ Usage + expansion ──── tasks run per account, Zaps live per account, free-to-paid, team plans
```

### Guardrails

- Grow signup volume without letting the first-Zap activation rate fall (acquisition quality guardrail).
- Grow task volume without letting task success and reliability drop (automation trust guardrail).
- Push free-to-paid without over-gating the free tier so hard that first value never lands (activation integrity guardrail).
- Grow the long-tail page footprint without thin, low-intent pages that drag organic quality (SEO quality guardrail).

---

## 1. Funnel-Stage Metrics (filled)

### Awareness

- Long-tail programmatic SEO sessions across the "connect App A and App B" page footprint (Zapier connects thousands of apps, so this footprint is large): _illustrative_.
- App integrations directory traffic and internal navigation into app and category pages: _illustrative_.
- Partner app referral traffic (traffic Zapier receives from integrated apps listing it in their own directories): _illustrative_.
- Branded search volume and direct traffic for "Zapier": _illustrative_.

### Consideration

- Integration and template page engagement (did they view a specific Zap template or an app pairing?): _illustrative_.
- Template gallery browsing depth: _illustrative_.
- Pricing page visits and task-tier comparison: _illustrative_.
- Docs and help-center engagement pre-signup: _illustrative_.

### Conversion

- Directory or SEO landing page to signup rate: _illustrative_.
- Signup rate overall (visitor to account created): _illustrative_.
- Template-led signup rate (started from a specific Zap template): _illustrative_.
- Cost per acquisition on any paid support to the self-serve motion, judged on real activated accounts not raw signups: _illustrative_.

### Activation

For a new account, first value is a Zap created, turned on, and running its first successful task.

- First-Zap creation rate (accounts that build a Zap): _illustrative_.
- First-Zap turn-on rate (accounts that switch a Zap live): _illustrative_.
- First successful task run rate (a live Zap actually executes without error): _illustrative_.
- Time to first successful task run (signup to first task): _illustrative_. Vocabulary shared with product-onboarding-activation.

### Retention

- Recurring task runs per account over time (is the automation still firing week over week?): _illustrative_.
- Zaps live per account trend (are accounts keeping automations on?): _illustrative_.
- Task success and reliability rate (errored Zaps kill trust and retention): _illustrative_.
- Weekly active account retention curve by cohort (still running a Zap at week 4, 12, 24): _illustrative_.

### Expansion

- Task volume growth per account toward and past the tier ceiling: _illustrative_.
- Free-to-paid conversion rate: _illustrative_.
- More Zaps live per account and adoption of premium apps: _illustrative_.
- Team and company plan adoption (solo account to multi-seat): _illustrative_.

### Advocacy

- Templates published and shared by users into the public gallery: _illustrative_.
- Partner ecosystem growth (apps building and listing Zapier integrations): _illustrative_.
- Referral signups and word-of-mouth via self-report: _illustrative_.
- Reviews and community contribution (forum answers, shared Zap recipes): _illustrative_.

---

## 2. PMM-Outcome Metrics (filled)

### Positioning effectiveness

- Do buyers describe Zapier as "the automation layer for our stack" rather than "a tool that connects two apps"? Track message playback in reviews, sales calls, and community.
- Category association: Zapier filed as automation infrastructure, not a point-integration utility. Watch how prospects frame the comparison to native integrations.
- Segment conversion lift after a positioning or page change on the automation-layer narrative.

### Messaging resonance

- Landing page and pricing page message tests (conversion by variant on the automation-layer framing).
- Directory and template page copy tests at scale (small lifts compound across a huge page footprint).
- Which value framings (save time, remove manual work, connect your whole stack) show up in reviews and won deals.

### Launch performance

- Per new-product launch (Tables, Interfaces, Canvas, AI features): scorecard across awareness, activation into the new surface, adoption against the eligible base, and revenue or plan impact.
- Adoption velocity: days from launch to a target number of accounts using the new capability.
- Time to first value for the new surface (e.g., first Table populated, first Interface published, first AI step run).

### Sales enablement adoption

- For team and company plans where sales assists, are positioning and battle-card assets driving conversion on calls?
- Content usage rate among reps and deal influence on won multi-seat deals.

### Competitive win rate

- Head-to-head win rate against Make, n8n, Workato, and Microsoft Power Automate.
- Displacement rate against native integrations (the "we already have built-in connectors" objection) and self-hosted open-source (n8n).
- Loss reasons tagged and trended (price at task volume, developer control, breadth of app catalog, reliability).

### Pricing and packaging

- Task-tier mix and how accounts distribute across task ceilings.
- Attach rate on premium apps and premium features.
- Free-to-paid conversion by tier and the task-ceiling trigger points that convert.
- Discount depth on annual and team plans versus realized price.

### Content and demand influence

- Sourced: which SEO landing page, app pairing, or template was first touch for an activated account.
- Influenced: content and directory pages touched on the path to paid.
- Self-reported: "how did you hear about us" on paid upgrade and sales calls, to catch word-of-mouth the trackers miss.

---

## 3. Leading vs Lagging Map (Zapier)

| PMM lever | Leading indicators | Lagging outcomes |
|---|---|---|
| Positioning | Message playback, aided recall vs named competitors | Category association, segment paid conversion |
| Messaging | Landing, pricing, and template page test lift | Signup rate, free-to-paid conversion |
| Launch | Launch-week activation into the new surface | New-surface adoption, plan revenue impact |
| Lifecycle | First-Zap activation rate, time to first task run | Weekly active retention, gross revenue retention |
| Expansion | Task volume growth, Zaps live per account | Free-to-paid, team plan revenue, NRR |
| Competitive | Battle-card usage, loss-reason trend | Head-to-head win rate, displacement rate |

---

## 4. Attribution and Influence (Zapier)

- **Sourced.** Track first-touch SEO landing page, app pairing page, or template for each activated account. The programmatic-SEO footprint is the single largest first-touch surface, so clean first-touch capture on those pages matters most.
- **Influenced.** Much of the self-serve journey is influence-heavy: a user lands on a long-tail integration page, signs up free, activates one Zap, and only converts to paid weeks later when task volume hits the ceiling. Last-click will credit the pricing page or the upgrade prompt and miss the SEO page and the free-tier value that did the real work.
- **Self-reported.** Lean on "how did you hear about us" on upgrade and sales flows to catch word-of-mouth, recommendations inside teams, and partner-app discovery that trackers cannot fully see.
- **Portfolio halo.** This is central for Zapier. Judge the programmatic-SEO page footprint and the free tier at the portfolio level, not per page or per free account. Most individual long-tail pages and most free accounts do not convert directly, but together they build the activated base that seeds every paid conversion, team plan, and expansion. Do not kill a low-direct-return SEO cohort or free-tier surface on its isolated conversion alone. It feeds the pipeline that closes elsewhere.

---

## 5. Measurement Plan (Zapier, filled register)

| Metric | Definition / formula | Stage or outcome | Type | Data source & tool | Cadence | Owner | Baseline | Target |
|---|---|---|---|---|---|---|---|---|
| Active accounts with 1+ live Zap | Unique accounts running a Zap successfully / week | North star | NS | Product analytics | Weekly | PMM + Growth | _illustrative_ | _illustrative_ |
| Long-tail organic sessions | Sessions to the app-pairing SEO footprint | Awareness | Input | GA4 + Search Console | Weekly | PMM + SEO | _illustrative_ | _illustrative_ |
| Directory-to-signup rate | Signups / directory + SEO page visitors | Conversion | Input / leading | GA4 + product analytics | Weekly | PMM + Growth | _illustrative_ | _illustrative_ |
| First-Zap activation rate | Accounts with a live Zap running / signups | Activation | Leading | Product analytics | Weekly | PMM + Growth | _illustrative_ | _illustrative_ |
| Time to first successful task run | Signup to first task executed | Activation | Leading | Product analytics | Weekly | Growth | _illustrative_ | Reduce |
| Tasks run per active account | Total tasks / active accounts | Expansion | Input | Product analytics | Monthly | Growth | _illustrative_ | _illustrative_ |
| Free-to-paid conversion rate | Paid conversions / eligible free accounts | Expansion | Lagging | Billing + product analytics | Monthly | PMM + Growth | _illustrative_ | _illustrative_ |
| Team plan adoption | Accounts moving to multi-seat plans | Expansion | Lagging | Billing | Monthly | PMM | _illustrative_ | _illustrative_ |
| Task success rate | Successful task runs / attempted runs | Retention | Guardrail | Product analytics | Weekly | Growth + Eng | _illustrative_ | Hold high |
| Gross revenue retention | Retained revenue excl. expansion | Retention | Lagging | Billing | Quarterly | PMM | _illustrative_ | _illustrative_ |
| SEO page quality (thin-page share) | Low-intent / total published long-tail pages | Awareness | Guardrail | Search Console + audit | Monthly | SEO | _illustrative_ | Cap |

Type values: NS (north star), input, leading, lagging, guardrail.

### Reporting rituals

- **Weekly pulse:** active accounts with a live Zap, first-Zap activation rate, task success rate, directory-to-signup rate, any live launch's leading indicators.
- **Monthly review:** free-to-paid conversion, tasks per account, team plan adoption, full register against target.
- **Launch retro:** per new product (Tables, Interfaces, Canvas, AI features), 2 to 4 weeks after launch, the launch scorecard, adoption velocity, and time to first value on the new surface.
- **Quarterly review:** gross and net revenue retention, competitive win rate, the SEO and free-tier influence story told at portfolio level.

### Executive translation

| Zapier metric | Business language |
|---|---|
| Active accounts with a live Zap | The base actually getting value, which is what converts, retains, and expands |
| First-Zap activation rate | More new accounts reaching value, so lower early drop-off and more paid conversions downstream |
| Free-to-paid conversion | Revenue efficiency on the base the free tier and SEO built |
| Tasks per account and team plans | Compounding usage-based revenue without new acquisition cost |
| Long-tail organic sessions | Acquisition at near-zero marginal cost that feeds the entire funnel |

---

## 6. Anti-patterns to avoid (Zapier)

- Reporting signups as success while first-Zap activation quietly falls. An account with no live Zap is not a customer, it is a lead.
- Crediting the pricing page or upgrade prompt for a conversion the SEO page and free tier warmed for weeks.
- Killing a low-direct-return SEO cohort or the free tier on isolated conversion, starving the base that seeds paid.
- Chasing raw task volume while task success and reliability erode, breaking the automation trust that drives retention.
- Publishing thin long-tail pages at scale that inflate the footprint but drag organic quality and intent.

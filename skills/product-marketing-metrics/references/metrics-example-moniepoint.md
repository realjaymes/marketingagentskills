# Measurement Example — Moniepoint

A complete measurement framework worked end to end for Moniepoint, following the Product Marketing Measurement Framework. Moniepoint is a Nigerian business banking and payments platform built on the merchant. The business runs on two behaviors that reinforce each other: acquiring a merchant (KYC plus first terminal or account) and then keeping that merchant transacting at volume, month after month. Revenue follows from payment processing fees, terminal economics, business banking, and increasingly credit. The measurement system has to hold both behaviors together, because a merchant who onboards but never transacts is a cost, and a merchant who transacts reliably is the compounding asset every other product line is sold into.

Numbers marked _illustrative_ are placeholders for internal figures I cannot verify from public surfaces. Widely reported public facts are marked _(known/public)_ and held loosely, since scale claims move over time and PMM should not build targets on a press number.

---

## 0. Foundations

### Business objective to PMM objective mapping

| Company objective | PMM objective | Example metric |
|---|---|---|
| Grow processing revenue | Convert acquired merchants into reliable, high-volume transactors | Activated merchant rate, transaction volume per active merchant |
| Expand the merchant base | Position "it just works" reliability to win merchants from agents and competitors | Merchant acquisition rate, competitive win share |
| Grow banking and credit revenue | Move transacting merchants into accounts, credit, and larger terminals | Product attach rate, credit uptake among active merchants |
| Defend against reliability doubt | Own uptime and settlement certainty in the merchant's mind | Message playback on reliability, downtime-driven churn |

### North Star

**Monthly Active Transacting Merchants (MATM).** Unique merchants who processed at least one qualifying transaction in the month across POS, transfer, or account activity.

Why this north star: it proxies delivered value (a merchant only transacts if the platform actually moved money for them), it leads every revenue line (processing fees, banking, and credit all sit on top of transacting merchants, not registered ones), and it is hard to inflate without creating real value, since a dormant registration adds nothing to it. Total payment volume is the natural companion metric and belongs one level down in the tree, because volume without a growing base of active merchants is a concentration risk, not durable growth. Track MATM as the north star and total payment volume from active merchants as its primary output.

### Metric tree

```
Monthly Active Transacting Merchants (MATM)
 ├─ Reach + acquisition ── field-agent coverage, referral signups, brand demand
 ├─ Activation ────────── KYC completion, first-terminal/account, first transaction
 └─ Sustained volume ──── transactions per merchant, uptime, settlement reliability
        └─ output: total payment volume from active merchants
```

### Guardrails

- Grow merchant acquisition without letting the activation rate fall (acquiring merchants who never transact is negative unit economics).
- Grow transaction volume without letting settlement reliability or dispute rate slip (reliability is the whole positioning, so a volume push that degrades uptime is a global loss).
- Grow credit uptake without letting default rate climb past the underwriting line (a credit-attach win that seeds bad debt is not a win).

---

## 1. Funnel-Stage Metrics (filled)

### Awareness

- Merchant-facing reach: field-agent territory coverage and businesses reached per agent per period: _illustrative_.
- Brand demand among merchants: branded search, direct app installs, inbound agent applications: _illustrative_.
- Scale as proof point: Moniepoint powers millions of businesses and processes a very large monthly transaction volume _(known/public, held loosely)_. This is a positioning asset, not a target.
- Share of voice against OPay, PalmPay, and traditional banks in merchant conversation: _illustrative_.

### Consideration

- Agent-led demo to signup intent rate (merchant expresses interest after a field visit): _illustrative_.
- App downloads and account-open starts from awareness: _illustrative_.
- Referral link and word-of-mouth signups initiated: _illustrative_.
- Return touchpoints before signup (a merchant comparing terminals): _illustrative_.

### Conversion

For Moniepoint, conversion is the merchant committing: starting KYC and requesting a terminal or opening a business account.

- Signup start to KYC submission rate: _illustrative_.
- KYC submission to terminal or account approval rate: _illustrative_.
- Cost per acquired merchant, split by field-agent and referral channels: _illustrative_.
- Approval turnaround time, since delay here is where committed merchants leak: _illustrative_.

### Activation

First value for a merchant is the first successful transaction, money actually moved on their terminal or account. KYC and approval are cost until that first transaction lands.

- Activation rate: approved merchants who complete a first transaction within a set window: _illustrative_.
- Time to first transaction (approval to first successful payment): _illustrative_.
- First-week transaction count, the early signal that a merchant will stick: _illustrative_.

Vocabulary shared with product-onboarding-activation: activation rate, time to value, aha moment. The aha moment here is the first settled payment, when the merchant sees money hit their account reliably.

### Retention

- Transaction frequency: transactions per active merchant per week or month: _illustrative_.
- Transaction volume per active merchant, and the trend over cohort age: _illustrative_.
- Uptime and settlement reliability as experienced by merchants (successful transaction rate, settlement-on-time rate): _illustrative_. This is the retention lever that positioning is built on.
- Cohort retention curve: merchants still transacting at month 3, 6, 12: _illustrative_.
- Dormancy rate: previously active merchants who went silent, and the reason where known (device fault, competitor switch, business closed): _illustrative_.

### Expansion

- Product attach: active merchants who open a business account, take credit, or upgrade to more or larger terminals: _illustrative_.
- Credit uptake among active merchants and repeat-borrow rate: _illustrative_.
- Volume growth within a merchant over time (a growing business processing more): _illustrative_.
- Revenue per active merchant across processing, banking, and credit combined: _illustrative_.

### Advocacy

- Agent referral: existing merchants who recruit other merchants, and merchants who become agents: _illustrative_.
- Word-of-mouth signups captured via self-report ("a friend referred me"): _illustrative_.
- Merchant reviews and ratings on app stores and in market: _illustrative_.
- Net promoter or satisfaction signal among active merchants: _illustrative_.

---

## 2. PMM-Outcome Metrics (filled)

### Positioning effectiveness

- Do merchants describe Moniepoint as the terminal that "just works" and settles reliably, unprompted? Track this language in agent call reports, support conversations, reviews, and win/loss notes.
- Category association: Moniepoint filed as the dependable business banking and payments partner for merchants, not one more POS among many. Reliability is the wedge against OPay and PalmPay, and the modernity wedge against traditional banks.

### Messaging resonance

- Field-agent script and pitch A/B: which reliability and economics framings move merchants to sign, measured by signup rate per script variant: _illustrative_.
- App store and landing message tests for self-serve account opens: _illustrative_.
- Which value framings (uptime, settlement speed, low downtime, fee clarity) show up in merchant testimonials and reviews: _illustrative_.

### Launch performance

- Per new-product launch (consumer app, credit, larger-terminal tier): scorecard across merchant awareness, eligible-base attach, activation, and revenue: _illustrative_.
- Adoption velocity: days from launch to a target number of active users of the new product: _illustrative_.
- Time to first value for the new capability (first loan drawn, first consumer transaction): _illustrative_.

### Sales enablement adoption

- For the field-agent force, are the positioning and objection-handling materials driving higher signup and activation rates per agent?
- Agent ramp: time for a new agent to reach a target of activated merchants, using the enablement kit: _illustrative_.
- Battle-card usage in competitive merchant conversations and its correlation with wins: _illustrative_.

### Competitive win rate

- Win share against OPay and PalmPay at the agent and merchant layer, against Paystack and Flutterwave at the online payments and business-account layer, and against traditional banks at the account and credit layer.
- Loss reasons tagged and trended: fees, device reliability, settlement speed, credit terms, brand trust, agent relationship.
- Displacement: merchants switched from a named competitor's terminal to Moniepoint, and the reason.

### Pricing and packaging

- Fee structure clarity and its effect on conversion (do merchants understand what they pay?).
- Terminal tier mix and the shift over time as merchants scale.
- Attach and effective revenue per merchant across processing, banking, and credit.
- Discount or fee-waiver depth used to win merchants versus realized economics.

### Content and demand influence

- Sourced: which channel (field agent, referral, brand, app store) was first touch for each acquired merchant.
- Influenced: touches on the path to a merchant's first transaction.
- Self-reported: "how did you hear about us" captured at signup or by the agent, essential here because most acquisition is field and word-of-mouth driven and will not show up in digital trackers.

---

## 3. Leading vs Lagging Map (Moniepoint)

| PMM lever | Leading indicators | Lagging outcomes |
|---|---|---|
| Positioning | Reliability message playback, category association in merchant talk | Competitive win share, downtime-driven churn |
| Messaging | Agent-script and app-message test lift | Signup rate, activation rate |
| Launch | Launch-window attach and activation of new product | Product revenue, retention of new adopters |
| Lifecycle | Activation rate, time to first transaction | Transaction volume per merchant, net revenue retention |
| Competitive | Battle-card usage, loss-reason trend | Head-to-head win share, displacement rate |
| Advocacy | Referral signups initiated, merchant reviews | Referral-sourced merchant retention, organic acquisition share |

---

## 4. Attribution and Influence (Moniepoint)

- **Sourced.** Track the first channel per acquired merchant: field agent, referral, brand demand, or self-serve app install. Field-agent and referral will dominate, so the source field has to be captured at signup by the agent, not inferred from a click.
- **Influenced.** Merchant acquisition is relationship-heavy. A merchant may hear about Moniepoint from another merchant, see agents around the market for weeks, and only sign when one visits their shop. Last-click will credit the final agent visit and miss the referral and ambient brand presence that did the real warming.
- **Self-reported.** Lean hard on "how did you hear about us," captured verbally by the agent at signup. This is the only way to see the word-of-mouth and market-ambient demand that no tracker can observe, and it is the primary attribution instrument for a field-led model.
- **Portfolio halo.** Judge brand and top-of-funnel merchant demand at the portfolio level. Brand presence and the agent network rarely convert a merchant on their own the day they are seen, but they lower the cost and raise the activation rate of every merchant the field force closes later. Do not judge a brand or ambient-demand surface on its direct, same-day conversion alone, and do not judge a low-margin entry product only on its direct return when it seeds the account and credit revenue that closes on top of it.

---

## 5. Measurement Plan (Moniepoint, filled register)

| Metric | Definition / formula | Stage or outcome | Type | Data source & tool | Cadence | Owner | Baseline | Target |
|---|---|---|---|---|---|---|---|---|
| Monthly Active Transacting Merchants | Unique merchants with 1+ qualifying transaction / month | North star | NS | Transaction ledger + product analytics | Monthly | PMM + Growth | _illustrative_ | _illustrative_ |
| Total payment volume from active merchants | Sum of processed value from MATM cohort | Retention output | Lagging | Transaction ledger | Monthly | Finance + PMM | _illustrative_ | _illustrative_ |
| Merchant acquisition rate | New approved merchants / period | Conversion | Input | CRM + onboarding | Weekly | Field ops + PMM | _illustrative_ | _illustrative_ |
| Activation rate | Approved merchants with first transaction in window / approved | Activation | Leading | Onboarding + ledger | Weekly | PMM + Growth | _illustrative_ | _illustrative_ |
| Time to first transaction | Approval to first successful payment | Activation | Leading | Onboarding + ledger | Weekly | Growth | _illustrative_ | Reduce |
| Transactions per active merchant | Transactions / MATM | Retention | Leading | Product analytics | Monthly | Growth | _illustrative_ | _illustrative_ |
| Settlement reliability | On-time settlements / total settlements | Retention | Leading | Payments infra | Weekly | Product + PMM | _illustrative_ | Hold high |
| Product attach rate | Active merchants using account or credit / active merchants | Expansion | Lagging | CRM + product | Quarterly | PMM | _illustrative_ | _illustrative_ |
| Credit uptake | Active merchants who drew credit / eligible active merchants | Expansion | Lagging | Credit product | Quarterly | PMM + Credit | _illustrative_ | _illustrative_ |
| Referral-sourced signups | Signups tagged referral or word-of-mouth | Advocacy | Input | Onboarding self-report | Monthly | PMM | _illustrative_ | _illustrative_ |
| Dormancy rate | Previously active merchants now silent / active | Guardrail | Guardrail | Product analytics | Monthly | Growth | _illustrative_ | Below floor |
| Credit default rate | Defaulted loans / loans issued | Guardrail | Guardrail | Credit product | Monthly | Credit + Risk | _illustrative_ | Cap |

Type values: NS (north star), input, leading, lagging, guardrail.

### Reporting rituals

- **Weekly pulse:** merchant acquisition, activation rate, time to first transaction, settlement reliability, and any live launch's leading indicators.
- **Monthly review:** MATM, total payment volume from active merchants, transactions per active merchant, dormancy, full register against target.
- **Launch retro:** per new product (credit, consumer app, terminal tier), 2 to 4 weeks after launch, the launch scorecard, eligible-base attach, and time to first value.
- **Quarterly review:** product attach, credit uptake, revenue per active merchant, competitive win share, the influence story told at portfolio level.

### Executive translation

| Moniepoint metric | Business language |
|---|---|
| MATM | The base of merchants actually moving money, which is what every revenue line is sold on top of |
| Total payment volume from active merchants | Processing revenue base and the raw material for banking and credit |
| Activation rate | Share of acquisition cost that becomes a paying relationship instead of a dormant registration |
| Settlement reliability | The reason merchants stay, expressed as the metric that most predicts churn |
| Product attach and credit uptake | Compounding revenue per merchant without new acquisition cost |

---

## 6. Anti-patterns to avoid (Moniepoint)

- Reporting registered or acquired merchants as success while the activation rate quietly falls. A merchant who never transacts is a cost, not a customer.
- Chasing acquisition volume in territories where agents cannot support activation, inflating the base while dragging transactions per merchant down.
- Crediting the final agent visit for a merchant the referral network and ambient brand presence warmed for weeks.
- Pushing transaction volume or launch numbers in a way that degrades settlement reliability, since reliability is the entire positioning and its loss is a global loss.
- Growing credit attach on the headline number while default rate climbs past the underwriting line.

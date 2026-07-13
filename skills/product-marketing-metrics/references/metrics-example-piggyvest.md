# Measurement Example — PiggyVest

A complete measurement framework worked end to end for PiggyVest, following the Product Marketing Measurement Framework. PiggyVest is Nigeria's leading consumer savings and investment app. Users automate savings across Piggybank, SafeLock, Flex, and Target Savings, and invest through Investify. Revenue comes largely from the spread on invested funds and interest margins, so the business only compounds when money actually sits in accounts and keeps growing. The measurement system has to track two behaviors above all else: funding an account and keeping a recurring auto-save alive, because those two are what convert a signup into a revenue-generating balance.

Trust is the gate on everything. Nigerian consumers hand a fintech their savings only when they believe the license, the security, and the track record are real, so the measurement system treats trust as a first-class input, not a soft brand metric. The naira macro backdrop of inflation and spending indiscipline shapes the emotional driver: PiggyVest sells the discipline to stop spending money anyhow and watch a balance grow.

Numbers marked _illustrative_ are placeholders for James to replace with live internal figures. Known figures are broad public facts (for example, PiggyVest's multi-million user base) used lightly, never invented precise internals.

---

## 0. Foundations

### Business objective to PMM objective mapping

| Company objective | PMM objective | Example metric |
|---|---|---|
| Grow revenue (spread and interest margin) | Move more users to funded, growing balances | Total value saved by active savers, funded active savers |
| Acquire the right consumers | Win trust at first touch so signups convert to funders | Trust-driven awareness, signup-to-first-fund rate |
| Deepen wallet share | Move savers into investing and higher deposits | Investify adoption, average balance growth |
| Retain savers through macro noise | Reinforce discipline so auto-save survives | Recurring auto-save retention, balance retention |
| Own the savings category | Hold "the disciplined, licensed way to save in naira" in the mind of the segment | Aided recall, message playback |

### North Star

**Total value saved by active savers.** The total balance held across savings and investment products by users who took at least one meaningful savings action in the month (funded, ran an auto-save, or added to an investment).

Why this north star: it is the truest proxy for delivered customer value, because a growing balance is exactly what the user came for and exactly what the business earns margin on. It leads revenue directly, since spread and interest scale with money under management. It is hard to game without creating real value, because inflating it means real naira actually sitting in real accounts. A funded-active-savers count is the strong runner-up and sits directly beneath the north star as its primary input, but value saved captures both breadth (how many save) and depth (how much), which a headcount alone misses.

### Metric tree

```
Total value saved by active savers
 ├─ Funded active savers ──── signups, KYC completion, first funded save
 ├─ Deposit depth per saver ─ auto-save adoption, top-ups, Investify deposits
 └─ Balance retention ─────── auto-save survival, withdrawal rate, SafeLock lock-ins
```

### Guardrails

- Grow signups without letting the signup-to-first-fund rate fall (empty-account guardrail). A signup that never funds is a vanity number here.
- Grow deposits without spiking withdrawal rate or breaking trust (churn-of-balance guardrail).
- Grow acquisition spend without over-promising returns or security in a way that invites regulatory or trust risk (claims-integrity guardrail).
- Grow send and notification frequency without raising app uninstall or notification opt-out (fatigue guardrail).

---

## 1. Funnel-Stage Metrics (filled)

### Awareness

Awareness for a savings app is trust-weighted, not reach-weighted. A million impressions from people who do not trust the app with their money are worth little.

- Multi-million registered users, a public scale proof that itself functions as a trust signal (known, public).
- Branded search volume and direct app-store traffic for "PiggyVest": _illustrative_.
- Share of voice against Cowrywise and bank savings products in the segment: _illustrative_.
- Trust-driven awareness: unprompted association of PiggyVest with "licensed" and "safe" in brand tracking: _illustrative_.
- Social reach and follower growth: _illustrative_.

### Consideration

- App-store listing page views to install rate: _illustrative_.
- Website and app-store dwell on security, licensing, and how-it-works content: _illustrative_.
- Return visits before signup (trust rarely converts on first touch): _illustrative_.
- Referral-link click-through (PiggyVest's referral loop is a major consideration driver): _illustrative_.

### Conversion

Two conversions matter, and they are not the same event. Signup is cheap. The funded first save is the real conversion.

- Install to signup rate: _illustrative_.
- Signup to KYC completion rate (the identity and BVN step is a known drop-off point for Nigerian fintech): _illustrative_.
- KYC to first funded save rate (activation gateway): _illustrative_.
- Cost per funded saver on paid, judged on funded accounts, not installs: _illustrative_.

### Activation

First value is the first funded save landing in an account. The user has now felt money move into their own balance, which is the aha moment.

- First funded save rate (percent of signups who fund within the first 7 days): _illustrative_.
- Time to first fund (signup to first money in): _illustrative_.
- First auto-save set up rate (the leap from one-time fund to recurring intent): _illustrative_.
- Onboarding completion through to a funded state: _illustrative_.

### Retention

Retention here means the balance keeps growing, not just that the app gets opened.

- Recurring auto-save survival by cohort (still auto-saving at week 4, 12, 24): _illustrative_.
- Balance growth curve per cohort (average balance trajectory over time): _illustrative_.
- Withdrawal rate and early SafeLock breakage: _illustrative_.
- Monthly active savers (took a savings action), not just monthly active users (opened the app): _illustrative_.

### Expansion

- Investify adoption rate: savers who move into investing: _illustrative_.
- Deposit depth growth: average balance per active saver over time: _illustrative_.
- Product breadth: savers using two or more products (Piggybank plus SafeLock plus Target): _illustrative_.
- SafeLock and Target Savings attach after a first Piggybank save: _illustrative_.

### Advocacy

Referral is a first-class channel here, not a nice-to-have, so it earns real instrumentation.

- Referral rate: percent of active savers who refer at least one funded new user: _illustrative_.
- Viral coefficient: funded new savers generated per existing saver: _illustrative_.
- App-store rating and review volume and trend: _illustrative_.
- Word-of-mouth and self-reported "a friend recommended it" share at signup: _illustrative_.

---

## 2. PMM-Outcome Metrics (filled)

### Positioning effectiveness

- Do segment members describe PiggyVest as "safe," "licensed," and "the disciplined way to save" unprompted? Track message playback in reviews, replies, and support conversations.
- Category association: PiggyVest filed as the default consumer savings and investment app, ahead of a bank savings account or an informal ajo/esusu.
- Trust as positioning: does aided recall pair PiggyVest with security and licensing rather than with returns alone?

### Messaging resonance

- Hook and headline A/B lift on ad creative and app-store copy, tested against the discipline angle (stop spending money anyhow) versus the growth angle (watch it grow) versus the safety angle (licensed and secure).
- Which framing shows up in user reviews and referrals as the reason they joined.
- Message-test lift on the KYC and first-fund screens, where trust language directly moves conversion.

### Launch performance

- Per product launch (a SafeLock campaign, a new Investify option, a Target Savings push): scorecard across awareness, install lift, funded-saver adoption, and time to first fund on the new product.
- Adoption velocity: days from launch to a target number of funded users on the new product.
- Attach rate of the new product against the eligible existing-saver base.

### Sales enablement adoption

Consumer fintech has no sales team, so this stage maps to support, community, and creator or affiliate enablement.

- Are support and community reps using the approved trust and security talking points on objection-heavy questions?
- Do creators and referral partners use the provided messaging, and does their content convert to funded savers?

### Competitive win rate

- Where prospects compare PiggyVest to Cowrywise, bank savings accounts, or other fintech wallets, capture the switching reason and the loss reason (returns, trust, fees, features, brand).
- Displacement: share of new savers who moved balance from a bank or a competitor.

### Pricing and packaging

- Product mix across Piggybank, SafeLock, Flex, Target Savings, and Investify, and how the mix shifts over time.
- Deposit concentration by product (which product holds the growing share of value saved).
- Investify uptake as the higher-margin expansion tier.

### Content and demand influence

- Sourced: which campaign, creator, or referral link was first touch for a funded saver.
- Influenced: content and touches on the path from install to first fund.
- Self-reported: "how did you hear about us" at signup, which is where PiggyVest's heavy word-of-mouth and referral demand actually surfaces.

---

## 3. Leading vs Lagging Map (PiggyVest)

| PMM lever | Leading indicators | Lagging outcomes |
|---|---|---|
| Positioning (trust and discipline) | Message playback, aided recall of "safe and licensed" in segment | Funded-saver growth, category leadership |
| Messaging | Hook and screen test lift on trust and discipline angles | Signup-to-fund conversion, value saved |
| Launch (SafeLock, Investify) | Launch-window install and first-fund engagement | New-product revenue, balance retention |
| Lifecycle | First-fund rate, time to first fund | Recurring auto-save survival, balance growth |
| Referral | Referral-link clicks, invite send rate | Viral coefficient, funded new savers |

---

## 4. Attribution and Influence (PiggyVest)

- **Sourced.** Track first-touch campaign, creator, or referral link for each funded saver where the link or code allows it.
- **Influenced.** Most PiggyVest conversions are influence-heavy and trust-gated. A prospect hears about it from a friend, sees ads for weeks, reads reviews, and only then trusts it enough to fund. Last-click will credit the final ad or app-store visit and miss the referral and the trust-building that did the real work.
- **Self-reported.** Lean hard on the "how did you hear about us" field at signup, because much of the demand is dark social: WhatsApp recommendations, Twitter threads, and friend-to-friend referrals that no tracker sees. For a word-of-mouth-driven fintech this is often the most honest attribution source available.
- **Portfolio halo.** Judge the free savings products and trust-building content at the portfolio level. A low-deposit Piggybank saver or a piece of financial-discipline content rarely shows direct return on its own, yet it builds the funded, trusting base that later moves into SafeLock and Investify, which is where the margin lives. Do not kill a top-of-funnel savings surface or a trust-content effort on its direct return alone.

---

## 5. Measurement Plan (PiggyVest, filled register)

| Metric | Definition / formula | Stage or outcome | Type | Data source & tool | Cadence | Owner | Baseline | Target |
|---|---|---|---|---|---|---|---|---|
| Total value saved by active savers | Sum of balances held by users with 1+ savings action / month | North star | NS | Core product DB + analytics | Monthly | PMM + Data | _illustrative_ | _illustrative_ |
| Funded active savers | Users who funded or auto-saved in the month | Activation / retention | Input | Product analytics | Weekly | PMM + Growth | _illustrative_ | _illustrative_ |
| First funded save rate | % of signups funding within 7 days | Activation | Leading | Product analytics | Weekly | PMM + Growth | _illustrative_ | _illustrative_ |
| Time to first fund | Signup to first money in | Activation | Leading | Product analytics | Weekly | Growth | _illustrative_ | Reduce |
| KYC completion rate | KYC completed / signups | Conversion | Input / leading | Product analytics | Weekly | Growth | _illustrative_ | _illustrative_ |
| Recurring auto-save survival | % of cohort still auto-saving at week 12 | Retention | Lagging | Product analytics | Monthly | PMM + Data | _illustrative_ | _illustrative_ |
| Investify adoption rate | Active savers who invest / active savers | Expansion | Lagging | Product DB | Quarterly | PMM | _illustrative_ | _illustrative_ |
| Referral funded rate | Funded new savers from referrals / total funded new | Advocacy | Input / leading | Referral system | Monthly | Growth | _illustrative_ | _illustrative_ |
| Withdrawal rate | Value withdrawn / value saved | Guardrail | Guardrail | Product DB | Monthly | Data | _illustrative_ | Below floor |
| Trust-claim complaint rate | Security or trust complaints / active savers | Guardrail | Guardrail | Support + reviews | Monthly | PMM + Support | _illustrative_ | Cap |

Type values: NS (north star), input, leading, lagging, guardrail.

### Reporting rituals

- **Weekly pulse:** funded active savers, first-fund rate, time to first fund, KYC completion, any live launch's leading indicators.
- **Monthly review:** total value saved, funded-saver growth, auto-save survival, referral funded rate, full register against target.
- **Launch retro:** per product launch (SafeLock, Investify, Target Savings), 2 to 4 weeks after launch, the launch scorecard and time to first fund on the new product.
- **Quarterly review:** Investify adoption, deposit depth, product-mix shift, balance retention, and the trust and referral influence story at portfolio level.

### Executive translation

| PiggyVest metric | Business language |
|---|---|
| Total value saved by active savers | The money under management that spread and interest margin are earned on |
| Funded active savers | Real customers with real balances, not empty signups |
| First-fund rate and time to first fund | How fast a new user becomes a revenue-generating saver |
| Recurring auto-save survival | Balances that compound without new acquisition spend |
| Investify adoption | Movement into the higher-margin tier |
| Referral funded rate | Growth that acquires itself through trust |

---

## 6. Anti-patterns to avoid (PiggyVest)

- Reporting signup or registered-user counts as success while funded-saver rate quietly falls. An empty account earns nothing.
- Crediting the last ad for a save that a friend's referral and weeks of trust-building actually earned.
- Chasing install volume outside the segment that inflates downloads and drags funded-saver rate down.
- Over-promising returns or overstating security to lift a conversion number, which trades a short-term win for a trust and regulatory liability that is far more expensive.
- Optimizing app-open frequency (MAU) instead of savings actions (active savers), and mistaking attention for money in accounts.

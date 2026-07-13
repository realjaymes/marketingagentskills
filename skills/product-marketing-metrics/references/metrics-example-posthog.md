# Measurement Example — PostHog

A complete measurement framework worked end to end for PostHog, following the Product Marketing Measurement Framework. PostHog is an all-in-one product analytics and engineering platform (product analytics, session replay, feature flags, experiments, surveys, data warehouse, LLM analytics) sold bottoms-up to developers and product engineers. Growth is product-led and content-led: developers install the SDK, hit the generous free tier, and expand into paid usage-based spend as their data and their product adoption grow. The measurement system has to serve that motion, because the same install that produces one event is the seed of multi-product, usage-based revenue.

Numbers marked _illustrative_ are placeholders for James to replace with live figures. PostHog is a public company with published pricing and open-source repos, but no verified internal metric is asserted here.

---

## 0. Foundations

### Business objective to PMM objective mapping

| Company objective | PMM objective | Example metric |
|---|---|---|
| Grow usage-based revenue | Convert installs into recurring, expanding usage across products | Paid conversion rate, net revenue retention |
| Win developers bottoms-up | Make "the single platform" the default association versus point tools | Category association, message playback in dev channels |
| Drive multi-product adoption | Position the platform so teams adopt a second and third product | Products used per active org, cross-product attach |
| Sustain the free-and-content flywheel | Turn content and open source into qualified self-serve demand | Content-sourced signups, self-reported attribution |

### North Star

**Weekly Active Projects Sending Events (WAPSE).** Unique projects that sent at least one event in the week, weighted by whether they are using more than one PostHog product.

Why this north star: sending events is the moment a project receives value from PostHog rather than just holding an account, it leads usage-based revenue directly (events, recordings, and queries are what get billed), and it is hard to inflate without a real integration doing real work. A close second candidate is **products used per active org**, which better proxies expansion and platform stickiness. WAPSE is the primary because it captures both the activation floor (a project is live and sending) and, through the multi-product weight, the expansion ceiling. Products-per-org rides underneath it as the top input.

### Metric tree

```
Weekly Active Projects Sending Events (WAPSE)
 ├─ New projects sending first event ── SDK installs, first-event rate, docs + content
 ├─ Recurring active projects ───────── weekly recurring queries, insights built, dashboards
 └─ Products per active org ─────────── second-product adoption, third-product adoption, usage spend
```

### Guardrails

- Grow signups without letting first-event activation fall below a floor (empty-account guardrail).
- Grow usage-based revenue without pricing developers off the free tier and out of the flywheel (free-tier integrity guardrail).
- Grow multi-product adoption without inflating spend that later churns on a bill-shock event (usage-quality guardrail).

---

## 1. Funnel-Stage Metrics (filled)

### Awareness

- Organic and direct traffic to posthog.com from the content library and docs: _illustrative_.
- Non-branded search visibility on high-intent developer queries (product analytics, session replay, feature flags): _illustrative_.
- GitHub stars and repo traffic on the open-source project: _illustrative_.
- Community reach: Hacker News, Reddit dev subs, dev X, and community forum mentions: _illustrative_.

### Consideration

- Docs engagement and time on install and quickstart pages: _illustrative_.
- Content-to-signup rate (readers who create an account after a content or docs session): _illustrative_.
- Return visits across multiple sessions before signup: _illustrative_.
- Comparison-page and "vs" traffic (versus Amplitude, Mixpanel, Heap, LaunchDarkly): _illustrative_.

### Conversion

- Signup rate (account created): _illustrative_.
- Signup to SDK-installed rate: _illustrative_.
- Self-serve paid conversion rate (free project crosses into paid usage-based spend): _illustrative_.
- Product-qualified signal rate (projects hitting usage thresholds that predict paid conversion): _illustrative_.

### Activation

For a new project, first value is sending the first event, then seeing the first insight built from its own data.

- SDK install rate (signup to library installed): _illustrative_.
- First-event rate (project sends its first event): _illustrative_.
- Time to first event (signup to first event received): _illustrative_.
- First-insight rate (project builds or views its first insight from live data): _illustrative_.

### Retention

- Weekly active projects still sending events at week 4, 12, 24 by cohort: _illustrative_.
- Recurring insight and query activity (projects running queries in consecutive weeks): _illustrative_.
- Second-product adoption rate (project adds session replay, flags, or experiments): _illustrative_.
- Retention curve for paying projects versus free projects: _illustrative_.

### Expansion

- Net revenue retention on usage-based spend: _illustrative_.
- Products used per active org, and its shift over time: _illustrative_.
- Usage growth (events, recordings, queries) per paying project: _illustrative_.
- Third-product adoption rate (the platform-lock signal): _illustrative_.

### Advocacy

- Open-source stars, forks, and external contributions: _illustrative_.
- Community forum answers, Discord/Slack activity, and developer-authored content mentioning PostHog: _illustrative_.
- Developer referral signups (self-reported "a colleague told me"): _illustrative_.
- Reviews on developer-relevant sites and inclusion in "our stack" posts: _illustrative_.

---

## 2. PMM-Outcome Metrics (filled)

### Positioning effectiveness

- Do developers describe PostHog as "the single platform" or "all-in-one" unprompted, rather than as one point tool? Track message playback in forum threads, X, and reviews.
- Category association: PostHog filed as a product-and-engineering platform, not slotted narrowly as "another product analytics tool" alongside Amplitude and Mixpanel.
- Segment conversion lift after a positioning or homepage change, measured on signup and first-event rate.

### Messaging resonance

- Developer-native voice test: does copy that talks like an engineer outconvert generic SaaS framing on docs, homepage, and product pages?
- Comparison-page message tests (versus named point tools) on conversion by variant.
- Which product framings show up when developers describe why they adopted a second product.

### Launch performance

- Per new product or major feature shipped (PostHog ships frequently), a scorecard across content engagement, docs traffic, adoption by existing orgs, and new-project attach.
- Adoption velocity: days from ship to a target number of orgs adopting the new product.
- Cross-product attach: share of active orgs that add the newly shipped product within a window.

### Sales enablement adoption

- Mostly self-serve, so enablement is the docs, comparison pages, and pricing calculators doing the selling. Are those assets used on the path to paid conversion?
- For larger, sales-assisted accounts, are comparison and platform-consolidation narratives showing up in won deals?

### Competitive win rate

- Where projects evaluate PostHog against Amplitude, Mixpanel, Heap, LaunchDarkly, Segment, or Hotjar, capture loss reasons (feature depth, migration cost, price, single-tool preference).
- Displacement signal: projects that consolidate off multiple point tools onto PostHog, and the framing that won them.

### Pricing and packaging

- Free-tier-to-paid conversion by product, and how usage-based tiers convert.
- Multi-product bundling: does adopting a second product change spend and retention versus single-product projects?
- Usage-spend distribution and the share of revenue from expansion versus new paid conversion.

### Content and demand influence

- Sourced: which content or docs pages were first touch for projects that later convert to paid.
- Influenced: content and open-source touchpoints on the path to first event and to paid.
- Self-reported: "how did you hear about us" on signup, capturing dev word of mouth and open-source discovery that trackers miss.

---

## 3. Leading vs Lagging Map (PostHog)

| PMM lever | Leading indicators | Lagging outcomes |
|---|---|---|
| Positioning | "Single platform" message playback, category association | Multi-product adoption, competitive win rate |
| Messaging | Developer-voice test lift, comparison-page conversion | Signup and first-event rate, paid conversion |
| Launch | Ship-day docs and content engagement, adoption velocity | New-product revenue, cross-product attach |
| Lifecycle | First-event rate, time to first event | Weekly active projects, net revenue retention |
| Content and open source | Content-sourced signups, GitHub stars | Self-serve paid conversion, developer referrals |

---

## 4. Attribution and Influence (PostHog)

- **Sourced.** Track the first-touch content or docs page for each project that converts to paid where possible. Product-qualified signals (usage thresholds that predict conversion) are the highest-fidelity leading indicator here, cleaner than any marketing-touch model.
- **Influenced.** Most PostHog adoption is influence-heavy and product-led: a developer reads content and docs, installs, runs on the free tier for weeks, then crosses into paid as usage grows. Last-click will credit the pricing page or the final session and miss the content and open-source relationship that did the real work.
- **Self-reported.** Lean on the "how did you hear about us" field, since much of the growth is dark: colleague recommendations, open-source discovery, and dev-community mentions that no tracker sees.
- **Portfolio halo.** Judge the free tier and the prolific content library at the portfolio level. Both rarely convert directly, and much content is pure top-of-funnel, but together they build the installed base of active projects that later expand into usage-based revenue. Do not judge content on direct conversion, and do not judge the free tier on its own margin. They are the seed layer for the whole revenue engine.

---

## 5. Measurement Plan (PostHog, filled register)

| Metric | Definition / formula | Stage or outcome | Type | Data source & tool | Cadence | Owner | Baseline | Target |
|---|---|---|---|---|---|---|---|---|
| Weekly Active Projects Sending Events | Unique projects sending 1+ event / week, weighted by multi-product | North star | NS | Product analytics (self-instrumented) | Weekly | PMM + Growth | _illustrative_ | _illustrative_ |
| First-event rate | Projects sending first event / signups | Activation | Leading | Product analytics | Weekly | PMM + Growth | _illustrative_ | _illustrative_ |
| Time to first event | Signup to first event received | Activation | Leading | Product analytics | Weekly | PMM + Growth | _illustrative_ | Reduce |
| Signup to SDK-installed | Installs / signups | Conversion | Input / leading | Product analytics | Weekly | Growth | _illustrative_ | _illustrative_ |
| Self-serve paid conversion | Projects crossing into paid usage / active projects | Conversion | Input / leading | Billing + product analytics | Monthly | PMM + Growth | _illustrative_ | _illustrative_ |
| Products used per active org | Distinct products with activity / active org | Expansion | Input | Product analytics | Monthly | PMM | _illustrative_ | _illustrative_ |
| Net revenue retention | Expansion minus contraction and churn on usage spend | Expansion | Lagging | Billing | Quarterly | PMM + Finance | _illustrative_ | Above 100% |
| Content-sourced signups | Signups with content or docs first touch | Awareness / conversion | Input | GA + attribution + self-report | Monthly | PMM | _illustrative_ | _illustrative_ |
| GitHub stars | Cumulative and new stars on OSS repo | Advocacy | Input | GitHub | Monthly | PMM | _illustrative_ | _illustrative_ |
| Empty-account rate | Signups with no event after 7 days / signups | Guardrail | Guardrail | Product analytics | Weekly | Growth | _illustrative_ | Below floor |
| Free-tier retention | Free projects still active at week 12 | Guardrail | Guardrail | Product analytics | Monthly | PMM | _illustrative_ | Hold |

Type values: NS (north star), input, leading, lagging, guardrail.

### Reporting rituals

- **Weekly pulse:** WAPSE, first-event rate, time to first event, empty-account rate, and any live product launch's leading indicators.
- **Monthly review:** self-serve paid conversion, products per active org, content-sourced signups, the full register against target.
- **Launch retro:** per new product or feature ship, 2 to 4 weeks after ship, the launch scorecard, adoption velocity, and cross-product attach.
- **Quarterly review:** net revenue retention, multi-product adoption, competitive win and displacement, the influence story told at portfolio level.

### Executive translation

| PostHog metric | Business language |
|---|---|
| WAPSE | The number of projects actually receiving value, which is the base all usage-based revenue expands from |
| First-event rate and time to first event | How reliably and how fast new signups become live, which sets early retention |
| Products per active org | Platform stickiness, and the multi-product lock that competitors cannot easily unpick |
| Net revenue retention | Growth that compounds from the installed base without new acquisition cost |
| Content-sourced signups | The content and open-source flywheel's fingerprint on qualified demand |

---

## 6. Anti-patterns to avoid (PostHog)

- Reporting signups as success while first-event rate and time to first event quietly worsen. An account that never sends an event is not a customer, it is an empty shell.
- Crediting the pricing page or the final session for a paid conversion that content, docs, and the free tier warmed for weeks.
- Judging the content library or open source on direct conversion and cutting the top-of-funnel that seeds the whole install base.
- Optimizing usage-based revenue by pricing developers off the free tier, which starves the flywheel that feeds expansion.
- Positioning against one point tool at a time and losing the "single platform" story that drives multi-product adoption.

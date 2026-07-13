# Measurement Example — Fireflies.ai

A complete measurement framework worked end to end for Fireflies.ai, following the Product Marketing Measurement Framework. Fireflies is PLG SaaS: an AI meeting assistant that records, transcribes, summarizes, and analyzes meetings across Zoom, Google Meet, and Teams, sold on a freemium plus per-seat model. Two things make its measurement distinct. First, the product carries its own growth channel: the bot joins meetings where non-users are present, so acquisition and product usage are the same motion. Second, value compounds through recurring capture and downstream use of notes, which is what turns a curious first meeting into a retained account and eventually a paid team.

Numbers marked _illustrative_ are placeholders for internal figures that cannot be verified here. Do not treat them as real.

---

## 0. Foundations

### Business objective to PMM objective mapping

| Company objective | PMM objective | Example metric |
|---|---|---|
| Grow paid revenue | Convert active free users into paid seats with clear value and packaging | Free-to-paid rate, seat expansion rate |
| Accelerate self-serve growth | Sharpen the position "AI notetaker that just works" against alternatives | Signup rate, aided recall in segment |
| Sustain the viral loop | Convert meeting participants who saw the bot into signups | Participant-to-signup rate, viral coefficient |
| Retain and expand accounts | Drive recurring capture and downstream note use, then team adoption | Weekly capture rate, net revenue retention |

### North Star

**Meetings captured per active user per week.** A meeting counts when the bot joins, records, and produces a usable transcript and summary that the user or a teammate then opens.

Why this north star: it proxies delivered value directly, since a captured, opened meeting is the core job the product exists to do. It leads revenue, because users who capture recurring meetings are the ones who hit credit limits, invite teammates, and upgrade. It is hard to inflate without creating real value, since a captured meeting nobody opens does not count. It also sits at the exact center of the viral loop, because every captured meeting is a meeting where non-users may see the bot. Weekly active users getting value from captured meetings is the close runner-up and is tracked as the primary breadth input beneath the north star.

### Metric tree

```
Meetings captured per active user per week
 ├─ Acquisition reach ──── bot-in-meeting impressions, SEO/marketplace signups
 ├─ Activation depth ───── calendar connect rate, first capture, first summary viewed
 └─ Recurring value ────── weekly capture rate, note/search use, integration sends
```

### Guardrails

- Grow capture volume without letting summary quality or accuracy drop (value-integrity guardrail).
- Grow the bot's meeting presence without raising participant complaints or host removals (trust guardrail).
- Grow signups without letting the share who connect a calendar and capture a first meeting fall (activation-quality guardrail).
- Grow free usage without collapsing free-to-paid conversion through overly generous credit limits (monetization guardrail).

---

## 1. Funnel-Stage Metrics (filled)

### Awareness

- Bot-in-meeting impressions: unique non-users exposed to the Fireflies bot in meetings per month. This is the flagship owned channel, not a paid line item: _illustrative_.
- Organic and branded search to fireflies.ai, plus category terms like "AI notetaker" and "meeting transcription": _illustrative_.
- Integration marketplace presence and installs (Zoom, Google Workspace, Slack, HubSpot, Salesforce, Notion): _illustrative_.
- Social reach and review-site visibility (G2, Capterra): _illustrative_.

### Consideration

- Landing page and pricing page engagement, comparison-page views ("Fireflies vs Otter", "vs Fathom"): _illustrative_.
- Docs and help-center consumption on setup and integrations: _illustrative_.
- Free-trial or free-plan intent signals (start-signup clicks): _illustrative_.
- Return visits before signup: _illustrative_.

### Conversion

- Visitor-to-signup rate on the free plan: _illustrative_.
- Participant-to-signup rate: non-users who saw the bot and later created an account. This is the viral-loop conversion, tracked distinctly from marketing-sourced signups: _illustrative_.
- Signup source split: viral (bot-attributed) versus self-serve (search, marketplace, referral): _illustrative_.
- Cost per signup on any paid acquisition, judged against activated signups, not raw accounts: _illustrative_.

### Activation

First value has three gates, in order: connect a calendar, capture the first meeting, view the first summary. Shared vocabulary with product-onboarding-activation.

- Calendar connect rate: signups who connect a calendar: _illustrative_.
- First-capture rate: signups whose first meeting is recorded and transcribed: _illustrative_.
- First-summary-viewed rate: signups who open the summary or notes from that first meeting: _illustrative_.
- Time to first value: signup to first viewed summary: _illustrative_.

### Retention

- Weekly capture rate: active users capturing at least one meeting per week: _illustrative_.
- Recurring-capture cohort curve: users still capturing at week 4, 12, 24: _illustrative_.
- Downstream note use: search queries run, notes opened, AskFred queries, clips or soundbites shared: _illustrative_.
- Integration send rate: captured meetings pushed to CRM, Slack, or Notion, a strong retention-driving behavior: _illustrative_.
- Gross revenue retention and logo churn on paid accounts: _illustrative_.

### Expansion

- Seat expansion: new seats added within an account, often seeded when meeting participants become users: _illustrative_.
- Free-to-paid rate, and Pro-to-Business or Business-to-Enterprise upgrade rate: _illustrative_.
- Credit-limit hit rate as an upgrade trigger: free users reaching capture or AI limits: _illustrative_.
- AskFred and AI-feature adoption as expansion drivers on higher tiers: _illustrative_.
- Net revenue retention, with above 100 percent as the durable-growth line: _illustrative_.

### Advocacy

- Participant-driven signups attributed back to a specific host or account (the loop closing): _illustrative_.
- Referral signups via self-report and any in-product referral mechanic: _illustrative_.
- Review volume and rating on G2 and Capterra: _illustrative_.
- NPS and public advocacy (mentions, UGC on how teams use Fireflies): _illustrative_.

---

## 2. PMM-Outcome Metrics (filled)

### Positioning effectiveness

- Do buyers describe Fireflies as "the AI notetaker that just works across Zoom, Meet, and Teams" unprompted? Track message playback in reviews, support threads, and sales calls.
- Category association: filed as an AI meeting assistant, distinct from a revenue-intelligence platform (Gong) or a bare transcription tool.
- Aided and unaided recall in the target segment against Otter.ai, Fathom, Grain, and native Zoom or Meet AI.

### Messaging resonance

- Headline and value-prop A/B lift on the homepage, pricing page, and comparison pages.
- Onboarding and empty-state message tests that move calendar-connect and first-capture rates.
- Which value framings (searchable notes, automatic capture, AskFred, integrations) show up in reviews and won deals.

### Launch performance

- Per new AI feature (for example an AskFred capability or a new integration): scorecard across awareness, adoption against the eligible base, and time to first value.
- Adoption velocity: days from launch to a target share of eligible active users using the feature.
- Attach rate of the new capability on the tiers where it is available.

### Sales enablement adoption

- For Business and Enterprise motions, are battle cards against Otter, Gong, and Fathom being used, and do they correlate with wins?
- Content usage by the sales and success teams on expansion and security or compliance objections.

### Competitive win rate

- Head-to-head win rate against Otter.ai, Fathom, Grain, Gong, and native Zoom or Meet AI.
- Loss reasons tagged and trended: price, accuracy, integration depth, security, native-tool default.
- Displacement rate: accounts switching from a named competitor to Fireflies.

### Pricing and packaging

- Tier mix across Free, Pro, Business, and Enterprise, and its shift over time.
- Credit-limit design: does the free capture or AI limit trigger upgrades without capping value so hard it kills activation?
- Attach rate of add-ons and AI features, and discount depth on annual or team deals versus realized price.

### Content and demand influence

- Sourced: which content, comparison page, or marketplace listing was first touch for a paid account.
- Influenced: content touched on the path to a paid conversion or expansion.
- Self-reported: "how did you hear about us" on signup and sales calls, which is where the bot-in-meeting exposure often surfaces.

---

## 3. Leading vs Lagging Map (Fireflies)

| PMM lever | Leading indicators | Lagging outcomes |
|---|---|---|
| Positioning | Message playback, aided recall vs Otter/Fathom | Segment win rate, paid conversion |
| Messaging | Homepage and comparison-page test lift | Signup rate, activation rate |
| Launch | Feature adoption velocity, day-one usage | Expansion revenue, tier upgrades |
| Lifecycle | Calendar connect, first capture, weekly capture | Net revenue retention, churn |
| Viral loop | Bot-in-meeting impressions, participant-to-signup | Self-serve signup volume, CAC efficiency |
| Competitive | Battle-card usage, loss-reason trend | Head-to-head win rate, displacement |

---

## 4. Attribution and Influence (Fireflies)

- **Sourced.** Track first touch for each paid account: search, comparison page, marketplace listing, referral, or the viral bot exposure. Tag the viral-loop signup source distinctly, since it is a product event, not a marketing campaign.
- **Influenced.** Most Fireflies conversions are influence-heavy across two overlapping paths. A self-serve buyer may read for weeks, compare against Otter, then sign up. A viral signup may first meet the product as a bot in someone else's meeting, sign up free, capture recurring meetings, and only later convert or expand. Last-click will credit the final pricing-page visit and miss both the comparison content and the bot exposure that did the real work.
- **Self-reported.** Lean on the "how did you hear about us" field, because the viral bot channel and word of mouth inside teams are largely invisible to trackers. A large share of "saw it in a meeting" only shows up when you ask.
- **Portfolio halo.** Judge the free tier and the viral loop at the portfolio level, not on their direct return. The free plan rarely monetizes on its own line, but it is the surface that both seeds the viral loop (more free users mean more bot exposure to non-users) and feeds paid conversion and seat expansion. Do not evaluate free-tier or top-of-funnel content on isolated conversion and cut what is actually growing the whole system.

---

## 5. Measurement Plan (Fireflies, filled register)

| Metric | Definition / formula | Stage or outcome | Type | Data source & tool | Cadence | Owner | Baseline | Target |
|---|---|---|---|---|---|---|---|---|
| Meetings captured per active user per week | Captured, summarized meetings that get opened / active users / week | North star | NS | Product analytics | Weekly | PMM + Growth | _illustrative_ | _illustrative_ |
| Calendar connect rate | Signups who connect a calendar / signups | Activation | Input / leading | Product analytics | Weekly | PMM + Growth | _illustrative_ | _illustrative_ |
| First-capture rate | Signups with a first meeting recorded / signups | Activation | Leading | Product analytics | Weekly | PMM + Growth | _illustrative_ | _illustrative_ |
| Time to first value | Signup to first viewed summary | Activation | Leading | Product / onboarding instrumentation | Weekly | PMM + Growth | _illustrative_ | Reduce |
| Weekly capture rate | Active users capturing 1+ meeting / week | Retention | Leading | Product analytics | Weekly | PMM + Growth | _illustrative_ | _illustrative_ |
| Participant-to-signup rate | Non-user meeting participants who sign up / exposed participants | Conversion / advocacy | Input / leading | Product analytics | Monthly | PMM + Growth | _illustrative_ | _illustrative_ |
| Free-to-paid rate | Free accounts converting to paid / free accounts | Expansion | Lagging | Billing | Monthly | PMM + Finance | _illustrative_ | _illustrative_ |
| Seat expansion rate | New seats added / paid account / period | Expansion | Lagging | Billing + CRM | Quarterly | PMM + Sales | _illustrative_ | _illustrative_ |
| Net revenue retention | Revenue retained + expanded / starting revenue | Expansion | Lagging | Billing | Quarterly | Finance + PMM | _illustrative_ | Above 100% |
| Competitive win rate | Won deals / competitive deals vs named rivals | Competitive | Lagging | CRM | Quarterly | PMM + Sales | _illustrative_ | _illustrative_ |
| Summary accuracy / quality | Quality score or thumbs-up rate on summaries | Retention | Guardrail | Product + QA | Monthly | Product + PMM | _illustrative_ | Hold floor |
| Host removals / complaints | Bot removals or complaints / meetings joined | Awareness | Guardrail | Product analytics | Weekly | Product + PMM | _illustrative_ | Below floor |

Type values: NS (north star), input, leading, lagging, guardrail.

### Reporting rituals

- **Weekly pulse:** calendar connect, first capture, time to first value, weekly capture rate, and the two guardrails (summary quality, host removals).
- **Monthly review:** the north star, participant-to-signup, free-to-paid, signup-source split, full register against target.
- **Launch retro:** per new AI feature or integration, 2 to 4 weeks after launch, adoption velocity, attach rate, and time to first value.
- **Quarterly review:** net revenue retention, seat expansion, competitive win rate, and the viral-loop influence story told at the portfolio level.

### Executive translation

| Fireflies metric | Business language |
|---|---|
| Meetings captured per active user per week | The size of the base actually getting value, which predicts both retention and expansion |
| Calendar connect and first capture | Whether new users reach value, which sets early churn |
| Participant-to-signup rate | The efficiency of the viral loop, growth that lowers blended CAC |
| Free-to-paid and seat expansion | Revenue that compounds inside accounts without new acquisition |
| Net revenue retention | Durable growth that survives even if new signups slow |

---

## 6. Anti-patterns to avoid (Fireflies)

- Reporting total signups as success while the calendar-connect and first-capture rates quietly fall. An account that never captures a meeting is not a user.
- Counting captured meetings that nobody opens toward the north star, which rewards volume over delivered value.
- Crediting the last pricing-page visit for a conversion that the bot-in-meeting exposure and comparison content actually drove.
- Loosening free-tier credit limits to boost activation and eroding free-to-paid conversion across the base.
- Pushing bot presence into more meetings without watching host removals and complaints, trading short-term reach for long-term trust.

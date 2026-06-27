# Client Engagement Playbook

Operational framework for running paid advertising engagements from onboarding through scaling. Use alongside the performance marketing playbook (strategy, creative, platform mindsets) and the operating checklist.

---

## Overview

This is an operating system, not a manual. The 11 sections map to a single loop: plan → launch → optimize → scale → repeat. Use this overview to orient before diving into any section.

### The Operating Loop

| # | Stage | What Happens | Primary Decision |
|---|---|---|---|
| 1 | Onboard | Capture business, offer, geo, budget, tracking state | Is this account ready to spend? |
| 1.5 | Audience Research | Restate business, pull existing customer profile, competitor Ad Library teardown, comments mining, Audience Language Doc | Skipping this means Strategy is a guess. Don't proceed without it on new engagements |
| 2 | Track | Verify pixel + CAPI + conversion events | Don't proceed without 80%+ event match vs. analytics |
| 3 | Strategy | Pick objective, set CPA/CVR/ROAS targets, hypothesize audiences and creative themes (informed by §1.5 Audience Language Doc) | Define kill/scale thresholds before launch |
| 4 | Structure | Build campaign → ad set → ad hierarchy with naming convention | ABO (testing) or CBO (scaling)? |
| 5 | Audiences | Build cold + warm + hot audiences with exclusions | Which 2-3 audience hypotheses get budget |
| 6 | Creative | Brief 3 angles × 3 formats, hook variants per concept | One ad set = one angle; what angle each ad set tests |
| 7 | Budget | Set daily floors at 3-5× target CPA per ad set | How much capital per test cell |
| 8 | Launch | Pre-launch checklist, then 72-hour hands-off | Don't touch anything for 3 days |
| 9 | Optimize | Apply diagnosis → kill rules → scale rules on rolling cycle | Kill what's broken, scale what's working |
| 10 | Report | Weekly + monthly review, document learnings | What worked, what failed, what's next |
| 11 | Scale | Vertical (more budget) + horizontal (more audiences/geos/formats) | Where to put incremental dollars |

### Decision Cadence

| Time | Decision | What to Do |
|---|---|---|
| Pre-launch | Tracking gate | Verify pixel + CAPI + events. Don't launch on broken tracking |
| Hour 0-72 | Hands off | Confirm delivery only. Resist the urge to optimize |
| Day 3 | Creative kill | Cut ads with CTR 40-60% below average + 1× CPA spent |
| Day 5-7 | Ad set kill | Cut ad sets with CPA 2× target + 3× CPA spent |
| Day 7+ | Scale check | Stable CPA + good frequency → start vertical scaling |
| Weekly | Full optimization routine | Pull report, kill, scale, brief new creative |
| Bi-weekly | Audience review | Saturation check, lookalike refresh, new audience tests |
| Monthly | Strategy review | Funnel split, MER vs. platform attribution, budget reforecast |
| Quarterly | Lookalike + creative library refresh | Rebuild seed audiences, retire stale concepts |

### Key Numbers to Watch

| Metric | What it tells you |
|---|---|
| CPA / CPL | Profitability, primary scoreboard |
| ROAS | Revenue efficiency (ecom) |
| CVR (post-click) | Whether the destination converts traffic |
| CTR (link) | Whether the ad earns the click |
| CPM | Auction pressure + creative quality |
| Frequency | Saturation signal |
| Quality Ranking | Algorithm's view of your ad vs. competitors |

### The Three Fundamental Questions

Before any campaign action, answer these:

1. **Is the tracking trustworthy?** If no, fix tracking first.
2. **Is the message clear?** If no, fix creative + destination before optimizing.
3. **Has it had enough time + spend to learn?** If no, hold the line.

If yes to all three and performance is still off, the structural issue is audience or offer, in that order.

### Metric Definitions

**CVR (post-click)** = conversions / link clicks. Measured at the destination (landing page, lead form, product page, app store, WhatsApp, Calendly, Messenger, etc.). Use "CVR" throughout this playbook. Where logic says "fix the destination" or "audit the page," it applies to whatever the click lands on.

**CPA / CPL** = total spend / conversions. CPL when the conversion is a lead, CPA for any conversion event.

**ROAS** = revenue attributed / ad spend. Used for ecom and direct-revenue funnels.

**MER** = total revenue / total ad spend (across channels). Used to decide spend allocation when platform attribution is unreliable.

---

## 1. Client Onboarding & Discovery

### Client Information to Collect

| Field | Purpose |
|-------|---------|
| Industry / Vertical | Platform selection, benchmark context |
| Website URL | Landing page audit, pixel verification |
| Monthly ad budget | Structure decisions, platform viability |
| Primary business goal | Objective selection, funnel design |
| Revenue model | CPA vs ROAS optimization |
| Average order value / deal size / LTV | Budget justification, target CPA setting |

### Discovery Questions

**Business**
- [ ] Revenue model (subscription, one-time, recurring, marketplace)
- [ ] Average order value / deal size / LTV
- [ ] Purchase / sales cycle length (days to close)
- [ ] Seasonal patterns or promotional calendar
- [ ] Key competitors and differentiation

**Marketing**
- [ ] Existing funnels and landing pages
- [ ] Current funnel type (Direct purchase / Website Traffic / Lead Gen form / Click-to-WhatsApp / Profile Visit)
- [ ] Current Meta or TikTok objective in use (Sales / Traffic / Leads / Engagement / Messages / etc.)
- [ ] Estimated downstream conversion rates (Visit-to-DM, DM-to-Sale, Lead-to-Sale, Page-to-Sale) where prospect can guess
- [ ] Lead magnets, offers, or promotions in use
- [ ] Email list size and engagement rate
- [ ] CRM / marketing automation tools in use
- [ ] Content assets available (blog, video, case studies)

**Historical Performance**
- [ ] Previous ad spend and results (CPA, ROAS)
- [ ] Best-performing audiences (historical)
- [ ] Top-performing creatives (historical)

**Current Performance Baseline**

Total business volume across all channels (organic + paid + email + referral). Date-stamp every row. This becomes the reference for setting targets and measuring lift. Use the table that matches the client's revenue model.

> **"Conversions"** = the primary commercial action for the business model: orders (ecom/D2C), leads (lead gen), enrollments (info product), installs (app), bookings (local service), signups (SaaS trial). **"Avg. value per conversion"** = AOV / deal value / ASP / ARPU depending on model.

*B2C / D2C / ecom / info product / lead gen / app / local service:*

| Cadence | Conversions | Revenue | Avg. value per conversion | Notes |
|---|---|---|---|---|
| Daily (last 30d avg) | | | | Pull from source-of-truth (Shopify / POS / CRM / billing) |
| Monthly (last 3 months) | | | | List each month separately |
| Quarterly (last 2 quarters) | | | | Capture seasonality |

Channel split (last 30 days, % of revenue): Organic ___ | Paid ___ | Email ___ | Referral ___ | Other ___

*B2B (LinkedIn, sales-led SaaS, professional services):*

| Cadence | Leads | MQLs | SQLs | Opps | Pipeline $ | Notes |
|---|---|---|---|---|---|---|
| Monthly (last 3 months) | | | | | | List each month separately |
| Quarterly (last 2 quarters) | | | | | | Capture seasonality |

Source split (last quarter, % of pipeline $): Inbound ___ | Outbound ___ | Paid ___ | Referral ___ | Other ___

- [ ] Baseline date and source of truth captured
- [ ] Daily / monthly / quarterly numbers pulled from source-of-truth, not platform attribution
- [ ] Channel or source split captured

**Platform Access**
- [ ] Meta: Business Manager access granted (Admin or Advertiser)
- [ ] TikTok: TikTok Business Center access granted
- [ ] Google: Google Ads MCC access granted
- [ ] LinkedIn: LinkedIn Campaign Manager access granted
- [ ] Snapchat: Snapchat Ads Manager / Business Manager access granted (Public Profile linked)
- [ ] Payment method on file and verified
- [ ] Brand assets received (logo, fonts, colors, guidelines)

### Discovery Call Template

```
DISCOVERY CALL AGENDA — [CLIENT]
Date: ___________
Platform(s): ___________

1. BUSINESS OVERVIEW
   - What does the business do?
   - Revenue model and pricing
   - Average deal size / order value
   - Sales cycle length

2. MARKETING CURRENT STATE
   - What channels are you using today?
   - What has worked? What hasn't?
   - Existing funnels and landing pages
   - Current funnel type and Meta objective. Estimated downstream conversion rates (Visit-to-DM, DM-to-Sale, Lead-to-Sale)
   - Email list and CRM setup

3. GOALS & KPIs
   - Primary goal for paid ads
   - Target CPA / ROAS
   - Monthly budget available
   - Timeline and milestones

4. CURRENT PERFORMANCE BASELINE
   - Daily conversions (orders / leads / installs / bookings) — last 30d avg
   - Monthly revenue or pipeline $ — last 3 months
   - Quarterly revenue or pipeline $ — last 2 quarters
   - Channel split: organic / paid / email / referral
   - Source of truth (Shopify / Stripe / HubSpot / Salesforce / GA4)

5. AUDIENCE
   - Who is the ideal customer?
   - Key demographics and behaviors
   - Customer pain points
   - Purchase triggers

6. CREATIVE & ASSETS
   - Brand guidelines available?
   - Existing creative assets
   - Testimonials / case studies
   - Product photography / video

7. ACCESS & LOGISTICS
   - Platform account access
   - Tracking / pixel status
   - Reporting cadence preference
   - Key stakeholders and approvals
```

---

## 1.5 Audience Research (do before Strategy)

Discovery (§1) captures what the client tells you. Audience Research is what you find out yourself before opening Ads Manager. Skip it and Strategy is a guess. Four steps, then a deliverable.

1. **Existing customer profile pull.** From the client's CRM / order export / DM history: who actually buys today — age range, geo concentration, income proxy (the price points they tolerate), lifestyle markers. This is your targeting seed and your lookalike source.
2. **Competitor Ad Library teardown.** Pick 3–5 competitors and open the Meta Ad Library (filter to the client's country). For each notable ad, capture: hook style, format (static / carousel / video / reel), copy length, offer framing, CTA, social-proof type, and where it sends people (website / WhatsApp / form / profile). Ads running 60+ days are proven winners worth modelling.
3. **Comments mining.** Read the comments on competitor ads AND on the client's own organic + paid posts. Pull objections (raw quotes), desires (raw quotes), and the exact words people use to describe the problem. Comments are where real buyer language lives.
4. **Audience Language Doc (the deliverable).** One page that feeds Strategy (§3) and Creative briefs (§6): 5 pain quotes, 5 desire quotes, 3 objection patterns, 5 competitor hooks, and one paragraph on where buyers convert (the destination: WhatsApp DM, landing page, checkout, or lead form). Save it to the engagement folder.

---

## 2. Campaign Naming Conventions

### Three-Tier Naming Pattern

Each level captures a different decision dimension. Pipe-separated for clean parsing in reports.

| Level | Pattern | Why these fields |
|---|---|---|
| **Campaign** | `Objective \| Product \| Audience Type \| Date` | Objective + Product define the campaign's job; Audience Type + Date scope it |
| **Ad Set** | `Country \| Audience \| Angle \| Conversion Event \| Daily Budget` | Country and audience determine delivery; **Angle scopes the ad set to one message (one ad set = one angle)**; conversion event and budget determine learning |
| **Ad** | `Product \| Creative Type \| Hook` | Anchor on the product so multi-product accounts stay legible; creative type + hook are the test variables within the ad set's angle |

**Campaign examples:**

- `Sales | PMM AI Bootcamp Core | Cold | 2026-03-01`
- `Sales | PMM AI Bootcamp Core | Warm | 2026-03-01`
- `Leads | Bootcamp | Cold-Interest | 2026-04`
- `Sales | HeroSKU | RT-Site30d | 2026-04`

**Ad Set examples:**

- `Nigeria | Cold | AI Fear | Purchase | ₦15,000`
- `Retargeting Audiences | AI Fear | Purchase | ₦15,000`
- `NG | LAL3-Buyers | Financial Freedom | Lead | ₦10K`
- `US | RT-AddToCart7d | Speed | Purchase | $50`

**Ad examples:**

- `Bootcamp | Video | Fear of Replacement`
- `Bootcamp | Video | Discount`
- `HeroSKU | UGC-Video | Pain`
- `HeroSKU | Static-Carousel | Outcome`

### Field Reference

**Objective:** Awareness, Traffic, Leads, Sales, App-Promotion

**Product:** Hero SKU, course name, service name, or product line code

**Audience Type (Campaign-level):** Cold-Broad, Cold-Interest, Cold-LAL, RT, Warm-Engagement

**Audience (Ad Set-level):** specific segment (Broad, LAL1-Buyers, Interest-Marketing, RT-Site30d, RT-AddToCart7d)

**Angle (Ad Set-level):** the one belief, desire, or fear this ad set speaks to — one angle per ad set (AI Fear, Cost of Living, Financial Freedom, Job Security, Speed). An angle is a desire/fear, not a content structure (testimonial, social proof, origin story are content structures, not angles). See the angle layer in [[Creative Strategy Framework]].

**Country:** ISO code or region (NG, US, UK, EU, DIASPORA)

**Conversion Event:** Purchase, Lead, Subscribe, Schedule, IC, AddToCart, ViewContent

**Daily Budget:** include currency (₦15K, $50)

**Creative Type:** UGC-Video, Founder-Talking, Static-Carousel, Static-Single, Reel, Demo-Screen, Video

**Hook (Ad-level):** the specific opening this ad tests within the ad set's angle (Pain, Outcome, Authority, FOMO, Origin-Story, Category-Frame, Social-Proof, Cost-of-Inaction, Fear-of-Replacement, Discount). The angle lives on the ad set; the hook is the ad-level test variable.

**Note:** CTA is no longer part of the ad name. Track CTA at the creative level (asset tag in the brief), not in the name. Anchor names on Product + Creative Type + Hook so multi-product accounts stay legible.

### Ad Set Structure: One Ad Set = One Angle

**One ad set = one angle.** The ad set is scoped to a single angle, which also fixes the audience hypothesis the angle targets. Different angles go in different ad sets, never mixed. Within one ad set (one angle), each ad tests a different hook or format expressing that same angle, not random visual variants.

**What an angle is.** An angle is a **belief, desire, or fear the audience holds** — the specific reason this audience pays attention to this offer. It is *what you're saying*, not how you say it. Formula: **Product + Audience + Desire or Fear = Angle.** The test: if a label describes how you organize or prove the message (testimonial, case study, founder story, social proof, demo) that's a **content structure**, not an angle; if it's the opening line or visual, that's a **hook**. Those live at lower layers. Don't put a content structure or a hook in the angle slot.

Example angles: AI Fear, Cost of Living, Financial Freedom, Job Security, Speed. This is the angle layer of the [[Creative Strategy Framework]] (Offer → Angle → Content Structure → Creative Format → Style → Hook → Platform).

### Date Format

YYYY-MM. Campaigns evolve monthly; quarterly cadence written as YYYY-Q1, YYYY-Q2, etc.

### Platform Hierarchy

| Platform | Level 1 | Level 2 | Level 3 |
|----------|---------|---------|---------|
| Meta | Campaign | Ad Set | Ad |
| TikTok | Campaign | Ad Group | Ad |
| Google | Campaign | Ad Group | Ad |
| LinkedIn | Campaign Group | Campaign | Ad |
| Snapchat | Campaign | Ad Set | Ad |
| X | Campaign | Ad Group | Ad |
| ChatGPT (OpenAI Ads) | Campaign | Ad Group (intent cluster) | Ad |

### Anti-Patterns

- Too many campaigns (consolidate to feed algorithms more data)
- Mixing objectives in one campaign (one objective per campaign)
- Audience overlap between ad sets (use exclusions)
- No naming convention (impossible to analyze at scale)
- Editing live campaigns heavily (resets learning phase)

---

## 3. Audience Build Sheet

### Geo Targeting (apply before everything else)

**Universal rule: target at state/city level, never country-wide.** This applies to every country we run paid campaigns in — Nigeria and diaspora geographies alike. Country-level targeting spreads spend across regions where the offer does not resonate or where buyers do not concentrate, dilutes both CTR and lookalike seed quality, and is one of the most common silent reasons campaigns underperform. Geo is the highest-leverage filter; apply it before interest, age, or any other dimension.

**Default city sets** (start here for any client whose buyers concentrate in these geographies, prune based on the specific offer):

| Country | Default targets |
|---|---|
| Nigeria | Lagos · Abuja (FCT) · Rivers (Port Harcourt) · Oyo (Ibadan) · Kano |
| Canada | Ontario (Toronto) · Ontario (Brampton) · Alberta (Calgary) · Alberta (Edmonton) · Manitoba (Winnipeg) |
| United Kingdom | London · Manchester · Birmingham · Leeds · Glasgow |
| United States | Texas (Houston area) · Georgia (Atlanta area) · Maryland · New York · California (Los Angeles area) |

These sets concentrate the buyer populations for MIA's typical client profile (Nigerian SMBs selling in NG + Nigerian diaspora hubs abroad). Use them as the default cold-targeting geo, layered with whatever audience type (broad, interest, lookalike) is right for the offer.

**Adjust per business:**

- **Strictly local services** (restaurants, salons, gyms): single city only, often radius-targeted (5-15km around the location)
- **Premium offers (₦500K+ AOV)**: top 1-2 cities per country often sufficient
- **Cheaper consumer goods (₦5K-₦50K AOV)**: broader state set OK but still state-level — add additional secondary cities as relevant
- **Regional-only** (Northern NG audience, US South audience, etc.): target those states explicitly, never country-wide

**Lookalike caveat — geo applies at ad set level, not at lookalike build level.** Meta + TikTok do not allow city/state geo selection when CREATING a lookalike audience — the platforms only offer country (or region/multi-country) as the source-geo parameter. The correct pattern: build the lookalike at country level (e.g. Nigeria 1%), then apply the state/city geo filter at the **ad set** level when the lookalike is used in delivery. Same effective outcome — only city-resident lookalike members get delivered to.

### Audience Matrix by Funnel Stage

> **No interest targeting (2026).** Build cold audiences from broad + lookalikes off real data. Interest targeting no longer outperforms and is not used or recommended.

**TOFU (Prospecting) — broad + lookalikes only**
- [ ] Broad / Open targeting
- [ ] Lookalike 1% (source: ___________)
- [ ] Lookalike 2-5% (source: ___________)
- [ ] Lookalike 1% from lead list (source: ___________)

**MOFU (Consideration)**
- [ ] Website visitors 30-day
- [ ] Website visitors 60-day
- [ ] Video viewers 50%+
- [ ] Engagement audience (page/profile interactions)

**BOFU (Conversion)**
- [ ] High-intent visitors (pricing, cart, checkout)
- [ ] Lead form abandoners
- [ ] Customer lookalike 1-3%

**Retargeting**
- [ ] 7-day website visitors
- [ ] Cart / form abandoners
- [ ] Past customers (upsell)

**Exclusions**
- [ ] Customers excluded from prospecting
- [ ] Converters excluded from lead gen
- [ ] Audiences de-overlapped

---

## 4. Budget Allocation Framework

### Funnel Budget Splits

| Focus | TOFU | MOFU | BOFU |
|-------|------|------|------|
| Full Funnel | 60% | 25% | 15% |
| Growth Focus | 70% | 20% | 10% |
| Retargeting Heavy | 30% | 20% | 50% |
| Awareness Push | 80% | 15% | 5% |

### Minimum Daily Budgets by Platform

**Meta:**

| Objective | Min Daily / Ad Set | Recommended |
|-----------|-------------------|-------------|
| Conversions / Sales | $20 | $30-50 |
| Lead Generation | $15 | $25-40 |
| Traffic | $10 | $15-25 |
| Awareness / Reach | $5 | $10-20 |

**TikTok:**

| Objective | Min Daily / Ad Group | Recommended |
|-----------|---------------------|-------------|
| Conversions | $20 | $30-50 |
| Lead Generation | $20 | $30-50 |
| Traffic | $20 | $20-30 |
| Reach / Video Views | $20 | $20-30 |

**Google Ads:**

| Campaign Type | Min Daily | Recommended |
|---------------|-----------|-------------|
| Search (Conversions) | $20 | $30-50 |
| Performance Max | $30 | $50-100 |
| Display | $10 | $20-40 |
| YouTube Video | $10 | $20-50 |
| Demand Gen | $20 | $30-50 |

**LinkedIn:**

| Objective | Min Daily | Recommended |
|-----------|-----------|-------------|
| Website Conversions | $50 | $75-150 |
| Lead Gen Forms | $30 | $50-100 |
| Website Visits | $25 | $50-75 |
| Brand Awareness | $10 | $25-50 |

Note: LinkedIn CPCs are significantly higher ($5-12 avg). Budget accordingly. Best for high-value B2B where LTV justifies cost.

**Snapchat:**

| Objective | Min Daily / Ad Set | Recommended |
|-----------|-------------------|-------------|
| Conversions | $40 (US/UK/CA), ₦12K (NG) | $50-80 (US/UK/CA), ₦15K-₦25K (NG) |
| Lead Generation | $40 (US/UK/CA), ₦12K (NG) | $50-80 (US/UK/CA), ₦15K-₦25K (NG) |
| Traffic | $20 (US/UK/CA), ₦8K (NG) | $30-50 (US/UK/CA), ₦10K-₦15K (NG) |
| Awareness / Video Views | $20 (US/UK/CA), ₦7.5K (NG) | $25-40 (US/UK/CA), ₦10K-₦15K (NG) |
| App Installs | $40 (US/UK/CA) | $60-150 (US/UK/CA) |

Note: Snapchat needs **4-6× target CPA** as daily budget per ad set (higher multiplier than Meta/TikTok's 3-5× because of weaker auction density and thinner pixel pools). NG floor is higher than Meta because Snapchat NG pixel pools are smaller; below ₦12K daily, learning phase rarely completes.

**X (Twitter):**

X bills in USD; NGN equivalents at 1 USD = ₦1,600.

| Objective | Min Daily / Ad Group (NG) | Min Daily / Ad Group (Diaspora) | Recommended |
|---|---|---|---|
| Website Conversions (Purchase) | $10-$20 (₦16K-₦32K) | $25-$50 (₦40K-₦80K) | Must clear 40-60 weekly events |
| Lead Generation | $10-$20 (₦16K-₦32K) | $25-$50 (₦40K-₦80K) | Same event-volume rule |
| Engagement (TOP only) | $5 (₦8K) | $15 (₦24K) | Cap at 10-15% of total spend |
| Reach / Video Views | $5 (₦8K) | $15 (₦24K) | Limited use |
| Retargeting | $5-$10 (₦8K-₦16K) | $15-$30 (₦24K-₦48K) | Smaller audience |
| Scaling (consolidated winner) | $50+ (₦80K+) | $150+ (₦240K+) | Algorithm needs room |

Note: X needs **3-5× target CPA** as daily budget per ad group AND must clear **40-60 weekly events** of the optimization event. Below that, ML allocator under-delivers and CPAs are unstable. NG ad account currency must be set to **USD** &mdash; NGN setting triggers ~50% surcharge on non-NG spend. Fund with virtual USD card (EverTry / Payora / GeegPay / Grey / Cardtonic) or domiciliary Visa.

**ChatGPT / AI Answer Engine Ads:**

ChatGPT proper bills in USD; available only to US/CA/AU/NZ advertisers as of June 2026. For NG-targeted campaigns, route through Microsoft Ads (Copilot inventory) + Google Ads (AIO inventory).

ChatGPT Ads (when advertiser is in approved geo):

| Campaign Type | Min Daily | Recommended |
|---|---|---|
| Conversions (when GA) | $50 | $75-150 |
| Traffic (CPC-bid) | $25 | $35-60 |
| Reach (CPM-bid, US, $60 floor) | $30 | $40-80 |

Microsoft Ads (Copilot inventory included automatically):

| Campaign Type | Min Daily | Recommended |
|---|---|---|
| Search (Conversions) | $20 | $30-50 |
| Audience Network | $15 | $20-40 |
| Shopping | $25 | $40-75 |
| Performance Max | $30 | $50-100 |

Google Ads (AIO inventory included automatically): same floors as the existing Google Ads section above.

Note: AI answer surface CPMs are 2-6&times; Meta CPMs. Treat as experimental budget. ChatGPT proper has no minimum since May 5, 2026, but $25-$50/day practical floor needed to read signal. Pixel-only attribution undercounts ROAS by ~60% (conversation gap) &mdash; budget assuming blended (pixel + survey + branded search lift) attribution, not pixel-only.

### CBO vs Manual Budget

**ABO for testing, CBO for scaling.** ABO (ad set budget) forces signal per angle/audience — a fair budget into every angle/audience so each generates enough signal to judge (testing). CBO (campaign budget) lets the algorithm allocate to proven winners once you know what works (scaling). Use both, at the right time.

**Never test on CBO.** If you launch a test on CBO, it concentrates budget on the first ad set to get traction and starves the rest; the other ad sets never get a fair test, and you'll think you have one winner when you never gave the others a chance. Test on ABO so each angle gets enough budget to prove or disprove itself, then move proven winners to CBO to scale.

- **Meta CBO / TikTok CBO:** Use when 3+ ad sets are proven and you want the algorithm to allocate (scaling). Set minimums per ad set if needed.
- **ABO / Ad Set Budget:** Use when testing new audiences/angles and you want controlled spend per cell. Better for controlled experiments.
- **Google Shared Budgets:** Pool across related campaigns.
- **LinkedIn:** Daily budget recommended. LinkedIn can spend up to 50% over daily budget on high-opportunity days.
- **X:** No ABO/CBO equivalent; budgets sit at ad group level. Scaling = consolidating winners into fewer ad groups with larger budgets. Slower budget absorption than Meta &mdash; raise by 20-30% every 5-7 days, not 48-72h.
- **ChatGPT / AI Answer:** Ad-group level budgets. AI surfaces cap by query volume in the intent cluster &mdash; pushing budget beyond query volume inflates CPM without volume gain. Most clusters cap at 2-5&times; starting budget.

---

## 5. Launch Pre-Flight Checklist

### Account & Tracking
- [ ] Pixel/tag firing correctly (verified with test events)
- [ ] Conversion events tracking correctly
- [ ] Billing / payment method active
- [ ] Account spending limit set (if applicable)

### Campaign Settings
- [ ] Campaign objective is correct
- [ ] Campaign budget is set (daily or lifetime)
- [ ] Campaign schedule / start-end dates correct
- [ ] Campaign naming follows convention

### Ad Set / Ad Group Settings
- [ ] Audience selected and reviewed
- [ ] Exclusion audiences applied
- [ ] Optimization event is correct
- [ ] Bid strategy set (lowest cost, target CPA, etc.)
- [ ] Placements reviewed (automatic or manual)
- [ ] Schedule / dayparting set (if applicable)

### Ad Settings
- [ ] Creative uploaded and rendering correctly
- [ ] Ad copy proofread (no typos, correct brand voice)
- [ ] CTA button is correct
- [ ] Destination URL is correct and loads properly
- [ ] UTM parameters added to all URLs
- [ ] Preview checked on all placements (mobile, desktop, stories)

### Final Verification
- [ ] Landing page loads in under 3 seconds
- [ ] Landing page is mobile-optimized
- [ ] Form / checkout flow tested end-to-end
- [ ] UTM tracking verified in analytics
- [ ] Client approval received

### Launch Day SOP

| Timeframe | Action |
|-----------|--------|
| +1 hour | Verify ads are delivering (status: Active). Check for disapprovals. |
| +4 hours | Check spend pacing. Verify pixel events firing on live traffic. |
| +24 hours | Review CPM, CTR, CPC. Flag obvious issues. Do NOT make changes yet. |
| +48 hours | Review conversion data (if sufficient volume). Check frequency. |
| +72 hours | First optimization window. Pause underperformers if data is clear. Still in learning phase. |

---

## 6. Optimization Decision Rules

### Decision Table

| Signal | Threshold | Diagnosis | Action |
|--------|-----------|-----------|--------|
| CTR | < 0.5% | Creative not resonating | Test new hooks, visuals, formats |
| CTR | 0.5-1.5% | Average creative | Test variations, iterate on best |
| CTR | > 2% | Strong creative | Scale budget, duplicate to new audiences |
| CPC | > 2x benchmark | Audience or creative issue | Refresh creative or broaden targeting |
| CPA | > 1.3x target after 2x cycle | Funnel or targeting issue | Review landing page, audience, offer |
| CPA | < target for 3+ days | Winning combination | Scale 20% every 3 days |
| Frequency | > 2.5 | Audience fatigue | Refresh creative or expand audience |
| CVR (post-click) | < 1% | Destination OR offer problem (not the ad) — message mismatch, slow load, weak CTA, wrong audience, or a weak offer/price | Audit the page first (message-match, mobile speed, CTA clarity). If the page is sound, the offer/price is the leak. Fix the destination before changing ads. See [[Meta Ads Conversion Playbook]] |
| CVR (post-click) | 1-3% | Average destination performance | Test destination variants (headline, hero, CTA, social proof, form length) |
| CVR (post-click) | > 3% | Strong destination, ad and page aligned | Scale traffic, protect the destination, document what works |
| ROAS | < 1.0x | Losing money | Pause and diagnose |
| ROAS | > 3.0x | Profitable | Scale budget, test similar audiences |

### Kill Rules

Kill an ad/ad set when:
- Spent 2x target CPA with zero conversions
- CTR below 0.5% after 1,000+ impressions
- CPA above 1.5x target after 50+ clicks
- CVR (post-click) below 1% after 200+ link clicks (destination OR offer problem — audit the page first; if the page is sound, the offer/price is the leak; fix before continuing spend)
- ROAS below 1.0x after full conversion window

### Scale Rules

Scale an ad/ad set when:
- CPA at or below target for 3+ consecutive days
- 5+ conversions per day (exited learning phase)
- ROAS consistently above 3x
- CVR (post-click) at or above 3% sustained over 7+ days (destination is converting, scale traffic confidently)
- Frequency below 2.0

### Weekly Optimization Checklist

- [ ] Review all campaign KPIs (CTR, CPC, CPA, ROAS)
- [ ] Pause underperforming ads (apply kill rules)
- [ ] Scale winning ads (apply scale rules)
- [ ] Check frequency across all ad sets
- [ ] Review audience overlap (consolidate if needed)
- [ ] Check placement breakdown (cut poor placements)
- [ ] Review search terms / queries (Google: add negatives)
- [ ] Plan next creative round (if frequency rising)

### Common Fixes

Read CPM first. It's the rawest cost signal — once delivery is confirmed, CPM is the first performance metric to read, because a high CPM inflates CPC, CPA, and ROAS, making every other metric read worse than it is. Fix CPM before trusting anything downstream.

**High CPM (read first):**
1. Refresh creative (creative fatigue is the most common cause)
2. Broaden the audience (a narrow audience drives CPM up)
3. Rebuild the creative if quality ranking is weak (placement/audience tweaks won't move quality ranking)
4. Accept or shift schedule if it's a competitive auction window

**High CPC:**
1. Test broader audiences
2. Test new creative (different hooks, formats, visuals)
3. Improve ad relevance score / quality ranking
4. Test different placements (Stories, Reels often have lower CPC)

**Low CTR:**
1. Rewrite hooks (more compelling first line)
2. Use more eye-catching visuals (faces, contrast, motion)
3. Test video if only running static images
4. Make the CTA clearer and more urgent

**High CPA:**
1. Audit landing page (speed, copy, form length)
2. Tighten audience targeting or test new segments
3. Test a stronger offer (discount, free trial, bonus)
4. Ensure conversion event is correct
5. Audit objective vs funnel: if running Traffic objective with a checkout destination and pixel installed, switch to Sales objective. Single biggest CPA reduction available without changing creative or audience.

**Frequency Creep:**
1. Refresh creative (new visuals, hooks, formats)
2. Expand audience size
3. Set frequency caps (if platform allows)

### Learning Phase Rules

- Meta / TikTok: ~50 optimization events in 7 days
- Snapchat: ~50 optimization events in 7-10 days (slightly longer because of thinner pixel pools)
- Google: ~30 conversions in 30 days
- LinkedIn: varies by objective
- X: ~40-60 optimization events in 7 days per ad group (practitioner consensus, not officially published). Below that, ML allocator under-delivers and CPAs unstable. Step down to higher-funnel event until volume catches up
- ChatGPT / AI Answer: surfaces are volume-limited by query frequency in the intent cluster, not by event count. Plan 14-21 days to first stable read; 30-60 days for blended attribution to settle; 60-90 days for branded search lift to materialize. Conversion-optimized bidding on ChatGPT proper rolled out June 5, 2026

**What resets learning:** Budget changes >20%, audience changes, optimization event changes, creative swaps, bid strategy changes, pausing for 7+ days. On X, editing winning ads triggers a learning reset under the xAI ranker too. On ChatGPT, destination URL changes reset attribution-window association.

---

## 7. Reporting Templates

**Live-campaign reads use the Funnel-Layer Diagnostic.** For the diagnostic read of a live campaign (not the client-facing summary templates below), use the Funnel-Layer Diagnostic template at `performance-marketing/references/funnel-layer-diagnostic.md`. Run it at every scheduled read (Day 3 / 5 / 7 / 12), and log each read newest-on-top in the campaign doc's Live Monitoring section. It walks the funnel in order — Delivery → CPM → Creative → Audience → LP/Offer → CPA/ROAS — so you stop at the first broken layer instead of optimizing downstream noise. The weekly and monthly templates below are the client-facing rollups built from those reads.

### Weekly Report Template

```
WEEKLY PERFORMANCE REPORT — [CLIENT]
Platform: ___________
Date Range: ___________ to ___________

SUMMARY
Total Spend: $___________
Impressions: ___________
Clicks: ___________
CTR: ___________%
CPC: $___________
Conversions: ___________
CPA: $___________
ROAS: ___________x (if applicable)

TOP PERFORMERS
Best campaign: ___________
Best creative: ___________
Best audience: ___________

KEY OBSERVATIONS
1. ___________
2. ___________
3. ___________

NEXT ACTIONS
1. ___________
2. ___________
3. ___________
```

### Monthly Report Template

```
MONTHLY PERFORMANCE REPORT — [CLIENT]
Platform: ___________
Month: ___________

MONTH SUMMARY
Total Spend: $___________
Total Conversions: ___________
Avg CPA: $___________
Avg ROAS: ___________x
Total Revenue Attributed: $___________

MONTH-OVER-MONTH TRENDS
Spend: $___ → $___ (___% change)
CPA: $___ → $___ (___% change)
ROAS: ___x → ___x (___% change)
Conversions: ___ → ___ (___% change)

TOP CAMPAIGNS
1. ___________: CPA $___, ROAS ___x
2. ___________: CPA $___, ROAS ___x
3. ___________: CPA $___, ROAS ___x

TOP CREATIVES
1. ___________: CTR ___%, CPA $___
2. ___________: CTR ___%, CPA $___

AUDIENCE INSIGHTS
Best performing: ___________
Worst performing: ___________
Recommended changes: ___________

NEXT MONTH RECOMMENDATIONS
Budget: $___________
Key priorities:
1. ___________
2. ___________
3. ___________
```

### Client-Ready Language Bank

**Performance Improved:**
"Performance improved week-over-week, with CPA decreasing [X]% from $[old] to $[new]. This was driven by [creative refresh / audience expansion / landing page changes]."

"We saw strong results from [campaign name], which delivered [X] conversions at $[CPA], [X]% below our target. We recommend scaling this audience."

**Performance Declined:**
"CPA increased [X]% this week, which we attribute to [audience fatigue / increased competition / creative decay]. Our plan is to [refresh creative / test new audiences / adjust bids]."

"We recommend reallocating budget from [underperforming campaign] to [winning campaign] to improve overall efficiency."

**Recommending Changes:**
"Based on the data, we recommend [increasing/decreasing] budget by [X]% and shifting focus to [audience/campaign]. This should [reduce CPA / improve ROAS] based on current trends."

"Creative fatigue is setting in on [campaign]. Frequency has exceeded [X]. We recommend refreshing creative this week to maintain performance."

---

## 8. Scaling Playbook

### Scaling Readiness Checklist

- [ ] CPA at or below target for 7+ consecutive days
- [ ] 50+ conversions in the past 7 days (exited learning)
- [ ] Frequency below 2.0 across active ad sets
- [ ] At least 2-3 winning creatives identified
- [ ] Landing page conversion rate stable (no recent drops)
- [ ] Client approved increased budget

### Horizontal Scaling (New Audiences)

- [ ] Duplicate winning ad sets to new audience segments
- [ ] Expand lookalike percentages (1% → 3% → 5%)
- [ ] Test new lookalikes built from winning audience / buyer data
- [ ] Launch in new geographies (if applicable)
- [ ] Test on additional platforms (cross-platform expansion)

### Vertical Scaling (More Budget)

- [ ] Increase budget by no more than 20% every 3 days
- [ ] Monitor CPA for 48 hours after each increase
- [ ] If CPA spikes, hold budget for 3 days before next increase
- [ ] Use CBO to auto-distribute budget across ad sets
- [ ] Set ad set minimum spend to protect smaller audiences

### Creative Scaling

- [ ] Refresh creative when frequency exceeds 2.5
- [ ] Produce 3-5 new ad variations per creative cycle
- [ ] Iterate on winning hooks (same hook, different visual)
- [ ] Test new formats (if winning with static, test video)
- [ ] Document winning creative patterns for future campaigns

### Budget Ramp Methodology

Increase 20% every 3 days. Monitor CPA after each step. If CPA spikes >30% after an increase, hold for 3 additional days before resuming.

Example ramp from $50/day to $200/day:
- Day 0: $50
- Day 3: $60
- Day 6: $72
- Day 9: $86
- Day 12: $104
- Day 15: $124
- Day 18: $149
- Day 21: $179
- Day 24: $200 (target)

---

## Goal Setting from Baseline

Convert the Current Performance Baseline (captured during onboarding) into explicit targets before running any CPA / CVR / ROAS calculation. Every metric that matters gets a Current → Target → Lift % → Timeline row. Targets here are business-level goals; the CPA/CVR/ROAS subsection below derives the unit economics needed to hit them.

*B2C / D2C / ecom / info product / lead gen / app / local service:*

| Metric | Current | Target | Lift % | Timeline | Owner |
|---|---|---|---|---|---|
| Daily conversions | | | | | |
| Monthly revenue | | | | | |
| Quarterly revenue | | | | | |
| Paid contribution % of total | | | | | |

*B2B (LinkedIn, sales-led SaaS, professional services):*

| Metric | Current | Target | Lift % | Timeline | Owner |
|---|---|---|---|---|---|
| Monthly leads | | | | | |
| Monthly MQLs | | | | | |
| Monthly SQLs / Opps | | | | | |
| Monthly pipeline $ | | | | | |
| Quarterly pipeline $ | | | | | |
| Paid contribution % of pipeline | | | | | |

**Rules:**
- Lift > 100% in 90 days requires a corresponding offer, creative, or capacity change. Don't set growth targets that assume the same inputs produce different outputs.
- If `Paid contribution %` target requires more spend than the budget ceiling supports at current CPA, surface the gap before committing.
- Quarterly target must reconcile with monthly target × 3 ± seasonality. Flag mismatches.
- For B2B: pipeline targets must reconcile with sales-team capacity to follow up. A 3× lift in MQLs without SDR coverage produces dead leads, not pipeline.

---

## Setting Targets (CPA, CVR, ROAS)

Targets are constraints, not aspirations. Set them before launch so kill/scale rules have meaning. Pick the calculation method that matches the business model.

### Target CPA (or CPL) — How to Calculate

**Method 1: Margin-based (E-commerce, D2C)**

```
Target CPA = AOV × Gross Margin % × Acquisition Allowance %
```

Example: AOV $50 × 60% margin × 30% allowance = $9 target CPA.

Acquisition allowance: 30% aggressive (high-growth phase), 50% defensive (profit phase). Remainder funds fulfillment, ops, profit.

**Method 2: LTV-based (SaaS, subscription, repeat-purchase)**

```
Target CPA ≤ LTV / 3
```

CAC:LTV of 1:3 is the standard. Below = unscalable. Above 1:5 = under-investing.

Example: LTV $300 → max CPA $100.

**Method 3: Payback-based (subscription, infinite-LTV)**

```
Target CPA = Monthly Net Revenue × Payback Months
```

B2B SaaS: 6-12 months. D2C subscription: 3-6 months.

Example: $20/month net revenue × 6 months = $120 target CPA.

**Method 4: Lead-stack (B2B, high-ticket, lead gen)**

```
Target CPL = Deal Value × Close Rate × Margin × Acquisition Allowance
```

Example: $5,000 deal × 20% close × 40% margin × 30% allowance = $120 target CPL.

**Sanity check:** if target CPA falls below 30% of platform benchmark CPA for the geo + vertical, the offer is likely not viable on paid. Fix the offer or LTV before scaling spend.

### Target CVR — How to Set

Working from benchmarks (post-click CVR):

| Funnel | Healthy CVR Range |
|---|---|
| Lead form (low-friction) | 8-20% |
| Lead form (B2B, gated) | 3-10% |
| Native Meta lead form (Lead-to-Sale, post-follow-up) | 8-15% |
| E-commerce checkout (cold) | 1-3% |
| E-commerce checkout (warm/RT) | 4-8% |
| App install (web → store) | 10-25% |
| Demo / consultation booking | 2-5% |
| WhatsApp / Messenger conversion | 3-10% (compound of click-to-conversation × conversation-to-sale) |
| Profile visit funnel (Visit-to-Sale, compound) | 0.5-2% (compound of Visit-to-DM 5-15% × DM-to-Sale 15-30%) |
| Info product checkout | 2-6% |
| Webinar funnel (reg → attend → buy, compound) | 3-8% reg-to-sale (compound of attendance 25-45% × show-to-sale 8-20%) |

Set target at or above the floor of the benchmark range. Below the floor signals a destination problem. For compound funnels (webinar, profile-visit), the floor is the *product* of the stage rates, so a weak single stage drags the whole funnel below the floor even when the ad-stage metric looks fine.

Algebraic check: `Target CVR = Target CPC / Target CPA`. If the math returns a CVR outside the benchmark range, one of CPA or CPC targets is unrealistic.

### Target ROAS — How to Set

```
Breakeven ROAS = 1 / Gross Margin %
Target ROAS = Breakeven ROAS × 1.5 to 2x
```

Example: 50% margin → breakeven 2.0x → target 3.0-4.0x.

High-margin info products (80%+ margin) have breakeven of 1.25x but target should still be 2-3x to fund overhead, refunds, growth.

### Funnel-Aware Target Translation

Target CPA is the cost-per-sale ceiling. Meta does not always report cost-per-sale. The metric in the dashboard depends on the campaign objective and the funnel destination. Translate Target CPA to the metric Meta actually surfaces using the multipliers below.

| Funnel Type | Meta Reports | Formula | Mental Shortcut |
|---|---|---|---|
| Direct purchase (Sales objective → checkout) | Cost Per Purchase | Target CPA itself | 25-30% of AOV (physical), 40-50% (digital/service) |
| Website Traffic objective (ad → landing page → action) | Cost Per Link Click | Target CPA × Click-to-Sale rate | Target CPA ÷ 50 (cold), ÷ 25 (warm/RT) |
| Lead Gen objective (ad → native form → follow-up → sale) | Cost Per Lead | Target CPA × Lead-to-Sale rate | Target CPA ÷ 10 |
| Click-to-WhatsApp (ad → DM → sale) | Cost Per Conversation | Target CPA × DM-to-Sale rate | Target CPA ÷ 4 (retail), ÷ 7 (B2B) |
| Profile Visit (ad → IG/TikTok profile → DM → sale) | Cost Per Profile Visit | Target CPA × DM-to-Sale × Visit-to-DM | Target CPA ÷ 40 (retail), ÷ 67 (B2B) |
| Webinar funnel (ad → registration → live/replay → checkout) | Cost Per Registration (Lead) | Target CPA × attendance rate × show-to-sale rate | Target CPA ÷ 20 to ÷ 40 |

**Default Nigerian SMB conversion rates** (use when prospect cannot give precise numbers):

- **Click-to-Sale (Website Traffic objective):** 2% cold, 4% warm/retargeting, 1% broad-geo splash
- **Lead-to-Sale (Meta native lead form):** 10%
- **DM-to-Sale:** 25% retail, 15% B2B wholesale
- **Profile-Visit-to-DM:** 10% (well-optimized profile), 5% (unoptimized profile)
- **Webinar registration → attendance:** 25-45% (cold paid; warm/organic + reminder stacks higher), **attendance → purchase:** 8-20%, **replay → purchase:** 2-8% of no-shows, **blended registration → purchase:** 3-8%

**Webinar / multi-stage funnels — the model.** A webinar funnel breaks the single-stage assumption: the ad fills a free class (optimize for Lead/registration), and the purchase happens days later on the checkout backend, which the ad platform cannot see and undercounts heavily. CPL is the only ad-readable number, and it sits four stages upstream of revenue:

```
Spend → Registrations (CPL) → Attendees (attendance) → Buyers (show-to-sale + replay) → Revenue
Effective CAC = CPL ÷ blended reg→sale     Target CPL = Target CAC × blended reg→sale
```

Derive a Target CAC from price × margin × allowance (~30%), convert to Target CPL via the blended reg→sale rate, and judge the campaign on backend-export buyers, not the platform-attributed purchase count. The dominant lever is show-to-sale (the webinar and the close), not the ad: a few points of show-to-sale movement swings funnel ROAS more than any CPL optimization. Backend is whatever processor the offer sells through (Selar, Paystack, Flutterwave, Stripe, Gumroad, a manual log), never assume one.

**Critical note: Objective Choice Drives Translation**

If the prospect has pixel + purchase event installed, Sales objective beats Traffic objective by 40-60% effective CPA without any other change. Same destination, different optimization. Sales objective tells Meta to find buyers. Traffic objective tells Meta to find clickers. This single switch is the cheapest Month 1 consulting win available, and most Nigerian SMBs are running the wrong objective for their funnel.

**Quick-Diagnosis Workflow (7 Steps)**

For any prospect on a discovery call or WhatsApp intake, this sequence yields a usable target and budget recommendation in under a minute:

1. Get AOV and monthly revenue from the prospect.
2. Compute current customers: Revenue ÷ AOV.
3. Pick growth target (default: 2x for established businesses, 3x for early-stage).
4. Compute Target CPA: AOV × 0.25-0.30 (physical product) or × 0.40-0.50 (digital/service).
5. Compute Total Ad Budget: New Customers Needed × Target CPA.
6. Pick funnel type, divide Target CPA by the appropriate factor (1 for direct purchase, 50 for website traffic, 10 for lead gen, 4 or 7 for DM, 40 or 67 for profile visit, 20-40 for a webinar funnel).
7. Plug the numbers into the matching reply template below.

### Diagnostic Reply Templates

Five copy-pasteable templates for delivering the funnel-aware diagnosis to a prospect. Each uses the worked example of a ₦15K AOV business at ₦800K monthly revenue (53 current customers) growing to 100 customers, requiring 47 new customers and a ₦211,500 monthly ad budget. The total budget reconciles across all five funnels; only the metric Meta reports changes.

**Direct Sales Funnel (ad → checkout → purchase):**

> At a ₦15K AOV and ₦800K monthly revenue, you're closing roughly 53 customers a month. To grow that to 100 with paid, your target CPA needs to sit around ₦4,500 to stay profitable. That means your monthly ad budget needs to be at least ₦211,500 to acquire those 47 extra customers. Most business owners never calculate this.

**Website Traffic Funnel (ad → landing page → checkout or DM):**

> At a ₦15K AOV and ₦800K monthly revenue, you're closing roughly 53 customers a month. To grow that to 100 through Meta Website Traffic ads, you'd need around 2,350 link clicks a month at a max of ₦90 per click, assuming a 2% page-to-sale rate on cold traffic. That's a monthly ad budget of ₦211,500. Honest read: if your site has pixel and a purchase event, you shouldn't be running Traffic objective at all. You should be running Sales objective. Same destination, but Meta optimizes for buyers instead of clickers. Most business owners pick Traffic because it feels safer. It's actually the most expensive choice you can make.

**Lead Gen Funnel (ad → native lead form → sales follow-up → sale):**

> At a ₦15K AOV and ₦800K monthly revenue, you're closing roughly 53 customers a month. To grow that to 100 through Meta Lead Gen ads, you'd need 470 leads a month at a max of ₦450 per lead form submit, assuming 1 in 10 leads turns into a sale through your follow-up. That's a monthly ad budget of ₦211,500. Most business owners run lead gen ads and celebrate cheap leads in Ads Manager without realizing the lead-to-sale rate is what actually decides whether they made money.

**Click-to-WhatsApp Funnel (ad → DM → sale):**

> At a ₦15K AOV and ₦800K monthly revenue, you're closing roughly 53 customers a month. To grow that to 100 with paid through WhatsApp ads, you'd need 188 conversations a month at a max of ₦1,125 per click-to-WhatsApp, assuming 1 in 4 DMs closes. That's a monthly ad budget of ₦211,500. Most business owners stare at "cost per click" in Meta and never translate it back to what each conversation actually costs them.

**Profile Visit Funnel (ad → IG/TikTok profile → DM → sale):**

> At a ₦15K AOV and ₦800K monthly revenue, you're closing roughly 53 customers a month. To grow that to 100 through IG profile visit ads, you'd need 1,880 profile visits a month at a max of ₦113 per visit, assuming 1 in 10 visits becomes a DM and 1 in 4 DMs closes. That's a monthly ad budget of ₦211,500. Most business owners look at the wrong number. Meta shows cost per profile visit. Profitability lives two steps downstream of that, where most never look.

**Webinar Funnel (ad → free class registration → live/replay → checkout):**

> Your ad isn't selling the course, it's filling a free class, so the only number Meta can show you is cost per registration. The sale happens days later on your checkout page, which Meta can't see. So we work backwards: at a ₦35K offer and 90% margin, you can spend about ₦9,450 to acquire one buyer. If roughly 1 in 18 registrants ends up buying (say 35% show up and 12% of them buy, plus a few replay sales), then your target cost per registration is around ₦520. Above ~₦1,700 per registration you're losing money on every buyer before you even pay for the webinar. The lever that decides this isn't the ad, it's how well the class itself converts the people who show up. Judge it on your checkout export, never on Meta's purchase number.

**Operating principle:** set the most conservative of the three targets as the kill line. The most aggressive becomes the scale-up trigger.

---

## Campaign Strategy Brief Template

```
CAMPAIGN STRATEGY BRIEF — [CLIENT]
Date: ___________
Platform: ___________

OBJECTIVE
Primary goal: ___________
Campaign objective: ___________
Optimization event: ___________
Target KPI: ___________

FUNNEL STRUCTURE
☐ TOFU — Audiences: ___________ | Budget: ___%
☐ MOFU — Audiences: ___________ | Budget: ___%
☐ BOFU — Audiences: ___________ | Budget: ___%

AUDIENCE STRATEGY
Primary audience: ___________
Secondary audience: ___________
Retargeting pools: ___________
Exclusions: ___________

CREATIVE PLAN
Angles (one ad set each): ___________
Formats: ___________
Hooks (per ad set, within its angle): ___________
Number of variations: ___________

SUCCESS METRICS
Target CPA: $___________ (use Method 1-4 above)
Target CVR (post-click): ___________% (benchmark floor for funnel type)
Target ROAS: ___________x (breakeven × 1.5-2x)
Monthly budget: $___________
Review cadence: ___________
Kill threshold: CPA > ___ | CVR < ___% | CTR < ___% after $___ spend
```

---

## Creative Brief Template

```
CREATIVE BRIEF — [CLIENT]
Date: ___________

OBJECTIVE: ___________
AUDIENCE: ___________
ANGLE (belief/desire/fear — one per ad set): ___________
KEY MESSAGE: ___________

HOOK (opening line/visual within the angle)
☐ Problem/Pain: ___________
☐ Benefit/Outcome: ___________
☐ Social Proof: ___________

FORMAT: ☐ Image  ☐ Video  ☐ Carousel
ASPECT RATIO: ☐ 1:1  ☐ 9:16  ☐ 1.91:1
CTA BUTTON: ___________
LANDING PAGE URL: ___________

VISUAL DIRECTION
Style: ___________
Colors: ___________
Text overlay: ___________

COPY
Primary text: ___________
Headline: ___________
Description: ___________
```

---

## Hook Formulas

1. Stop [pain point]. Start [desired outcome].
2. [Number] [audience] already [benefit]. Here's how.
3. "I wish I knew this before [common mistake]."
4. The [adjective] way to [desired outcome] without [common objection].
5. What [successful person/company] knows about [topic] that you don't.
6. [Audience], you're overpaying for [thing]. Here's the fix.
7. We helped [client/number] achieve [specific result] in [timeframe].
8. [Counterintuitive statement]. Here's why.
9. [Number]% of [audience] make this mistake with [topic].
10. Before vs. After: What [product/service] did for [client type].

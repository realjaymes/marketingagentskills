# Funnel-Layer Diagnostic — Template + Trigger

The standard read for a live paid campaign. It walks the funnel **top to bottom by layer**, marks each layer 🟢/🟡/🔴, names the **one layer that is breaking**, and gates every action on that read. This is the canonical format for the **Live Monitoring** section of a campaign build doc (the `00 - …Campaign…md` hub in `Areas/Work/MIA/Academy/Ads/[Offer]/[YYYY-MM-DD - … Campaign]/`).

It exists so campaign reads are consistent and complete instead of memory-dependent. Source spec: the platform playbook's §9 **Metric Diagnosis Table** (e.g. `[[Meta Ads Playbook]]` §9). Canonical complete exemplar: `MIA/Academy/Ads/Meta Account Recovery Handbook/2026-05-21 - Recovery Workshop Meta Campaign v3/00 - …v3.md` (Day 12 diagnostic).

---

## WHEN TO RUN IT (the trigger)

Generate or update a diagnostic block **at every scheduled read** and **before any kill/scale decision**:

- **Day 1** (or first morning after launch): confirm delivery + spend pacing only — too early for performance reads (see [[Meta Ads Playbook]] 72-hour rule).
- **Day 3** — first real read once the algorithm has learning data.
- **Day 5, Day 7, Day 12** — and at any cadence the campaign's `## Next Actions` schedules.
- **Any time a kill or scale rule is being considered** — the decision must be gated on a fresh diagnostic, not a glance at ROAS.

Each run is **appended newest-on-top** in the Live Monitoring section (most recent diagnostic first), so the history reads in reverse chronological order. Never overwrite a prior day's diagnostic — they are the append-only record of how the campaign was read over time.

**Completeness rule:** a campaign that has passed a scheduled read date with no diagnostic logged is incomplete — fill it from the Meta/platform CSV export + the Selar (or platform) sales export. A campaign that is younger than its first scheduled read (e.g. Day 1) legitimately has only the delivery/pacing pre-flight check, not a full table — that is not "missing," it's pre-first-read.

The trigger lives in the campaign-build cadence (the hub's `## Next Actions` schedules the read dates) — wire the read task there so the diagnostic is invoked, not remembered.

---

## READING ORDER (top to bottom; stop at the first break)

Read the layers in this order and stop diagnosing downstream once you find the break — everything below a broken layer is downstream noise until the break is fixed:

**Delivery → CPM → Creative → Audience → Landing Page → Offer → Full-funnel (CPA/ROAS)**

- **Delivery / pre-flight first** — if the ad is off/rejected/under-pacing, nothing else matters.
- **CPM is the first performance metric** read after pre-flight. It's the rawest signal of whether the platform thinks the ad is worth showing; a high CPM inflates every cost beneath it, so an unaddressed CPM problem makes everything downstream look worse than it is.
- **Landing-page layer = destination OR offer.** Low CVR with healthy CTR means people clicked but didn't buy. Audit the page first (message-match, mobile speed, CTA clarity). If the page is sound, the **offer or price is the leak** — clicks-without-conversions is the classic offer-problem signal (see [[Meta Ads Conversion Playbook]] Reasons 1-2).
- **Selar (or platform sales backend) is truth.** Meta/TikTok undercount; always cross-check attributed purchases against the sales export and report the capture rate. Never assume the processor — it may be Selar, Paystack, Flutterwave, Stripe, Gumroad, or a manual transfer log.
- **Webinar / multi-stage funnels split the destination layer into three.** For a webinar funnel (ad → registration → live/replay → checkout) the platform optimizes for the Lead (registration) and cannot see the sale at all. Insert two breakpoints between the Landing-page layer and the Full-funnel layer: **Registration → Show-up** (attendance rate, from the webinar room / Sheet) and **Show-up → Purchase** (from the backend export). CPL is the only ad-side number; everything past registration is read downstream, not from the platform. A healthy CPL with weak full-funnel ROAS almost always breaks at Show-up→Purchase — the fix is the webinar and the close, not the campaign.

---

## REPORT COLUMN SETUP (do this once, before you read anything)

The diagnostic only works if Ads Manager shows the right columns. Build a saved custom column set once and reuse it for every read so the numbers are always comparable. In Meta Ads Manager: **Columns → Customise Columns**, add the set below, tick **Save as preset**, name it "MIA Read-the-Funnel".

**The MIA Meta column set (in funnel-read order):** delivery · amount spent · budget · results · purchases · purchase ROAS · adds to cart · leads · cost per result · reach · impressions · CPM · hook rate · hold rate · thruplay completion rate · frequency · results ROAS · clicks (all) · CTR · quality ranking · landing page views · cost per landing page view.

- **Hook rate, hold rate, and ThruPlay completion usually aren't default columns** — add them as **custom metrics** (Customise Columns → Create Custom Metric): hook rate = 3-second video plays ÷ impressions; hold rate = 15-second (or ThruPlay) plays ÷ 3-second plays; ThruPlay completion = 100% plays ÷ ThruPlays.
- **Quality ranking** is only in the campaign-level view, not the placement/age breakdown exports.
- Use the same saved set for every scheduled read (Day 3/5/7/12) and for the weekly report.

---

## THE TEMPLATE (copy, fill, append newest-on-top)

```markdown
### Funnel-Layer Diagnostic — Day [N] ([YYYY-MM-DD])

Per [[Meta Ads Playbook]] §9 Metric Diagnosis Table.

**Snapshot date:** [YYYY-MM-DD] ([Day N cumulative / window])

**Source:** [path to platform CSV export] + [Selar/sales export, window]

**Campaign totals:** [spend] / [attributed purchases] / [LPVs] / [ATCs] / [Leads] / [impressions] / [reach] across [N] ads. Pacing: [spend/day] vs [planned] ([%]).

| Layer | Metric | Reading | Status | Note |
|---|---|---|---|---|
| Pre-flight | Delivery Status | [Active/…] | 🟢/🟡/🔴 | |
| Pre-flight | Spend vs. Planned | [x/day vs planned] | 🟢/🟡/🔴 | |
| Auction cost | **CPM (read first)** | [value vs NG/diaspora target] | 🟢/🟡/🔴 | high CPM inflates everything downstream |
| Creative (first 2s) | Hook Rate (3s views ÷ impressions) | [%] | 🟢/🟡/🔴 | target 20%+ NG / 25%+ diaspora; low = first 1-2s isn't stopping the scroll |
| Creative (mid) | Hold Rate (15s views ÷ 3s views) | [%] | 🟢/🟡/🔴 | target 15%+ NG / 20%+ diaspora; low = the middle loses people, rewrite it |
| Creative (end) | ThruPlay Completion (100% plays ÷ ThruPlays) | [%] | 🟢/🟡/🔴 | target 25%+ (15s) / 15%+ (30s) / 8%+ (60s); low = weak ending, drags, or too long |
| Creative + Offer match | CTR (link) | [%] | 🟢/🟡/🔴 | |
| Creative × Audience | CPC (link) | [value] | 🟢/🟡/🔴 | |
| Audience saturation | Frequency | [value] | 🟢/🟡/🔴 | cold <2.0, RT <4.0 |
| Landing page | CVR (post-click) | [%] | 🟢/🟡/🔴 | 2-5%+ target; if low + CTR healthy → destination OR offer |
| Full funnel | True CPA (Selar-corrected) | [value] | 🟢/🟡/🔴 | |
| Full funnel | True ROAS (Selar) | [value] | 🟢/🟡/🔴 | ≥2x floor, 3x+ healthy |
| Creative algorithmic | Quality Ranking | [Above/Avg/Below] | 🟢/🟡/🔴 | Below = rebuild creative, not placement |

**[Sales backend] truth cross-check ([window]):**

| Source | Sales | Notes |
|---|---|---|
| [Selar channel, full window] | [n] | |
| [platform]-attributed | [n] | |
| Capture rate | [%] | attributed / Selar |

**Layer breaking right now:**

1. [Name the broken layer + the evidence. Stop here if upstream is the break.]

**Action gated on this read:**

1. [Specific action tied to the broken layer — pause / refresh / reallocate / scale, with the threshold that justifies it.]
2. [Next scheduled read + what leading indicator confirms or kills the hypothesis.]
```

Add a **per-ad incremental table** (spend/purchases between the last read and this one → marginal CPA) whenever a campaign has multiple ads and you need to see which ad is decaying — that marginal read catches efficiency decay a cumulative read hides.

---

## STATUS KEY

- 🟢 in healthy range for the geo (NG vs diaspora thresholds differ — see the platform playbook §9).
- 🟡 off-threshold but not yet actionable / trending wrong.
- 🔴 broken — this layer gates the action.

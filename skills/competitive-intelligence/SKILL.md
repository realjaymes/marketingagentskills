---
name: competitive-intelligence
description: "Builds a complete competitive intelligence pipeline: gather intel, synthesize it into a SWOT, construct a one-per-competitor battlecard, then validate and refresh it with win-loss interview evidence. Use when the user wants a 'battlecard,' 'competitor battlecard,' 'competitive intelligence,' 'win-loss analysis,' 'win-loss interview,' 'why did we lose that deal,' 'competitor SWOT,' or 'objections we get about [competitor].' Distinct from competitor-alternatives, which builds public-facing 'vs' and alternative pages for SEO — this skill builds internal, rep-facing sales assets."
version: "1.0.0"
argument-hint: "[competitor name]"
---

# Competitive Intelligence & Win-Loss

You are a competitive intelligence strategist who arms sales teams with accurate, evidence-based competitor knowledge — not guessed positioning.

## When to Use This Skill

Invoke when the user:
- Wants a battlecard for a specific competitor
- Needs to gather or organize competitive intelligence
- Wants to run or synthesize win-loss interviews
- Asks "why do we lose to [competitor]" or "how do we compare to [competitor]"
- Needs objection responses tied to a specific competitor

**Not this skill**: public-facing "[Product] vs [Competitor]" or "[Product] alternative" pages for SEO — that's `competitor-alternatives`. This skill is for internal, rep-facing material. For general objection handling not tied to a specific competitor, and for demo scripts, decks, and one-pagers, see `sales-enablement`.

## Before Starting

Gather this context (ask if not provided):

### Required Inputs
- **Your product**: what you sell and to whom
- **The competitor**: which one this pipeline is being built for
- **What's driving this**: a specific deal, a recurring loss pattern, a new competitor entering the market, or a standing quarterly refresh

### Optional Context
- Existing customer research or ICP docs (see `customer-research`, `icp-persona`)
- Prior win-loss interviews or notes
- Known pricing, features, or positioning for the competitor

---

## Why One Pipeline, Not Three Separate Documents

A competitive intel checklist that dead-ends after data collection, a SWOT that restates the checklist without translating it into "so what," and a battlecard that crams multiple competitors into one table are three disconnected documents doing one job badly. This skill runs them as stages of a single pipeline — gather, synthesize, weaponize, validate — because each stage's output is the next stage's input, and none of them are useful in isolation.

---

## 0. Foundations & Cadence

**Scope decision.** Not every competitor deserves a full battlecard. Rank competitors by deal frequency and win-rate risk. Build full cards only for the top 3-5; keep a lighter one-paragraph note for the long tail.

**Cadence.** Full refresh quarterly for top-tier competitors, or immediately when: a competitor changes pricing, a rep reports losing to a competitor not yet carded, or a win-loss interview surfaces new intelligence.

**Ownership.** One owner per competitor card. Intelligence without an owner goes stale silently.

---

## 1. Intelligence Gathering

Six categories, each entry carrying **source**, **confidence** (verified / inferred / stale), and **last verified** date. An unsourced claim doesn't reach the battlecard.

- **Market** — target customers and segments, customer count, notable clients, geography, review sentiment and trend.
- **Product** — product suite, defining features, value drivers, pricing versus yours, current promotions, perceived strengths and weaknesses, free trial/pilot availability, partnerships.
- **Positioning** — how they differentiate, their messaging, listed use cases, how messaging shifts by segment.
- **Marketing** — tagline, channel activity and content mix, ABM versus industry-wide targeting, keywords bid on, social engagement, organic ranking versus yours, tools/calculators they run.
- **Sales & customer success** — sales process and cycle length, sales asset types, support response time, complaint escalation pattern.
- **Company** — recent acquisitions or funding, growth trajectory, headcount by department, hiring surges (a leading indicator of where they're about to invest).

Prioritize Product, Positioning, and Sales for the battlecard; the rest mostly inform Section 2's synthesis.

---

## 2. SWOT Synthesis

For each top-tier competitor, translate Section 1's findings into Strengths, Weaknesses (including *perceived* weaknesses — a prospect's mistaken belief is just as usable as a real one), Opportunities, and Threats.

**The translation test.** Every SWOT line must answer: does this become a Key Differentiator, a Customer Pain Point, an Objection, or a Why-We-Win proof point on the battlecard? If it doesn't map to one of those four, it's interesting but not actionable — leave it in the intelligence log, not the card.

---

## 3. Battlecard Construction

One card per competitor. Never merge competitors into a shared table — a rep needs the one card for who they're actually up against, fast.

- **Overview** — your company, top 1-3 features, target audience.
- **This competitor, in one line** — who they are and who they're strongest with.
- **Key differentiators** — a scored comparison on the axes that actually matter for this product, each with a one-line "why this matters to the buyer."
- **Why we win** — 3 benefits, each with a proof point sourced from a real win (ideally from Section 4's win-loss evidence), never invented.
- **Customer pain points** — why buyers are in the market at all, sourced from Section 1.
- **Handling objections** — objection/response pairs specific to this competitor, sourced from Section 4 where possible.
- **Key features** — feature, benefit, and how it beats or concedes to this competitor's equivalent.
- **Questions to ask** — 2-3 discovery questions that surface whether this competitor is a real threat in this specific deal.
- **Pricing** — comparison, sourced and dated, flagged stale if not reverified this quarter.
- **Segment note** — which ICP tier this card applies to.
- **Relevant customers** — reference customers sized and shaped like the prospect.
- **Third-party validation** — accreditations, analyst mentions, an attributed customer quote.
- **Last verified** — date and owner, visible at the top.

---

## 4. Win-Loss Validation

The highest-confidence source for Section 3's Why We Win and Objection Handling — real deal evidence beats guessed positioning every time.

**Trigger.** Interview within 1-2 weeks of close, while the decision is still fresh.

**Sampling.** Prioritize: deals lost to a competitor being carded, deals won against a competitor being carded, and any surprising outcome.

**Recruitment.** Won-deal invite: warm, curiosity-framed, low-pressure. Lost-deal invite: explicitly zero-sales-pressure, framed as helping you improve. Interviewer should ideally not be the closing rep, to reduce social-desirability bias.

**Interview guide** — trimmed to a recommended ~8 questions per flow, not a 2-hour master list:

*Won-deal flow*: business drivers, brand perception, selection criteria, committee, solution fit, competition, selection (what tipped it), sales experience.

*Lost-deal flow*: business drivers, selection criteria, competition (what won and why), solution gaps, selection (primary reason, what could we have done differently), price, sales experience, future intent.

**Loss-reason taxonomy.** Code every interview into one primary category before synthesizing: Price, Product gap, Competitor advantage, Timing, No decision, Sales experience. Cluster by category, pull 3-5 verbatim quotes per category, and calculate frequency. A single interview is an anecdote; 3+ interviews citing the same category is a pattern worth acting on.

**Confidence labeling** (same standard as `customer-research`): High = 3+ independent interviews, unprompted, consistent across segments. Medium = 2 interviews or prompted only. Low = single source, a hypothesis to validate, not a finding to act on.

---

## 5. Feeding the System

- **Competitor advantage** findings → update the battlecard's Why We Win and Handling Objections with real evidence.
- **Product gap** findings → route to product/roadmap, tagged with frequency and deal value at stake.
- **Sales experience** findings → route to `sales-enablement`'s objection handling and discovery material.
- **Price** findings → inform `pricing-strategy` work.
- A recurring loss-reason pattern is also raw material for a storytelling engine's "false path" / status-quo section, if one is in use.

---

## Output Format

Output as Markdown with: Sections 1-4 in order, tables for the intelligence log, SWOT, key differentiators, and pricing comparison, and one battlecard per competitor (never a multi-competitor grid). Every claim in Section 3 carries a source and confidence rating, or a `[proof needed]` placeholder — never an invented number.

## Constraints

- No claim on a battlecard without a source and confidence rating.
- One card per competitor, always.
- Segment every card; "the market" is not one buyer.
- Never fabricate a testimonial, quote, or figure. Mark unverified claims `[proof needed]`.
- Never run the full win-loss question bank by default; use the recommended 8-question flow per won/lost.
- Don't act on a single win-loss interview; wait for 3+ independent sources before it changes a battlecard.
- Recheck pricing and positioning claims every quarter minimum.

---

## Reference Examples

Each worked example runs the full pipeline (intelligence → SWOT → battlecard → win-loss validation) for one company against a real, named competitor:

- [Fireflies vs. Otter.ai](references/example-fireflies.md) — PLG-vs-PLG dynamics, Considered complexity
- [Notion vs. Confluence](references/example-notion.md) — prosumer flexibility vs. enterprise-structure positioning, Simple-to-Considered
- [PostHog vs. Mixpanel/Amplitude](references/example-posthog.md) — unified-platform vs. point-tool dynamics, Considered-to-Enterprise

Figures and specific claims in the examples are marked illustrative; they demonstrate the framework, not verified facts about the named real companies.

---

## Related Skills

- **competitor-alternatives**: for public-facing "vs" and alternative pages, not internal battlecards
- **sales-enablement**: for general objection handling, demo scripts, decks, and one-pagers not tied to a specific competitor
- **customer-research**: shares the confidence-labeling standard used in win-loss synthesis
- **product-positioning**: sets the differentiation claims this skill tests against real competitors
- **pricing-strategy**: consumes price-related win-loss findings

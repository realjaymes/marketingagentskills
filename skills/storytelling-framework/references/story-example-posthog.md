# Story Example: PostHog

Usage-based, open-source developer analytics platform (product analytics, session replay, feature flags, experiments on one event schema). Multi-product, self-serve with a sales-assisted enterprise/self-hosted motion. Considered complexity. Numbers marked illustrative are placeholders; do not treat them as real.

## Story Bible

### 0. Story Objective & Calibration

**Objective**: get an engineering or product lead evaluating fragmented analytics tooling to start a discovery conversation instead of renewing three separate vendor contracts.

**Calibration**: B2B, Considered complexity (leaning Enterprise for self-hosted/security-reviewed deals).

**Output destination**: Sales & Pitch Narrative (Mode B), for outbound and the first-call talk track.

### 1. The Hero

A startup engineer or product manager at a Series A-B company who needs to understand user behavior but is currently stitching together several point tools to do it.

### 2. The World As It Is

Analytics live in one tool, session replays in another, feature flags in a third, and none of them share the same event data. Answering "did this feature actually help retention" means exporting data from three dashboards and reconciling it by hand.

### 3. The Want

Practical: one platform with product analytics, replays, and feature flags on the same event data. Identity: to be the team that ships data-informed, not the team that argues from opinion because pulling the real numbers takes too long.

### 4. The Problem

- **External** — fragmented tooling means no single source of truth for user behavior, so answering a real product question takes hours of manual reconciliation across tools.
- **Internal** — frustration at being the "data person" who has to manually stitch together numbers that should already agree with each other.
- **Philosophical** — a startup's own product usage data shouldn't be locked behind five vendor dashboards that don't talk to each other. It's the team's data, and reassembling it manually is friction that shouldn't exist.

### 5. The False Path

Bolting together a legacy analytics tool, a separate session-replay tool, and a separate feature-flag service, each billed and configured independently, with engineering time spent gluing them together instead of shipping product.

### 6. The Guide

**Empathy**: built and marketed by engineers who hit this exact fragmentation problem at a previous startup, so the pitch opens with "we got tired of stitching tools together too," not a feature list.

**Authority**: open-source core, self-hostable, product analytics, replays, feature flags, and experiments on one shared event schema, adopted by thousands of engineering teams (illustrative).

### 7. The Plan

Install the SDK once, get analytics, replays, and flags on the same event data immediately, self-host or use cloud depending on data requirements. No separate billing relationship per capability.

### 8. The Stakes

| Cost of inaction | Reward of action |
|---|---|
| Product decisions keep getting made on partial or manually reconciled data; engineering time keeps going to tool-gluing instead of features; usage data stays fragmented across vendors | One event schema powers every product question; engineering time goes back to the product; decisions get made faster because the data's already unified |

### 9. The Call to Action

**Direct**: start free, self-host or cloud.

**Transitional**: read how the unified event schema actually works.

### 10. World As It Could Be

A PM asks "did the new onboarding flow improve activation," and the answer comes from one dashboard in minutes, not a Friday afternoon spent exporting CSVs from three tools.

### 11. Proof

`[proof needed — pull a verified team's before/after tool-consolidation or decision-speed stat before use in a live deck]`

---

## Applied: Sales & Pitch Narrative (Mode B)

Leads with Part 2 and Part 8 before naming the specific team, per Mode B's structure.

**Opening beat**: "Most product teams under 50 engineers are running 3-4 separate analytics tools that don't share data, and it's costing them the one thing that actually matters: how fast they can answer 'is this working.'" (World As Is, framed as an industry pattern.)

**Second beat**: "Keep gluing tools together, and every product decision takes longer than it should. Unify the event schema, and 'did this feature work' becomes a 5-minute question instead of a Friday project." (Stakes, stated before introducing the hero, per Raskin's structure.)

**Third beat**: introduce the specific team's situation (Parts 1, 3, 4) as the concrete instance of the pattern just named.

**Fourth beat**: Guide (empathy + authority), Plan, close on the Direct CTA.

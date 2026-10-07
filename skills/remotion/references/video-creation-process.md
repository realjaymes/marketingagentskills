# Remotion Video Creation Process

A structured process for creating programmatic videos with Remotion. Follow these steps sequentially. Step 2 selects 3-5 concepts from the catalog based on the brief and cold audience optimization. Steps 4 and 5 require approval before implementation begins.

---

## Step 0: Brand Identification

Before any creative work, identify the brand. Ask the user: **"What brand is this video for?"**

**If the brand is MIA** (see Step 5), use its theme directly. No further brand questions needed.

**If the brand is not listed**, ask the user to provide a brand website URL or brand guidelines document. Extract from the website/guidelines: background color, primary accent, secondary accent, text colors, font family, and theme (light/dark). If no guidelines exist, ask for at minimum: primary color, background color, and font preference.

---

## Step 1: Creative Brief

Gather and lock the following before any creative work begins.

| Field | Description | Example |
|-------|-------------|---------|
| **Purpose** | Why does this video exist? What problem does it solve? | "Explain the Agentic Loop Framework for prospects who land on the homepage" |
| **Audience** | Who is watching? What do they already know? | "B2B marketing leaders evaluating growth partners" |
| **Core message** | One sentence. If the viewer remembers one thing, what is it? | "The product runs a continuous insight-hypothesis-action loop that compounds over time" |
| **Content type** | What kind of asset is this video promoting? | blog-post, case-study, tool-launch, webinar, etc. |
| **Distribution channels** | Where will this video live? List all intended placements | Website embed, LinkedIn post, sales deck |
| **CTA** | What should the viewer do after watching? | Visit the product site |
| **Source assets** | Existing brand components, website sections, design files to reference | `LoopFramework.astro`, brand color palette |
| **Tone** | Technical, conversational, bold, minimal, playful? | "Minimal, confident, technical but accessible" |
| **Brand** | Brand identified in Step 0 | MIA or custom |

### Brief Template

```
Purpose: [Why this video exists]
Audience: [Who is watching]
Core message: [One sentence]
Content type: [blog-post, case-study, webinar, podcast, lead-magnet, product-update, tool-launch, industry-report, event-recap, client-testimonial, playbook, template, ai-demo, custom-gpt]
Channels: [Where it will be distributed]
CTA: [What the viewer should do next]
Source assets: [Files, components, or URLs to reference]
Tone: [Descriptive words for the feel]
Brand: [Brand name from Step 0]
```

---

## Step 2: Concept Selection (3-5 Recommended Concepts)

After locking the creative brief, analyze it to select the best video concepts for this specific use case. Do not present a fixed set of variants. Draw from the concept catalog in [concept-catalog.md](concept-catalog.md).

The catalog contains 18 primary concepts, 8 visual style modifiers, and 5 cold audience hook patterns. Read it before generating recommendations.

### Selection Process

1. **Score concepts against the brief.** For each concept in the catalog, evaluate:
   - Does the concept's "Best For" match the content type?
   - Can the core message land in 15-30 seconds with this structure?
   - Does the concept work at the target duration and dimensions?
   - Does the brief provide the data/visuals this concept needs?

2. **Apply the cold audience filter.** For each scored concept, evaluate:
   - Can a viewer with ZERO prior context understand the value in the first 3 seconds?
   - Does the concept create scroll-stopping visual motion in the opening beat?
   - Does the concept avoid requiring prior knowledge of the brand, product, or problem space?
   - If the concept naturally front-loads a result or data point (metric-counter, animated-infographic, before-after), it is inherently stronger for cold audiences than narrative concepts that need setup time.

3. **Select a hook pattern.** For each recommended concept, pair it with a hook pattern from the catalog:
   - Content with data → result-first
   - Product launches and tools → pattern-interrupt
   - Thought leadership and education → curiosity-gap
   - Trust-building content → social-proof-hook
   - Competitive and pricing content → loss-aversion

4. **Present 3-5 recommended concepts** as one-page briefs. For each:
   - Concept name (from the catalog) and one-sentence description
   - Why it fits this brief (1-2 sentences referencing the specific content and audience)
   - Recommended hook pattern and opening beat description
   - Scene-by-scene table (from the catalog template, customized for this content)
   - Optional visual style modifier if one enhances the concept

5. **Rank the recommendations.** Mark the top recommendation and explain why.

6. **User selects one (or a hybrid of two).** Lock the selected concept before proceeding to Step 3.

### Cold Audience Optimization Rules

These rules apply to all concept recommendations and override content-type defaults when they conflict:

- **Default assumption: cold audience.** Unless the brief explicitly states the audience is warm (retargeting, existing users, newsletter subscribers), assume zero brand awareness.
- **First scene requirements for cold audiences:**
  1. A visual pattern interrupt (motion, color contrast, or scale change)
  2. Text that names a problem or result the viewer recognizes WITHOUT knowing the brand
  3. No brand identification in scene 1 (save brand card for scene 2 or later)
- **Hook pattern restrictions for cold audiences:** Use pattern-interrupt, result-first, or loss-aversion. Avoid curiosity-gap unless the stat/claim is universally relatable without brand context.
- **Concept flexibility:** If no concept in the catalog fits the brief well for a cold audience, create a hybrid or adapt an existing concept. The catalog is a starting library, not a constraint.

### Presenting Concepts

When presenting concepts to the user:
1. Generate the recommended 3-5 concepts as one-paragraph summaries with scene-by-scene tables
2. Highlight the top recommendation and explain why
3. The user selects one concept or requests a hybrid of two
4. Lock the selected concept before proceeding to Step 3

---

## Step 3: Format and Specs

Specs are derived from the brief and selected variant. Use the decision matrix below.

### Format Decision Matrix

| Distribution Channel | Recommended Dimensions | Duration Range | Notes |
|---------------------|----------------------|----------------|-------|
| LinkedIn feed post | 1080x1080 (1:1) | 15-30s | Square performs best in feed |
| LinkedIn carousel/article | 1920x1080 (16:9) | 30-60s | Widescreen for embedded context |
| Twitter/X feed | 1080x1080 (1:1) or 1920x1080 (16:9) | 15-45s | Under 2:20 total limit |
| Instagram Reels / TikTok | 1080x1920 (9:16) | 15-60s | Vertical, full-screen |
| Instagram feed | 1080x1080 (1:1) | 15-30s | Square |
| Website embed | 1920x1080 (16:9) | 15-60s | Widescreen, can be longer |
| Sales deck / presentation | 1920x1080 (16:9) | 15-45s | Match slide dimensions |
| Email embed (GIF) | 600x600 or 800x450 | 5-10s | Must be lightweight |

### Specs Template

```
Dimensions: [width]x[height]
Duration: [X] seconds ([X * fps] frames)
FPS: 30 (default)
Composition ID: [PascalCase identifier]
Loop: [yes/no - does last frame connect to first?]
Output formats: [mp4, gif, webm]
```

### Multi-Channel Adaptation

If the video targets multiple channels with different formats, define a **primary format** and list **adaptations**:

```
Primary: 1080x1080 (LinkedIn + Twitter feed)
Adaptations:
  - 1920x1080 (website embed, sales deck)
  - 1080x1920 (Instagram Reels)
```

Adaptations may require layout adjustments, not just cropping. Flag these during scene breakdown.

---

## Step 4: Scene Breakdown

This is the most critical step. Every scene must be defined before code is written. Changes to scenes after implementation are expensive. Use the selected variant's scene template as the starting structure, then customize.

### Narrative Arc

Short-form video follows a consistent structure:

```
Hook (stop the scroll)
  → Context (who/what, brand identification)
    → Core Content (the thing itself, built progressively)
      → Proof/Application (why it matters, use cases)
        → CTA (what to do next)
```

Not every video needs all five stages. A 10-second GIF might only have Hook + Core + CTA.

### Scene Definition Template

For each scene, define:

| Field | Description |
|-------|-------------|
| **Scene number and name** | Sequential identifier (e.g., "Scene 3: Framework Title") |
| **Timing** | Start and end in seconds (frames are calculated from fps) |
| **Copy** | Exact text that appears on screen. Bold key words. Indicate hierarchy (headline, description, label) |
| **Animation description** | What moves, in what order, how it enters/exits. Use plain language, not code |
| **Visual elements** | Icons, shapes, diagrams, images, or UI components in the scene |
| **Transitions** | How this scene enters and how it exits (fade, slide, cut, overlap) |
| **Purpose** | Why this scene exists in the narrative. One sentence |

### Scene Table Format

| # | Name | Time | Copy | Animation | Purpose |
|---|------|------|------|-----------|---------|
| 1 | Hook | 0-3.5s | "You have the data." / "You have the tools." / "You're missing **the loop**." | Lines fade up sequentially, 0.7s apart. "the loop" highlighted in accent color. All fade out together | Stop the scroll. Name the tension |
| 2 | Brand | 3.5-6s | "Product name" / one-line descriptor | Logo springs in with bounce. Description fades in below | Brand identification |
| ... | ... | ... | ... | ... | ... |

### Timing Guidelines

| Video Duration | Recommended Scene Count | Avg Scene Duration |
|---------------|------------------------|-------------------|
| 10s | 3-4 | 2.5-3.3s |
| 15s | 4-6 | 2.5-3.75s |
| 30s | 8-12 | 2.5-3.75s |
| 60s | 12-20 | 3-5s |

Rules of thumb:
- Hook scene: 2-4 seconds maximum
- CTA scene: 2-3 seconds (should hold, not rush)
- Core content scenes can be longer if building progressively
- Transition overlaps reduce total duration (account for this)

### Approval Gate

Present the complete scene table to the user for approval. Lock copy, timing, and narrative structure before proceeding. Animation details can be refined during implementation, but the scene list and copy should not change.

---

## Step 5: Visual Design

### Brand Theme Preset

Use this for MIA. Skip color questions when the brand is MIA.

| Brand | Background | Primary Accent | Secondary Accent | Text Primary | Text Muted | Font | Theme |
|-------|-----------|---------------|-----------------|-------------|-----------|------|-------|
| MIA | `#F7F4FA` / `#1c1422` (dark) | `#F1DE71` (Yellow) | `#7184F1` (Purple) | `#1c1422` / `#f7f4fa` (dark) | `rgba(28,20,34,0.62)` | system-ui, -apple-system, Segoe UI | Light |

**MIA accent palette**: Blue `#71C4F1`, Purple `#7184F1`, Pink `#F171C4`, Green `#71F19E`

**Custom brands**: Colors come from the product's own screens or the brand kit. Extract them from the brand website or guidelines provided in Step 0. Fill the same roles below.

### Color Palette

Define the full palette before implementation. Minimum required:

| Role | Purpose | Example |
|------|---------|---------|
| **Background** | Main background color | `#09090b` |
| **Primary accent** | Key highlights, important elements | `rgba(139, 92, 246, 1)` (purple) |
| **Secondary accent** | Supporting elements, secondary nodes | `rgba(59, 130, 246, 1)` (blue) |
| **Tertiary accent** | Additional differentiation (if needed) | `rgba(236, 72, 153, 1)` (pink) |
| **Text primary** | Headlines, labels | `#fafafa` |
| **Text secondary** | Descriptions, body text | `#a1a1aa` |
| **Text tertiary** | Subtle labels, de-emphasized text | `#71717a` |
| **Border/divider** | Subtle separators | `rgba(255, 255, 255, 0.08)` |

### Typography

| Element | Font | Weight | Size (at 1080px) |
|---------|------|--------|-------------------|
| Headline | [Font family] | Bold (700) | 48-64px |
| Subheadline | [Font family] | Semi-bold (600) | 32-40px |
| Body/description | [Font family] | Regular (400) | 24-28px |
| Label/tagline | [Font family] | Medium (500) uppercase | 16-20px |

### Animation Style

Choose the dominant motion style:

| Style | When to Use | Remotion Implementation |
|-------|-------------|------------------------|
| **Spring (bouncy)** | Entrances, playful brand, emphasis | `spring({ damping: 12, mass: 0.5 })` |
| **Spring (smooth)** | Professional, subtle entrances | `spring({ damping: 200 })` |
| **Spring (snappy)** | Quick, confident transitions | `spring({ damping: 20, stiffness: 300 })` |
| **Linear** | Progress bars, path drawing, mechanical motion | `interpolate()` with no easing |
| **Ease out** | Exits, elements leaving the scene | `interpolate()` with `Easing.out(Easing.quad)` |

### Source of Truth

If the video must match an existing design (website, app, brand guide):

```
Source file: [path to component or design file]
Elements to match: [colors, layout, icons, typography]
Last verified: [date]
```

---

## Step 6: Architecture Decision

This step is deterministic based on scene complexity. The agent resolves this, not the user.

### File Structure Decision

| Condition | Approach |
|-----------|----------|
| Under 15 scenes, no reusable components | Single file (all scenes in one `.tsx`) |
| 15+ scenes or reusable scene components | Multi-file (scene components in `scenes/` directory) |
| Shared visual elements across scenes | Persistent layer with opacity envelope |
| Multiple compositions sharing components | Shared `components/` directory |

### Timing System

Always use a centralized timing constant:

```typescript
const T = {
  hookStart: 0,        hookEnd: 105,
  brandStart: 105,     brandEnd: 185,
  // ... all scene boundaries
};
```

This makes timing adjustments propagate automatically.

### Composition Registration

Register in `Root.tsx` with proper folder organization:

```typescript
<Folder name="ProjectName">
  <Composition
    id="CompositionId"
    component={VideoComponent}
    durationInFrames={totalFrames}
    fps={30}
    width={1080}
    height={1080}
  />
</Folder>
```

---

## Step 7: Implementation

With scenes, design, and architecture locked, write the code.

### Implementation Checklist

- [ ] Create timing constants from scene breakdown
- [ ] Set up color and typography constants from design decisions
- [ ] Build scene-by-scene, previewing each in Remotion Studio
- [ ] All animation driven by `useCurrentFrame()` (no CSS transitions)
- [ ] Use Remotion components (`<Img>`, `<Video>`, `<Audio>`) not native HTML
- [ ] Use `staticFile()` for all public folder assets
- [ ] Test transitions between scenes for smooth flow
- [ ] Verify total duration matches spec
- [ ] Preview at 1x speed for pacing check

### Common Patterns

| Pattern | Implementation |
|---------|---------------|
| Sequential text lines | `interpolate()` with staggered `inputRange` offsets |
| Element entrance | `spring()` with scale from 0 to 1 |
| Fade in/out | `interpolate()` on opacity, 0 to 1 |
| Path drawing | SVG `stroke-dashoffset` animated via `interpolate()` |
| Persistent background element | Single opacity envelope wrapping shared layer |
| Cycling content | Array of items with calculated frame ranges per item |

---

## Step 8: Output Documentation

Generate an output document for every completed video. This serves as the reference for future edits, adaptations, and handoffs.

### Output Document Template

```markdown
# [Video Title]

[One sentence description of what this video is and what it's for.]

## Specs

| Property | Value |
|----------|-------|
| Format | [dimensions] |
| Duration | [X] seconds ([frames] frames) |
| FPS | [fps] |
| Composition ID | `[ID]` |
| Source file | `src/[filename].tsx` |

## How to Preview

[Commands to preview in Remotion Studio]

## How to Render

[Commands for each output format: mp4, gif, webm]

## Distribution

[List of intended placements and channels]

## Scene Breakdown

[Full scene table from Step 3, updated with final timing]

## Color Palette

[Final palette table from Step 4]

## Timing Configuration

[The T constant or timing system used]

## Architecture Notes

[File structure, key decisions, shared layers]

## Source of Truth

[Reference files for design consistency]

## Iteration Guide

[Table of common changes and where to make them]
```

---

## Process Summary

```
Step 0: Brand Identification      → Identify brand, use the MIA theme or extract from website/guidelines
Step 1: Creative Brief            → Lock purpose, audience, message, content type, channels, CTA, brand
Step 2: Concept Selection       → Analyze brief, select 3-5 concepts from catalog, optimize for cold audience
Step 3: Format and Specs          → Resolve dimensions, duration, fps from brief + selected variant
Step 4: Scene Breakdown           → Define every scene with copy, timing, animation  ← APPROVAL GATE
Step 5: Visual Design             → Lock colors, typography, animation style         ← APPROVAL GATE
Step 6: Architecture Decision     → Agent resolves file structure and timing system
Step 7: Implementation            → Write code against locked decisions
Step 8: Output Documentation      → Generate reference doc for the completed video
```

Steps 4 and 5 are approval gates. Everything before them is input gathering and variant selection. Everything after them is execution.

**Content rule**: Every concept must be self-explanatory. A viewer scrolling with zero context should understand the value from the video alone. No scene should depend on external knowledge. Copy must carry the full message independently. Always assume a cold audience unless the brief says otherwise.

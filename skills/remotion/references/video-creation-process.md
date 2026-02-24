# Remotion Video Creation Process

A structured process for creating programmatic videos with Remotion. Follow these steps sequentially. Steps 1-4 require approval before implementation begins.

---

## Step 1: Creative Brief

Gather and lock the following before any creative work begins.

| Field | Description | Example |
|-------|-------------|---------|
| **Purpose** | Why does this video exist? What problem does it solve? | "Explain the Agentic Loop Framework for prospects who land on the homepage" |
| **Audience** | Who is watching? What do they already know? | "B2B marketing leaders evaluating growth partners" |
| **Core message** | One sentence. If the viewer remembers one thing, what is it? | "GrowthNode runs a continuous insight-hypothesis-action loop that compounds over time" |
| **Distribution channels** | Where will this video live? List all intended placements | Website embed, LinkedIn post, sales deck |
| **CTA** | What should the viewer do after watching? | Visit growthnode.ai |
| **Source assets** | Existing brand components, website sections, design files to reference | `LoopFramework.astro`, brand color palette |
| **Tone** | Technical, conversational, bold, minimal, playful? | "Minimal, confident, technical but accessible" |

### Brief Template

```
Purpose: [Why this video exists]
Audience: [Who is watching]
Core message: [One sentence]
Channels: [Where it will be distributed]
CTA: [What the viewer should do next]
Source assets: [Files, components, or URLs to reference]
Tone: [Descriptive words for the feel]
```

---

## Step 2: Format and Specs

Specs are derived from the brief, not chosen arbitrarily. Use the decision matrix below.

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

## Step 3: Scene Breakdown

This is the most critical step. Every scene must be defined before code is written. Changes to scenes after implementation are expensive.

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
| 2 | Brand | 3.5-6s | "GrowthNode" / "AI Native Growth Engineers" | Logo springs in with bounce. Description fades in below | Brand identification |
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

## Step 4: Visual Design

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

## Step 5: Architecture Decision

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

## Step 6: Implementation

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

## Step 7: Output Documentation

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
Step 1: Creative Brief         → Lock purpose, audience, message, channels, CTA
Step 2: Format and Specs       → Resolve dimensions, duration, fps from brief
Step 3: Scene Breakdown        → Define every scene with copy, timing, animation  ← APPROVAL GATE
Step 4: Visual Design          → Lock colors, typography, animation style         ← APPROVAL GATE
Step 5: Architecture Decision  → Agent resolves file structure and timing system
Step 6: Implementation         → Write code against locked decisions
Step 7: Output Documentation   → Generate reference doc for the completed video
```

Steps 3 and 4 are approval gates. Everything before them is input gathering. Everything after them is execution.

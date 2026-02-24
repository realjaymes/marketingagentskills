---
name: remotion
version: 2.0.0
description: Remotion video creation in React - process workflow and technical best practices
metadata:
  tags: remotion, video, react, animation, composition, programmatic-video
---

## When to Use

Use this skill when:
- Creating a new Remotion video from scratch
- Modifying an existing Remotion composition
- Debugging Remotion animation or rendering issues
- Working with any Remotion-specific APIs or components

## Video Creation Process

When creating a new Remotion video, follow this 7-step process. Steps 3 and 4 are approval gates. Do not write code until both are approved.

For the full process document with templates and decision matrices, read [references/video-creation-process.md](references/video-creation-process.md).

### Step 1: Creative Brief

Gather and lock before any creative work:

```
Purpose: [Why this video exists]
Audience: [Who is watching]
Core message: [One sentence]
Channels: [Where it will be distributed]
CTA: [What the viewer should do next]
Source assets: [Files, components, or URLs to reference]
Tone: [Descriptive words for the feel]
```

### Step 2: Format and Specs

Resolve from the brief using the format decision matrix:

| Channel | Dimensions | Duration |
|---------|-----------|----------|
| LinkedIn/Instagram feed | 1080x1080 | 15-30s |
| Website/presentation | 1920x1080 | 15-60s |
| Reels/TikTok/Stories | 1080x1920 | 15-60s |
| Email (GIF) | 600x600 or 800x450 | 5-10s |

Default FPS: 30. Only use 60 if smooth motion is critical.

```
Dimensions: [width]x[height]
Duration: [X] seconds ([X * fps] frames)
FPS: 30
Composition ID: [PascalCase]
Loop: [yes/no]
Output formats: [mp4, gif, webm]
```

### Step 3: Scene Breakdown (APPROVAL GATE)

Define every scene before writing code. Present the scene table for approval.

**Narrative arc:**
```
Hook → Context → Core Content → Proof/Application → CTA
```

**Scene table format:**

| # | Name | Time | Copy | Animation | Purpose |
|---|------|------|------|-----------|---------|
| 1 | Hook | 0-3s | Exact text | Motion description | Why it exists |

**Timing guidelines:**

| Duration | Scene Count | Avg Per Scene |
|----------|-------------|---------------|
| 10s | 3-4 | 2.5-3.3s |
| 15s | 4-6 | 2.5-3.75s |
| 30s | 8-12 | 2.5-3.75s |
| 60s | 12-20 | 3-5s |

Lock copy, timing, and narrative structure before proceeding.

### Step 4: Visual Design (APPROVAL GATE)

Lock before implementation:

**Color palette** (minimum required roles):
- Background, Primary accent, Secondary accent
- Text primary, Text secondary, Text tertiary
- Border/divider

**Typography**: Font family, weight hierarchy, sizes at target resolution.

**Animation style**: Spring (bouncy/smooth/snappy), linear, or ease-based. Pick a dominant style.

**Source of truth**: If matching an existing design, reference the source file.

### Step 5: Architecture Decision

Agent resolves this based on scene complexity:

| Condition | Approach |
|-----------|----------|
| Under 15 scenes | Single file |
| 15+ scenes or reusable parts | Multi-file with `scenes/` directory |
| Shared elements across scenes | Persistent layer with opacity envelope |

Always use a centralized timing constant (`const T = { ... }`).

### Step 6: Implementation

Write code against locked decisions. All animation must follow Remotion rules (see Technical Reference below).

### Step 7: Output Documentation

Generate a reference doc covering: specs, preview/render commands, scene breakdown, color palette, timing config, architecture notes, iteration guide.

---

## Technical Reference

Read individual rule files for API details and code examples.

### Core Animation and Timing

- [rules/animations.md](rules/animations.md) - Animation fundamentals. All motion via `useCurrentFrame()`. No CSS transitions
- [rules/timing.md](rules/timing.md) - `interpolate()`, `spring()`, easing functions, spring configs
- [rules/sequencing.md](rules/sequencing.md) - `<Sequence>` and `<Series>` for timing, delay, and duration control
- [rules/trimming.md](rules/trimming.md) - Trim beginnings (negative `from`) and ends (`durationInFrames`)
- [rules/transitions.md](rules/transitions.md) - `<TransitionSeries>` with fade, slide, wipe, flip, clockWipe

### Media

- [rules/assets.md](rules/assets.md) - `staticFile()` for public folder assets
- [rules/videos.md](rules/videos.md) - `<Video>` with trimming, volume, speed, looping, pitch
- [rules/audio.md](rules/audio.md) - `<Audio>` with trimming, volume, speed, pitch
- [rules/images.md](rules/images.md) - `<Img>` component (ensures load before render)
- [rules/gifs.md](rules/gifs.md) - `<AnimatedImage>` for GIF/APNG/AVIF/WebP
- [rules/fonts.md](rules/fonts.md) - Google Fonts via `@remotion/google-fonts`, local fonts via `@remotion/fonts`

### Text and Captions

- [rules/text-animations.md](rules/text-animations.md) - Typewriter, word highlighting patterns
- [rules/measuring-text.md](rules/measuring-text.md) - `measureText()`, `fitText()`, `fillTextBox()`
- [rules/display-captions.md](rules/display-captions.md) - TikTok-style captions, word-by-word highlighting
- [rules/import-srt-captions.md](rules/import-srt-captions.md) - Parse `.srt` files with `parseSrt()`
- [rules/transcribe-captions.md](rules/transcribe-captions.md) - Whisper.cpp, Whisper Web, OpenAI API

### Composition and Metadata

- [rules/compositions.md](rules/compositions.md) - `<Composition>`, `<Still>`, `<Folder>`, `defaultProps`
- [rules/calculate-metadata.md](rules/calculate-metadata.md) - Dynamic duration, dimensions, and props

### Advanced

- [rules/3d.md](rules/3d.md) - `<ThreeCanvas>` with React Three Fiber
- [rules/charts.md](rules/charts.md) - SVG/D3.js charts animated via `useCurrentFrame()`
- [rules/lottie.md](rules/lottie.md) - `<Lottie>` component with `@remotion/lottie`
- [rules/tailwind.md](rules/tailwind.md) - TailwindCSS (no `transition-*` or `animate-*` classes)

### Media Utilities (Mediabunny)

- [rules/extract-frames.md](rules/extract-frames.md) - Extract video frames at timestamps
- [rules/can-decode.md](rules/can-decode.md) - Check video/audio decodability
- [rules/get-video-duration.md](rules/get-video-duration.md) - Video duration in seconds
- [rules/get-video-dimensions.md](rules/get-video-dimensions.md) - Video width and height
- [rules/get-audio-duration.md](rules/get-audio-duration.md) - Audio duration in seconds

### Layout

- [rules/measuring-dom-nodes.md](rules/measuring-dom-nodes.md) - `useCurrentScale()` for accurate measurements

---

## References

- [references/video-creation-process.md](references/video-creation-process.md) - Full process document with templates, decision matrices, and detailed guidance

---

## Hard Rules

These apply to all Remotion code. Violations will produce incorrect output.

1. **All animation driven by `useCurrentFrame()`**. No CSS transitions, no Tailwind `animate-*` or `transition-*` classes, no React Three Fiber `useFrame()`
2. **Use Remotion components** (`<Img>`, `<Video>`, `<Audio>`) not native HTML elements
3. **Use `staticFile()`** for all assets in the `public/` folder
4. **Time in seconds**: multiply by `fps` from `useVideoConfig()` to get frames
5. **No third-party animation libraries** driving motion (disable their animations, use `useCurrentFrame()` instead)

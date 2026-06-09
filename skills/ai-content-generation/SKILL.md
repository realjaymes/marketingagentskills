---
name: ai-content-generation
description: "When the user wants to create AI-generated image or video content: a faceless influencer or persona for TikTok and Instagram, a faceless YouTube channel, an AI clone or talking-head of themselves, or AI ad creative (UGC, product video, static images). Also use when the user mentions 'faceless influencer,' 'faceless channel,' 'AI avatar,' 'AI UGC,' 'talking head,' 'clone myself,' 'AI ad creative,' 'AI video ads,' or tools like Veo, Google Flow, Kling, Higgsfield, Seedance, Runway, ElevenLabs, HeyGen, Arcads, Nano Banana, Midjourney, or Ideogram. Gives step-by-step, copy-paste-prompt playbooks for each use case plus the realism rules that beat AI slop. For paid-ad strategy and targeting, see performance-marketing or paid-ads."
metadata:
  version: 1.0.0
---

# AI Content Generation

Help the user actually make AI image and video content, end to end, with copy-paste prompts at every step. This skill covers four use cases, each a self-contained, do-this-then-that playbook. The hard parts (keeping a character consistent and killing the AI-slop look) are baked into the prompts, so the user can follow the steps without prior experience.

## The core idea

The model is the easy part. What makes AI content win is the niche, the script, keeping the character or product consistent, and beating the AI-slop look. Every playbook bakes those in. Roughly 80% of quality is set before the model runs (research, script, consistency, realism); the model is the last 20%.

## Pick the use case, then open its reference

| The user wants to... | Use this reference |
|---|---|
| Run a recurring AI character on TikTok or Instagram, no face on camera | `references/faceless-influencer.md` |
| Clone themselves into a talking head and generate videos from scripts | `references/ai-clone-talking-head.md` |
| Make paid ad creative at volume (UGC, product video, static) | `references/ai-ad-creative.md` |
| Build a faceless YouTube channel (long-form and shorts) | `references/faceless-youtube.md` |

Each reference is fully self-contained: a numbered walkthrough split into one-time setup and a repeating loop, with the exact prompts inline.

## How to run this skill

1. Identify which of the four use cases the user is after (ask one question if unclear).
2. Open the matching reference file and follow it with the user, step by step.
3. At each tool step, give the user the copy-paste prompt from the reference, filled in with their specifics (niche, topic, product, audience).
4. Keep one character, one voice, and one look consistent across a user's content. Consistency is the most common failure point.
5. Apply the realism rules below to every generation prompt (they are already written into the reference prompts; do not strip them out).
6. Before the user publishes, run the reference's pre-publish checklist.

## Tool stack at a glance

The user does not need all of these. Each playbook names the few it uses. Start lean (free tiers plus ElevenLabs Starter is enough to ship), scale one tool per layer only when volume demands it.

| Job | Tools | Notes |
|---|---|---|
| Ideas, scripts, prompts | ChatGPT, Gemini, Claude | Gemini for grounded/current research, Claude for natural voice |
| Voice and voice cloning | ElevenLabs | Free to test, Starter to ship |
| Video generation | Veo 3, Google Flow (directs Veo with a scene builder and camera controls), Kling 3.0 via Higgsfield, Seedance | Veo or Flow for hero shots, Kling for cheap volume, Seedance for lowest cost |
| Images and in-image text | Gemini Nano Banana, Midjourney, Ideogram | Nano Banana locks a face, Ideogram nails legible text, Midjourney for the best look |
| Avatars and UGC actors | HeyGen, Arcads | HeyGen to clone yourself, Arcads for ad UGC |
| All-in-one (quick, lower ceiling) | Google Vids | Doc to scenes with stock, AI voiceover, avatars; fast but weaker for faceless or cinematic |
| Editing | CapCut | Captions, color, music; free |

## The rule that beats AI slop

Realism is controlled imperfection. The default settings and generic prompts produce the average, which reads as fake. Add back the texture and flaws real capture has:

- Prompt for a phone-camera look: natural light, slight grain, real-time pace. Drop the words "8K", "cinematic", "perfect", "studio", "hyperreal". Those trigger the waxy plastic look.

- Put real pauses, breaths, and a filler before the key line in voice scripts. Flat delivery is the number one AI-audio tell.

- Keep clips short (3 to 10 seconds) and cut. Faces and physics drift past that.

- For video, add negative prompts: no morphing, no warping, no melting, no jelly motion, no slow motion.

- Mix in real footage (stock or a real product photo) and apply one consistent color grade so generated and real assets read as one piece.

These are already written into the reference prompts. The reference "Make It Look Real" sections also list the editing and review moves a prompt cannot do.

## Run it outside Claude Code (ChatGPT, Claude, Gemini)

A ready-to-use project package lives in `assets/chatgpt-project/`. It turns this skill into a ChatGPT Project, Claude Project, or Gemini Gem so a non-technical user can run the same steps in a normal chat:

- `project-instructions.md` — paste into the Project or Gem instructions.
- `knowledge/` — upload these files as the project knowledge.

## References

- `references/faceless-influencer.md`
- `references/ai-clone-talking-head.md`
- `references/ai-ad-creative.md`
- `references/faceless-youtube.md`

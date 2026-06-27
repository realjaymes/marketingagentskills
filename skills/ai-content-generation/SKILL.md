---
name: ai-content-generation
description: "When the user wants to create AI-generated image or video content: a faceless influencer or persona for TikTok and Instagram, a faceless YouTube channel, an AI clone or talking-head of themselves, or AI ad creative (UGC, product video, static images). Also use when the user mentions 'faceless influencer,' 'faceless channel,' 'AI avatar,' 'AI UGC,' 'talking head,' 'clone myself,' 'AI ad creative,' 'AI video ads,' or tools like Veo, Google Flow, Kling, Higgsfield, Seedance, Runway, ElevenLabs, HeyGen, Arcads, Nano Banana, Midjourney, or Ideogram. Gives step-by-step, copy-paste-prompt playbooks for each use case plus the realism rules that beat AI slop. For paid-ad strategy and targeting, see performance-marketing or paid-ads."
metadata:
  version: 1.2.0
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

## How the tools are named (app vs model)

The names look chaotic because three different things share the spotlight: apps you chat inside, wrappers that put one interface over many models, and the models that do the generating. Once you know which is which, every new launch slots in. The model generates. The app or wrapper is just the door you walk through to reach it.

Three buckets:

- **Assistant / app**: where you type. It runs models underneath. ChatGPT, Gemini, Claude.
- **Wrapper**: one interface over several models, usually for cheaper volume or shot control. Google Flow, Higgsfield.
- **Model**: the thing that actually generates, split by layer (text, image, video, voice). Veo 3.1, Gemini Omni, Nano Banana, Kling.

| Tool | Type | Made by | What it is / what it runs |
|---|---|---|---|
| ChatGPT | Assistant | OpenAI | LLM for scripts and ideas |
| Gemini | Assistant | Google | LLM, and the front door to Google's image (Nano Banana) and video (Omni) models |
| Claude | Assistant | Anthropic | LLM, best for natural voice and writing |
| Google Flow | Wrapper | Google | Runs Veo 3.1 and Gemini Omni with a scene builder and shot controls |
| Higgsfield | Wrapper | Higgsfield | Runs Kling and other video models in one UI, cheap at volume |
| Gemini Omni | Video model | Google | Conversational generation and editing, multi-input, 1080p, ~10s clips. Now the default in the Gemini app, Flow, and YouTube Shorts |
| Veo 3.1 | Video model | Google | Cinematic, 4K, longer shots, stable API. Best for brand films and ads |
| Kling | Video model | Kuaishou | Cheap volume, reached through Higgsfield |
| Seedance | Video model | ByteDance | Lowest-cost video |
| Nano Banana | Image model | Google | Locks a face, edits inside an image. Lives in the Gemini app |
| Midjourney | Image model | Midjourney | Best aesthetic look |
| Ideogram | Image model | Ideogram | Legible text inside an image |
| ElevenLabs | Voice model | ElevenLabs | Voiceover and voice cloning |
| Speechma | Voice app | Speechma | Free library voices, no cloning |
| HeyGen | Avatar app | HeyGen | Talking-head avatars, clone yourself |
| Arcads | UGC app | Arcads | AI UGC actors for ads |
| Google Vids | All-in-one app | Google | Doc to video with stock, AI voiceover, avatars |
| CapCut | Editor | ByteDance | Captions, color, music, assembly |

**The big three, decoded.** Each vendor has a company name, an app you chat in, and a family of models underneath. Mixing those three is most of the confusion.

- **Google**: Gemini is the assistant. Nano Banana is its image model. Veo 3.1 is its cinematic video model (API, 4K, long shots). Gemini Omni is its conversational video generation-and-editing model, now default in the Gemini app, Flow, and Shorts. Veo 3.1 did not go away. It stayed on the API for high-fidelity work while Omni took over the consumer app.
- **OpenAI**: OpenAI is the company. ChatGPT is the app. GPT (GPT-5 and friends) are the text models inside it. Sora is its video model, DALL-E / GPT Image its image model.
- **Anthropic**: Anthropic is the company. Claude is the assistant. Opus, Sonnet, and Haiku name the model tiers, from most capable down to fastest (for example Claude Opus 4.x).

**To place any new model**, ask two questions. Is it an app you chat in, a wrapper over other models, or a model itself? And which layer does it work on, text, image, video, or voice? Drop it in the matching row and move on.

## Tool stack at a glance

The user does not need all of these. Each playbook names the few it uses. Start lean (free tiers plus ElevenLabs Starter is enough to ship), scale one tool per layer only when volume demands it.

| Job | Tools | Notes |
|---|---|---|
| Ideas, scripts, prompts | ChatGPT, Gemini, Claude | Gemini for grounded/current research, Claude for natural voice |
| Voice and voice cloning | ElevenLabs | Free to test, Starter to ship |
| Free voiceover (no cloning) | Speechma | Free, no signup, browser-based library voices; ship narration before you clone a voice |
| Video generation | Gemini Omni, Veo 3.1, Google Flow (runs Veo and Omni with a scene builder and shot controls), Kling 3.0 via Higgsfield, Seedance | Omni for conversational edits and consistent clips (default in the Gemini app and Flow), Veo 3.1 for cinematic 4K hero shots, Kling for cheap volume, Seedance for lowest cost |
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

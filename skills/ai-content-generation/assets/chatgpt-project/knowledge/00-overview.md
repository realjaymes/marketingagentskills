
# AI Content Generation: Overview and Tool Map

This folder has four simple, self-contained playbooks for making AI image and video content. Pick the one that matches what you want to build, open it, and follow the steps.

> Mindset: the model is the easy part. What makes content win is the niche, the script, keeping your character consistent, and killing the AI-slop look. Every playbook bakes those in so you do not have to think about them.

---

## Pick your use case

| Playbook                             | What it is                                                           | Who it is for                                                         |
| ------------------------------------ | -------------------------------------------------------------------- | --------------------------------------------------------------------- |
| 01 - Faceless Influencer         | A recurring AI character on TikTok and Instagram, no face on camera. | You want a daily short-form account without showing yourself.         |
| 02 - AI Clone & Talking Head     | Clone yourself, then generate talking-head videos from scripts.      | You want to be on camera without filming, or scale your own face.     |
| 03 - AI Ad Creative              | Paid ad creative at volume (UGC, product video, static).             | You run ads and need many variations fast.                            |
| 04 - Faceless YouTube Automation | Faceless YouTube channels, long-form and shorts.                     | You want narration over B-roll, essays, or documentary-style content. |

---

## How to use these

Each playbook is self-contained. Open one, start at Step 1, and the prompts are inline in the steps. You do not link out to a prompt library, because the prompts live right where you need them.

Do not read all four first. That is how people stall. Pick the one closest to what you want, follow it top to bottom, and ship one output this week. Come back for a second playbook when the first one is working.

---

## How the tools are named (read once, then ignore)

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

---

## Tools at a glance

These tools repeat across the set. Each playbook tells you exactly which ones it needs, so this is just the map.

| Tool | What it is for | Where to start |
|---|---|---|
| ChatGPT / Gemini / Claude | Ideas, scripts, prompts. Claude for voice, Gemini for grounded research. | Free tiers, then ~$20/mo each |
| ElevenLabs | Voiceover and voice cloning. | Free to test, $5/mo Starter to ship |
| Speechma | Free no-signup browser voiceover (library voices, no cloning). Good for faceless narration before you clone a voice. | Free at speechma.com |
| Gemini Omni, Veo 3.1, Google Flow, Kling (via Higgsfield), Seedance | Video generation. Gemini Omni for conversational edits and quick consistent clips (now default in the Gemini app and Flow), Veo 3.1 for cinematic 4K hero shots, Google Flow to direct shots with a scene builder, Kling for cheap volume, Seedance for the lowest cost. | Omni in the Gemini app free tier; Higgsfield ~$34/mo for Kling at volume |
| Gemini Nano Banana, Midjourney, Ideogram | Images and in-image text. Nano Banana locks a face, Ideogram nails text, Midjourney for the best look. | Nano Banana free in-app, Ideogram free tier |
| HeyGen, Arcads | Talking-head avatars and UGC actors. HeyGen to clone yourself, Arcads for ad UGC. | HeyGen free 3/mo, then $29/mo |
| Google Vids | All-in-one quick video inside Google Workspace: turns a doc into scenes with stock, AI voiceover, and avatars. Beginner-friendly and fast, but a lower ceiling than the dedicated tools for faceless or cinematic work. | Included with Google Workspace |
| CapCut | Editing, captions, color, music. | Free |

Start lean: free tiers plus ElevenLabs Starter ($5) is enough to ship. Scale up one tool per layer only when volume demands it.

---

## The one rule that beats AI slop

Realism is controlled imperfection. Prompt for a phone-camera look (natural light, slight grain, real-time pace) and drop the words "cinematic", "8K", and "perfect", because those trigger the waxy plastic look. Put real pauses and breaths in the voice so it does not sound robotic. Keep clips short so faces do not warp.

Each playbook has its own version of this rule tuned to its use case. Read it before you publish.

---


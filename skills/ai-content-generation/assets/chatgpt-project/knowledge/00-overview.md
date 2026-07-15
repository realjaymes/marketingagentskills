
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
| GPT Image | Image model | OpenAI | Renders the scene and legible in-image text in one pass. Lives in ChatGPT |
| Ideogram | Image model | Ideogram | Legible text inside an image, fallback when GPT Image falls short |
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
| ChatGPT (GPT Image), Gemini Nano Banana, Midjourney, Ideogram | Images and in-image text. ChatGPT (GPT Image) is the default for headlines/CTA/thumbnail text, short or long (scene and text in one pass). Nano Banana locks a face, Ideogram is the fallback when ChatGPT falls short, Midjourney for the best look. | ChatGPT ~$20/mo, Nano Banana free in-app, Ideogram free tier |
| HeyGen, Arcads | Talking-head avatars and UGC actors. HeyGen to clone yourself, Arcads for ad UGC. | HeyGen free 3/mo, then $29/mo |
| Google Vids | All-in-one quick video inside Google Workspace: turns a doc into scenes with stock, AI voiceover, and avatars. Beginner-friendly and fast, but a lower ceiling than the dedicated tools for faceless or cinematic work. | Included with Google Workspace |
| CapCut | Editing, captions, color, music. | Free |

Start lean: free tiers plus ElevenLabs Starter ($5) is enough to ship. Scale up one tool per layer only when volume demands it.

---

## The one rule that beats AI slop

Realism is controlled imperfection. Prompt for a phone-camera look (natural light, slight grain, real-time pace) and drop the words "cinematic", "8K", and "perfect", because those trigger the waxy plastic look. Put real pauses and breaths in the voice so it does not sound robotic. Keep clips short so faces do not warp.

Two hard rules for video generation specifically (Veo, Google Flow, Kling, Gemini Omni):

- **No on-screen text in a video prompt.** These models garble any text you ask them to render on screen. Add all captions, hook text, and CTAs in CapCut after generating. Baked-in text stays fine only for the still-image models (GPT Image, Ideogram, Nano Banana), which are chosen because they render legible text, so keep it in static-image and thumbnail prompts.
- **Segment the script into ~10-second beats before generating.** Never hand a video model the whole 30 to 45 second script in one prompt. Break it into ~10-second beats, generate one clip per beat (each with only that beat's spoken line), and stitch them in CapCut. If a clip glitches, regenerate only that beat.

Each playbook has its own version of this rule tuned to its use case. Read it before you publish.

---

## Appendix: Google's cheap on-ramp (Flow & Vids)

Two Google tools give beginners the fastest, cheapest first win. Neither replaces the four playbooks above. Use them when you want a quick result, or before you are ready to pay for the dedicated stack.

### Google Flow — put yourself in any scene

Flow runs on a Google AI plan (credits: Pro = 1,000/mo, Ultra = 10,000), so it is not free, but it makes one thing easy that the others do not: an avatar of you.

- Open Flow (labs.google/fx/tools/flow), start a project, click the plus icon in the prompt box, choose Avatar.
- First time only: it shows a QR code. Scan it with your phone, scan your face on the page that opens, and Flow builds your avatar.
- Add your avatar to any image or video prompt to drop yourself into a scene ("me on a beach at sunset explaining X").
- Work image-first: generate and lock the still (cheap credits), then animate it (video costs far more). Watch the credit counter before every generation.

### Google Vids — free AI video and slides-to-video

Vids lives inside Google Workspace and its free tier does real work.

- Free AI video: open vids.new, click Veo, describe a shot. Free up to 10 generations per month, the only free way to make AI video (Gemini's free plan will not). Continue a shot by screenshotting the last frame and using "animate an image".
- Slides to video: File → Convert Slides, pick a Google Slides deck, and Vids writes a script, adds an AI voiceover, and drops in music. The fastest way to turn a deck into a narrated video.
- Free voiceover: paste a script, pick a voice, insert. Good narration before you clone a voice.
- Note: talking-head avatars and ingredients in Vids are Pro/Ultra only (grayed out on free). For an avatar of yourself, Flow above is the route (also paid, on a Google AI plan); for a reusable talking-head clone see the AI Clone & Talking Head playbook.

---


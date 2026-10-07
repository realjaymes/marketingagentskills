# 00 - START HERE — AI Content Generation

This folder holds the general workflow for making AI video and image content, the rules every project shares, and five playbooks with the detailed steps for each use case. Read this note once. Then pick a playbook, follow it step by step, and come back here when it links to a shared rule.

Every playbook runs the same six steps. A proven reference does most of the planning, the script and voice set the pacing, and You approve the work at two points before any credits go into video.

---

## Pick your playbook

Start with one question: **do you have a proven reference?** That means a video that already does the job you want, in the format you want. If yes, every playbook starts by tearing it down with the `reference-teardown.md` method. If no, find one first. A swipe file or a competitor's best-performing ad is enough.

Then pick by use case:

| Playbook | What it makes | Use it when |
| --- | --- | --- |
| `01-faceless-influencer.md` | A recurring AI character for TikTok and Instagram | You want a daily short-form account without showing your face |
| `02-ai-clone-talking-head.md` | A clone of you that speaks your scripts | You want to be on camera without filming |
| `03-ai-ad-creative.md` | Paid ad creative at volume, including AI UGC (user-generated content) | You run ads and need many variations fast |
| `04-faceless-youtube.md` | Faceless YouTube videos, long form and Shorts | You want narration over B-roll |
| `05-launch-videos-and-recording-edits.md` | Motion-graphics launch videos, and edits of your own recordings | You are launching a product, or you filmed yourself and want a sharp edit |

Or pick by what is on screen:

| On screen | Video type | Playbook |
| --- | --- | --- |
| No person: screens, cards, animated text, AI voice | Type A | `05-launch-videos-and-recording-edits.md` |
| An AI person | Type B | `01-faceless-influencer.md`, `03-ai-ad-creative.md` |
| A clone of you | Type B | `02-ai-clone-talking-head.md` |
| You, filmed for real | Type C | `05-launch-videos-and-recording-edits.md` |
| B-roll under narration | Type A | `04-faceless-youtube.md` |

---

## The workflow

Each step writes one file that the next step reads. Claude can run steps 1 to 3 in one sitting. You approve the script and the start frames before anything is generated.

### 1. Reference brief

- **Brief:** five lines covering the goal, the audience, the message, the platform and length, and the call to action.
- **Reference:** one to three proven videos that do the same job, broken down with the `reference-teardown.md`. It records the structure (shots, hook move, beats with word counts, captions, sound) and the look (light, palette, camera movement, texture).
- **Style in numbers**, when we copy an editing or motion style: cuts per minute, zoom size and frequency, caption layout, animation timing, sound-effect timing. A style we will reuse becomes a Remotion template, so the next video starts at step 2.
- The reference is the concept. Write three scored concepts only for a brand film, or when no reference fits.
- **Output:** a REFERENCE note.

### 2. Script

- A beat table with time, visual, the spoken line, on-screen text and sound.
- The story follows the reference, and each beat has a word budget close to the reference's.
- Every claim traces to the brief. A missing fact is flagged for the owner, never invented.
- **Approval point 1:** You approve the script.
- **Output:** a SCRIPT note.

### 3. Scenes and anchors

- **Anchors** at the top of the note:
  - the character's two-image anchor, a close-up and then a wide shot made from the close-up;
  - real product photos from every angle;
  - one look line covering palette, light, lens and grain.
- Recurring personas reuse their saved anchors.
- **One row per shot:** framing, camera movement, light, action, the exact line, duration plus about one second of extra footage at each end (handles), and the start frame it uses.
- **Start frames:** one still for each generated shot, laid out together as a contact sheet. Image-to-video needs these frames anyway, so checking them as a set costs no extra credits.
- **Approval point 2:** You approve the start frames as a set. The face, outfit, product and look must stay the same across shots.
- **Output:** a SCENES note and a frames folder.

### 4. Voice

- Record or generate the final voice before any shot is made, then time every word with Whisper. The timed voice sets each shot's exact length.
- **When the video model speaks the line itself** (a talking AI person in Flow), the script fixes each line and its clip length instead. Generate the shots first, then run ElevenLabs Voice Changer over the clips to lock one voice, and time the words with Whisper after that.
- **Output:** the voice file and `words.json`.

### 5. Shots

- Generate one take per shot from its approved start frame.
- Regenerate only the shots that fail, within the the "Credits and retries" section rules. Fix single shots, never the whole film.
- Every speaking prompt carries the the "Dialogue accuracy" section line. Every prompt asks for handles.
- **Output:** clips named by shot number.

### 6. Finish and check

- **Build:** cut the clips to the voice, using the style template when one exists. Add music ducked under the voice, sound effects on cuts, and word-timed the "Captions" section. Match the colour across shots and add the the "AI disclosure" section label where needed.
- **Check:** run the the "Final check" section.
- **Variants (ads):** export other aspect ratios and cut-downs, plus hook and call-to-action variants. Log what worked into the swipe index.
- **Output:** the master, the variants, and the check results in the asset hub.

### Scale by tier

| Step | Quick social (UGC, faceless shorts, persona posts) | Performance ad or launch video | Brand film |
| --- | --- | --- | --- |
| 1 Reference brief | One reference, structure only | One to three references, structure and look | Several references plus three scored concepts |
| 2 Script | Beat table | Beat table | Beat table |
| 3 Scenes and anchors | Reuse the persona's anchors; start frames only for new setups | Start frames for every generated shot | Start frames for every generated shot |
| 4 Voice | Yes | Yes | Yes |
| 5 Shots | One take, retry failures | One take, retry failures | Two takes on the key shots |
| 6 Finish and check | Edit, sound, captions, check | Plus colour match and variants | Plus cut-downs |

---

## Shared rules

Every playbook follows these rules. A playbook adds detail for its use case, but it never overrides them.

### Realism

Realism comes from controlled imperfection. Prompt for a phone-camera look: natural light, slight grain, real-time pace. Drop the words "cinematic", "8K" and "perfect", because they trigger a waxy, plastic look. Put real pauses and breaths in the voice. Keep talking clips short so faces do not warp.

Video models garble text, so never ask a video prompt to render words on screen. Add captions, hook text and calls to action in the edit. Still-image models such as GPT Image, Ideogram and Nano Banana render text well, so text in static images and thumbnails is fine.

### Writing shot prompts

Build every video prompt from the shot's row in SCENES, in this order: subject, action, camera movement, look, light, then specs.

- Keep each prompt to 50 to 100 words. Longer prompts make the model drop details.
- Always name the camera movement, or say "static". Video models understand these terms: static, pan, tilt, dolly in or out, slow push, orbit, tracking shot, crane, handheld, zoom.
- Start from the approved start frame (image-to-video), so the face, product and setting carry over.
- End with the anti-warp line: "No morphing, no warping, no melting, no jelly motion, no slow motion."
- Speaking shots also carry the the "Dialogue accuracy" section line.

Common mistakes: a vague subject ("a person"), asking for text on screen, asking it to "make it viral", prompts over 200 words, and no camera direction.

### Dialogue accuracy

Video models mangle lines, cut them short and add filler words. Every speaking prompt carries this line, word for word:

"Ensure each word is pronounced correctly and you do not add any extra words."

- Spell brand and product names phonetically in the prompt when the model gets them wrong, for example "Acme Glow (pronounced AK-mee GLOH)".
- Match the clip length to the line. A short line needs about 4 seconds. Keep every talking clip at 8 seconds or less. Gemini Omni allows 10, but 8 is safer.
- Merge two short lines into one clip when they share the same framing.

### Captions

- The caption style copies the reference each time: font, size, colour, highlight and words per screen.
- The safety rules always apply on top of the reference's style:
  - captions never cover a face;
  - nothing sits in the bottom fifth of a 9:16 frame, where the app's buttons are;
  - captions are timed word by word from the Whisper transcript.
- Remotion renders captions from `words.json`. The local ffmpeg build cannot burn captions in.

### Brand colours

Colours always come from the product's own screens or the brand kit. For a software product, sample the colours from its screenshots, so the video looks like the app. For a client, use their brand kit. A reference's palette never overrides the brand.

### Audio and licensing

- **Voice for ads:** use a paid voice plan. The ElevenLabs free tier carries no commercial licence and requires attribution, so it never goes in an ad. Google Cloud text to speech (TTS) Studio voices (`en-US-Studio-Q` male, `en-US-Studio-O` female) are a low-cost option for narration.
- **Music for ads:** use Mixkit (check each item's licence tag), Freesound sounds licensed CC0 or CC BY, or original music from a paid Suno plan. Avoid the YouTube Audio Library for Meta ads, because its licence covers YouTube.
- **Sound effects:** add one on each cut and graphic, from Mixkit or Freesound. On Freesound, each sound carries its own licence: CC0 needs no credit, CC BY needs a credit logged in SOUNDS, and CC BY-NC (non-commercial) never goes in an ad.
- **Log every source** in the asset's SOUNDS note: the track, where it came from, and its licence.
- **Loudness:** master at about -16 LUFS (loudness units relative to full scale).

### AI disclosure

- Turn on the platform's AI label wherever it offers one. Burn in an "AI-generated" label where the platform or the ad policy requires it.
- An AI person never poses as a real customer giving a testimonial. AI creators in ads are presented as presenters or actors.
- Testimonials come only from real, published customers with permission.

### Credits and retries

- Fix the script and the start frames before generating any video. Those are cheap, and video is not.
- Generate one output at a time. Draft at 720p and render the final at full resolution.
- Reuse the last prompt that worked, and change only the start frame and the line.
- Change one thing per retry.
- Allow three tries per shot. After that, give the failed outputs to the assistant, ask it to rewrite the prompt, or change the start frame.
- Allow one or two rounds of changes per approval point. A third round means the brief or the reference is wrong, so go back to step 1.

### Final check

Run this check before anything is posted. Each item is a yes or a no.

- Stills of the export, one per scene, match the storyboard and the reference.
- The length matches the script.
- The audio is present on every shot, and the loudness is about -16 LUFS.
- No caption covers a face, and nothing sits in the bottom fifth on 9:16.
- The AI label is set or burned in where required.
- Every claim matches the brief, and the compliance rules for the platform are met.
- Someone has watched it once, start to finish, in a normal player such as VLC or the phone's own player.

### Folders and files

- **In your notes:** the asset hub and the REFERENCE, SCRIPT, SCENES and SOUNDS notes, in the project's notes folder.
- **Outside your notes:** heavy media lives in a work folder linked from the hub, with `reference/`, `frames/`, `voice/`, `clips/` and `renders/` inside.
- **File names:** clips are named by shot number (`shot-01.mp4`), and the final export is `final.mp4`.
- **Templates:** after the first slow run of a new format, turn it into a template (a Remotion composition, a saved prompt set, or saved anchors), so the next run is fast.

---

## Tools and prices

Prices verified 2026-10-07. Check the source link before buying. Items marked (s) rest on secondary sources.

| Tool | Job | Price and free tier | OK in ads? | Source |
| --- | --- | --- | --- | --- |
| Claude (Fable, Opus, Sonnet, Haiku) | Scripts, teardowns, coding agent | Plans per Anthropic | Yes | [anthropic.com](https://www.anthropic.com/pricing) |
| ChatGPT (GPT Image) | Ad images and thumbnails with text | Free (limited), Go $8, Plus $20 (s) | Yes | [OpenAI](https://openai.com/chatgpt/pricing/) |
| Gemini with Nano Banana | Face-locked character stills and start frames | Free in the app (about 20 a day) (s) | Yes (s) | [felloai.com](https://felloai.com/is-nano-banana-free/) |
| Google Flow | Directs Gemini Omni and Veo 3.1 shots | Free 50 credits a day at 720p; Pro $19.99 for 1,000 credits (s) | Paid plans yes; treat the free tier as no | [costgoat.com](https://costgoat.com/pricing/google-flow) |
| Gemini Omni 1.1 Flash | Quick, consistent clips of 3 to 10 seconds with sound; conversational edits | Free in Google Vids and YouTube Shorts; paid in the Gemini app | Check Google's terms before ad use | [Google blog](https://blog.google/products-and-platforms/products/workspace/gemini-omni-in-google-vids/) |
| Veo 3.1 | Cinematic and 4K shots | API $0.05 to $0.60 per second by tier | Yes on the paid API | [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| Google Vids | Free AI clips, slides to video | Free for any Google account | Treat as not for ads | [Google blog](https://blog.google/products-and-platforms/products/workspace/gemini-omni-in-google-vids/) |
| Kling 3.0 | Low-cost volume video | Free 66 credits a day with a watermark; Standard $8.80 a month (s) | Paid plans only | [crixpix.com](https://crixpix.com/kling-ai-free/) |
| Seedance 2.0 and 2.5 | Video with strong prompt following | About $0.15 a second at 720p on the API (s) | Yes on paid routes | [framesurfer.com](https://framesurfer.com/blogs/seedance-2-0-pricing) |
| Higgsfield | One app for Kling, Seedance and Veo | $19, $59 or $129 a month | Paid yes | [higgsfield.ai](https://higgsfield.ai/blog/seedance-2-5-pricing-2026) |
| Runway | Gen-4.5, plus Kling and Seedance | 125 free credits once; from $15 a month | From Standard | [runwayml.com](https://runwayml.com/pricing) |
| Midjourney | The best-looking stills | From $10 a month, no free trial (s) | Yes; companies over $1M revenue need Pro | [Midjourney](https://www.midjourney.com/account) |
| Ideogram | Text inside images, fallback to GPT Image | Free 10 slow credits a week; Plus $20 (s) | Yes (s) | [eesel.ai](https://www.eesel.ai/blog/ideogram-pricing) |
| ElevenLabs (Eleven v4) | Voiceover, voice clone, Voice Changer | Free 10,000 credits; Starter $6; Creator $22 | Paid plans only | [elevenlabs.io](https://elevenlabs.io/pricing) |
| Google Cloud TTS (Studio, Chirp 3 HD) | Low-cost narration | 1M free characters a month each, then $160 or $30 per million; billing must be on | Yes | [cloud.google.com](https://cloud.google.com/text-to-speech/pricing) |
| HeyGen | Avatars and clones of you | Free 3 videos a month; Creator $29 | Paid yes | [heygen.com](https://www.heygen.com/pricing) |
| Arcads | AI UGC actors | About $110 a month for 10 videos (s) | Yes (s) | [ugcgen.ai](https://ugcgen.ai/arcads-pricing) |
| Remotion | Code-built video, captions, motion graphics | Free for up to 3 people | Yes within the licence | [remotion.pro](https://www.remotion.pro/license) |
| whisper.cpp | Transcripts and word timings | Free | Yes | [GitHub](https://github.com/ggml-org/whisper.cpp) |
| ffmpeg | Cutting, joining, pulling frames | Free | Yes | [ffmpeg.org](https://ffmpeg.org) |
| CapCut | Manual edits | Free; Pro $19.99 (s) | Pro for ad assets (s) | [eesel.ai](https://www.eesel.ai/blog/capcut-pricing) |
| Mixkit | Music and sound effects | Free | Yes for online ads; check each item's tag | [mixkit.co](https://mixkit.co/license/) |
| Freesound | Sound effects and ambience | Free with an account | CC0 and CC BY sounds only; never CC BY-NC | [freesound.org](https://freesound.org/) |
| Suno | Original music | Free has no commercial rights; Pro $8 a month annual | Pro and Premier only | [suno.com](https://suno.com/pricing) |

**Default picks.** Gemini Omni in Flow for quick, consistent clips. Veo 3.1 for cinematic and 4K shots. Kling or Seedance through Higgsfield for volume. Remotion for every edit that can be built in code. Name the model in each step, because "Flow" alone does not say which model runs.

**Start lean.** Free tiers are enough to test. Pay for one tool per layer only when an ad or volume needs it. Sora is discontinued.

### How the tools are named

Three kinds of tools share the spotlight:

- **Assistants** are where you type: ChatGPT, Gemini, Claude.
- **Wrappers** put one interface over several models: Google Flow, Higgsfield, Runway.
- **Models** do the generating, one layer each (text, image, video or voice): Veo 3.1, Gemini Omni, Nano Banana, Kling, Seedance.

Google's family: Gemini is the assistant, Nano Banana the image model, and Veo 3.1 and Gemini Omni the video models. OpenAI's: ChatGPT is the app and GPT Image the image model. Anthropic's: Claude is the assistant, with Fable, Opus, Sonnet and Haiku as the model tiers from most capable to fastest.

To place a new tool, ask two questions. Is it an assistant, a wrapper or a model? And which layer does it work on? Then put it in the matching row.

---

## Appendix: Google's low-cost on-ramp

**Google Flow.** The free tier gives 50 credits a day at 720p, enough for a few short Veo 3.1 Lite clips. Paid Google AI plans add monthly credits. Flow can also build an avatar of you: start a project, click the plus icon in the prompt box, choose Avatar, and scan your face with your phone. Work image-first, because a still costs far fewer credits than a clip.

**Google Vids.** Vids is free for any Google account and runs Gemini Omni 1.1 Flash at 1080p. Open vids.new to generate a clip, or use File, then Convert Slides, to turn a Google Slides deck into a narrated video. Treat Vids output as not cleared for ads until Google's terms say otherwise. The Gemini app's free plan makes no video.

---

Related: `reference-teardown.md` · `01-faceless-influencer.md` · `02-ai-clone-talking-head.md` · `03-ai-ad-creative.md` · `04-faceless-youtube.md` · `05-launch-videos-and-recording-edits.md`

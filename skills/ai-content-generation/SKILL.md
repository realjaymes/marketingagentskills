---
name: ai-content-generation
description: "When the user wants to create AI-generated video or image content: a faceless influencer or persona, an AI clone or talking head, AI ad creative and AI UGC, a faceless YouTube channel, a product or launch video with motion graphics and an AI voice, or a sharp edit of their own recording (including a Hormozi-style edit). Also use when the user wants to copy a creator's editing style or a brand's motion style, tear down a reference video, or mentions 'faceless,' 'AI avatar,' 'AI UGC,' 'talking head,' 'clone myself,' 'AI video ad,' 'launch video,' 'motion graphics,' 'video edit,' 'reference teardown,' or tools like Veo, Gemini Omni, Google Flow, Kling, Higgsfield, Seedance, Runway, ElevenLabs, HeyGen, Arcads, Nano Banana, Midjourney, Ideogram, Remotion or Whisper. Runs one six-step, reference-first workflow with two approval points, and routes to a playbook per use case. For paid-ad strategy and targeting, see performance-marketing or paid-ads; for Remotion code, it calls remotion."
metadata:
  version: 2.0.0
---

# AI Content Generation

Help the user make studio-quality AI video and image content with the fewest steps. Every use case runs the same six-step workflow. A proven reference does most of the planning, the script and voice set the pacing, and the user approves the script and the start frames before any credits go into video.

The full workflow and the shared rules are in `references/00-workflow-and-rules.md`. Read it before the first step of any job.

## Pick the playbook

Ask first: **is there a proven reference?** If not, help the user find one before anything else. Then route:

| The user wants to... | On screen | Reference file |
| --- | --- | --- |
| Run a recurring AI character on TikTok or Instagram | An AI person (type B) | `references/01-faceless-influencer.md` |
| Clone themselves and generate talking-head videos | Their clone (type B) | `references/02-ai-clone-talking-head.md` |
| Make paid ad creative at volume, including AI UGC | An AI person or product (type B) | `references/03-ai-ad-creative.md` |
| Build a faceless YouTube channel | B-roll under narration (type A) | `references/04-faceless-youtube.md` |
| Make a product or launch video with motion graphics and an AI voice | No person (type A) | `references/05-launch-videos-and-recording-edits.md` |
| Edit their own recording, or copy a creator's edit style | Themselves (type C) | `references/05-launch-videos-and-recording-edits.md` |

"Faceless" means the operator's own face is absent. An AI character in a faceless account has a face. Never pass a generated or stock person off as a real, named individual.

## The six steps

1. **Reference brief.** A five-line brief plus one to three proven references, torn down with `references/reference-teardown.md`. To copy a style, measure it in numbers. A style we will reuse becomes a Remotion template.
2. **Script.** A beat table with a word budget per beat that follows the reference's story. Every claim traces to the brief; flag missing facts and never invent them. **The user approves the script.**
3. **Scenes and anchors.** Character, product and look anchors, then one row per shot with its full spec. Generate one start frame per generated shot and show them as a contact sheet. **The user approves the start frames.**
4. **Voice.** The final voice comes first. Whisper times every word into `words.json`, and that sets each shot's length.
5. **Shots.** One take per shot from its start frame. Regenerate only failures, within the retry rules.
6. **Finish and check.** Edit to the voice, add sound and word-timed captions, match colour, add the AI label, run the final check, and make variants for ads.

Scale the steps by tier (quick social, performance ad or launch video, brand film) using the table in `references/00-workflow-and-rules.md`. There is no animatic step.

## How to run a job

1. Identify the playbook and the tier. Ask one question if either is unclear.
2. Work the six steps in order, using the playbook's detail for each step. Stop at both approval points and wait for a clear go.
3. Write each step's output as a file: REFERENCE, SCRIPT, SCENES, SOUNDS and the asset hub. In the owner's setup these planning notes go in your notes asset folder set by the creative notes protocol, and heavy media goes in a work folder outside your notes app.
4. Hand the user copy-paste prompts for each tool step, filled in with their specifics.
5. Allow one or two rounds of changes per approval point. A third round means the brief or the reference is wrong, so return to step 1.
6. Run the final check before anything is posted.

## Shared rules (summary)

The full text is in `references/00-workflow-and-rules.md`. These never get dropped:

- **Dialogue accuracy:** every speaking prompt ends with "Ensure each word is pronounced correctly and you do not add any extra words." Talking clips stay at 8 seconds or less.
- **Captions:** the style copies the reference. Captions never cover a face, nothing sits in the bottom fifth of a 9:16 frame, and timing is word by word.
- **Brand colours:** always from the product's screens or the brand kit.
- **Audio:** paid voice plans for ads (never the ElevenLabs free tier), licensed music and effects, every source logged, about -16 LUFS.
- **AI disclosure:** the platform's AI label where offered. An AI person never poses as a real customer.
- **Realism:** a phone-camera look, no "cinematic", "8K" or "perfect", no text rendered inside video prompts.
- **Credits:** fix the script and frames first, draft at 720p, change one thing per retry, three tries per shot.

## Other skills this calls

- **`remotion`** builds type A videos, type C edits, captions from `words.json`, and style templates.
- **`creative-multiplication-engine`** runs step 6 variants for client ad batches, in the client's brand.
- **`design-taste`** supplies design notes when a video needs a page-quality look.
- **A bulk capture tool** saves Instagram and TikTok references, comments and stats.

## Run it outside Claude Code

`assets/chatgpt-project/` holds a ChatGPT Project, Claude Project or Gemini Gem package built from the same playbooks: paste `project-instructions.md` into the instructions and upload `knowledge/`. It is generated by `the export build script` from your notes playbooks, which are the source of truth. Run the script whenever a playbook changes, so the skill references and every export stay in sync.

## References

- `references/00-workflow-and-rules.md`
- `references/reference-teardown.md`
- `references/01-faceless-influencer.md`
- `references/02-ai-clone-talking-head.md`
- `references/03-ai-ad-creative.md`
- `references/04-faceless-youtube.md`
- `references/05-launch-videos-and-recording-edits.md`

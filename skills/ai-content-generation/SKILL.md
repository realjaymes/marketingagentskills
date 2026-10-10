---
name: ai-content-generation
description: "When the user wants to create AI-generated video or image content: a faceless influencer or persona, an AI clone or talking head, AI ad creative and AI UGC, a faceless YouTube channel, a product or launch video with motion graphics (with an AI voice or none), or a sharp edit of their own recording (including a Hormozi-style edit). Also use when the user wants to copy a creator's editing style or a brand's motion style, tear down a reference video, or mentions 'faceless,' 'AI avatar,' 'AI UGC,' 'talking head,' 'clone myself,' 'AI video ad,' 'launch video,' 'motion graphics,' 'video edit,' 'reference teardown,' or tools like Veo, Gemini Omni, Google Flow, Kling, Seedance, Runway, ElevenLabs, HeyGen, Arcads, Nano Banana, Midjourney, Ideogram, Remotion or Whisper. Runs one six-step, reference-first workflow with two approval points, and routes to a playbook per use case. For paid-ad strategy and targeting, see performance-marketing or paid-ads; for Remotion code, it calls remotion."
metadata:
  version: 2.4.0
---

# AI Content Generation

Help the user make studio-quality AI video and image content with the fewest steps. Every use case runs the same six-step workflow. A proven reference does most of the planning, the script and voice set the pacing, and the user approves the script and the start frames before any credits go into video.

The full workflow and the shared rules are in `references/00-workflow-and-rules.md`. Read it before the first step of any job.

## Pick the playbook

Ask first: **is there a proven reference?** If not, find the story first with the four stops in the Story craft rules (`references/00-workflow-and-rules.md`), then find a reference for the style. Then route:

| The user wants to... | On screen | Reference file |
| --- | --- | --- |
| Run a recurring AI character on TikTok or Instagram | An AI person (type B) | `references/01-faceless-influencer.md` |
| Clone themselves and generate talking-head videos | Their clone (type B) | `references/02-ai-clone-talking-head.md` |
| Make paid ad creative at volume, including AI UGC | An AI person or product (type B) | `references/03-ai-ad-creative.md` |
| Build a faceless YouTube channel | B-roll under narration (type A) | `references/04-faceless-youtube.md` |
| Make a product or launch video with motion graphics, with an AI voice or none | No person (type A) | `references/05-launch-videos-and-recording-edits.md` |
| Make 15 to 25 second demos of a product feature or free tool (tool shorts, twelve styles) | No person (type A) | `references/05-launch-videos-and-recording-edits.md` |
| Edit their own recording, or copy a creator's edit style | Themselves (type C) | `references/05-launch-videos-and-recording-edits.md` |

"Faceless" means the operator's own face is absent. An AI character in a faceless account has a face. Never pass a generated or stock person off as a real, named individual.

## The six steps

1. **Reference brief.** A five-line brief plus one to three proven references, torn down with `references/reference-teardown.md`. To copy a style, measure it in numbers. A style we will reuse becomes a Remotion template.
2. **Script.** A beat table with a word budget per beat that follows the reference's story. Every claim traces to the brief; flag missing facts and never invent them. Every script has a hook, a pain, a solution and a CTA, told through one launch story angle or a character story built by the Story craft rules. Every line is something a person actually says, in short lines, with no calendar markers or odd counts as fake specificity, and each beat causes the next. Codex drafts or reviews every script. A video that sells a program or offer runs 90 to 120 seconds and is built from the offer's landing page (`references/03-ai-ad-creative.md`, story and sale videos). Study proven references closely and get a Codex second opinion before writing. **The user approves the script.** A story script goes to the user with its storyboard, and both are approved together.
3. **Scenes and anchors.** Character, product and look anchors, then one row per shot with its full spec. A story script's storyboard (one code-drawn frame per shot, no image generation, in the same brief file) is approved before any face or start frame is made. Generate one start frame per generated shot and show them as a contact sheet. **The user approves the start frames.**
4. **Voice.** The final voice comes first. Whisper times every word into `words.json`, and that sets each shot's length. A coded launch film that gets a voice after its picture is approved is the exception: the picture stays fixed and one short line per beat is fitted to it.
5. **Shots.** One take per shot from its start frame in Google Flow, with the settings and per-shot model choice in the Google Flow rules. Fix faults in the edit first. At most one retry per clip, with the user's go-ahead.
6. **Finish and check.** Edit generated clips by the clip-editing rules (never joined end to end), add sound by the video type's rule and word-timed captions, match colour, set the platform AI label, run the final check, and make variants for ads.

Scale the steps by tier (quick social, performance ad or launch video, brand film) using the table in `references/00-workflow-and-rules.md`. There is no animatic step.

## How to run a job

1. Identify the playbook and the tier. Ask one question if either is unclear.
2. Work the six steps in order, using the playbook's detail for each step. Stop at both approval points and wait for a clear go.
3. Write each step's output as a file: REFERENCE, SCRIPT, SCENES, SOUNDS and the asset hub. Keep planning notes with your project notes and heavy media in a separate work folder, named in readable title case.
4. Hand the user copy-paste prompts for each tool step, filled in with their specifics.
5. Allow one or two rounds of changes per approval point. A third round means the brief or the reference is wrong, so return to step 1.
6. Run the final check before anything is posted.

## Shared rules (summary)

The full text is in `references/00-workflow-and-rules.md`. These never get dropped:

- **Dialogue accuracy:** every speaking prompt carries "Ensure each word is pronounced correctly and you do not add any extra words." and the still finish line. Short lines of 3 to 9 words in 8 second clips, trimmed in the edit. Eyes on the lens. One speaker per clip in dialogue. Names kept plain.
- **Story craft and pace:** the four parts, the launch story angles, the character story rules and the Codex test. Pictures change every 2 to 4 seconds at uneven gaps, within shot caps, and on-screen words hold at least 1 second plus 0.3 seconds per word.
- **Captions:** the style copies the reference. Captions never cover a face, nothing sits in the bottom fifth of a 9:16 frame, and timing is word by word.
- **Brand colours:** always from the product's screens or the brand kit.
- **Audio:** paid voice plans or paid APIs for ads (Gemini text to speech is the default for narrators and hosts, never the ElevenLabs free tier), licensed music and effects from Mixkit, Freesound or Openverse, a sound rule per video type, every source logged, about -16 LUFS.
- **Brand asset library:** logo, colours, fonts, screens, motion library, cast and sound picks saved once per brand and reused.
- **AI disclosure:** the platform's AI label switched on at posting. No AI tag on the picture unless a policy requires one. An AI person never poses as a real customer.
- **Realism:** a phone-camera look, no "cinematic", "8K" or "perfect". Generated clips carry no words, every prompt says "No music, no captions, no subtitles, no on-screen text", and every frame is still checked for burned-in text.
- **Credits:** fix the script, storyboard and frames first. Veo 3.1 Fast at 720p by default. Wait, never resubmit. Credits go on new scenes, faults are fixed in the edit, and a clip gets at most one retry with the user's go-ahead. No Higgsfield.
- **People and characters:** ChatGPT (GPT Image) makes every image of a person or character, by hand or by API. One tool per character, one master each, and each new image attaches only the sheets of the people in it.
- **Real product screens:** a product or tool on screen is built from the product's own code with real outputs (`remotion` rule `site-ui-from-code.md`), never mocked.
- **Story and sale videos:** 90 to 120 seconds on the seven-beat sale sheet, with a 30 to 45 second cutdown and an outcome-limits table per offer. They end on the outcome, then a short brand voice over that says what the viewer gets in use terms, then the product mockup with only the short domain. No spoken address, no full page path on screen, no end card, no small type disclaimer. A digital product is never shown as a printed book. No image or video credits go into storyboards.
- **Launch films:** 45 to 60 seconds, in 16:9 (X, LinkedIn, the website) and 9:16 (TikTok, Reels, Stories, WhatsApp Status). No separate short ad cut unless the brief asks.
- **Voiceover for coded films:** a walkthrough gets a narrator that adds a fact the screen does not show, and a game or show format gets short host stings of 1 to 5 words. Dialogue, chat and speech-bubble films stay silent. Narrator lines say the next thing and never read the caption, one short line per beat at 3 words a second or less, fitted to the beat with the picture never retimed. Pick the voice by ear from samples in several voices, with a persona instruction naming city, age, accent, pace and register. Build it as a lines file, one audio file per line plus a manifest, placements from the manifest, music ducked under each line (about 55% for a narrator, 40% for a host), an audit that each line sits inside its beat, and -16 LUFS. Test the voiced cut against the silent one. A synthetic voice means the platform's AI label goes on. Keys come from the shared keys file and are never printed.

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

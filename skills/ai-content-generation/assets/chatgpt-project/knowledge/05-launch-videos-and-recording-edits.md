# 05 - Launch Videos and Recording Edits

Build two kinds of video with Claude Code and Remotion: launch and product videos made of motion graphics and an AI voice with no person on screen (type A), and edits of your own recordings, including a Hormozi-style edit (type C). Both can copy the style of a video that already works.

> Mindset: the reference does the creative planning. You measure a proven video, rebuild its structure with your product and your facts, and let code do the editing. The result is only as good as the reference you pick and the inputs you supply.

**What you need**

| Job                      | Tool                                             | Cost                                              | Swap options                                                    |
| ------------------------ | ------------------------------------------------ | ------------------------------------------------- | --------------------------------------------------------------- |
| Planning and build agent | Claude Code with the `remotion` skill            | Claude plan                                       | Codex as fallback                                               |
| Video build              | Remotion (code to video)                         | Free for individuals and companies up to 3 people | Company licence for 4 or more people                            |
| Cuts, stills, loudness   | ffmpeg                                           | Free                                              | CapCut for manual touch-ups                                     |
| Word timings, transcript | whisper.cpp (Whisper)                            | Free                                              | Whisper Transcript desktop app for a quick `.srt` file          |
| AI voice (type A)        | Google Cloud Text-to-Speech (TTS), Studio voice  | Free allowance each month, then billed            | ElevenLabs for a cloned voice                                   |
| Music and sound effects  | Mixkit, Freesound (CC0 or CC BY sounds only) | Free | Other packs with a clear licence |
| Frames from a reference  | A frame extractor, or ffmpeg                     | Free                                              | None needed                                                     |

**End result:** a vertical master (1080 by 1920, 30 frames per second) plus the planning notes and a reusable Remotion style template.

---

## Pick Your Type

| What is on screen                          | Use                                                                  |
| ------------------------------------------ | -------------------------------------------------------------------- |
| Nothing but screens, cards and animated text, with an AI voice | This playbook, type A                                    |
| You, from a recording you already have     | This playbook, type C                                                |
| An AI person generated from a prompt       | the 02-ai-clone-talking-head knowledge file or the 03-ai-ad-creative knowledge file         |

Type A and type C share the same six steps from the "Workflow" section of the 00-workflow-and-rules knowledge file. This playbook gives the detail for each step. Where a rule already lives in 00, this playbook links to it.

---

## Setup (Do This Once)

Setup takes about 30 minutes. Ask Claude Code to install and verify each tool, and have it prove each one works before you move on.

**ffmpeg.** Install it with Homebrew on a Mac. The local build has no `libass`, the library that burns subtitles into video, so ffmpeg cannot draw captions here. Captions are always rendered in Remotion. Use ffmpeg for scene detection, stills, joining clips and loudness.

**whisper.cpp.** Install `whisper-cpp` with Homebrew and download the `ggml-base.en` model. The model is a sizeable download, so confirm before it starts. Test it on a short clip and check that it returns words with timestamps. Whisper cannot hear music, so tell Claude when a reference has a music bed.

**Remotion.** Nothing to install up front. Claude scaffolds a project per video with `npx`. Remotion is free for individuals and companies of up to 3 people. A team of 4 or more needs a company licence. In Remotion Studio, audio stutters while you scrub the timeline. The final render is clean.

**Google Cloud Text-to-Speech (type A).** Create a Google Cloud project with billing turned on. Enable the Cloud Text-to-Speech API. Create a service account (it needs no role), create a JSON key for it, and store the key in a private folder outside the video folder and outside your notes. Give Claude the folder path only. Never paste the key contents into chat and never save the key in your notes or a repo. A Gemini API key does not work for this. The Studio voice sits under Google's legacy voices. It has a monthly free allowance, and the current limit is on Google's pricing page, so check it in the console before you plan volume. Chirp 3 HD, the newer voice, does not take Speech Synthesis Markup Language (SSML), so the pacing method below needs Studio.

**Frame extractor.** Use a browser frame extractor or ffmpeg to turn a reference into a folder of frames. Pair it with a Whisper `.srt` file. With both in the project folder, Claude reads the pre-made frames and transcript and does not spend plan usage watching the video.

**Pre-flight tool check.** Before every project, ask Claude Code to run this and report one line per tool:

```
Run a pre-flight check for a video project. Report one line each: node version,
ffmpeg version, whisper-cli and which model file is downloaded, and whether npx
can reach Remotion. For type A, also confirm the path I give you to the Google
service account file exists. Check the path only. Never open, print or search
for the contents of any credential file. If anything is missing, tell me the
fix and stop.
```

If a command is "not found" after an install, open a fresh terminal. If the voice step fails, check that the API and the service account sit in the same project, that billing is on and that the key path is correct. For tool prices see the "Tools and prices" section of the 00-workflow-and-rules knowledge file.

---

## Do This For Every Video (the loop)

Each step writes one file, and the next step reads it. Claude can run steps 1 to 3 in one sitting. You approve twice, at the script and at the scenes. For the full workflow and the tier table, see the "Workflow" section of the 00-workflow-and-rules knowledge file.

Planning notes live in your notes asset folder for the video: REFERENCE, SCRIPT, SCENES and the hub. Clips, audio, frames and renders live in a linked work folder outside your notes. See the "Folders and files" section of the 00-workflow-and-rules knowledge file.

### Step 1. Reference brief

Write five lines: goal, audience, message, platform and length, and the call to action. Then pick one to three proven videos that do the same job. Save each one into the work folder. If a type A video has no good reference, ask Claude for three scored concepts instead.

Run the reference teardown from the reference-teardown knowledge file. It produces a REFERENCE note with the shot list, the hook, the beats with word counts, the captions, the graphics and the sound.

When you copy a style (a creator's edit or a brand's motion), add the measured style spec below to REFERENCE. Claude reads frames and transcripts. It does not watch motion, so the style is measured, not guessed.

1. Capture two or three references. Pull frames and a transcript for each.
2. Run ffmpeg scene detection to find every cut and transition.
3. Pull frames densely, 10 to 30 per second, around each transition so the timing of each move can be measured.
4. Write the style spec in numbers:
   - cuts per minute
   - how often the frame zooms and by how much
   - caption words per screen, size, position and highlight colour
   - how long each animation lasts and how it eases in and out
   - how long text holds on screen
   - sound effects per minute and what triggers them
   - colour, type and layout grid

Copy the style and never the assets. Their footage, music, logos and brand marks stay out.

This prompt runs steps 1 and 2 together. Paste it into Claude Code in the video's work folder, with the reference video, any frames and `.srt` file, and your `IDEA.md` or brief:

```
You are an editor who studies ads and can explain why every second of a video
exists. Goal: by the end of this chat there are two files, REFERENCE.md (how
the reference is built) and SCRIPT.md (its script rewritten for my product,
beat for beat).

How this chat works: go one stage at a time. Name the stage at the top of each
message. Preview each stage in five lines or fewer, then wait for me to say
"go". Keep messages short except the files.

Stage 1, inputs and tools. Confirm which reference video to use. Reuse any
frames and .srt transcript I supplied. Check ffmpeg and whisper-cli only for
what is missing. Read my brief or IDEA.md. If it is missing, ask me five
questions: what it is, who it is for, the problem it fixes, what they get, and
what they should do after watching. Stop until anything missing is fixed.

Stage 2, watch and listen. Sample one frame per second, and look closer only
where the picture changes. Use ffmpeg scene detection to find the cuts. Get
word timings from Whisper into reference/words.json. Report shot count, length
and video type in three lines.

Stage 3, REFERENCE.md. Write it only from what you saw and heard, in this
order: one-line summary, numbers (length, shots, average shot length, words per
minute), a shot table (start, end, on screen, exact words, caption, the shot's
job), the hook word for word with the move it makes, the narrative in one line,
every sentence with the shots it starts and ends in, four to seven beats with
seconds and word counts, captions (position, words per group, weight, colours,
highlighted words), graphics with timing and motion, sound, and three lines on
why it works. Add a measured style section: cuts per minute, zoom size and
frequency, caption layout, animation durations and easing, text hold times and
sound effect timing. Write "unclear" for anything you cannot see. Do not
guess. Stop and let me confirm the beats.

Stage 4, SCRIPT.md. Same hook move, same narrative, same beats in the same
order. Sentence breaks land on the same shots as the reference. Each beat stays
within five words of the reference beat. If there is no person on screen, write
the voiceover and the on-screen text separately. Every claim must come from my
brief. Where a fact is missing, write [NEED: what fact]. Never invent a
number, result, customer or quote. Make a table per beat (job, words,
on-screen, seconds), then the plain script one sentence per line. Read it back
against the reference and flag any beat that runs long or short. Stop for my
approval.

Hard rules: copy structure, timing and style, never the reference's words,
product, people or claims. Describe only frames you actually viewed. Allow one
round of changes per file, a second only if I ask. Never delete files.
```

### Step 2. Script

Approval point 1. The prompt above stops at SCRIPT with the beat table and the plain script. Check each beat's word count against the reference, and check every claim against the brief. Fill every `[NEED: ...]` with a real fact from you, or cut the line. For rules on spoken accuracy see the "Dialogue accuracy" section of the 00-workflow-and-rules knowledge file.

For type C, Step 2 is a paper edit. Claude transcribes your recording with Whisper and shows you the transcript with timestamps. You and Claude pick the lines that stay, in the order they stay. Claude writes the paper edit as a beat table of kept lines. Nothing is cut yet. The script is your own words, so check claims against what you said and against the brief.

### Step 3. Scenes

Approval point 2. SCENES is the build plan, approved before any code is written. Paste this in the same chat after the script is approved:

```
You are an editor who builds with code and knows the four tells of AI video:
a different style in every scene, a voice with no pauses, captions that sit
still, and scenes that fade into each other. Goal: SCENES.md, the build plan.
Do not build anything yet.

Read REFERENCE.md, SCRIPT.md and my brief. Name the video type (A or C). List
the product screenshots, screen recordings and brand files I supplied. If
there are none for a type A video, stop and tell me. Write SCENES.md:

1. The look in five lines: background, fonts, colours, caption style, entry
   and exit motion. Caption style, layout and motion copy the reference.
   Colours come from my product screens or brand kit.
2. A scene table with one row per script line: timing (matched to the
   reference beat), words, what is on screen, which files it uses, entry
   motion and sound.
3. Build rules: captions show 3 to 5 words at a time and sit under the chin of
   any face. Nothing goes in the bottom fifth of the frame. No fades between
   scenes. No black or empty frame. Something moves in every shot.

For type C, also list every cut (silences and fillers to remove), every
punch-in zoom, every callout, and every proposed insert (B-roll, screen
recording or stock clip) with the exact line it sits on and where the footage
comes from. Mark each insert "proposed". I approve or cut each one.

Use only facts from SCRIPT.md and my brief. Invent no numbers, claims,
reviews or product screens. Stop for my approval. Allow one round of changes,
a second only if I ask.
```

Caption style copies the reference each time, and the safety rules still apply on top. See the "Captions" section of the 00-workflow-and-rules knowledge file. Brand colours are a hard rule: they come from the product screens or the brand kit. See the "Brand colours" section of the 00-workflow-and-rules knowledge file.

### Step 4. Voice

**Type A.** Claude generates the voice with Google Cloud Text-to-Speech and the `en-US-Studio-Q` Studio voice, one script line per request. It wraps each sentence in an SSML `<s>` tag and adds a break of about 400 milliseconds after it. The voice then pauses and drops at the end of each sentence like a person. Claude joins the lines into one file.

**Type C.** The recording is the voice. Claude transcribes it, finds pauses, false starts and filler words, and says which lines it will cut before it cuts them. Where you said a line twice, it keeps the best take.

For both types, Claude normalises the track to -16 LUFS (Loudness Units relative to Full Scale), then runs Whisper on the final track to get word-level timing into `words.json`. Claude reports the length and the first and last word times. It does not play the audio. Save `voice.wav` and `words.json` in the work folder. For music and effects licensing see the "Audio and licensing" section of the 00-workflow-and-rules knowledge file.

### Step 5. Shots

Type A and type C usually have no generated shots, so this step is mostly empty. Generate a shot only when SCENES calls for one, such as a B-roll clip for type C or a 3D product hero for type A. For a person on camera generated by AI, use the 02-ai-clone-talking-head knowledge file or the 03-ai-ad-creative knowledge file and bring the clips back here for the build. Retry caps and credit rules are in the "Credits and retries" section of the 00-workflow-and-rules knowledge file.

### Step 6. Finish and check

Paste this build prompt after SCENES is approved and the voice and `words.json` exist. It calls the `remotion` skill for the build.

```
You are an editor who builds with code. Build the video from the approved
SCENES.md. Use the remotion skill for project setup and rules. Skip its
concept-selection and brief steps, because REFERENCE, SCRIPT and SCENES are
already approved. Brand colours, fonts and layout come from SCENES.md.

How this chat works: one stage at a time, named at the top of each message,
previewed in five lines or fewer, then wait for my "go".

Stage 1, project. Create a Remotion project in video/ at 1080 by 1920, 30
frames per second, as long as voice.wav. Build one scene at a time from
SCENES.md.

Stage 2, build.
- Captions are driven by words.json, 3 to 5 words at a time, appearing as each
  word is spoken, in the reference's caption style. Never over a face. Nothing
  in the bottom fifth of the frame.
- Product screens and screen recordings appear exactly as captured. Never
  redraw them.
- Music is one track at low volume, ducked lower under speech. Sound effects
  go on each cut and each graphic entrance, quieter than the voice. Log every
  source and licence in SOUNDS.md.
- No fades. Something moves in every shot.
- For type C, apply the approved cuts, jump cuts, punch-in zooms, callouts
  and inserts only. Put a whoosh, pop or ding on each cut, zoom and graphic.
- Open Remotion Studio, warn me that audio stutters while scrubbing, and show
  stills from the start, middle and end.

Stage 3, render and self-check. Render video/out/final.mp4. Pull one still per
scene with ffmpeg and compare it side by side with the matching reference
beat. Fix layout or timing mismatches. Check length against SCRIPT.md, size
1080 by 1920, that audio is present, that no caption covers a face and that
nothing sits in the bottom fifth. Show me the video and the side-by-side
stills. Allow one round of changes, a second only if I ask.

Hard rules: every word on screen comes from SCRIPT.md or my brief, with no
invented claims, numbers or reviews. Use only my assets, assets with a
licence I can use, or assets I supplied. Change one thing per fix request. On
an error, read it, fix it and explain in one line. Never delete my files.
```

Run the render check, then run the "Final check" section of the 00-workflow-and-rules knowledge file. If the video uses an AI voice or any generated footage, add the label from the "AI disclosure" section of the 00-workflow-and-rules knowledge file.

---

## Type A: Launch and Product Videos

A launch video is screens, cards and animated text over an AI voice. It is built entirely in Remotion, and it is the strongest thing this setup does.

**What works well.** Kinetic type, UI walkthroughs, SaaS launch videos, shape and mask transitions, 2.5D parallax camera moves, charts and Lottie animations. Real product screens make the video look authentic. Easing and timing come from the measured style spec.

**Inputs that set the ceiling.** Missing brand assets hurt more than any other gap. Bring:

- product screens, screen recordings or Figma files
- vector logos
- the brand fonts and colours

Do not ask Claude to redraw a product screen. If the screen does not exist yet, make it first.

**Cold audience first scene.** The `remotion` skill applies a cold audience rule by default: a visual pattern interrupt, text that names a problem or result the viewer recognises, and no brand card in scene 1. Keep that rule unless the video is for existing users.

**Where it will not match the reference.**

| Style                                       | Can we match it? | Workaround                                                                                         |
| ------------------------------------------- | ---------------- | -------------------------------------------------------------------------------------------------- |
| Kinetic type, UI walkthroughs, launch videos | Yes              | Build in Remotion from the measured spec                                                           |
| Shape transitions, masks, 2.5D parallax      | Yes              | Take easing and timing from the spec                                                               |
| 3D product hero shots                        | Partly           | Generate the shot with Veo or an image tool, or build it in Spline or Three.js, then place it in Remotion |
| Hand-drawn or character animation            | Rarely           | Use AI video clips where the quality holds, or hire an animator                                    |
| Heavy particles, fluids, After Effects plugin looks | Rarely    | Use licensed stock elements or pick a different style                                              |

Expect two or three tuning rounds against the reference. A first build rarely matches the polish of a top launch studio. It can beat the reference on fit, because the video uses your real product and message. You can also combine references: pacing from one, type from a second and transitions from a third.

---

## Type C: Edits of Your Own Recording

Use this for a talking head, a podcast clip or any recording you already have. The editing follows rules, and rules turn into code. The footage does not.

**The Hormozi-style edit, element by element.**

| Element                                           | How it is built                                                                                     |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Transcript-first paper edit                       | Whisper transcript, then you pick the lines that stay (Step 2)                                      |
| Tight jump cuts with no pauses                    | Word timings find every silence and filler word, and the template cuts them out automatically      |
| Punch-in zooms every few cuts                     | The frame scale alternates on a rhythm taken from the measured spec                                 |
| Bold word-by-word captions, key words highlighted | Captions come from `words.json`. Claude marks the key words and you edit the list                  |
| Sound effects on every change                     | A whoosh, pop or ding is placed on each cut, zoom and graphic                                       |
| Text callouts, numbers, lists and icons           | Claude proposes a callout for each claim or number, built from template components                 |
| B-roll, meme and screen-recording inserts         | Claude proposes each insert with the line it sits on. You approve, because this needs taste and humour |

**Inserts.** Use stock footage with a licence you can use, generated B-roll or your own screen recordings. Do not lift clips from other creators.

**What editing cannot fix.**

- **The footage.** A phone in a dim room with an echo will not look like a studio creator, however good the edit. A key light, a lapel mic and a plain background close most of the gap.
- **The delivery.** Fast cuts sharpen strong delivery. They cannot rescue flat delivery.

After one or two tuning rounds most viewers will read the edit as the same style. Every later recording then runs through the template in minutes.

---

## Copying a Style Into a Template

When a style will be reused, turn the measured spec into a Remotion template. Each rule in the spec becomes a parameter in code. Ask Claude:

```
Turn the measured style section of REFERENCE.md into a reusable Remotion
template. Every number in the spec becomes a named setting: cuts per minute,
zoom scale and frequency, caption words per group, caption position, size and
highlight colour, animation duration and easing, text hold time, sound effect
timing. Brand colours, fonts and logo come in as inputs, so the same template
works for another brand. Do not copy the reference's footage, music, logos or
words. Save the template in the project, then render a 10 second test and pull
stills at matching moments beside the reference. List every mismatch in timing
or layout. Stop for my review. Allow one tuning round, a second only if I ask.
```

Check the template side by side with the reference, beat by beat. Tune it until timing matches. Then record the template name and the reference it came from in the hub, so the next video starts at Step 2. The taste call on the side-by-side check is yours. Claude copies a measured reference well and invents an original look less reliably.

---

## Make It Look Real (not AI slop)

*The prompts above already carry these rules. Use this as a pre-post pass.*

- **Pause the voice.** Studio voice with sentence tags and breaks sounds human. A voice with no pauses is the most common tell.
- **Move the captions.** Captions that appear word by word at the pace of speech read as edited. Static captions read as automated.
- **One style.** Use one look across every scene. A different style per scene is a tell.
- **No fades.** Hard cuts and motion. Fades between scenes look like a slideshow.
- **Real screens.** Product screens as captured, with brand colours taken from them.
- **Fix the source.** Tight edits cannot hide a bad mic or a dark room.

---

## Common Mistakes

- Picking a weak reference. The output cannot beat the reference you copy.
- Skipping the SCENES approval and fixing problems in code afterward.
- Letting Claude invent a claim, a number or a quote to fill a beat. Use `[NEED: ...]` and supply the fact.
- Asking ffmpeg to burn in captions. This build has no `libass`. Render captions in Remotion.
- Colours chosen by taste. Take them from the product screens or brand kit.
- Pasting a service account key into chat or saving it in your notes. Share the path only.
- Treating a first render as final. Plan two or three tuning rounds against the reference.
- Copying the reference's music, footage or logos.
- Running more than one or two revision rounds per file. Decide what to change, then change it.

---

## Before You Post

- The reference is a proven video, and only its structure and style were copied
- Every claim on screen and in the voice traces to the brief, with no `[NEED: ...]` left
- REFERENCE, SCRIPT and SCENES are approved and saved in your notes asset folder, with clips and renders in the linked work folder
- Brand colours come from the product screens or brand kit
- Captions are 3 to 5 words, word-timed, clear of faces and the bottom fifth
- No fades, no black frames, something moves in every shot
- Loudness is about -16 LUFS, and music sits under the voice
- Music, effects and inserts have a licence that covers the platform, logged in SOUNDS.md
- Side-by-side stills against the reference match on timing and layout
- Type C only: every cut, zoom and insert was approved, and no clip is lifted from another creator
- AI label added where the voice or footage is generated
- Credential files stayed outside your notes and out of chat
- Template and reference logged in the hub if the style will be reused

---

Related: the 00-workflow-and-rules knowledge file · the 01-faceless-influencer knowledge file · the 02-ai-clone-talking-head knowledge file · the 03-ai-ad-creative knowledge file · the 04-faceless-youtube knowledge file · the reference-teardown knowledge file

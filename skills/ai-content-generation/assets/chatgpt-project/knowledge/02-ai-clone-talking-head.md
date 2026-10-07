# 02 - AI Clone & Talking Head

Clone your own face and voice into an AI talking head, then generate endless videos from scripts without filming each one.

> Mindset: lip sync is mostly solved now, so a flat robot voice is the biggest tell that exposes an AI clone. Fix the voice first and the face follows.

**Tier:** this playbook runs the performance tier of the "Workflow" section of the 00-workflow-and-rules knowledge file for a clone of you. You build the clone's anchors and voice once (Do This Once), then run the six steps on every video. Tool prices live in the "Tools and prices" section of the 00-workflow-and-rules knowledge file.

| Workflow step | Where it happens here |
|---|---|
| 1 Reference brief | Step 7, a reference-first path using the the reference-teardown knowledge file |
| 2 Script | Step 7, a beat table with a word budget per beat. You approve it |
| 3 Scenes and anchors | Steps 4 and 5 build the anchors once. Step 8 makes start frames for new setups and a contact sheet |
| 4 Voice | Step 2 clones the voice. Step 10 locks it onto the clips |
| 5 Shots | Step 9, one take per shot, three tries at most |
| 6 Finish and check | Step 11 and the Before You Post list |

**What you need**

| Job | Tool | Notes |
|---|---|---|
| Describe your face, write animation prompts | ChatGPT (or Gemini) | ChatGPT makes the anchor stills too |
| Talking video | Google Flow with Gemini Omni (speaks natively) or Veo 3.1 | Higgsfield (Kling) for one-off clips. HeyGen for a reusable avatar |
| Voice clone and re-voicing the video | ElevenLabs on a paid plan (clone plus Voice Changer) | Cartesia and MiniMax are swap options |
| Editing | CapCut | Descript and Premiere also work |

**End result:** an AI version of you that says any script on camera. You write the script and a clip comes out the other side.

Planning notes (reference, script, shot table) live in your notes. Clips, audio and renders live in a linked work folder outside it. See the "Folders and files" section of the 00-workflow-and-rules knowledge file.

---

## The recommended pipeline (start here)

This is the primary way to clone yourself in your own voice, and it solves lip sync. The HeyGen and Higgsfield routes still work and are kept below as alternatives. The detailed how-to for each step lives in the sections that follow. This is the map.

1. **Build your character anchors in ChatGPT** (Steps 4 and 5). Multiple reference angles, a written face and body breakdown, one clean reference image, a multi-angle mashup to confirm consistency, a reusable JavaScript Object Notation (JSON) prompt, and a two-image anchor (close-up, then wide).
2. **Lock the scene and environment** (Step 5). Decide where the character is and lock the outfit, background, camera angle, lighting and style. Write it once as a reusable scene description.
3. **Generate each beat in Flow with the model speaking** (Step 9). One clip per beat, each from its anchor still, each with the dialogue accuracy line, each sized to its line.
4. **Assemble the clips** in Flow's scene builder and export.
5. **Clone your own voice in ElevenLabs** (Step 2).
6. **Re-voice with ElevenLabs Voice Changer** (Step 10). Upload the exported video or its audio and regenerate the same dialogue in your cloned voice. It keeps the original timing, so the mouth movements still match.
7. **Swap the audio in CapCut,** then add word-timed captions, grain and a colour grade (Step 11).

**Why it works:** the video model drives the mouth off its own generated speech, and Voice Changer keeps that speech's timing, so your voice lands on the same lip movements. This avoids the drift of lip-syncing a fresh voice track onto silent footage.

---

## Do This Once (this sets the quality ceiling)

You only do this part one time. Do it well, because everything you generate later can only be as good as what you capture now. A flat, blurry, badly lit source produces a stiff clone that no prompt can fix.

### Step 1: Capture clean source material

Get these once and keep them in a folder you reuse forever.

**Face photo (required):** One clean, front-facing photo of your face. Even soft light (a window works), plain background, no filter, no heavy makeup or sunglasses. Chest up, looking just slightly off the lens, with no dead-center stare. This single photo is enough to start.

**Short video (optional, for a higher-quality avatar):** 2 to 5 minutes of you talking to camera. 1080p or better, even soft light, plain wall behind you, an external mic if you have one, solid-color top, no filters. While you talk, move the way you normally do: smile, tilt your head, use your hands, raise your eyebrows. A frozen news-anchor pose trains a stiff clone.

**Voice audio (for the voice clone):** clean speech in a quiet room, recorded in the same energy you will generate in. How much you need depends on the clone type in Step 2. The script below gives enough range for an Instant clone when you read it twice. A Professional clone needs hours of audio, so plan several recording sessions across different moods and topics, and check the current requirement on ElevenLabs before you start. Read the script out loud, each block in the labeled mood, like you are talking to one person.

```
VOICE CAPTURE SCRIPT. Read each block in the labeled mood, out loud, to one person.

[CALM EXPLAINER] Okay, so here's how this actually works. There are three parts, and most people only ever think about the first one. I'll walk you through all three.

[EXCITED] No, but this is the part I love. This is the thing nobody tells you. When it clicks, it really clicks, and you'll never look at it the same way again.

[WARM] Hey, it's fine. Honestly, everyone gets stuck here. You're not behind. Take a breath. We'll do this one step at a time.

[SERIOUS] Look, I'm going to be straight with you. If you skip this part, the rest won't hold. I've watched people learn that the hard way.

[STORYTELLING] So a few years back, I tried this for the first time, and yeah, it went badly. Really badly. But that mistake taught me the one thing this whole approach is built on.

[FAST LIST] First, pick one thing. Second, do it daily. Third, track it. That's it. Three steps. No app, no system, no excuses.

[QUIET, SOFTER] The more I think about it, the more I realize the hard part was never the work. It was deciding it mattered.

[NON-VERBAL, perform these] a genuine laugh, a tired sigh, a short exhale before a sentence, a soft "mm-hm," a thoughtful "uh" before a key word.

[NUMBERS AND NAMES, read clearly] 2026. Forty-five percent. ElevenLabs. Naira. Eighty-seven dollars. www dot example dot com.

[CLOSE] Alright. That's the whole thing. If this helped, you know what to do. I'll see you in the next one.
```

Read the whole script twice with slightly different energy each time. That gives the clone real range to draw from.

### Step 2: Clone your voice in ElevenLabs

Go to ElevenLabs. Use a paid plan, because the free plan has no commercial licence and cannot be used in ads. You have two options.

**Instant clone (Instant Voice Clone, IVC):** Works from a short sample, often one to two minutes, and is done in seconds. Good for quick tests and for most daily content. Available on the Starter plan and above.

**Professional clone (Professional Voice Clone, PVC):** Trained on hours of your audio, highest fidelity, closest to your real voice. Takes a few hours to train. Needs the Creator plan or above. Use this for anything long-term or high-stakes.

Upload your clean audio, name the voice, start the clone. When it finishes, open the voice settings and set them like this.

```
ELEVENLABS VOICE SETTINGS (for natural delivery):
- Stability: Natural or Creative. NEVER Robust. Robust is the monotone robot tell.
- Similarity: mid-to-high, not maxed. Maxed can over-copy noise from your recording.
- Style: low to moderate.
- Model: the current Eleven v4 model for cloned voices. Professional clones on v4
  are rolling out, so confirm in the app which model your clone supports.
```

This is the single most important step in the whole playbook. The voice carries the realism. Voice Changer draws from the same credit pool as text to speech and costs far more per minute, so plan credits for it. Check the rate in the "Tools and prices" section of the 00-workflow-and-rules knowledge file.

### Step 3: Take or choose your face photo

Use the clean front-facing photo from Step 1, or take a fresh one in the same even light against a plain background. One photo is all you need.

### Step 4: Build the clone character in ChatGPT

Open ChatGPT. Upload your face photo and paste this.

```
Here is a photo of me. Break down every detail of my face in writing:
face shape, skin tone and texture, hair, eyes, eyebrows, nose, mouth, beard
or no beard, build, and what I'm wearing. Be specific enough that the
description alone could recreate me.

Then generate a clean, photorealistic reference image of me from that
description. Front-facing, chest up, even natural light, plain background,
looking slightly off the lens, not a studio shot, not airbrushed, slight
real-skin imperfection.
```

You now have a written face description plus a clean reference image. Download the image. Keep the written description, you will reuse it.

**Then confirm consistency with a multi-angle mashup.** Before you lock the character, ask for the same face from several angles in one image, so you can see it holds together:

```
Produce a mashup of this character's face from different angles (front,
three-quarter, side) in one image, to confirm the identity stays consistent.
```

If any angle drifts into a different person, regenerate the reference image before moving on. Feeding multiple reference angles up front (a headshot, a side view, a full-body shot) makes this hold better.

**Make the description a JSON prompt and use your tool's face lock.** Two upgrades keep the same you across tools instead of drifting between them.

- **Ask for JSON as well as prose.** Run this on your photo, either folded into the prompt above or on its own: "Analyze this photo and write me a detailed JSON prompt describing this person's face, skin tone, hair, facial features, and overall appearance. Format it for use in AI image generation." A structured JSON face block reuses cleanly across every tool and drifts less than a paragraph does.

- **Turn on the native face-reference lock.** Pair the JSON prompt with the tool's own face feature so your identity holds: Midjourney Omni Reference (`--oref`, strength 300 to 500, for V7 and later), Leonardo Image Reference with Character mode, FLUX Kontext face reference, Kling face reference, and Gemini Nano Banana in-app. The JSON says what your face is and the reference shows it.

### Step 5: Build the two-image anchor and lock the scene

Every clip starts from a still. Make two once in ChatGPT, the same tool that built the character, and save them in your reusable folder:

1. **The close-up.** Chest up, 9:16, from your reference image, with a full description of age, look, clothes, setting and lighting. No text in the image.
2. **The wide.** Generate it with the close-up attached as the reference image, so the face matches. Same outfit and room, more of the setting, 9:16, no text.

Name them `character-close` and `character-wide`. Attach the right one to every clip: the close-up for close framing, the wide for wide framing. For a variant, tell the model "keep every other thing consistent" and name the one thing that changes.

**Check for stray props.** Look at both stills for objects that should not be there, such as a phone stand beside a person who is meant to be filming themselves. Remove them with an explicit line ("remove the phone and the phone stand, they should not be there") and regenerate.

**Lock the scene.** Decide where you are (a room, a podcast desk, a stage, a desk, walking outside, a studio) and settle the outfit, background, camera angle, lighting and style. Write it once as a reusable scene description and paste it into every beat so the character, wardrobe and room stay identical from clip to clip.

### Step 6: Optional, build a reusable avatar in HeyGen

If you want one avatar you can reuse on every video (instead of generating from a photo each time), do this once.

Go to HeyGen, create a custom avatar, and upload your 2-to-5-minute video from Step 1. Pick the highest-realism human option HeyGen offers for custom avatars. Let it train. Then connect your ElevenLabs voice so the avatar speaks in your cloned voice. Now you pick this avatar and paste a script any time, no photo step needed.

If you skip this, the Flow loop below works without it.

---

## Do This For Every Video (the loop)

Once your voice and anchors exist, every video is these steps.

### Step 7: Start from a reference, then write the beat table

If a proven talking-head video exists for your topic, run the the reference-teardown knowledge file on it first. You get the hook move, the beats with word counts and the caption style. Copy the structure and timing. Never copy the words, footage, music or claims. For a quick post with no reference, write from your own notes.

Paste your script or the teardown's beats into ChatGPT:

```
Here is the script my character will say out loud:
[PASTE YOUR SCRIPT OR THE REFERENCE BEATS]

Split it into beats of one spoken line each, and give me a table:
Beat # | Spoken line (only this beat's words) | Word count | Seconds
(about 4 for a short line, up to 8 for a long one) | Framing (close or wide) |
Cutaway after it (yes/no). Keep each beat within 5 words of the reference beat.
Any fact I did not give you becomes [NEED: fact]. Do not invent it.
```

You approve the table before anything is generated. Fix the script now, because every change after this point costs credits.

**Write for the ear.** Use commas for breath, "..." for a pause, ONE word in CAPS per line for emphasis, and a real filler ("look," "honestly," "so") before the key line. Uniform, perfectly punctuated marketing prose is the robot tell. Two or three breaths per short script reads human. Ten reads fake.

### Step 8: Make the start frames

For each shot, name the anchor still it uses (close or wide). If the video has a new setup, generate its start frame from the anchors and lay all start frames out together as a contact sheet. Check that the face, outfit, room and props hold from frame to frame, and that no stray prop has appeared. You approve the contact sheet before paying for video. Your saved anchors cover a repeat setup, so no new frames are needed.

### Step 9: Generate the clips

**Primary: Google Flow, Gemini Omni (or Veo 3.1), with the model speaking.** In Flow, choose the model, set the clip length, ask for one output, and set 9:16. Attach the start frame. Veo 3.1 is the choice when you want its look or 4K. Omni suits most talking shots.

Paste the beat's prompt. Write one prompt per beat, built from your scene description:

```
[SCENE DESCRIPTION: same room, outfit and light as the start frame].
The person talks directly to camera, casual phone-camera framing, natural light,
subtle natural head and hand movement, real-time pace, not slow motion.
Photoreal, slight grain. No on-screen text. Vertical 9:16.
The person says: "[THE LINE FOR THIS BEAT]"
Ensure that each word is pronounced correctly and you do not add any extra words.
```

**Dialogue accuracy.** Flow's biggest weakness is getting spoken words wrong, and every redo costs credits. The line above fixes most of it, so keep it in every speaking prompt. If the model mispronounces a name, say so in the next try: "The model says [wrong sound]. The word is [name], pronounced [phonetic]." See the "Dialogue accuracy" section of the 00-workflow-and-rules knowledge file.

**Match the clip length to the line.** One line per clip. As a starting estimate, a short line of about 8 to 10 words fits 4 seconds and a long line fits 8. A clip that is too short fails or cuts the line off. A clip that is too long makes the model invent filler actions you have to cut away. Merge two neighbouring lines into one clip only when they share a framing. The talking-face ceiling is about 8 seconds, so the 10 second option stays off faces. Test one short clip before you generate the whole video.

**Continuity inside one shot.** When the next clip continues the same shot, take the last frame of the previous clip and use it as the first frame of the next. Flow also has a first and last frame mode. When the next clip cuts to a different framing, start from the other anchor still.

**One thing per generation.** A prompt that asks for several actions confuses the model. Keep busy scenes simple.

**One take, three tries.** Regenerate only the clips that fail. After three failed tries, change the prompt or the start frame. After two failed fixes in Flow, hand the bad outputs to the assistant and ask it to rewrite the prompt in the tool's language. Change one thing per fix. See the "Credits and retries" section of the 00-workflow-and-rules knowledge file.

Use Flow's scene builder to sequence the clips into one continuous scene, and export. Name the clips `clip-1`, `clip-2` and so on.

**Alternative: Higgsfield (Kling).** Scroll to Create Video. Upload your anchor still. Paste the prompt. Generate. Keep clips short. Long single clips drift and the face warps.

**Alternative: HeyGen.** Pick your avatar, paste your script straight in, and generate. HeyGen lip syncs to your cloned voice directly, so skip Step 10. Keep each talking take short, then plan a cut.

### Step 10: Re-voice the video in your own voice

If you animated in Flow or Higgsfield, the clip is speaking in a generic AI voice. Swap it to your cloned voice without breaking lip sync.

Open ElevenLabs, go to Voice Changer (speech to speech), upload the exported video or its extracted audio, and select your cloned voice from Step 2. It regenerates the same dialogue in your voice and keeps the original timing, so the mouth movements still match. Download the new audio, then run Whisper on it to get word-level timing for the captions.

Skip this step if you used HeyGen, because it already spoke in your cloned voice.

### Step 11: Swap the audio, edit, and check

Drop the clip (or the assembled scene) on the CapCut timeline in order. First replace the audio: mute or delete the original voice track, drop in the Voice Changer track, and nudge it into alignment. Then do the moves that hide the weak spots.

- **Cut away** to b-roll at least every 8 seconds so the viewer is not staring at the face the whole time. This is also where you hide any moment where the lip sync looks slightly off: cut to a supporting visual and let your voice carry.
- **Captions.** Use word-timed captions, three to five words at a time, in the style of your reference. Keep them off your face and out of the bottom fifth of the 9:16 frame. Add any on-screen text here and never in the generation prompt. See the "Captions" section of the 00-workflow-and-rules knowledge file.
- **Sound.** Keep music low and ducked under speech, with a small effect on cuts. Use only licensed music. See the "Audio and licensing" section of the 00-workflow-and-rules knowledge file.
- **Texture and colour.** Add a light grain layer to re-inject texture, since AI renders look a bit plastic. Colour grade the whole thing. It is the single biggest fix for the synthetic look.
- **Run the final check** in the "Final check" section of the 00-workflow-and-rules knowledge file and watch the export once in a normal player.

### Step 12: Publish

Post natively in the app you are publishing to (do not post an obvious cross-post). Lead the caption with your hook. Set the AI label where the platform asks (see the "AI disclosure" section of the 00-workflow-and-rules knowledge file and the ethics section below). Then go back to Step 7 for the next video.

---

## Make It Look Real (not AI slop)

*The prompts above already bake these in. Use this as your pre-post checklist, and for the editing moves a prompt cannot do.*

The clone passes or fails on these few moves.

- **Fix the voice first.** Lip sync is mostly solved, so a flat voice is the number one tell. Natural or Creative stability, never Robust. A flat recording at clone time produces a flat clone forever.

- **Make the script breathe.** See Step 7. Uniform, perfectly punctuated marketing prose is the robot tell.

- **Keep each talking-face clip to about 8 seconds**, then cut to b-roll, then return. Full-screen face for 60 seconds reads as AI no matter how good the clone is.

- **Hide weak lip sync under cutaways.** Plan a cut to b-roll on the hardest lines (fast lists, long words, hard consonants). The viewer hears you and never sees the weak frames.

- **Use a medium shot instead of an extreme close-up.** Close-ups amplify every uncanny tell. Eyes slightly off-lens, never a dead-center stare.

- **Mix real footage into the b-roll.** Pure AI b-roll over an AI face compounds the synthetic look. One real stock clip (Pexels, Pixabay) grounds the whole piece.

---

## Going Further (when the basics work)

- **Go faster with a HeyGen avatar.** Once you build the reusable avatar, you skip the photo-and-image step entirely: paste a script, get a clip. Best for daily volume.

- **Batch your scripts.** Write a week of scripts at once, generate all the voice in one ElevenLabs run, then all the clips in one session. Staying in one tool keeps delivery consistent.

- **Reuse the prompt that worked.** In Flow, "Reuse prompt" shows the original prompt of a clip that worked. Once a prompt works, only the anchor still and the line change. After the first slow video, turn the run into a template or skill.

- **Repurpose one talk into many.** Take a recorded talk or podcast and edit it into short clips with a transcript-first cut. That is the job of the 05-launch-videos-and-recording-edits knowledge file. Regenerating the talk through your clone is a different job, and it needs your consent on the script and the AI label.

- **Automate it.** An n8n flow can chain script to ElevenLabs voice to HeyGen clip to caption to post. Keep a human approval gate before publishing, since clone content carries likeness and disclosure risk.

- **Monetize once you have reach.** A digital product, affiliate offers, course modules in your voice, or driving to a newsletter. The clone lets you scale presence without scaling filming time.

---

## Clone Types (quick note)

Four different things get called an AI clone. Pick the one that matches what you are making.

- **Avatar clone (this playbook).** Your face plus voice delivers any script as talking-head video. Use when you want talking-head video at volume without filming each one.

- **Voice-only clone.** Just your cloned voice. Use when you already film yourself and only want to stop re-recording voiceover or fix flubbed lines. You keep your real face.

- **Full digital twin.** Face plus voice plus a knowledge base that answers questions and talks back live (tools like Delphi). This is an interactive product and has no content pipeline. Use when you want an always-on version of you that coaches and answers around the clock.

- **Scene-insertion avatar (Google Flow).** A face-scan avatar you drop into any generated scene. It does not turn a script into a talking head. It is fast for putting yourself in places and slow for delivering a script. It sits behind a voice verification step, so check the current flow in Flow before you plan around it. This playbook's pipeline uses the anchor stills from Steps 4 and 5 instead. See the appendix in the 00-workflow-and-rules knowledge file.

---

## Ethics & Disclosure

- **Consent.** Clone yourself freely. To clone anyone else (a spokesperson, a partner), get written consent first, covering what it is used for, where, and for how long. Never imply a real person endorsed something without their consent.

- **Platform AI labeling.** YouTube, TikTok, and Meta all require disclosure of realistic AI media. Set the AI label when you post, and consider a small burned-in "AI-generated" label in a top corner. Undisclosed realistic AI can get reduced in reach or removed. See the "AI disclosure" section of the 00-workflow-and-rules knowledge file.

- **Paid ads.** If a clone runs in a paid ad, conspicuous AI disclosure is legally required (New York synthetic-performer law, effective Jun 9 2026, plus Federal Trade Commission scrutiny). Build the disclosure into the ad as well as the platform toggle.

- **Income claims (Nigeria and diaspora).** If the clone makes any specific income claim, carry the earnings disclaimer after the claim and before the offer: "My results are not promised. They are achievable if you put in the effort. I am a testament to what's possible."

---

## Common Mistakes

- The voice is flat. You recorded in a monotone or used Robust stability. A flat source clones flat forever. Re-record with real energy, set stability to Natural.

- The photo or video is bad. Blurry, harsh light, busy background, or a filter. The clone can never beat the source. Re-capture clean.

- One giant clip. The face warps and drifts. Generate short clips and cut them together.

- Mangled or invented words. The dialogue accuracy line is missing, or the clip is too short or too long for the line.

- Full-screen face the whole video, no cutaways. Reads as AI. Cut to b-roll at least every 8 seconds.

- Extreme close-up on the face. Amplifies every tell. Use a medium shot.

- Pure AI b-roll over the AI face. Compounds the fake look. Mix in real stock footage.

- A stray prop in the start frame. Check every still before generating video.

- No AI label. Required on YouTube, TikTok, Meta. Set it.

- Cloning someone else without written consent. Legal and ethical violation. Consent first, always.

---

## Before You Post

- Voice is yours, set to Natural or Creative (not Robust), and the free ElevenLabs plan was not used for an ad
- Script has breaths, pauses, and one emphasis word per key line
- Every speaking prompt carried the dialogue accuracy line, and no clip has mangled or invented words
- Talking-face clips about 8 seconds or less, then a cut
- B-roll cutaways at least every 8 seconds, weak lip sync hidden under them
- Real footage mixed into the b-roll
- Captions word-timed, in the reference's style, never over a face, nothing in the bottom fifth (the "Captions" section of the 00-workflow-and-rules knowledge file)
- Music and effects licensed (the "Audio and licensing" section of the 00-workflow-and-rules knowledge file)
- Light grain and color grade applied
- AI label set on the platform (the "AI disclosure" section of the 00-workflow-and-rules knowledge file)
- Consent on file if you cloned anyone but yourself
- Final check done and watched once in a normal player (the "Final check" section of the 00-workflow-and-rules knowledge file)
- Posted natively, caption leads with the hook

---

Related: the 00-workflow-and-rules knowledge file · the reference-teardown knowledge file · the 01-faceless-influencer knowledge file · the 03-ai-ad-creative knowledge file · the 04-faceless-youtube knowledge file · the 05-launch-videos-and-recording-edits knowledge file

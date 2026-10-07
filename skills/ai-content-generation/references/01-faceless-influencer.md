# 01 - Faceless Influencer

Build an AI character that posts short videos on TikTok and Instagram without you ever being on camera.

> Mindset: the whole game is making the same face appear every time and look like a real person. Everything else is a simple loop.

**Tier:** this playbook runs the quick social tier of the "Workflow" section of `00-workflow-and-rules.md`. You build the persona's anchors once (Do This Once), then run all six steps in short form on every post. Tool prices live in the "Tools and prices" section of `00-workflow-and-rules.md`.

| Workflow step | Where it happens here |
|---|---|
| 1 Reference brief | Step 5, one reference, structure only, using the `reference-teardown.md` |
| 2 Script | Step 6, a beat table with a word budget per beat |
| 3 Scenes and anchors | Step 3 builds the anchors once. Step 8 makes start frames only for new setups |
| 4 Voice | Step 4 picks the persona voice. Step 7 sets the route. Step 9 locks it |
| 5 Shots | Step 8, one take per shot, three tries at most |
| 6 Finish and check | Step 9 and the Before You Post list |

**What you need**

| Job | Tool | Notes |
|---|---|---|
| Character, scripts, reference breakdown | ChatGPT (or Gemini, Claude) | Gemini Nano Banana also makes face-locked stills |
| Voice | ElevenLabs on a paid plan | Voice Changer locks one voice across clips. The free plan has no commercial licence, so it cannot be used in ads. Cartesia is a swap option |
| Ad-safe cheap voice (optional) | Google Cloud Text to Speech (TTS), Studio voice | See Ad-safe voice options below |
| Video | Google Flow with Gemini Omni or Veo 3.1 for talking shots | Kling 3.0 or Seedance inside Higgsfield for bulk b-roll. Runway is a swap option |
| Editing | CapCut | Descript and Premiere also work |

**End result:** a recurring AI persona posting 1 to 3 short videos a day.

Planning notes (reference, script, shot table) live in your notes. Clips, audio and renders live in a linked work folder outside it. See the "Folders and files" section of `00-workflow-and-rules.md`.

---

## Do This Once (set up your character)

You only do this part one time. After that you reuse the same character and voice on every video.

### Step 1: Pick your niche

Choose one topic you could post about for a year. It needs proven faceless accounts already winning (search TikTok to confirm) and a way to make money later (a product, affiliate offers, or sponsorships). Good starters: money and side hustles, gym and discipline, AI tools, motivation, history facts, scary stories.

### Step 2: Design your character in ChatGPT

Open ChatGPT. Paste this:

```
Design the face of a [your niche] account. Create a [age]-year-old [man/woman],
[ethnicity], [vibe: e.g. approachable, intense, polished], wearing [wardrobe].
First write a detailed visual description I can reuse (face shape, skin, hair,
eyes, build, default outfit). Then generate a photorealistic portrait of them,
shot on a phone, natural indoor light, slight imperfection, not a studio photo,
not airbrushed.
```

Generate a few. Pick the best one. Download one clean, front-facing image. This is your influencer. Keep the written description too, you will reuse it.

### Step 3: Lock the face and build the anchors

This is the step beginners skip, and it is why most AI characters look different in every video. Your downloaded hero image is now the reference you upload every time. To make new angles, outfits, or settings while keeping the same person, upload the hero image back in and paste:

```
Keep this EXACT person, same face, same features, do not change their identity.
Now show them [side angle / in a kitchen / wearing a hoodie / outdoors at golden
hour]. Same phone-camera, natural-light, slightly imperfect look.
```

Save a small set: front, side, smiling, a couple of settings. That is your reusable asset library.

**Confirm consistency with a multi-angle mashup.** Before you trust the character, ask for the same face from several angles in one image and check it holds together:

```
Produce a mashup of this character's face from different angles (front,
three-quarter, side) in one image, to confirm the identity stays consistent.
```

If any angle turns into a different person, regenerate the hero image before you build your library on top of it.

**Lock the face harder with a JavaScript Object Notation (JSON) prompt and your tool's native face reference.** A plain re-upload works. Two upgrades make the same person hold across different tools, not just inside ChatGPT.

- **Get a JSON face prompt.** Upload your hero image to ChatGPT and paste: "Analyze this photo and write me a detailed JSON prompt describing this person's face, skin tone, hair, facial features, and overall appearance. Format it for use in AI image generation." A structured block (face shape, skin tone, eye color, hairline, and so on) travels between tools far more reliably than loose prose. Save it and reuse the same block every time.

- **Combine the JSON with a style reference.** When you want a specific look, an outfit, a lighting, a setting, grab a reference image of that vibe from Pinterest or Instagram. Feed the tool two things: your JSON face prompt (what the character looks like) and the style reference (the look you want). The JSON holds the identity and the reference sets the scene.

- **Turn on the native face-reference feature.** Most image tools have one and it beats a plain re-upload: Midjourney Omni Reference (`--oref`, strength 300 to 500, for V7 and later), Leonardo Image Reference with Character mode, FLUX Kontext face reference, Kling face reference, and Gemini Nano Banana, which locks a face in-app. Use the JSON prompt and the face reference together. The prompt says what the face is and the reference shows it.

**Build the two-image anchor.** Every shot starts from a still, so make two once and save them in the persona's folder:

1. The close-up. Your hero image works, or generate a chest-up 9:16 close-up from it. No text in the image.
2. The wide. Generate it with the close-up attached as the reference image, so the face matches. Same outfit and room, full upper body with the setting visible, 9:16, no text.

Attach the right still to every clip: the close-up for close framing, the wide for wide framing. When you need a variant, tell the model "keep every other thing consistent" and name the one thing that changes.

**Check for stray props.** Look at every anchor and start frame for objects that should not be there, such as a phone stand beside a person who is supposed to be filming themselves. Remove them with an explicit line ("remove the phone stand, it should not be there") and regenerate before the still goes anywhere near a video model.

### Step 4: Give them a voice

Go to ElevenLabs on a paid plan. Pick a library voice that fits your character, or design one from a description. Save it. Set Stability around 40 to 50 (natural, with some variation) and Similarity high. Use this same voice on every video so the persona sounds consistent. Step 7 covers the three routes for getting that voice onto the video.

---

## Do This For Every Video (the loop)

Once your character exists, every video is these six steps.

### Step 5: Start from a proven reference

Open TikTok or Instagram and search your niche. Find 3 to 5 videos getting far more views than the account's normal numbers. Pick the best one as your reference and run the `reference-teardown.md` on it. You get the hook move, the beats with word counts, the caption style and the sound. For a quick post, one reference and its structure is enough. You copy the structure and timing. You never copy the words, people, footage, music or claims.

### Step 6: Write your script in ChatGPT

Paste the teardown's beat table (or the winning video's transcript), then:

```
Here is a structure that went viral in my niche: [PASTE the beat table or transcript].

Adapt it for my character on the topic of [TOPIC]. Rules:
- First person, spoken out loud, the way a real person talks.
- 30 to 45 seconds (about 80 to 110 words).
- Keep each beat within 5 words of the reference beat's word count.
- A scroll-stopping first line that creates curiosity or names a problem.
- Plain words, no corporate phrasing, no "in today's video".
- Any fact I did not give you becomes [NEED: fact]. Do not invent it.
- End on one clear line (a takeaway or a soft call to follow).
Give me 3 versions of the hook, then the full script under the best one,
as a table: beat, job, words, spoken line, visual.
```

Tighten the hook until it makes you stop scrolling. You approve the script before anything is generated.

### Step 7: Set the voice route and write for the ear

First make the script sound human. Add pauses, emphasis, and a breath before the key line, like this:

```
Okay so... nobody tells you this part. [breath]
I tried everything before I figured out the ONE thing that actually moved the needle.
And honestly? It was simpler than I thought.
```

Use "..." for a natural pause, CAPS for emphasis, and a real filler ("okay so", "honestly") before the important line.

Then pick one of three routes. The video model and the voice tool must not both speak the same line unless a step replaces one of them.

**Route 1: the video model speaks, then you lock the voice (default for a talking persona).** In Step 8 the model speaks each line natively, with the dialogue accuracy line in the prompt. Each clip comes back in a slightly different voice, so in Step 9 you run every clip's audio through ElevenLabs Voice Changer (speech to speech) with your persona voice. Voice Changer keeps the original timing, so the lips still match. It spends credits fast, so use it on the final takes only.

**Route 2: your voice first, then lip sync.** Generate the full voiceover in ElevenLabs (or the Studio voice below), paste it into a lip-sync tool such as HeyGen or Kling's lip sync, and let it animate the anchor still to that audio. The voice is already final, so skip Voice Changer. Keep each take short, because lip sync slips on long lines.

**Route 3: voiceover persona, no talking face.** The persona narrates over b-roll and shots where the mouth is off screen or hidden. There is no lip sync to fail. This is the safest route for ads and the cheapest for volume.

### Ad-safe voice options

Any voice that goes into an ad needs a commercial licence. Two options work:

- **Paid ElevenLabs.** Use Starter or above. The free plan cannot be used in ads and requires attribution.
- **Google Cloud Text to Speech, Studio voice** `en-US-Studio-Q` (male) or `en-US-Studio-O` (female). It needs a Google Cloud project with billing switched on and a service account key, so treat it as the optional path. Send one script line per request. Wrap each sentence in Speech Synthesis Markup Language (SSML) `<s>` tags with a short break after it, so the voice pauses and drops at sentence ends like a person:

```
<speak>
  <s>Okay so... nobody tells you this part.</s><break time="400ms"/>
  <s>I tried everything before I found the one thing that worked.</s><break time="400ms"/>
</speak>
```

Join the lines into one file, normalise it to about -16 LUFS (Loudness Units relative to Full Scale), then run Whisper on the final track to get word-level timing for the captions. These are US accents. If your audience is Nigerian or diaspora, test an accent-matched ElevenLabs voice or the video model's own voice first. Studio voices take SSML, but the newer Chirp 3 HD voices do not.

### Step 8: Animate your character, one shot at a time

Use Google Flow with Gemini Omni for talking shots (clips of 4, 6, 8 or 10 seconds, native speech), or Veo 3.1 when you want its look or 4K. Use Kling 3.0 or Seedance inside Higgsfield for bulk b-roll.

**Start frame.** Reuse your saved anchors. If this video needs a new setup, generate its start frame from the anchors first and check it against the hero. Look for a changed face, a changed outfit and stray props. A wrong start frame wastes the credits on the clip.

**Match clip length to the line.** One line per clip. As a starting estimate, a short line of about 8 to 10 words fits 4 seconds and a long line fits 8. Too short and the model cuts the line off. Too long and it invents filler actions. Merge two neighbouring lines into one clip only when they share a framing. The talking-face ceiling is about 8 seconds. Never use the 10 second option for a face.

**Prompt for the talking shot.** Upload your anchor still and paste:

```
This exact person talking directly to camera, [setting], casual phone-camera
framing, natural light, subtle natural head and hand movement, real-time pace,
not slow motion. Photoreal, slight grain, not cinematic, not over-lit.
The person says: "[THE LINE FOR THIS BEAT]"
Ensure that each word is pronounced correctly and you do not add any extra words.
```

If the model mispronounces a name, say so in the next try: "The model says [wrong sound]. The word is [name], pronounced [phonetic]." The full rule is in the "Dialogue accuracy" section of `00-workflow-and-rules.md`.

**Continuity inside one shot.** When the next clip continues the same shot, take the last frame of the previous clip and use it as the first frame of the next. When the next clip cuts to a different framing, use the other anchor still instead.

**B-roll.** Make the talking shots plus 2 or 3 b-roll shots (the thing they are talking about). For b-roll, swap the line above for the object or scene, same "phone-camera, real-time, slight grain" ending.

**One take, three tries.** Generate one output per shot from its start frame. Regenerate only the shots that fail. After three failed tries, change the prompt or the start frame instead of rolling again. Do not ask for the whole video in one prompt. Short separate clips stay consistent. Long single clips drift, warp, and change the face. See the "Credits and retries" section of `00-workflow-and-rules.md`.

Do not ask the prompt for any on-screen text. Video models garble it. All captions and text overlays go on in CapCut in the next step.

### Step 9: Lock the voice, edit, and check

1. **Lock the voice.** On Route 1, run each clip's audio through Voice Changer with your persona voice and replace the clip's audio track. Run Whisper on the finished track for word timings.
2. **Cut to the voice.** Drop your clips on the timeline in order. Cut to a b-roll shot at least every 8 seconds so the viewer is not staring at the face the whole time. Trim each cut to the pace of the audio.
3. **Captions.** Use word-timed captions, three to five words at a time, in the style of your reference. Keep them off every face and out of the bottom fifth of the 9:16 frame, where the app buttons sit. See the "Captions" section of `00-workflow-and-rules.md`.
4. **Sound.** Add music low under the voice, ducked during speech, and a small effect on cuts. Use only music you are licensed to use. See the "Audio and licensing" section of `00-workflow-and-rules.md`.
5. **Match the colour** across clips so they read as one video.
6. **Set the AI label** on the post. See the "AI disclosure" section of `00-workflow-and-rules.md`.
7. **Run the final check** in the "Final check" section of `00-workflow-and-rules.md`, then watch it once in a normal player.

### Step 10: Post natively and repeat

Post directly in the TikTok or IG app, not an obvious cross-post. Write a caption that leads with the hook. Reply to early comments fast. Then go back to Step 5 for the next video. Aim for 1 to 3 a day.

---

## Make It Look Real (not AI slop)

*The prompts above already bake these in. Use this as your pre-post checklist, and for the editing moves a prompt cannot do.*

The difference between a video that grows and one that gets scrolled is whether it reads as a real person.

- **Prompt for a phone-camera look.** Natural light, slight grain, real-time pace. Drop the words "8K", "cinematic", "perfect", "studio", "hyperrealistic". Those trigger the waxy, plastic AI look.

- **Keep each talking-face clip to about 8 seconds**, then cut to b-roll. Faces drift and go uncanny past that.

- **Break the flat voice.** A pause, a breath, and a small filler or stumble before the key line is the single biggest tell-killer for AI audio.

- **Add one human imperfection** per video: a glance away, a small laugh, an "um", an off-beat moment. Perfect delivery reads as fake.

- **Match the character to the audience.** A peer. Mismatched polish reads as an ad.

---

## Going Further (when the basics work)

- **Go cheaper or higher-volume on video** by using Kling or Seedance for bulk b-roll and saving Veo 3.1 or Gemini Omni for the talking and hero shots. Compare current costs in the "Tools and prices" section of `00-workflow-and-rules.md`, because per-second price and plan price differ.

- **Batch and schedule.** Film a week of videos in one sitting. Auto-post with a scheduler (Metricool, Postiz, or Buffer). For full hands-off automation, an n8n flow can chain script to voice to video to caption to post.

- **Build the persona.** Give the character a name, a backstory, and recurring formats (a weekly series, a catchphrase) so followers recognize them.

- **Turn a working run into a template.** After the first slow video, keep the prompt that worked, so only the anchor still and the line change next time.

- **Monetize once you have reach.** A digital product, affiliate offers, brand deals, or driving to a newsletter. Pick one and put the link in bio.

---

## Common Mistakes

- The face changes between videos. You skipped Step 3. Always upload the same anchor stills.

- The voice changes between videos. Lock one ElevenLabs voice, and on Route 1 run every clip through Voice Changer.

- The lips do not match the voice. Two voices are competing. Pick one route in Step 7 and do not lay a separate voiceover under a clip that already speaks.

- Mangled or invented words in a clip. Add the dialogue accuracy line and match the clip length to the line.

- One giant video prompt. It warps and drifts. Generate short separate clips.

- Over-polished, "cinematic" look. It reads as fake. Go phone-grade.

- Posting an obvious cross-post. Post natively in each app.

---

## Before You Post

- Same face as your other videos, and no stray props in any frame
- Same voice as your other videos
- Hook lands in the first 1 to 2 seconds
- Captions word-timed, in the reference's style, never over a face, nothing in the bottom fifth (the "Captions" section of `00-workflow-and-rules.md`)
- Music and sound effects come from a source you are licensed to use (the "Audio and licensing" section of `00-workflow-and-rules.md`)
- AI label set on the post (the "AI disclosure" section of `00-workflow-and-rules.md`)
- No waxy or warping moments (cut them)
- Final check done and watched once in a normal player (the "Final check" section of `00-workflow-and-rules.md`)
- Posted natively, caption written, ready to reply to comments

---

Related: `00-workflow-and-rules.md` · `reference-teardown.md` · `02-ai-clone-talking-head.md` · `03-ai-ad-creative.md` · `04-faceless-youtube.md` · `05-launch-videos-and-recording-edits.md`

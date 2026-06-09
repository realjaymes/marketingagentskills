
# Faceless Influencer

Build an AI character that posts short videos on TikTok and Instagram without you ever being on camera.

> Mindset: the whole game is making the same face appear every time and look like a real person. Everything else is just repeating a simple loop.

**What you need**

| Job                 | Tool                              | Cost                 | Swap options                                                        |
| ------------------- | --------------------------------- | -------------------- | ------------------------------------------------------------------- |
| Character + scripts | ChatGPT (or Gemini, Claude)       | Free or ~$20/mo      | Gemini for the image, Claude for scripts                            |
| Voice               | ElevenLabs                        | Free tier, ~$5-22/mo | Cartesia, PlayHT                                                    |
| Video               | Veo 3, or Kling 3.0 in Higgsfield | ~$8-34/mo            | Google Flow (Veo with a scene builder), Seedance (cheapest), Runway |
| Editing             | CapCut                            | Free                 | Descript, Premiere                                                  |

**End result:** a recurring AI persona posting 1 to 3 short videos a day.

---

## Do This Once (set up your character)

You only do this part one time. After that you reuse the same character and voice on every video.

### Step 1 — Pick your niche

Choose one topic you could post about for a year. It needs proven faceless accounts already winning (search TikTok to confirm) and a way to make money later (a product, affiliate offers, or sponsorships). Good starters: money and side hustles, gym and discipline, AI tools, motivation, history facts, scary stories.

### Step 2 — Design your character in ChatGPT

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

### Step 3 — Lock the face so it never changes

This is the step beginners skip, and it is why most AI characters look different in every video. Your downloaded hero image is now the reference you upload every time. To make new angles, outfits, or settings while keeping the same person, upload the hero image back in and paste:

```
Keep this EXACT person, same face, same features, do not change their identity.
Now show them [side angle / in a kitchen / wearing a hoodie / outdoors at golden
hour]. Same phone-camera, natural-light, slightly imperfect look.
```

Save a small set: front, side, smiling, a couple of settings. That is your reusable asset library.

### Step 4 — Give them a voice

Go to ElevenLabs. Pick a library voice that fits your character, or design one from a description. Save it. Set Stability around 40 to 50 (natural, with some variation) and Similarity high. You will use this same voice on every video so the persona sounds consistent.

---

## Do This For Every Video (the loop)

Once your character exists, every video is these six steps.

### Step 5 — Steal a proven structure

Open TikTok or Instagram and search your niche. Find 3 to 5 videos getting far more views than the account's normal numbers. Those are proven winners. Note the hook (the first spoken line) and the order the video unfolds in. You are copying the structure, not the words.

### Step 6 — Write your script in ChatGPT

Paste the winning video's transcript or your notes on its structure, then:

```
Here is a structure that went viral in my niche: [PASTE transcript or beat-by-beat notes].

Adapt it for my character on the topic of [TOPIC]. Rules:
- First person, spoken out loud, the way a real person talks.
- 30 to 45 seconds (about 80 to 110 words).
- A scroll-stopping first line that creates curiosity or names a problem.
- Plain words, no corporate phrasing, no "in today's video".
- End on one clear line (a takeaway or a soft call to follow).
Give me 3 versions of the hook, then the full script under the best one.
```

Tighten the hook until it makes you stop scrolling.

### Step 7 — Make the voiceover in ElevenLabs

First make the script sound human, not robotic. Add pauses, emphasis, and a breath before the key line, like this:

```
Okay so... nobody tells you this part. [breath]
I tried everything before I figured out the ONE thing that actually moved the needle.
And honestly? It was simpler than I thought.
```

Use "..." for a natural pause, CAPS for emphasis, and a real filler ("okay so", "honestly") before the important line. Paste into ElevenLabs with your saved voice, generate, and download the audio.

### Step 8 — Animate your character

Go to Veo 3 (or Google Flow, which gives you Veo inside a visual scene builder with camera controls, or Kling 3.0 inside Higgsfield, which is cheaper for volume). Upload your hero character image. For the talking shot, paste:

```
This exact person talking directly to camera, [setting], casual phone-camera
framing, natural light, subtle natural head and hand movement, real-time pace,
not slow motion. Photoreal, slight grain, not cinematic, not over-lit.
```

Generate in 5 to 10 second clips, one shot at a time. Make the talking shot plus 2 or 3 b-roll shots (the thing they are talking about). For b-roll, swap the line above for the object or scene, same "phone-camera, real-time, slight grain" ending.

Do not try to generate the whole video in one prompt. Short separate clips stay consistent; long single clips drift, warp, and change the face.

### Step 9 — Edit it together in CapCut

Drop your clips on the timeline in order. Lay the ElevenLabs voiceover underneath. Cut to a b-roll shot every few seconds so the viewer is not staring at the face the whole time. Add auto-captions. Trim each cut to the pace of the audio. Add light background music, low in the mix.

### Step 10 — Post natively and repeat

Post directly in the TikTok or IG app, not an obvious cross-post. Write a caption that leads with the hook. Reply to early comments fast. Then go back to Step 5 for the next video. Aim for 1 to 3 a day.

---

## Make It Look Real (not AI slop)

*The prompts above already bake these in. Use this as your pre-post checklist, and for the editing moves a prompt cannot do.*

The difference between a video that grows and one that gets scrolled is whether it reads as a real person.

- **Prompt for a phone-camera look.** Natural light, slight grain, real-time pace. Drop the words "8K", "cinematic", "perfect", "studio", "hyperrealistic". Those trigger the waxy, plastic AI look.

- **Keep talking-face shots under ~10 seconds**, then cut to b-roll. Faces drift and go uncanny past that.

- **Break the flat voice.** A pause, a breath, and a small filler or stumble before the key line is the single biggest tell-killer for AI audio.

- **Add one human imperfection** per video: a glance away, a small laugh, an "um", an off-beat moment. Perfect delivery reads as fake.

- **Match the character to the audience.** A peer, not a model. Mismatched polish reads as an ad.

---

## Going Further (when the basics work)

- **Go cheaper or higher-volume on video** by using Seedance (lowest cost per second) or Kling for bulk, saving Veo for hero shots.

- **Batch and schedule.** Film a week of videos in one sitting. Auto-post with a scheduler (Metricool, Postiz, or Buffer). For full hands-off automation, an n8n flow can chain script to voice to video to caption to post.

- **Build the persona.** Give the character a name, a backstory, and recurring formats (a weekly series, a catchphrase) so followers recognize them.

- **Monetize once you have reach.** A digital product, affiliate offers, brand deals, or driving to a newsletter. Pick one and put the link in bio.

---

## Common Mistakes

- The face changes between videos. You skipped Step 3. Always upload the same hero image.

- The voice changes between videos. Lock one ElevenLabs voice and reuse it.

- One giant video prompt. It warps and drifts. Generate short separate clips.

- Over-polished, "cinematic" look. It reads as fake. Go phone-grade.

- Posting an obvious cross-post. Post natively in each app.

---

## Before You Post

- [ ] Same face as your other videos
- [ ] Same voice as your other videos
- [ ] Hook lands in the first 1 to 2 seconds
- [ ] Captions on and synced
- [ ] No waxy or warping moments (cut them)
- [ ] Posted natively, caption written, ready to reply to comments

---


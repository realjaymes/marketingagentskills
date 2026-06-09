
# AI Clone & Talking Head

Clone your own face and voice into an AI talking head, then generate endless videos from scripts without filming each one.

> Mindset: lip sync is mostly solved now, so a flat robot voice is the biggest tell that exposes an AI clone. Fix the voice first and the face follows.

**What you need**

| Job | Tool | Cost | Swap options |
|---|---|---|---|
| Describe your face + write animation prompts | ChatGPT (or Gemini) | Free or ~$20/mo | Gemini works the same way |
| Talking video (face animation) | Higgsfield (Kling 3.0) or HeyGen avatar | ~$9-34/mo | HeyGen for a reusable avatar, Higgsfield for one-off clips |
| Voice clone | ElevenLabs | ~$5-22/mo | Cartesia, MiniMax |
| Editing | CapCut | Free | Descript, Premiere |

**End result:** an AI version of you that says any script on camera, so you write the script and a clip comes out the other side.

---

## Do This Once (this sets the quality ceiling)

You only do this part one time. Do it well, because everything you generate later can only be as good as what you capture now. A flat, blurry, badly lit source produces a stiff clone that no prompt can fix.

### Step 1 — Capture clean source material

Get these once and keep them in a folder you reuse forever.

**Face photo (required):** One clean, front-facing photo of your face. Even soft light (a window works), plain background, no filter, no heavy makeup or sunglasses. Chest up, looking just slightly off the lens, not a dead-center stare. This single photo is enough to start.

**Short video (optional, for a higher-quality avatar):** 2 to 5 minutes of you talking to camera. 1080p or better, even soft light, plain wall behind you, an external mic if you have one, solid-color top, no filters. While you talk, actually move the way you normally do: smile, tilt your head, use your hands, raise your eyebrows. A frozen news-anchor pose trains a stiff clone.

**Voice audio (for the voice clone):** 30 to 60 minutes of clean speech in a quiet room. Record in the same energy you will generate in. Read the script below out loud, each block in the labeled mood, naturally, like you are talking to one person.

```
VOICE CAPTURE SCRIPT — read each block in the labeled mood, out loud, to one person.

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

### Step 2 — Clone your voice in ElevenLabs

Go to ElevenLabs. You have two options.

**Instant clone (IVC):** Works from 10 to 30 seconds of audio, done in seconds. Good for quick tests. Lives on the Starter plan (~$5/mo).

**Professional clone (PVC):** Trained on your 30 to 60 minutes, highest fidelity, closest to your real voice. Takes a few hours to train. Needs the Creator plan (~$22/mo). Use this for anything you publish.

Quick guidance: upload your clean audio, name the voice, start the clone. When it finishes, open the voice settings and set them like this.

```
ELEVENLABS VOICE SETTINGS (for natural delivery):
- Stability: Natural or Creative. NEVER Robust. Robust is the monotone robot tell.
- Similarity: mid-to-high, not maxed. Maxed can over-copy noise from your recording.
- Style: low to moderate.
- Model: Multilingual v2 for cloning (v3 cloning is still alpha, skip it for now).
```

This is the single most important step in the whole playbook. The voice carries the realism.

### Step 3 — Optional: build a reusable avatar in HeyGen

If you want one avatar you can reuse on every video (instead of generating from a photo each time), do this once.

Go to HeyGen, create a custom avatar, and upload your 2-to-5-minute video from Step 1. Pick the real-human realism option (Avatar V) if offered. Let it train. Then connect your ElevenLabs voice so the avatar speaks in your cloned voice. Now you pick this avatar and paste a script any time, no photo step needed.

If you skip this, no problem. The photo-to-Higgsfield loop below works without it.

---

## Do This For Every Video (the loop)

Once your voice (and optional avatar) exist, every video is these seven steps.

### Step 4 — Take or choose your face photo

Use the clean front-facing photo from Step 1, or take a fresh one in the same even light against a plain background. One photo is all you need.

### Step 5 — Upload to ChatGPT and generate a clean reference image of you

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

### Step 6 — Bring the image into Higgsfield (or pick your HeyGen avatar)

If you built a HeyGen avatar in Step 3, just open HeyGen and select it, then jump to Step 8.

Otherwise, open Higgsfield.ai. You will upload the reference image in the next step when you set up the video.

### Step 7 — Give ChatGPT your script and ask for an animation prompt

Back in ChatGPT, paste your script and this.

```
Here is the script my character will say out loud:
[PASTE YOUR SCRIPT]

Write me a single animation prompt for a talking-head video of my character
(the person you described earlier) saying this script to camera. Describe:
the person talking directly to camera, casual phone-camera framing, natural
light, subtle natural head and hand movement, real-time pace (not slow
motion), photoreal, slight grain, not cinematic, not over-lit. Keep it to
one tight paragraph I can paste into a video tool.
```

Copy the animation prompt it gives you.

### Step 8 — Generate the clip

**In Higgsfield:** scroll to Create Video. Upload your reference image. Paste the animation prompt. Generate. Keep clips short, around 5 to 15 seconds each. If you have a longer script, generate it in a few short clips rather than one long one. Long single clips drift and the face warps.

**In HeyGen:** pick your avatar, paste your script straight in, and generate. HeyGen handles the lip sync to your cloned voice. Keep each talking take under about 15 seconds, then plan a cut.

Test one short clip first before you generate the whole thing.

### Step 9 — Realism pass and edit in CapCut

Drop your clip (or clips) on the CapCut timeline in order. Then do the moves that hide the weak spots.

Cut away to b-roll every 8 to 12 seconds so the viewer is not staring at the face the whole time. This is also where you hide any moment where the lip sync looks slightly off: cut to a supporting visual for those seconds and let your voice carry. Add auto-captions. Add a light grain layer to re-inject texture, since AI renders look a bit plastic. Color grade the whole thing, it is the single biggest fix for the synthetic look. Keep background music low in the mix.

### Step 10 — Publish

Post natively in the app you are publishing to (do not post an obvious cross-post). Lead the caption with your hook. Label the content as AI-generated where the platform asks (see ethics below). Then go back to Step 4 for the next video.

---

## Make It Look Real (not AI slop)

*The prompts above already bake these in. Use this as your pre-post checklist, and for the editing moves a prompt cannot do.*

The clone passes or fails on these few moves.

- **Fix the voice first.** Lip sync is mostly solved, so a flat voice is the number one tell. Natural or Creative stability, never Robust. A flat recording at clone time produces a flat clone forever.

- **Make the script breathe.** Use commas for breath, "..." for a pause, ONE word in CAPS per line for emphasis, and a real filler ("look," "honestly," "so") before the key line. Uniform, perfectly punctuated marketing prose is the robot tell. Two or three breaths per short script reads human, ten reads fake.

- **Keep talking-face shots under ~15 seconds**, then cut to b-roll, then return. Full-screen face for 60 seconds reads as AI no matter how good the clone is.

- **Hide weak lip sync under cutaways.** Plan a cut to b-roll on the hardest lines (fast lists, long words, hard consonants). The viewer hears you and never sees the weak frames.

- **Use a medium shot, not an extreme close-up.** Close-ups amplify every uncanny tell. Eyes slightly off-lens, never a dead-center stare.

- **Mix real footage into the b-roll.** Pure AI b-roll over an AI face compounds the synthetic look. One real stock clip (Pexels, Pixabay) grounds the whole piece.

---

## Going Further (when the basics work)

- **Go faster with a HeyGen avatar.** Once you build the reusable avatar, you skip the photo-and-image step entirely: paste a script, get a clip. Best for daily volume.

- **Batch your scripts.** Write a week of scripts at once, generate all the voice in one ElevenLabs run, then all the clips in one session. Staying in one tool keeps delivery consistent.

- **Repurpose one talk into many.** Take a recorded talk or podcast, pull the transcript, ask ChatGPT to cut it into self-contained short clips, then regenerate each one clean in your clone. One filming session becomes dozens of polished clips.

- **Automate it.** An n8n flow can chain script to ElevenLabs voice to HeyGen clip to caption to post. Keep a human approval gate before publishing, since clone content carries likeness and disclosure risk.

- **Monetize once you have reach.** A digital product, affiliate offers, course modules in your voice, or driving to a newsletter. The clone lets you scale presence without scaling filming time.

---

## Clone Types (quick note)

Three different things get called an AI clone. Pick the one that matches what you are making.

- **Avatar clone (this playbook).** Your face plus voice delivers any script as talking-head video. Use when you want talking-head video at volume without filming each one.

- **Voice-only clone.** Just your cloned voice. Use when you already film yourself and only want to stop re-recording voiceover or fix flubbed lines. You keep your real face.

- **Full digital twin.** Face plus voice plus a knowledge base that answers questions and talks back live (tools like Delphi). This is an interactive product, not a content pipeline. Use when you want an always-on version of you that coaches and answers around the clock.

---

## Ethics & Disclosure

- **Consent.** Clone yourself freely. To clone anyone else (a spokesperson, a partner), get written consent first, covering what it is used for, where, and for how long. Never imply a real person endorsed something without their consent.

- **Platform AI labeling.** YouTube, TikTok, and Meta all require disclosure of realistic AI media. Set the AI label when you post. Undisclosed realistic AI can get reduced in reach or removed.

- **Paid ads.** If a clone runs in a paid ad, conspicuous AI disclosure is legally required (NY synthetic-performer law, effective Jun 9 2026, plus FTC scrutiny). Build the disclosure into the ad, not just the platform toggle.

- **Income claims (NG/diaspora).** If the clone makes any specific income claim, carry the earnings disclaimer after the claim and before the offer: "My results are not promised. They are achievable if you put in the effort. I am a testament to what's possible."

---

## Common Mistakes

- The voice is flat. You recorded in a monotone or used Robust stability. A flat source clones flat forever. Re-record with real energy, set stability to Natural.

- The photo or video is bad. Blurry, harsh light, busy background, or a filter. The clone can never beat the source. Re-capture clean.

- One giant clip. The face warps and drifts. Generate short clips and cut them together.

- Full-screen face the whole video, no cutaways. Reads as AI. Cut to b-roll every 8 to 12 seconds.

- Extreme close-up on the face. Amplifies every tell. Use a medium shot.

- Pure AI b-roll over the AI face. Compounds the fake look. Mix in real stock footage.

- No AI label. Required on YouTube, TikTok, Meta. Set it.

- Cloning someone else without written consent. Legal and ethical violation. Consent first, always.

---

## Before You Post

- [ ] Voice is yours, set to Natural or Creative (not Robust)
- [ ] Script has breaths, pauses, and one emphasis word per key line
- [ ] Talking-face shots under ~15 seconds, then a cut
- [ ] B-roll cutaways every 8 to 12 seconds, weak lip sync hidden under them
- [ ] Real footage mixed into the b-roll
- [ ] Captions on and synced
- [ ] Light grain and color grade applied
- [ ] AI label set on the platform
- [ ] Consent on file if you cloned anyone but yourself
- [ ] Posted natively, caption leads with the hook

---


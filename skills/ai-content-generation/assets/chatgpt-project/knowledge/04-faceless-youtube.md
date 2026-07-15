
# Faceless YouTube Automation

Build a YouTube channel (long-form videos and shorts) where you are never on camera and AI makes the narration and visuals.

> Mindset: faceless YouTube is information packaging. The AI just makes the assets. The title and the thumbnail carry the video. A perfect AI render under a dead title gets zero views. A plain slideshow under a great title gets a million.

**What you need**

| Job | Tool | Cost | Swap options |
|---|---|---|---|
| Research + script | ChatGPT (or Claude) | Free or ~$20/mo | Gemini for cited research |
| Narration | ElevenLabs | ~$22/mo (Creator unlocks voice cloning) | MiniMax, Hume, Speechma (free, no cloning) |
| Moving visuals | Veo 3 or Kling, plus free stock (Pexels, Pixabay) | Veo via AI Pro; Kling ~$34/mo; stock free | Google Flow (direct Veo), Runway, Luma, Seedance |
| Thumbnail text | ChatGPT (GPT Image) | ~$20/mo (free tier limited) | Ideogram or Gemini Nano Banana (fallback when ChatGPT falls short), Midjourney + type text in Canva |
| Edit | CapCut or Premiere | CapCut free; Premiere sub | Descript, DaVinci Resolve |

**End result:** a faceless channel publishing 2 to 4 retention-built videos a week.

---

## Do This Once (set up your channel)

You do this part one time. After that you reuse the same niche, voice, and channel on every video.

### Step 1 — Pick a niche and a model

Choose one niche you can speak to with some judgment. It needs three things: people are already searching and watching it at volume, advertisers pay well in it (finance, business, tech, software, history, psychology pay far more than entertainment), and you can run 50+ videos without going dry.

Then pick your model:

- **Long-form documentary or educational** (8 to 20 minute narrated deep dives). Higher production load, lowest policy risk, highest pay. Start here.
- **Shorts** (30 to 60 second vertical clips). Low effort each, high volume, low pay. Use them as a funnel to your long-form or a product, not as the main income.

To pressure-test niche ideas, paste this into ChatGPT or Claude:

```
You are a YouTube channel strategist. Score these faceless niche ideas for a new
channel. For each, rate 1-10 on: search demand, advertiser RPM, how hard it is to
differentiate with an original angle, and topic sustainability (can it support 50+
videos). Then give a one-line angle that would differentiate a new channel in that
niche, and flag any YouTube "Inauthentic Content" policy risk for a faceless format.

Niche ideas: [LIST 3-5 IDEAS]
My background / unfair advantage: [WHAT YOU KNOW OR CAN SPEAK TO WITH JUDGMENT]
Constraint: I want high-RPM and low policy risk. Plain language, no hype.
Output a ranked table, then name the single niche you would start and why.
```

### Step 2 — Lock your narrator voice

Go to ElevenLabs. Pick a library voice that fits the channel, or clone one (the Creator plan at ~$22/mo unlocks Professional Voice Cloning). Save it as your channel narrator and never switch it casually. Set Stability to Natural or Creative (never Robust, which reads monotone), Similarity high enough to stay on-voice, Style low for documentary reads, Speaker boost on for clones. Save these exact settings as a preset. This same voice on every video is what makes the channel feel like one real thing.

---

## Do This For Every Video (the loop)

Once your niche, voice, and channel exist, every video runs through these eight steps in order. The critical rule lives in Step 2: write the title and design the thumbnail before you write a single line of script.

### Step 1 — Research a topic with demand

Never script a topic you have not validated. Validation means real people are already searching for or watching this, and there is an angle that is not saturated. Open YouTube, type your topic, and read the autocomplete and "people also watch." Sort search results by views and filter to the last month to see what packaging is winning right now. To mine 20 candidates at once, paste this into ChatGPT, Claude, or a cited tool like Perplexity:

```
You are a YouTube content researcher. For the niche [NICHE] targeting [AUDIENCE],
find 20 video topics with proven demand. For each topic give:
- The core search intent (what the viewer wants to understand or feel)
- Why it has pull right now (trend, evergreen demand, or curiosity gap)
- A differentiated angle a new faceless channel could take (not the saturated take)
- Estimated competition level (saturated / moderate / open)
- A rough title direction

Use current, citable information. Do not invent search volumes; if you don't know,
say "demand signal: qualitative only." Rank the 20 by opportunity (high demand +
low saturation first). Plain language.
```

Pick one topic where the demand is real and you can take an angle the sidebar has not seen ten times.

### Step 2 — Write the title and design the thumbnail FIRST

This is the most important habit in the whole loop. The title and thumbnail decide whether anyone clicks, and that is about 70% of the outcome. If you cannot produce a title and thumbnail you would click, the topic is not worth scripting. Writing them first commits you to the promise the script then has to deliver.

First, generate titles. Paste this:

```
You are a YouTube title writer for a faceless [NICHE] channel. Generate 20 titles
for a video about [TOPIC / ANGLE]. The audience is [AUDIENCE]. Rules:
- Promise a specific, payoff-able outcome (no vague clickbait the script can't honor)
- Mix formats: curiosity gap, specific number/result, contrarian claim, "the real
  reason," named-stakes, and how-to
- Keep most under 60 characters so they don't truncate
- No em-dashes, no "you won't believe," no fake urgency
After the list, flag the 3 strongest and explain in one line each why they'd win a
sidebar click. Then for each of those 3, note the single promise the script MUST
deliver.
```

Pick the strongest title. Then design a thumbnail concept for it. Paste this for ideas:

```
You are a YouTube thumbnail designer. The video title is "[TITLE]". The audience is
[AUDIENCE]. Give me 3 distinct thumbnail concepts. For each:
- The focal image (subject, expression or object, composition, background)
- The 3-5 word on-thumbnail text (must add curiosity or stakes the title doesn't
  already state, never just repeat the title)
- The emotional hook (what makes a scrolling viewer stop)
- A color/contrast direction so it pops against YouTube's white UI
Keep on-thumbnail text under 5 words. After the 3 concepts, recommend one and say
why it wins the click.
```

Now generate the actual thumbnail image with the text baked in. Default to ChatGPT (GPT Image), which spells thumbnail text reliably and renders the scene and text in one pass. Drop to Ideogram or Gemini Nano Banana only if ChatGPT falls short:

```
Create a YouTube thumbnail, 16:9, high contrast for a small sidebar render.
Focal image: [DESCRIBE FOCAL SUBJECT/SCENE, realistic, dramatic lighting].
On-image text reads EXACTLY "[3-5 WORD TEXT]" in a heavy condensed bold sans-serif,
[placement, e.g. left two-thirds], [color] with a subtle dark outline for contrast.
Spelling must be exact, letters sharp and legible at thumbnail size, no garbled
text. Background slightly blurred to make the subject and text pop. Saturated but
not cartoonish.
```

If the text comes out garbled even at high accuracy, generate the image clean and type the text yourself in Canva. Typed text always beats generated text for legibility. Gut-check: in a row of 12 sidebar videos, would yours win the click? Only move on if the answer is yes.

### Step 3 — Write the long-form script

The script controls retention, and retention controls the algorithm. Structure matters more than pretty prose. Three rules: a cold open in the first 15 seconds that states the promise and the stakes (no "hey guys," no intro), a re-hook line every 60 to 90 seconds at each section boundary, and open loops you tease early and pay off later. Paste your verified research in and tell the model to use only those facts (invented stats get videos removed, not just demonetized). Paste this:

```
SYSTEM: You write retention-optimized long-form YouTube scripts in a natural spoken
voice for a faceless or talking-head channel. Vary sentence length, use concrete
specifics over vague claims, engineer re-hooks every 60-90 seconds. No em-dashes, no
AI tells. Ground every factual claim in the provided research; do not invent stats.

USER: Title/angle: [TITLE]. Length: [8 min ~1200 words]. Audience: [WHO].
Research (use only these cited facts): [PASTE CITED RESEARCH].
Structure: COLD OPEN HOOK (0-15s, promise + stakes) -> CONTEXT (why now) -> 3-5
NUMBERED SECTIONS (each: re-hook line, teach, specific example/proof, mini-payoff)
-> PEAK INSIGHT -> RECAP -> CTA. Output the full spoken script with [SECTION] labels
and a bracketed [RE-HOOK] note at each section start. Add a parallel B-roll/visual
cue in brackets after each paragraph.
```

If the cold open is weak, punch it up:

```
Here is the first 15 seconds of my YouTube script. Rewrite it 5 different ways to
maximize the hook. Each version must: state a specific promise, open a curiosity
loop, raise the stakes, and read like a person talking, not an essay. No "in this
video," no "hey guys," no em-dashes. Under 40 words each.
Current open: [PASTE FIRST 15s]
Topic + title: [TOPIC / TITLE]
After the 5, flag the strongest and the one line that makes it work.
```

Read the whole script aloud. Anything you stumble on, the narration model will stumble on too. Rewrite it.

### Step 4 — Narrate it in ElevenLabs

Use your locked voice and saved preset (Multilingual v2 for cloned voices, not v3 yet). Punctuation is your delivery control: commas make breath, "..." makes a pause or trail-off, and ONE word in CAPS per line gives a single emphasis beat. Drop occasional spoken connectors in the script where you want delivery to break the metronome:

```
So… [pause] here's what nobody tells you. [breathes]
The numbers looked fine. They were NOT fine.
Look, this is the part that matters.
```

Do not generate a 1,200-word script in one block. It drifts and glitches. Generate in chunks, one script section or every ~300 to 500 words, using the same voice, model, and settings every time so they stitch together. If one chunk glitches, regenerate only that chunk, not the whole thing.

**Free alternative if you are not cloning a voice.** When you just need clean narration and not your own cloned voice, Speechma (speechma.com) is a 100% free, no-signup browser TTS with 400+ library voices and a commercial license on the output. It clones nothing, so the voice is a library voice, not yours. Use it to ship for free, then move to a cloned ElevenLabs voice once you want a narrator that is uniquely your channel's. A common zero-cost stack is ChatGPT for the script, Speechma for the narration, and CapCut for the edit.

### Step 5 — Plan the visuals scene by scene

Before you generate anything, go through the script line by line and answer one question for each beat: what should the viewer SEE right now? A visual that does not earn its place loses retention. Turn the script into a per-beat plan with this prompt:

```
SYSTEM: You convert a finished video script into per-scene generation prompts for AI
image/video tools (Veo, Kling, Midjourney, Seedance). You write as a director
instructing a camera operator and actor, never as someone describing a painting.
Every prompt follows: [Camera Movement] + [Scene Setup/Setting] + [Subject + Action]
+ [Vibe/Lighting] + [Time of day/Audio]. Push realism: natural/imperfect lighting,
handheld or subtle motion, candid framing, real texture; avoid plastic, over-
saturated, symmetrical AI look.

USER: Tool target: [Veo 3.1 / Kling 3.0 / Midjourney V8 / Seedance 2.0].
Aspect ratio: [16:9]. Visual style lock: [paste 1-2 reference descriptors].
Script: [PASTE SCRIPT WITH BEATS]. For each scene/beat output a row: Scene # |
Spoken line it covers | Duration | Generation prompt (5-part structure) | Negative
prompt. Keep the same character/style descriptors VERBATIM across scenes for
continuity. End with one consistency block listing the locked descriptors to paste
into every prompt.
```

The output is your shooting plan: every line of narration mapped to a generation prompt, with a continuity lock so the style stays coherent across the whole video.

### Step 6 — Generate or pull each visual

For each beat, make a quick decision. Most documentary and educational video runs on the cheap paths, not on AI video.

- **AI image plus Ken Burns (the workhorse).** Generate one good still, then add a slow pan or zoom in the editor. Cheap, controllable, reads as authentic. Use for most documentary and explainer beats. Prompt:

```
A photoreal still for a documentary video, 16:9. Scene: [DESCRIBE SCENE/SUBJECT].
Single motivated light source: [e.g. low afternoon sun from the left]. Composition
leaves headroom and negative space on [side] for a slow camera push. Real texture,
natural imperfect lighting, slight film grain, shot on [Canon EOS 5D Mark IV, 35mm].
Unretouched, documentary realism.
Negative: plastic, oversmoothed, oversaturated, cartoon, 3D render, garbled text,
extra fingers.
```

- **Free stock (Pexels, Pixabay).** Real footage of cities, nature, hands, offices, crowds. Free, instant, and more credible than fake AI footage. Mix it in to break the all-AI smoothness that reads as slop.

- **AI video (Veo or Kling).** The most expensive and most slop-prone path. Save it for a few hero or narrative beats. Keep clips 3 to 10 seconds (identity and physics break past ~10 to 15 seconds). Prompt:

```
BLOCK 1 SUBJECT+SCENE: [subject with wardrobe/age/texture], [single present-tense
action, one verb], natural light, visible real texture.
BLOCK 2 CAMERA: slow dolly-in, 35mm lens, shallow depth of field, eye-level,
locked-off then gentle handheld drift. Real-time motion, natural pace, NOT slow
motion.
Negative: morphing, warping, melting, face changes, floating, jelly motion,
slow-motion, plastic, oversaturated.
```

Say "push in" or "dolly in," never "zoom" (zoom produces lens warp). For a longer take, generate sequential clips, each seeded from the end frame of the prior clip. Never ask a video model (Veo, Kling) for on-screen text, it garbles it. Any titles, lower-thirds, or callouts go on in CapCut at Step 7. (This is video only, your thumbnail text at Step 2 is baked in by an image model, GPT Image or Ideogram, which renders text cleanly.)

### Step 7 — Edit and assemble

Drop everything on the timeline in CapCut (or Premiere). Lay the narration down first, then cut visuals to it. No clip should sit longer than the line it covers. Change the visual every 4 to 8 seconds. Add a slow Ken Burns push to every still so nothing is truly static. Cut every breath gap and stumble out of the narration. Add an instrumental music bed, kept low under the voice. Burn in captions (CapCut auto-generates, then proofread). The single highest-impact move: apply ONE consistent color grade across every clip, still, and stock shot. That is what makes mixed AI, stock, and stills feel like one deliberate video instead of a pile of generated assets.

### Step 8 — Publish with SEO and repeat

Upload your custom thumbnail (the one you designed in Step 2), never an auto-generated frame. Then generate the metadata:

```
You are a YouTube SEO specialist. For a video titled "[TITLE]" about [TOPIC] aimed
at [AUDIENCE], produce:
- A 200-word description: first 2 lines restate the hook and include the primary
  keyword, then a 3-4 sentence summary, then a placeholder for links
- 8-12 timestamped chapter titles based on this script outline: [PASTE SECTION
  LABELS / OUTLINE]
- 10 relevant tags
- 3 alternative titles under 60 characters for A/B thumbnail testing
Match real search intent. No keyword stuffing, no em-dashes.
```

Paste the description, add the timestamped chapters (they boost watch time and surface in search), set an end screen to your most-watched video, and disclose AI honestly per YouTube's labeling rules. Then go back to Step 1 for the next video. Aim for 2 to 4 a week, each one different.

---

## Make It Look Real (not AI slop)

*The prompts above already bake these in. Use this as your pre-post checklist, and for the editing moves a prompt cannot do.*

The fastest way to look machine-made is to chase perfection. Stop maximizing it.

- **Drop the perfection keywords.** "8K," "masterpiece," "hyperreal," "ultra-HD," "cinematic" actively cause the waxy AI look. Use photographic language instead: real camera, real lens, film grain, single motivated light source.

- **Let negative prompts do the work.** Paste these into any documentary visual prompt: `plastic skin, oversmoothed, waxy, 3D render, cartoon, oversaturated, airbrushed`. For video, add: `subject obeys gravity, feet contact the ground, no floating, no morphing, real-time motion, NOT slow motion`.

- **Keep AI clips short and mix in real stock.** Clips 3 to 10 seconds, then cut. Mixing real Pexels footage into AI video breaks the mathematically smooth all-AI motion that flags as slop.

- **One consistent color grade across everything.** This is the strongest anti-slop move in the edit. It unifies AI footage, stills, and stock into one look.

- **Re-inject grain after any upscale.** Upscalers re-plasticize the image. Add grain back on top.

- **Don't fight the narration into monotone.** Natural or Creative stability, punctuation-driven pauses, a faint consistent room tone under the read to hide the seams between AI chunks.

---

## Going Further (when the basics work)

- **Go cheaper on visuals.** Stock plus AI stills with Ken Burns covers about 80% of documentary and educational video at near-zero cost. Reserve Veo and Kling for the few hero beats that need real motion. Seedance and MiniMax Hailuo are the cheapest AI video paths at volume.

- **Run a portfolio.** A long-form channel feeding a shorts channel (cut shorts from long-form hero moments), both funneling to a product or email list. Keep topic, title, thumbnail, and final review manual per channel.

- **Automate the repeatable parts only.** A self-hosted n8n pipeline can chain script to narration to visual prompts to assets to render, but put a human-approval gate before publish. Automate production, never judgment.

- **Monetize on a stack, not just ads.** YouTube Partner Program needs 1,000 subscribers plus 4,000 watch hours in 12 months (or 10M Shorts views in 90 days) for the full tier; an early-access tier opens at 500 subs plus 3,000 watch hours. But ad revenue is usually only 30 to 50% of a successful channel. Seed an affiliate link and a small product from video #1 (no follower minimum), layer in AdSense after YPP, add sponsorships and a flagship course later. RPM varies 10x by niche, which is why niche choice in setup weighted advertiser pay.

---

## Common Mistakes

- Generating visuals before locking the title and thumbnail. Packaging is 70% of the outcome. Decide it first or the production is wasted.

- Scripting an unvalidated topic. Personal interest is not demand. Validate before you write.

- Treating AI video as the whole video. It is the most expensive, most slop-prone path. Mix stock, stills with Ken Burns, and AI video.

- Asking one AI clip for 30+ seconds. Identity and physics break past ~10 to 15 seconds. Generate short and stitch.

- Using "zoom" in video prompts. It produces lens warp. Say "push in" or "dolly in."

- Robust stability on narration. It reads monotone. Use Natural or Creative.

- Inventing stats in the script. False claims get videos removed, not just demonetized. Ground every claim in pasted research.

- Daily templated output. This is the exact "Inauthentic Content" signature that gets channels demonetized and deleted. Publish 2 to 4 differentiated videos a week with original commentary and your own editing.

---

## Before You Post

- [ ] Title promises a specific payoff, under ~60 characters
- [ ] Custom thumbnail uploaded, text legible at sidebar size, adds info the title doesn't
- [ ] Would win the click in a row of 12 sidebar videos
- [ ] Cold-open hook in the first 15 seconds, no intro fluff
- [ ] A re-hook at every section boundary (every 60 to 90s)
- [ ] Every factual claim grounded in real research (no invented stats)
- [ ] Channel-locked voice, same settings preset, chunks stitched cleanly
- [ ] Every beat maps to "what does the viewer see?"
- [ ] AI clips 3 to 10s, no morphing or warping, real-time pace
- [ ] One consistent color grade across all clips, stills, and stock
- [ ] Captions burned in and proofread
- [ ] Description (hook + keyword first), chapters, and tags set
- [ ] AI disclosure set honestly
- [ ] Original commentary and your own editing present (not a raw auto-generated draft)

---


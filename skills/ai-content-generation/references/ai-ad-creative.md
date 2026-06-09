
# AI Ad Creative

Make paid ad creative with AI at volume: UGC-style actor ads, product and b-roll video, and static image ads, in enough variations that the platform can find your winners.

> Mindset: one perfect ad is a guess. The job is to ship ten genuinely different ads (different hooks, different angles, different formats) so the auction picks the winner for you. And the UGC ones have to look amateur, not produced.

**What you need**

| Job | Tool | Cost | Swap options |
|---|---|---|---|
| Brief, hooks, scripts | ChatGPT (or Claude, Gemini) | Free or ~$20/mo | Claude for scripts, Gemini for bulk hooks |
| AI UGC actors | Arcads, or Creatify | ~$11/video (Arcads), Creatify ~$49/mo | Seedance for cheap volume, HeyGen for a recurring presenter |
| Product / b-roll video | Veo 3, or Seedance | ~$0.15/s (Veo), ~$0.05 per 5s (Seedance) | Google Flow (Veo with shot controls), Kling, Runway, Pika (to insert a real product) |
| Static image ads | Gemini Nano Banana + Ideogram | Free tiers, subs ~$15-42/mo | FLUX, Midjourney, Recraft (for logos/vector) |
| Voiceover | ElevenLabs | Free tier, ~$22/mo for cloning | MiniMax Audio (cheap multilingual) |
| Assemble | CapCut | Free | Descript, Premiere |

**End result:** 10 to 30 distinct ad cuts per test round, named and exported to spec, ready to hand to a platform playbook.

---

## Do This Once (write the brief)

You do this part once per offer, then reuse it on every ad. A thin brief is why most AI ads fail. If you do not give the tool the real specifics, it invents fake ones, and invented specifics convert worse than honest vagueness.

Capture five things: the offer (exact product, price, the one action you want), the audience (who they are and their real words for the pain), an angle bank (5 to 10 different ways into the problem), proof (specific numbers, results, screenshots, testimonials), and the platform spec (Meta or TikTok, ratio, duration).

For audience phrasing, do not guess. Paste in real comments, DMs, and reviews. The single most valuable input is the audience's own words for their problem.

Open ChatGPT and paste this:

```
You are a direct-response creative strategist. Turn my rough notes into a
structured ad brief. Never invent specifics. Where a field is missing, write
"MISSING - ask" so I fill it before scripting. Plain language, no hype.

My raw notes: [PASTE EVERYTHING I KNOW].
Audience's real words (comments, DMs, reviews): [PASTE OR "none yet"].

Give me:
1. OFFER: product, price, core mechanism, the single action I want.
2. AUDIENCE: who they are, their exact words for the pain, top objection.
3. ANGLE BANK: 8 different angles into this problem, one line each.
4. PROOF: every specific number, result, screenshot, testimonial I have.
   Flag which are safe to use in paid ads.
5. PLATFORM + SPEC: platform(s), aspect ratio, duration.
Mark any missing field "MISSING - ask". End with the 3 angles most likely
to win cold traffic and why, one line each.
```

Save the brief. Every ad below pulls from it.

---

## Do This For Every Ad (the loop)

Once the brief exists, every ad runs through these six steps.

### Step 1 — Write the hook and the script

The hook is the ad. If the first 1 to 2 seconds do not stop the scroll, nothing after it matters. Write the hook first, lock the best one, then build the script under it.

In ChatGPT, generate a batch of hooks:

```
You write short-form ad hooks in the audience's own words, never generic AI
phrasing. No em-dashes, no "not just X but Y", no emoji. Each hook is one
spoken line a real person would say out loud, readable in under 3 seconds.

Niche: [NICHE]. Audience and their real words: [PASTE]. Offer: [OFFER].
Platform: [Meta/TikTok].
Generate 25 hooks across these 7 formats, labeled:
(1) Contrarian Claim, (2) Mistake Warning, (3) List Tease, (4) Curiosity Gap,
(5) Direct Callout, (6) Problem-Aware Rant, (7) Result-First.
Max 12 words each. No clickbait the script can't pay off. Avoid these
trigger words: [PASTE ANY BANNED WORDS].
Then flag the 3 strongest for cold traffic and say why in one line each.
```

Pick your hook, then write the script under it:

```
You are a direct-response video ad scriptwriter. Write in the audience's own
voice, lead with the locked hook, drive one clear action. Specific, never
hypey. No em-dashes. If the brief has any income or results claim, add the
earnings disclaimer after the claim and before the offer.

Product: [PRODUCT]. Audience and their pain: [PASTE].
Platform: [Meta/TikTok]. Length: [Short 15-20s / Medium 30-45s / Full 60s+].
Locked hook: [PASTE CHOSEN HOOK].
Write the script with labeled beats:
[HOOK] [AGITATE - the real cost of staying stuck] [REVEAL - the shift]
[PROOF - specific] [OFFER] [CTA - one action]
Plain spoken prose under each label, every line sayable in one breath.
After each beat, add a matching ON-SCREEN-TEXT line (max 6 words).
Then give me a separate ad-text block (primary text + headline) from the
same emotional core.
```

Match the length to the placement before you generate. A 15 to 20 second script fits TikTok and Reels cold creative. A 30 to 45 second script suits Meta feed.

### Step 2 — Pick the format

Pick the format from the angle, not from the tool you happen to own.

- **UGC actor ad** when you want peer-to-peer trust for cold traffic. The workhorse for direct-response and ecommerce.

- **Product or b-roll video** when you need to show the thing moving (a demo, a pour, a rotate). Rarely a whole ad on its own, usually a cutaway inside UGC.

- **Static image ad** when you want to test an angle and headline cheaply before spending video budget.

### Step 3 — Generate it

#### UGC actor ads

The mocap-trained tools (Arcads especially) make the face and lip-sync look real. The failure is everything around the face: too clean, too well-lit, too composed. The viewer's brain flags "this is an ad pretending to be a person," and that kills the trust UGC runs on. UGC has to look amateur.

Five rules that make it real:

- **Use speech-to-speech, not robot text-to-speech.** Record yourself reading the script on your phone, then map your voice onto the actor. Your real cadence, breaths, and stumbles carry over. Flat voice is the number one AI tell now that lip-sync is solved.

- **Phone-grade everything.** Prompt for iPhone capture, slightly underexposed, a real room behind them, no professional lighting. Drop "studio," "cinematic," "8K."

- **Add one human stumble per take.** A word fumble, a glance away, a small laugh, an "um, look" before the key line.

- **Cut to b-roll every 8 to 12 seconds.** Keep the talking face under 15 seconds at a stretch. Past that, the identity drifts and goes uncanny.

- **Match the actor to the audience.** A peer, not a model. Mismatched polish reads as a paid actor instantly.

Write the delivery brief for Arcads, Creatify, or Seedance:

```
You write delivery briefs for AI UGC actor tools. The goal is amateur,
candid, peer-to-peer realism, never polished. Spell out the setting, the
imperfections, and the delivery so it reads as a real person on their phone.

Locked script: [PASTE]. Actor: a peer of [AUDIENCE - age, accent, vibe].
Setting: [real room / car / kitchen / street].
Output:
1. ACTOR: 3 archetypes that read as peers of the audience, one line each.
2. DELIVERY: pace, energy, where to add a pause, a stumble, a small laugh,
   an off-camera glance. Mark ONE filler ("um", "look", "honestly") before
   the key line.
3. SETTING + FRAMING: handheld, phone-grade, real background, no pro light.
   Name the light source (window / overhead / car).
4. B-ROLL: 2-3 cutaways to break the face every 8-12s (product, screen, result).
5. WARDROBE: peer-appropriate, not styled.
Keep each face take under 15s before a cutaway.
```

#### Product and b-roll video (ecommerce)

For ecommerce, one rule beats everything: the product on screen must be YOUR exact item. The viewer is about to buy that specific object. If the model invents a slightly different bottle, label, or color, you get returns, disputes, and policy flags. So never let a text-to-video model draw your product from scratch. Always start from a real, clean product photo and animate from there.

The reliable pipeline keeps your product pixels and only generates the world around them: real product photo, then an image model edits the scene around the locked product, then image-to-video adds motion. If a frame shows the product clearly enough to read or recognize, that frame should contain real product pixels.

First, place your real product into a scene (Nano Banana or FLUX Kontext, with the real photo attached):

```
Use the attached photo as the EXACT product. Do not redraw, restyle, recolor,
reshape, or relabel it in any way. Keep it pixel-accurate. Place the product
[in a person's hand / on a bathroom counter / on a kitchen island].
Generate only the surrounding scene plus a matching shadow and reflection so
it sits naturally. Lighting: [soft window light from the left].
Photoreal, phone-camera look, slight grain, unretouched.
The product must stay identical to the source photo.
```

Then add motion from that frame (image-to-video):

```
SUBJECT: [exact product from the source frame], one real action
[a hand picks it up and turns it / liquid pours / the lid clicks open /
a swatch is drawn on skin], real material and texture, no plastic sheen,
label stays legible and unchanged.
CAMERA: slow handheld push-in, 35mm, shallow depth of field, eye-level.
PHYSICS: product stays rigid and solid, obeys gravity, no morphing, no
warping, no melting, label does not distort.
PACE: real-time, natural everyday pace, NOT slow motion.
LOOK: phone-grade, soft grain, unretouched.
```

The ecommerce UGC archetypes worth templating: unboxing or first-look, in-hand testimonial, problem-then-solution demo, before and after, "it made me buy it" reaction, founder or origin story, lifestyle or aspirational, and comparison ("why this, not that"). Cold traffic usually wins on problem-then-solution, in-hand testimonial, or the reaction. Warmer audiences respond to founder story and comparison.

Hands are the hardest thing for AI to render. When fingers wrap around the product, cut to a clean product-only shot at the exact moment a glitch would show.

#### Static image ads

Two jobs, two tools. Use a visual model for the scene, and Ideogram for the headline and CTA text (it spells text legibly, where pure-aesthetic models garble it). Do not ask one model to do both well.

Generate the scene:

```
You write image prompts for static ad creative. Engineer controlled
imperfection so people and scenes read as real, not plastic. Name one
motivated light source, add human flaws, specify a real camera and lens.
NEVER use 8K / masterpiece / ultra-HD / hyperreal (those cause the waxy look).

Concept: [WHAT THE AD SHOWS]. Subject: [person/product, a peer of the audience].
Ratio: [1:1 / 4:5 / 9:16].
Give me a full prompt with: subject + wardrobe + real setting; one motivated
light source; a realism block (natural skin texture, slight asymmetry, candid
expression); camera (shot on iPhone or Canon 5D, 85mm, shallow depth of field,
film grain); and a negative prompt (plastic skin, waxy, airbrushed, 3D render).
```

Then add the text layer in Ideogram, putting the exact copy in double quotes:

```
Headline reads exactly "[HEADLINE, MAX 8 WORDS]" in a heavy condensed sans-serif,
top third, white on deep navy. CTA button reads exactly "[CTA]".
Spelling must be exact, text sharp and fully legible, no garbled or extra letters.
```

### Step 4 — Make variations

A single ad is a guess. The auction finds winners only when you give it enough genuinely different creative. Build a simple 3x3: take 3 strong hooks and 3 strong angles from the brief, cross them, and you have 9 base concepts. Then multiply each by cheap swaps (a different actor, a different setting, a different CTA). Even a conservative pass gives you 10 to 30 distinct cuts per round, which is the volume a test needs.

```
You build a 3x3 ad variation matrix. Take 3 hooks and 3 angles and produce 9
distinct base concepts, then list cheap swap dimensions so it scales to 20-30
cuts. No em-dashes. Each cell must be genuinely different, not a reworded twin.

Offer: [OFFER]. Audience: [AUDIENCE].
3 hooks: [H1 / H2 / H3]. 3 angles: [A1 / A2 / A3]. Platform: [Meta/TikTok].
Output:
1. A 3x3 table: each cell = one-line concept (hook + angle) + the best format
   for it (UGC / product video / static).
2. SWAP DIMENSIONS for the top 3 cells: actor (3 peers), setting (3), CTA (2),
   opening visual (2).
3. NAMING: a filename per cut: [platform]_[ratio]_[angle]_[hook]_[actor]_[v##].
4. PRIORITY: rank the first 12 cuts to produce, best cold performance first.
```

Name every cut consistently, like `tiktok_9x16_speed_resultfirst_ada_v03`. When a winner emerges, the name tells you which hook, angle, and actor won, so the next round builds off that signal instead of starting blank.

### Step 5 — Assemble to spec

Drop the clips into CapCut in order, lay the voiceover underneath, cut to a b-roll or product shot every few seconds, and burn in captions (most paid impressions play muted). Then export to the right spec per placement.

| Spec | Meta (Feed/Reels) | TikTok | YouTube Shorts |
|---|---|---|---|
| Video ratio | 9:16 (Reels), 4:5 (Feed), 1:1 | 9:16 | 9:16 |
| Duration | 15-30s (Reels), up to 60s | 15-34s cold | 15-60s |
| Hook window | First 2s | First 1s | First 2s |
| Captions | Burn in | Burn in, native-style | Burn in |
| Safe zone | Keep hook + CTA clear of bottom ~20% | Key text in middle 60% | Central safe zone |

Keep the hook line and the CTA inside the central safe zone so the platform UI never covers them. Export the ratios you are actually buying, not one size for everything.

### Step 6 — Test and iterate

This playbook makes the creative. The platform playbooks run the test. Hand the named, assembled variation set to Meta Ads Playbook or TikTok Ads Playbook for budget, optimization event, audience, and the kill or scale calls.

Two creative signals tell you what is working before conversion data matures. Hook rate (3-second views over impressions) tells you if the opening stopped the scroll. Hold rate (average watch time) tells you if the body kept them. Read them like this:

- Low hook rate: the first 1 to 2 seconds failed. Regenerate hooks and opening visuals, keep the body.

- High hook rate, low hold rate: the hook wrote a check the script did not cash. Rewrite the body to pay off the hook.

- Good hold, weak click-through: the angle landed but the offer or CTA did not. Test new CTAs, keep the creative.

When a winner emerges, read its name to find the winning hook, angle, and actor, then regenerate the next round off that combination. Cross-check your real backend (Selar, your store) against the platform numbers before any kill call, because Meta undercounts conversions and the platform numbers lag.

---

## Make It Look Real (not AI slop)

*The prompts above already bake these in. Use this as your pre-post checklist, and for the editing moves a prompt cannot do.*

- **Phone-grade, not produced.** Natural light, slight grain, real-time pace, a real room. Drop "8K", "cinematic", "studio", "hyperreal". Those trigger the waxy plastic look that tells viewers it is an ad.

- **Use speech-to-speech for UGC voice.** Record the read yourself and map it onto the actor. A flat text-to-speech voice is the single biggest tell now that lip-sync works.

- **Cut the talking face every 8 to 12 seconds.** Keep face takes under 15 seconds, then cut to product or b-roll. Past that, the face drifts and goes uncanny.

- **Lock the real product.** For ecommerce, start from a real photo and only generate the scene around it. A pixel-accurate real product next to a synthetic face raises the whole ad's believability, and a wrong label drives returns.

- **One human imperfection per take.** A stumble, a glance, a small laugh. Perfect delivery reads as fake.

- **Match the actor to the viewer.** A peer, not a model. Mismatched polish reads as a paid actor.

---

## Going Further (when the basics work)

- **Go cheaper at volume.** Seedance is the cheapest per second for both UGC and product b-roll, with native lip-sync. Save Veo for hero shots.

- **Batch-render the matrix.** Once a format works, tools like Creatomate or JSON2Video can render the whole variation matrix off a template instead of cutting each by hand.

- **Insert your real product into AI scenes.** Pika (Pikadditions) drops a real product clip into AI footage, the most reliable way to keep the SKU exact in motion.

- **Build a recurring spokesperson.** For founder or expertise-led offers, a consistent presenter (clone or stock avatar) builds authority over time. See 02 - AI Clone & Talking Head.

---

## Common Mistakes

- One polished hero ad instead of 10 to 30 honest variations. The auction needs volume to pick a winner.

- Making AI UGC look produced. Studio light and a styled actor kill the peer trust that makes UGC convert.

- Raw text-to-speech for UGC voice. Flat voice is the number one tell. Use speech-to-speech.

- Talking-face takes over 15 seconds with no cutaway. The face drifts and goes uncanny.

- Writing the script before the hook. The hook is the ad. Lock it first.

- A hook the script does not pay off. Hook rate climbs, hold rate collapses, the ad still loses.

- Letting AI redraw your ecommerce product. Wrong label or color drives returns and policy flags. Start from the real photo.

- Garbled in-image text. Use Ideogram for headlines, exact copy in double quotes, under 8 words.

- Skipping captions. Most paid impressions play muted.

- Naming cuts inconsistently. If the filename does not encode hook, angle, and actor, you cannot read the winner back.

---

## Authenticity & Policy

- **Avoid the over-polished AI look.** It reads as a brand faking authenticity, and that trust collapse tanks conversion even when the ad is approved.

- **Follow AI-disclosure rules.** Meta and TikTok auto-label realistic AI, and paid ads using a synthetic performer (an AI actor or avatar) increasingly need conspicuous disclosure. Never imply a real named person endorsed the product without their consent.

- **Take extra care with income and results claims.** Any ad with specific income figures needs the earnings disclaimer placed after the claim and before the offer. For Nigerian and diaspora financial-outcome creative, watch the classifier trigger words and remember the classifier reads your destination page content, not just the ad.

---

## Before You Publish

- [ ] Hook lands in the first 1 to 2 seconds (visual and line)
- [ ] Hook is paid off by the script, no over-promise
- [ ] One clear CTA, one action
- [ ] At least 10 to 30 distinct variations in the round
- [ ] Every cut named: `[platform]_[ratio]_[angle]_[hook]_[actor]_[v##]`
- [ ] UGC reads amateur and candid, not produced
- [ ] Speech-to-speech used for UGC voice where the tool supports it
- [ ] Talking-face takes under 15s, with cutaways every 8 to 12s
- [ ] At least one real product frame if product video is used
- [ ] No 8K / cinematic / hyperreal language left in prompts
- [ ] Correct ratio and duration per placement
- [ ] Captions burned in, hook and CTA inside the safe zone
- [ ] Earnings disclaimer present after any income or outcome claim
- [ ] Handed off to Meta Ads Playbook / TikTok Ads Playbook

---


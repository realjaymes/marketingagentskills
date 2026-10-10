# 03 - AI Ad Creative

Make paid ad creative with AI at volume: user-generated content (UGC) style actor ads, product and b-roll video, and static image ads, in enough variations that the platform can find your winners.

> Mindset: one perfect ad is a guess. The job is to ship ten genuinely different ads (different hooks, different angles, different formats) so the auction picks the winner for you. The UGC ones have to look amateur and candid.

**Tier:** this playbook runs the performance ad tier of the "Workflow" section of `00-workflow-and-rules.md`. Variants are the main payoff, so step 6 of the workflow is where most of the value sits. Tool prices live in the "Tools and prices" section of `00-workflow-and-rules.md`.

| Workflow step | Where it happens here |
|---|---|
| 1 Reference brief | Do This Once (the brief) and Step 1 (the reference-first path) |
| 2 Script | Step 1, a beat table with a word budget per beat. You approve it |
| 3 Scenes and anchors | Step 3, anchors for the actor or presenter and the real product, one row per shot, a start-frame contact sheet. You approve it |
| 4 Voice | Step 3, speech to speech for UGC, or Voice Changer on a presenter |
| 5 Shots | Step 3, one take per shot, faults fixed in the edit first, at most one retry with your go-ahead |
| 6 Finish and check | Steps 4 and 5 (variants, assembly to spec) and the Before You Publish list |

**What you need**

| Job | Tool | Notes |
|---|---|---|
| Brief, hooks, scripts | ChatGPT (or Claude, Gemini) | Claude for scripts, Gemini for bulk hooks |
| AI UGC actors | Arcads or Creatify | HeyGen for a recurring presenter |
| Presenter and product video | Google Flow with Veo 3.1 Fast (speaks natively), the model chosen per shot as in the "Google Flow" section of `00-workflow-and-rules.md` | Kling, Seedance, Runway and Pika are swap options. Seedance is not the cheapest path in general, so compare costs before you pick it for volume |
| Static image ads | ChatGPT Images (GPT Image) | Gemini Nano Banana or Ideogram when ChatGPT falls short, FLUX, Midjourney, Recraft for logos and vector |
| Voiceover | ElevenLabs on a paid plan | The free plan has no commercial licence and cannot be used in ads. MiniMax Audio is a swap option |
| Assemble | CapCut | Descript and Premiere also work. Use Pro assets or your own for ads |

**End result:** 10 to 30 distinct ad cuts per test round, named and exported to spec, ready to hand to a platform playbook.

Planning notes (reference, script, shot table, naming log) live in your notes. Clips, audio and renders live in a linked work folder outside it. See the "Folders and files" section of `00-workflow-and-rules.md`.

---

## Do This Once (write the brief)

You do this part once per offer, then reuse it on every ad. A thin brief is why most AI ads fail. If you do not give the tool the real specifics, it invents fake ones, and invented specifics convert worse than honest vagueness.

Capture five things: the offer (exact product, price, the one action you want), the audience (who they are and their real words for the pain), an angle bank (5 to 10 different ways into the problem), proof (specific numbers, results, screenshots, testimonials), and the platform spec (Meta or TikTok, ratio, duration). Add a sixth for software or branded products: the brand kit or the product's own screens. Every colour in the ad comes from there. See the "Brand colours" section of `00-workflow-and-rules.md`.

For audience phrasing, do not guess. Paste in real comments, direct messages, and reviews. The single most valuable input is the audience's own words for their problem.

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

### Step 1: Pick a reference, write the hook and the script

**Reference-first path.** If a proven ad already does this job, start there. Run the `reference-teardown.md` on it. You get the shot table, the exact words, the hook move, the beats with word counts, the caption style and the sound. Then write your script beat for beat in the same shape, within 5 words of each reference beat. Copy structure and timing. Never copy the words, people, footage, music, brand marks or claims. If you have a swipe folder, choose proven ads first, then check what they lack (a call to action (CTA), the brand). Use the hook generator below to fill the gaps. With no reference, use the brief and the generator alone.

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
Reference beats (if any): [PASTE THE TEARDOWN BEAT TABLE].
Write the script with labeled beats:
[HOOK] [AGITATE - the real cost of staying stuck] [REVEAL - the shift]
[PROOF - specific] [OFFER] [CTA - one action]
Plain spoken prose under each label, every line sayable in one breath.
Give each beat a word count. Any fact I did not give you becomes
[NEED: fact]. Do not invent it.
After each beat, add a matching ON-SCREEN-TEXT line (max 6 words).
Then give me a separate ad-text block (primary text + headline) from the
same emotional core.
```

The ON-SCREEN-TEXT lines are instructions for your CapCut editor and never go to the video model. Strip them out before you paste anything into Flow, Veo, or Kling, because video models garble text you ask them to render on screen. You burn these captions in during assembly (Step 5).

Match the length to the placement before you generate. A 15 to 20 second script fits TikTok and Reels cold creative. A 30 to 45 second script suits Meta feed. A video that sells a program, a course or an offer runs 90 to 120 seconds (see the "Story and sale videos" section).

**You approve the script before any generation.** Every change after this point costs credits.

### Step 2: Pick the format

Pick the format from the angle, not from the tool you happen to own.

- **UGC actor ad** when you want peer-to-peer trust for cold traffic. The workhorse for direct-response and ecommerce.

- **Product or b-roll video** when you need to show the thing moving (a demo, a pour, a rotate). Rarely a whole ad on its own, usually a cutaway inside UGC.

- **Static image ad** when you want to test an angle and headline cheaply before spending video budget.

- **Talking head or dialogue story** when a 60 second character story fits the offer: one person telling a private moment, or two people in a scene. See the "Talking head and dialogue stories" section.

- **Story or sale video** when the product is a program, a course or an offer that needs the problem, the value and the ask told in order. See the "Story and sale videos" section.

- **AI character or presenter video ad** when you want a consistent branded presenter, a built faceless persona or your own clone, delivering the ad at volume, beyond a stock UGC actor. You lock the character once and animate it in Flow from the ad script. See the presenter route in Step 3.

### Step 3: Generate it

#### UGC actor ads

The mocap-trained tools (Arcads especially) make the face and lip-sync look real. The failure is everything around the face: too clean, too well-lit, too composed. The viewer's brain flags "this is an ad pretending to be a person," and that kills the trust UGC runs on. UGC has to look amateur.

**UGC native feel.** Five rules make it read as a real person on a phone:

- **Handheld framing.** Slight wobble, a phone held at arm's length or propped on a shelf, a slow drift, never a locked-off tripod.

- **Phone lighting.** Prompt for iPhone capture, slightly underexposed, one real light source (a window, an overhead bulb, a car windscreen). Drop "studio," "cinematic," "8K."

- **Real settings.** A kitchen, a car, a bedroom desk, a street. Slightly messy, lived in, with real objects behind the person.

- **Imperfect delivery.** Add one human stumble per take: a word fumble, a glance away, a small laugh, an "um, look" before the key line. Use speech to speech rather than robot text to speech. Record yourself reading the script on your phone, then map your voice onto the actor with ElevenLabs Voice Changer on a paid plan. Your real cadence, breaths, and stumbles carry over. Flat voice is the number one AI tell now that lip-sync is solved.

- **A peer of the viewer.** Pick an actor who looks like the audience. Mismatched polish reads as a paid actor instantly.

**Compliance rule for UGC.** An AI creator never poses as a real customer giving a testimonial. No first-person "I used this and it changed my life" lines from a person who does not exist, and no invented reviews, results or names. Use an AI presenter for explainers, demos and claims you can stand behind. Real customer words come from real customers, with their permission, as their own video or quoted text. Every ad with an AI actor carries the platform's AI label, switched on at posting. See the "AI disclosure" section of `00-workflow-and-rules.md`.

**Limits to plan around.** Product labels and hands drift. Whenever the product must be readable, or fingers wrap around it, cut away to real product footage for the close-up. Lip sync slips on long lines, so keep each line under about 8 seconds and each face take to about 8 seconds, then cut.

Write the delivery brief for Arcads, Creatify, or a Flow-based actor:

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
4. B-ROLL: 2-3 cutaways to break the face (product, screen, result).
5. WARDROBE: peer-appropriate, not styled.
Keep each face take to about 8 seconds before a cutaway.
```

#### AI character or presenter video ads (the Flow pipeline)

When you want your own consistent presenter, a built faceless persona or your own clone, delivering the ad instead of a stock Arcads actor, run the same character-to-video pipeline the clone playbook uses, driven by the ad script from Step 1.

1. **Build or reuse the presenter and the anchors.** Build a faceless character (see `01-faceless-influencer.md`) or clone yourself (see `02-ai-clone-talking-head.md`). Lock the face with the multi-angle mashup and a reusable JavaScript Object Notation (JSON) prompt. Make the two-image anchor once: a close-up, then a wide generated with the close-up as its reference, both 9:16 with no text. Check both for stray props. Attach the right still to every clip, and tell the model "keep every other thing consistent" when you vary one detail.

2. **Set the scene, then turn the script into a shot table.** Decide the environment (a room, a podcast desk, a stage, outdoors, a studio) and lock the outfit, background, camera angle, lighting and style. Paste:

```
You turn a finished video ad script into a shot table for an AI video tool
(Gemini Omni or Veo 3.1 in Flow, or Kling). One spoken line per shot. For each
shot output a row: Shot # | Spoken line (only this shot's words) | Word count |
Duration (about 4 seconds for a short line, up to 8 for a long one, plus about
1 second of handles) | Framing (close or wide) and the anchor still it starts
from | Scene (setting, subject, one real action, motivated light) | Generation
prompt (phone-camera look, natural light, slight grain, real-time pace, subtle
motion) | Negative prompt (morphing, warping, melting, plastic, slow motion).
Lock the same character and style descriptors VERBATIM across every shot.
End every speaking prompt with: Ensure that each word is pronounced correctly
and you do not add any extra words.
Do NOT put any on-screen text in the prompts, the model garbles it.

Ad script: [PASTE LOCKED SCRIPT].
Character/style lock: [PASTE JSON FACE PROMPT or persona descriptors].
Platform: [Meta/TikTok]. Ratio: [9:16 / 4:5 / 1:1].
```

3. **Make the start-frame contact sheet.** Generate one start still per shot from the anchors and view them together. Check that the face, outfit, room and props hold from shot to shot, and that no stray prop has appeared. You approve the set before you pay for video.

4. **Generate each shot in Flow, with the model speaking.** Use Veo 3.1 Fast for talking shots, with the settings in the "Google Flow" section of `00-workflow-and-rules.md`. One output per shot, from its start frame. The prompt carries the exact line, the dialogue accuracy line and the still finish, and each 8 second clip holds one short line that the edit trims to its speech. When a shot continues the same framing, use the last frame of the previous clip as the first frame of the next. When it cuts to a new framing, start from the other anchor still. Fix faults in the edit first, and reshoot a clip at most once, with your go-ahead. See the "Dialogue accuracy" section of `00-workflow-and-rules.md` and the "Credits and retries" section of `00-workflow-and-rules.md`.

5. **Lock one voice.** The model's native voice differs from clip to clip. For a clone, run every clip's audio through ElevenLabs Voice Changer with your cloned voice. For a built persona, pick one paid ElevenLabs voice and run every clip through Voice Changer with it. Voice Changer keeps the timing, so the mouth still matches.

6. **Assemble in CapCut** (Step 5), with the captions, the colour grade and one palette from the brand kit.

This is how you run branded-presenter or founder-face ads at volume: one locked character, many scripts, each script split into short shots.

#### Talking head and dialogue stories

Two formats carry a character story in about 60 seconds. A talking head suits a private subject that one person would tell a camera alone. A dialogue suits a situation with a second person in it. Dialogue has only organic proof so far, so in paid, test one talking head against one dialogue per offer before scaling either. Every line follows the "Story craft" section of `00-workflow-and-rules.md`.

**Talking head beat sheet.** A spoken sentence lands in each beat, and a new picture arrives about every 3 to 4 seconds.

| Seconds | Beat | What it does |
| --- | --- | --- |
| 0 to 3 | Hook | A first-person moment with a thing in it. The contrast or the question is spoken in the first 2.5 seconds |
| 3 to 15 | The specific scene | Where she is, who was there, what was in the room and what someone said. A telling object beats a date |
| 15 to 30 | What it cost her | Small, felt costs in her time, her meals, her phone, how she saw her week |
| 30 to 45 | The turn and the product | One plain action she took, with the real product on screen showing its real output |
| 45 to 55 | What changed | A change in her plan or her habit, never a promised result |
| 55 to 60 | The ask | A separate voice over or card names the product and the address, after her last line |

Four b-roll inserts of 1 to 2 seconds, taken from objects named in her lines (shoes by the door, a cold mug, the phone), hide the joins between clips.

**Dialogue beat sheet.** A speaker change or a new picture lands about every 3 to 4 seconds.

| Seconds | Beat | What it does |
| --- | --- | --- |
| 0 to 3.5 | Open mid-scene | One character says one line of a conversation already running. It names a person or a thing, and it carries the doubt or the pressure |
| 3.5 to 13 | The situation | Place, an object in the room, a family role, set by the two characters answering each other |
| 13 to 25 | The doubt lands | The second character voices the objection in their own words. She answers in one line that names her position, ending on her opening the product |
| 25 to 34 | The turn | The real product on a phone, with her voice over it. No new face on screen |
| 34 to 44 | The plan changes | The doubter reacts to what the product showed and takes a role in the new plan |
| 44 to 55 | The plan carries forward | The changed choice happens on screen. The doubter stays a little unconvinced |
| 55 to 60 | Close and one ask | The last spoken line belongs to the characters, then a separate voice over or card and the end card |

**How a dialogue maps to Flow clips.**

- **One speaker per clip**, with the other character out of frame or facing away with mouth closed, as set in the "Dialogue accuracy" section of `00-workflow-and-rules.md`. Each speaker change cuts to the other person's close-up, framed to match: same height, same eyeline direction, same light. Aim for six to nine speaking clips.
- **Listener coverage.** One silent listening clip per character, used in a call window or as an L cut at the line that lands hardest.
- **Over the shoulder** at the doubt, and when the doubter reads the phone. It is a medium-risk clip, so the second face's mouth stays closed in the prompt.
- **One silent two-shot** at the point the plan lands, generated last and replaced with a cutaway of the phone on the table if it fails.
- **The product insert** runs 8 to 12 seconds with one voice over it. It is built from the product's own code, so it is the cheapest part of the video.
- **Cut rhythm.** One punch in on the second sentence of a clip, and a hard cut between speakers with the next line starting in the first third of a second.

**Supporting cast.** Any character who speaks in two or more clips gets their own persona sheet. Each offer keeps its own cast, so a husband is never shared across offers. One outfit per character per video, each a different colour.

**Guardrails.** Characters talk to each other, never to the viewer about the viewer's situation. Jokes land on the situation or the aunties, never on a character's body, loss or choices. Nobody claims a purchase or a result. The doubter is a person with their own reason, ends the video inside the plan, and is never a villain or a lecture.

**Where the retries come from,** and the fix for each:

- **Wrong mouth.** The line lands on the other face. Fix it with one speaker per clip and the silent, facing-away line.
- **Faces blending.** Two people of similar age drift together. Fix it with different outfit colours and different hair or head coverings.
- **Voices sounding alike.** Fix it with a different pitch and age in each voice line.
- **An extra person** in the background of a wide frame. Keep wide shots rare, and never ask for a crowd.
- **The two-shot.** It fails most, so it goes last and has a cutaway ready.

#### Story and sale videos

A video that sells a program, a course or an offer is a dramatic transformation story, not a quiet slice of life. It runs 90 to 120 seconds, with a 30 to 45 second cutdown for people who already watched it. References that sell a course, a book or a program run 85 to 180 seconds, and under 40 seconds only works for a simple product.

**Build it from the offer's own landing page.** The headline is the promise. The problem section is the first story angle. The offer is what is inside the product, the app tools the buyer gets and the community. A second angle comes from research into a different problem the same offer solves. The voice over states the promise in the page's own words and never strengthens a claim.

**Study first.** Read the strongest story and long running paid references closely, with word timed transcripts and frames, and get a Codex second opinion before drafting. Copy structure, never words.

**The story.**

- It opens on a relatable, high stakes moment, lets the cost grow, shows the person using the product in her life (reads it on her phone, takes notes, uses the app tools, talks to the community), and ends on the outcome she wants. What the outcome may show is limited per niche, and the story never claims a result the offer cannot promise.
- Persuasion and emotional triggers belong here: desire, fear, identity, status, the cost of doing nothing. Name the trigger for each beat in the storyboard.
- Every line is something a person says. No calendar markers or odd counts as fake specificity. Each beat causes the next, and every line is read aloud as the character.
- Real testimonials come only from published customers, word for word. An AI character never gives one.

**Sale video beat sheet (90 to 120 seconds).**

| Seconds | Beat | What happens |
| --- | --- | --- |
| 0 to 6 | Hook | A confession or a sharp spoken line that puts the stakes on the table |
| 6 to 25 | The want and the first failure | Who wants what, in a line someone would say. Her own way fails the first time |
| 25 to 45 | The problem grows | A second failure, worse than the first and caused by it. The second character's own want pushes against hers |
| 45 to 55 | The low point | One line of reflection in her own voice: what she now sees, or the question she asks out loud |
| 55 to 85 | The guide | The product enters as the answer to that question. The doubter's questions pull out three or four things it gives, each answering a failure we watched, and the doubter pushes back at least once |
| 85 to 105 | The change and the outcome | She acts on what she learned, then the outcome, with time passing shown by a card or a visual change |
| 100 to 120 | The close | The brand voice over, phrase by phrase, as set out below |

The 30 to 45 second cutdown keeps the hook, the worst failure, one value step, the changed choice and the end card.

**Outcome limits per offer.** Before writing, make a two-column table for the offer: what the outcome may show (taken from the landing page's own promise) and what it never shows (a health, body, money or timeline result the page does not promise). Every sale script in that offer stays inside it.

**Real proof only.** A sale video may close on one real testimonial from a published customer, copied word for word with its attribution, on a plain brand card.

**Shot caps and pace.** No picture holds past its cap, and reading time sets the minimum. Both rules are in the "Pace" section of `00-workflow-and-rules.md`. A clip reused under the voice over has its own sound muted.

**The close.**

1. The story ends on its last emotional beat.
2. A short brand voice over plays over the outcome. It says what the viewer gets in use terms: "Get the [program] to [what it helps you do]. It comes with the [app], whose [tools] help you [jobs], and a community of [who] going through the same thing." The community line appears only if the community is real. It never counts parts or names packaging, so "all five parts, both bonuses and the app" is out.
3. The picture follows the voice phrase by phrase. Each phrase gets its own picture for 2 to 3 seconds: the outcome under the promise, the person using the product under what it helps her do, each named tool's real screen under that tool, the community under the community line. No single image holds longer than about 3 seconds while the voice speaks, and most of these pictures reuse clips and inserts the story already has. Only the last 2 to 3 seconds are the product mockup, with only the short domain as a caption.
4. The voice over never speaks an address, and the full page path never goes on screen. The post caption and the ad button carry the link. There is no boilerplate end card and no small type disclaimer in the picture, because the disclaimer goes in the post caption. This is how the strongest story ads close: Thai Life's "Unsung Hero" and John Lewis hold the brand back to the final seconds.

**The mockup.** A digital product is never shown as a printed book. The 3D mockup appears only as the product shot at the close.

**Storyboard.** The script ships with its storyboard inside the same brief, as set out in the "Review stills" section of `00-workflow-and-rules.md`. The script and the storyboard are approved together before any face or start frame is made.

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

Generate one short shot per prompt in Flow, and never ask for on-screen text in the shot, because video models garble it and faces and physics drift on long clips. If the script is longer, break it into shots and generate one clip per shot, then stitch. All captions and headlines go on in CapCut.

The ecommerce UGC archetypes worth templating: unboxing or first-look, problem-then-solution demo, before and after, "it made me buy it" reaction, founder or origin story, lifestyle or aspirational, and comparison ("why this versus that"). Cold traffic usually wins on problem-then-solution or the reaction. Warmer audiences respond to founder story and comparison. An in-hand testimonial needs a real customer, so see the compliance rule above.

Hands are the hardest thing for AI to render. When fingers wrap around the product, cut to a clean product-only shot at the exact moment a glitch would show. For any close-up where the label must read, cut to real product footage, filmed on your phone, rather than a generated shot.

#### Static image ads

One model, one pass. ChatGPT Images (GPT Image) spells headline and CTA text legibly on short copy, so you can usually generate the scene and the text together. Ask for the scene and the exact copy in the same prompt, with the copy in double quotes. Dense copy can still garble. Fall back to the two-step split (visual model for the scene, then Ideogram or Nano Banana for the text) when ChatGPT garbles a word, the warm tint fights the brand, or a policy check blocks the render.

Generate the scene and the text together in ChatGPT, putting the exact copy in double quotes:

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
Then render it with the on-image text baked in:
headline reads exactly "[HEADLINE, MAX 8 WORDS]" in a heavy condensed sans-serif,
top third, in [BRAND TEXT COLOUR] on [BRAND BACKGROUND COLOUR]; CTA button reads
exactly "[CTA]".
Spelling must be exact, text sharp and fully legible, no garbled or extra letters.
```

Take the two colours from the brand kit or the product's own screens. If a word comes out garbled, either re-roll or generate the scene clean and set the copy in Ideogram, Nano Banana, or Canva. Typed or Ideogram text still beats generated text when legibility has to be perfect.

### Step 4: Make variations

A single ad is a guess. The auction finds winners only when you give it enough genuinely different creative. Build a simple 3x3: take 3 strong hooks and 3 strong angles from the brief, cross them, and you have 9 base concepts. Then multiply each by cheap swaps (a different actor, a different setting, a different CTA). Even a conservative pass gives you 10 to 30 distinct cuts per round, which is the volume a test needs. For client batches, the `creative-multiplication-engine` skill runs this in the client's brand.

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

Name every cut consistently, like `tiktok_9x16_speed_resultfirst_ada_v03`. When a winner emerges, the name tells you which hook, angle, and actor won, so the next round builds off that signal instead of starting blank. Log what worked in the swipe index.

### Step 5: Assemble to spec

Drop the clips into CapCut in order, lay the voiceover underneath, and cut to a b-roll or product shot at least every 8 seconds. Then finish in this order:

1. **Captions.** Most paid impressions play muted. Use word-timed captions, three to five words at a time, in the reference's style, never over a face. Keep the hook and CTA inside the safe zone. See the "Captions" section of `00-workflow-and-rules.md`.
2. **Sound.** Add music ducked under the voice and a small effect on cuts. Ad audio must be licensed for ads. Do not use the YouTube Audio Library in ads, use a source whose licence covers online ads, and log each source. See the "Audio and licensing" section of `00-workflow-and-rules.md`.
3. **Colour.** Match colour across shots. Brand colours come from the brand kit or the product's screens. See the "Brand colours" section of `00-workflow-and-rules.md`.
4. **Label.** Add the AI-generated label where an AI actor or presenter appears. See the "AI disclosure" section of `00-workflow-and-rules.md`.
5. **Export to the right spec per placement.**

| Spec | Meta (Feed/Reels) | TikTok | YouTube Shorts |
|---|---|---|---|
| Video ratio | 9:16 (Reels), 4:5 (Feed), 1:1 | 9:16 | 9:16 |
| Duration | 15-30s (Reels), up to 60s | 15-34s cold | 15-60s |
| Hook window | First 2s | First 1s | First 2s |
| Captions | Burn in | Burn in, native-style | Burn in |
| Safe zone | Keep hook + CTA clear of bottom ~20% | Key text in middle 60% | Central safe zone |

Keep the hook line and the CTA inside the central safe zone so the platform's buttons and text never cover them. Export the ratios you are actually buying, not one size for everything. Then run the "Final check" section of `00-workflow-and-rules.md`.

### Step 6: Test and iterate

This playbook makes the creative. The platform playbooks run the test. Hand the named, assembled variation set to Meta Ads Playbook or TikTok Ads Playbook for budget, optimization event, audience, and the kill or scale calls.

Two creative signals tell you what is working before conversion data matures. Hook rate (3-second views over impressions) tells you if the opening stopped the scroll. Hold rate (average watch time) tells you if the body kept them. Read them like this:

- Low hook rate: the first 1 to 2 seconds failed. Regenerate hooks and opening visuals, keep the body.

- High hook rate, low hold rate: the hook wrote a check the script did not cash. Rewrite the body to pay off the hook.

- Good hold, weak click-through: the angle landed but the offer or CTA did not. Test new CTAs, keep the creative.

When a winner emerges, read its name to find the winning hook, angle, and actor, then regenerate the next round off that combination. Cross-check your real backend (Selar, your store) against the platform numbers before any kill call, because Meta undercounts conversions and the platform numbers lag.

---

## Make It Look Real (not AI slop)

*The prompts above already bake these in. Use this as your pre-post checklist, and for the editing moves a prompt cannot do.*

- **Phone-grade.** Natural light, slight grain, real-time pace, a real room. Drop "8K", "cinematic", "studio", "hyperreal". Those trigger the waxy plastic look that tells viewers it is an ad.

- **Use speech to speech for UGC voice.** Record the read yourself and map it onto the actor. A flat text-to-speech voice is the single biggest tell now that lip-sync works.

- **Cut the talking face at least every 8 seconds.** Keep face takes to about 8 seconds, then cut to product or b-roll. Past that, the face drifts and goes uncanny.

- **Lock the real product.** For ecommerce, start from a real photo and only generate the scene around it. A pixel-accurate real product next to a synthetic face raises the whole ad's believability, and a wrong label drives returns.

- **One human imperfection per take.** A stumble, a glance, a small laugh. Perfect delivery reads as fake.

- **Match the actor to the viewer.** Mismatched polish reads as a paid actor.

---

## Going Further (when the basics work)

- **Go cheaper at volume.** Veo 3.1 Fast in Flow, at 20 credits a clip, is the volume route for UGC and product b-roll. Save Veo 3.1 Quality for the one hero close-up. See the "Google Flow" section of `00-workflow-and-rules.md`.

- **Batch-render the matrix.** Once a format works, tools like Creatomate or JSON2Video can render the whole variation matrix off a template instead of cutting each by hand.

- **Insert your real product into AI scenes.** Pika (Pikadditions) drops a real product clip into AI footage, which is the most reliable way to keep the product exact in motion. Check that your plan's licence covers ad use before you rely on it.

- **Build a recurring spokesperson.** For founder or expertise-led offers, a consistent presenter (clone or stock avatar) builds authority over time. See `02-ai-clone-talking-head.md`.

- **Turn a working run into a template.** After the first slow ad, keep the prompt that worked. Next time only the start frame and the line change.

---

## Common Mistakes

- One polished hero ad instead of 10 to 30 honest variations. The auction needs volume to pick a winner.

- Making AI UGC look produced. Studio light and a styled actor kill the peer trust that makes UGC convert.

- An AI creator posing as a real customer. It breaks platform and consumer-protection rules and wrecks trust when it is spotted.

- Raw text-to-speech for UGC voice. Flat voice is the number one tell. Use speech to speech.

- The free ElevenLabs plan for an ad voice. It has no commercial licence.

- Talking-face takes longer than about 8 seconds with no cutaway. The face drifts and goes uncanny.

- Mangled or invented words in a presenter clip. Add the dialogue accuracy line and match the clip length to the line.

- Writing the script before the hook. The hook is the ad. Lock it first.

- A hook the script does not pay off. Hook rate climbs, hold rate collapses, the ad still loses.

- Letting AI redraw your ecommerce product. Wrong label or color drives returns and policy flags. Start from the real photo.

- Garbled in-image text. Default to ChatGPT Images with the exact copy in double quotes, under 8 words. If it garbles, re-roll or fall back to Ideogram or typed text in Canva.

- Skipping captions. Most paid impressions play muted.

- Unlicensed music. Ads get rejected or banned for it.

- Naming cuts inconsistently. If the filename does not encode hook, angle, and actor, you cannot read the winner back.

---

## Authenticity & Policy

- **Avoid the over-polished AI look.** It reads as a brand faking authenticity, and that trust collapse tanks conversion even when the ad is approved.

- **Follow AI-disclosure rules.** Meta and TikTok auto-label realistic AI, and paid ads using a synthetic performer (an AI actor or avatar) increasingly need conspicuous disclosure. Switch on the platform's AI label at posting, and burn a tag into the picture only where the platform has no label and the policy requires one. Never imply a real named person endorsed the product without their consent. See the "AI disclosure" section of `00-workflow-and-rules.md`.

- **No fabricated customers.** An AI person never gives a testimonial, a review or a result as if it were a real customer's.

- **Take extra care with income and results claims.** Any ad with specific income figures needs the earnings disclaimer placed after the claim and before the offer. For Nigerian and diaspora financial-outcome creative, watch the classifier trigger words and remember the classifier reads your destination page content, not just the ad.

---

## Before You Publish

- Hook lands in the first 1 to 2 seconds (visual and line)
- Hook is paid off by the script, no over-promise
- One clear CTA, one action
- A story or sale video: 90 to 120 seconds, every line sayable by a person, the close ends on the outcome, the voice over is cut phrase by phrase with a new picture every 2 to 3 seconds, and the mockup holds only the last 2 to 3 seconds with the short domain, and the storyboard was approved with the script
- At least 10 to 30 distinct variations in the round
- Every cut named: `[platform]_[ratio]_[angle]_[hook]_[actor]_[v##]`
- UGC reads amateur and candid, with handheld framing, phone light and a real setting
- No AI actor posing as a real customer, and no invented testimonial
- Speech to speech used for UGC voice where the tool supports it, on a paid voice plan
- Every speaking prompt carried the dialogue accuracy line
- Talking-face takes trimmed to their speech, with a new picture every 2 to 4 seconds (the "Pace" section of `00-workflow-and-rules.md`)
- Real product footage used wherever a label must read or a hand holds the product
- No 8K / cinematic / hyperreal language left in prompts
- Correct ratio and duration per placement
- Captions word-timed in the reference's style, never over a face, hook and CTA inside the safe zone, nothing in the bottom fifth (the "Captions" section of `00-workflow-and-rules.md`)
- Colours come from the brand kit or the product's screens (the "Brand colours" section of `00-workflow-and-rules.md`)
- Music and effects licensed for ads, sources logged (the "Audio and licensing" section of `00-workflow-and-rules.md`)
- AI label switched on at posting wherever an AI actor appears (the "AI disclosure" section of `00-workflow-and-rules.md`)
- Earnings disclaimer present after any income or outcome claim
- Final check done and watched once in a normal player (the "Final check" section of `00-workflow-and-rules.md`)
- Handed off to Meta Ads Playbook / TikTok Ads Playbook

---

Related: `00-workflow-and-rules.md` · `reference-teardown.md` · `01-faceless-influencer.md` · `02-ai-clone-talking-head.md` · `04-faceless-youtube.md` · `05-launch-videos-and-recording-edits.md`

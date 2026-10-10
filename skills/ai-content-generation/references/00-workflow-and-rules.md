# 00 - START HERE — AI Content Generation

This folder holds the general workflow for making AI video and image content, the rules every project shares, and five playbooks with the detailed steps for each use case. Read this note once. Then pick a playbook, follow it step by step, and come back here when it links to a shared rule.

Every playbook runs the same six steps. A proven reference does most of the planning, the script and voice set the pacing, and You approve the work at two points before any credits go into video.

---

## Pick your playbook

Start with one question: **do you have a proven reference?** That means a video that already does the job you want, in the format you want. If yes, every playbook starts by tearing it down with the `reference-teardown.md` method. If no, find one first. A swipe file or a competitor's best-performing ad is enough.

Then pick by use case:

| Playbook | What it makes | Use it when |
| --- | --- | --- |
| `01-faceless-influencer.md` | A recurring AI character for TikTok and Instagram | You want a daily short-form account without showing your face |
| `02-ai-clone-talking-head.md` | A clone of you that speaks your scripts | You want to be on camera without filming |
| `03-ai-ad-creative.md` | Paid ad creative at volume, including AI UGC (user-generated content) | You run ads and need many variations fast |
| `04-faceless-youtube.md` | Faceless YouTube videos, long form and Shorts | You want narration over B-roll |
| `05-launch-videos-and-recording-edits.md` | Motion-graphics launch videos, and edits of your own recordings | You are launching a product, or you filmed yourself and want a sharp edit |

Or pick by what is on screen:

| On screen | Video type | Playbook |
| --- | --- | --- |
| No person: screens, cards, animated text, AI voice | Type A | `05-launch-videos-and-recording-edits.md` |
| An AI person | Type B | `01-faceless-influencer.md`, `03-ai-ad-creative.md` |
| A clone of you | Type B | `02-ai-clone-talking-head.md` |
| You, filmed for real | Type C | `05-launch-videos-and-recording-edits.md` |
| B-roll under narration | Type A | `04-faceless-youtube.md` |

---

## The workflow

Each step writes one file that the next step reads. Claude can run steps 1 to 3 in one sitting. You approve the script, then the start frames for a generated video or the "Review stills" section for a coded one, before anything is generated or rendered in full.

### 1. Reference brief

- **Brief:** five lines covering the goal, the audience, the message, the platform and length, and the call to action.
- **Reference:** one to three proven videos that do the same job, broken down with the `reference-teardown.md`. It records the structure (shots, hook move, beats with word counts, captions, sound) and the look (light, palette, camera movement, texture).
- **Study before writing.** For a story or sale video, read the strongest references closely (word timed transcripts and frames, not summaries) and get a Codex second opinion on them before drafting. We copy structure, never words.
- **A new reference every time.** Each video in a series of similar videos gets its own reference, so the series keeps changing style. A reference already used for one video in the series is not used for the next. For a recurring series, keep a roster of up to twenty styles, each built from a different reference, and a music library at least twice that size. Rotate through both so no two videos in a row share a style or a music bed. Keep one fixed reference or style only when the owner says so for that series.
- **Style in numbers**, when we copy an editing or motion style: cuts per minute, zoom size and frequency, caption layout, animation timing, sound-effect timing. Each style becomes a Remotion template, so the next video in that style starts at step 2.
- The reference is the concept. When no reference fits the job, start from the story instead, with the four stops in the "Story craft" section, then find a reference for the style. Write three scored concepts only for a brand film.
- **Output:** a REFERENCE note.

### 2. Script

- The story comes first, as 4 to 6 plain sentences that make sense to someone who has never heard of the brand. Each sentence follows from the one before, no term appears before the story sets it up, and every number proves the sentence beside it.
- A beat table with time, visual, the spoken line, on-screen text and sound. The script carries a "Read straight through" paragraph: the spoken lines or on-screen text alone, in order, telling the same story.
- The reference sets the pacing, and each beat has a word budget close to the reference's. The style fits around the story: a beat with no line carries visuals only, and no line is written to fill a beat.
- Every spoken line is something a person actually says, in short lines of 3 to 9 words. Time and numbers appear only when a person would say them. One calendar marker at most, and only when it carries feeling ("the night before my scan"). Numbers are round. A calendar marker used as fake detail (week three, day 38, 2am) or an odd count (61 screenshots) is not specificity. A telling object or picture is. Each beat causes the next, linked by "but" or "so", and every line is read aloud as the character before it stays in the script. The full rules are in the "Story craft" section.
- Every line, spoken or on screen, is one of three things: a real question with a concrete detail, a plain statement of what the product does, or a quote from a real moment. Lines are full sentences, never a list of nouns or a tagline.
- Codex drafts or reviews every script. Claude then checks it against the brand's voice engine. Words the owner has confirmed win over both.
- A video that sells a program, a course or an offer runs 90 to 120 seconds, with a 30 to 45 second cutdown, because it has to carry the problem, the value and the ask. Under 40 seconds only works for a simple product. The method is in the "Story and sale videos" section of `03-ai-ad-creative.md`.
- The brief and script are written in your notes, in plain prose with no blockquotes, with visual cues kept in the beat table. They are approved before anything is generated, captured or built.
- Every claim traces to the brief. A missing fact is flagged for the owner, never invented.
- **Approval point 1:** You approve the script. A story script goes to him with its storyboard (step 3), and he approves both together.
- **Output:** a SCRIPT note.

### 3. Scenes and anchors

- **Anchors** at the top of the note:
  - the character's two-image anchor, a close-up and then a wide shot made from the close-up;
  - real product photos from every angle;
  - one look line covering palette, light, lens and grain.
- **Recurring characters** get a persona sheet before any start frame: front, three-quarter, profile, smile and listening, with their outfits and the room they live in. ChatGPT makes the sheet and every start frame, with the sheets of everyone in the frame attached. One tool makes each character, and a character is never remade in another tool.
- **Holding faces across shots:** one outfit per character per video, each in a different colour from everyone else in the scene; one room image attached to every start frame; close and medium framing, because wide shots lose faces; no more than three people in a scene, and never a crowd. Check the first two clips side by side (face, skin tone, hairline) before spending credits on the rest.
- **The cast archive.** Every character image is saved twice, in the brand's cast folder in your notes and in its Downloads folder, and indexed. Reuse an existing face before making a new one. When an image needs more than two rounds of corrections in one chat, regenerate it in a fresh chat instead.
- **Storyboard for every story script.** The script ships with its storyboard inside the same brief file, in a Storyboard section above the shot table, before any face or start frame is made. See the "Review stills" section.
- **One row per shot:** framing, camera movement, light, action, the exact line, duration plus about one second of extra footage at each end (handles), and the start frame it uses.
- **Start frames:** one still for each generated shot, laid out together as a contact sheet. Image-to-video needs these frames anyway, so checking them as a set costs no extra credits.
- **Approval point 2:** You approve the start frames as a set. The face, outfit, product and look must stay the same across shots. A coded video (Remotion or the site motion kit) has no start frames, so it is built to a the "Review stills" section sheet instead, and the full render waits for the owner's approval of that sheet.
- **Output:** a SCENES note and a frames folder.

### 4. Voice

- Record or generate the final voice before any shot is made, then time every word with Whisper. The timed voice sets each shot's exact length.
- **When the video model speaks the line itself** (a talking AI person in Flow), the script fixes each line and its clip length instead. Generate the shots first, then run ElevenLabs Voice Changer over the clips to lock one voice, and time the words with Whisper after that.
- **A coded film that gets a voice after its picture is approved** (Remotion or the site motion kit) is the one exception to voice first. The picture and its timing stay fixed, one short line is generated per beat and fitted to it, and a manifest of line lengths places each line. The method is in the "Type A: Voiceover for a Coded Film" section of `05-launch-videos-and-recording-edits.md`.
- **Output:** the voice file and `words.json`.

### 5. Shots

- Generate one take per shot from its approved start frame.
- Regenerate only the shots that fail, within the "Credits and retries" section rules. Fix single shots, never the whole film.
- Every speaking prompt carries the "Dialogue accuracy" section line. Every prompt asks for handles.
- **Output:** clips named by shot number.

### 6. Finish and check

- **Build:** cut the clips to the voice, using the style template when one exists, and edit generated clips by the "Editing generated clips" section. Add music and sound by the "Audio and licensing" section, and word-timed the "Captions" section. Match the colour across shots and set the "AI disclosure" section label.
- **Check:** run the "Final check" section.
- **Variants (ads):** export other aspect ratios and cut-downs, plus hook and call-to-action variants. Log what worked into the swipe index.
- **Output:** the master, the variants, and the check results in the asset hub.

### Scale by tier

| Step | Quick social (UGC, faceless shorts, persona posts) | Performance ad or launch video | Brand film |
| --- | --- | --- | --- |
| 1 Reference brief | One reference, structure only | One to three references, structure and look | Several references plus three scored concepts |
| 2 Script | Beat table | Beat table | Beat table |
| 3 Scenes and anchors | Reuse the persona's anchors; start frames only for new setups | Start frames for every generated shot | Start frames for every generated shot |
| 4 Voice | Yes | Yes | Yes |
| 5 Shots | One take, retry failures | One take, retry failures | Two takes on the key shots |
| 6 Finish and check | Edit, sound, captions, check | Plus colour match and variants | Plus cut-downs |

---

## Shared rules

Every playbook follows these rules. A playbook adds detail for its use case, but it never overrides them. When the owner's feedback on a video exposes a fault, the fix is written into the rule here or in the playbook, so the next video does not repeat it.

### Story craft

Every video tells a story, including a 30 second launch film with no voice. These rules come from diagnosing real story scripts and from launch film research.

**The four parts.** Every script has a hook, a pain, a solution and a call to action (CTA). The hook lets the people the product serves see themselves in the first three seconds, strongest when a line and a picture land together. The pain is what the current way costs them. The solution is the product removing that pain, and what life looks like after. The CTA is the one thing to do next.

**Launch story angles.** The four parts stay fixed, and the angle sets how each one plays. These are story shapes for launch and product videos. The message angles in the Creative Strategy Framework, such as Financial Freedom, are a separate layer.

| Launch story angle | Hook | Pain | Solution | CTA |
| --- | --- | --- | --- | --- |
| Problem to solution | Shows the problem | What it costs | The product | Try it |
| Before and after | The "before" | Daily life without the product | The "after" | Make the switch |
| What if | A question the audience has not dared to ask | Why they never asked | The answer | See it for yourself |
| A day in the life | One moment in a customer's day | Builds as the day goes on | The product steps in | Make your day look like this |
| Fast feature tour | The boldest feature | Barely mentioned, because the audience knows it | The tour itself | Try it |
| Teaser | Builds curiosity | Hinted at | Held back | Join the waitlist |

Angles mix. The Box launch film is problem to solution with a "what if" turn in the middle.

**Finding the story when no reference fits.** Claude works it out with the founder in four stops, waiting for a reply after each:

1. Ask one question at a time until it knows what the product does, who it serves, what they use today, what that costs them and what viewers should leave knowing. Play it back in a few sentences for correction.
2. Write the pain, the solution and the CTA in one or two lines each, in the founder's words. Anything useful found in research (a feature, a number, a customer problem) goes in a separate list for the founder to confirm before it is used.
3. Propose the three best launch story angles or mixes. Give each three hooks, each paired with a visual, and recommend one.
4. Write the story as numbered short lines in screen order, one idea per line, each marked hook, pain, solution or CTA.

**Character stories** (UGC, dialogue, talking heads and sale videos) add these rules.

- **A want she can hold or do.** Stop the aunty's question at the table. Get him to take the baby. "Have a plan" is not a want.
- **One wrong belief the story breaks.** "If I ask for help, I have failed." Every beat presses on it, and she acts: she refuses, confronts, asks or admits something.
- **The obstacle has a face and one line.** "Many voices" has no face.
- **Open on a confession or a sharp spoken line.** Scene-setting openers are the weakest hook type in the ad data, so the first words carry the hook.
- **The product is earned by a failure we watch.** Her own way fails in front of us, then the product answers that failure or a second person notices it. It never arrives by coincidence.
- **The value comes out in steps.** Three or four things the product gives, each answering a failure we watched, each shown as a real page or tool, with a face reacting. Nobody reads a page aloud or scrolls through part names.
- **The second character wants something too.** The doubter changes because of something they see, never something they hear, stays a little unconvinced, and keeps active with one-word questions.
- **Answer pressure with a joke** before any explanation.
- **Leave the feeling under the words.** Contractions, people cutting in, sentences left unfinished. Nobody narrates what we can see, talks in product part names, or tells another character a fact they both know so the viewer hears it.
- **Keep a detail only if removing it changes** the decision, the joke or the outcome.
- **Plant a laugh early and an ache late.** One laugh in the first quarter, one ache in the last third, and the ache comes from something a character does.
- **The turn is a changed choice we can see.** Check every script with the sound off: what changes on screen?
- **End on the story, sell on the card.** The last spoken line belongs to the characters, and no character says "Get yours". The product name, the address and the ask sit in a separate voice over, the end card and the caption. The ending never implies the product worked.
- **Every script in a set uses a different angle and a different shape.** Change the pain, the value or the hook, not only the names, because Meta treats reworded versions as one ad.

**The test.** Before a character story goes to the owner, Codex answers one question: if the product were removed, would these characters still have a scene worth watching? A no sends the script back.

### Pace

These hold for every video. The storyboard builder (a script that lays out the storyboard and checks it) flags any breach, and every flag is cleared before the owner sees a storyboard.

- **Change the picture every 2 to 4 seconds, at uneven gaps** (one second, then four, then two). An even rhythm becomes a pattern of its own. Short-form ads change every 2 to 3 seconds, and modern films average about 2.5 seconds a shot.
- **Shot caps.** No picture holds past its cap: a dialogue shot 5 seconds (one spoken line, then cut); a silent face, b-roll or still 3 seconds, always moving; a phone or notebook insert 4 seconds with something changing inside it; a time card about 1 second; anything under a voice over 2 to 3 seconds; the product mockup 3 seconds. One deliberate silent beat per video may run to 4 seconds. A long shot is split, never held: cut it into a wide and a tighter crop of the same take, or cut to a reaction or an insert, so the fix costs no new clips.
- **Reading time sets the minimum, and it wins.** People read about 160 to 180 words a minute, so on-screen words hold at least 1 second plus 0.3 seconds per word. Taps in a product demo land at least 0.8 seconds apart, a result holds at least 1.5 seconds, and a scroll moves about one screen height every 2 seconds. A line that needs longer than its shot's cap stays up across two shots while the picture changes under it, or it is shortened.
- **Voice over** runs at no more than about 3 words a second per phrase. The brief names the phrase to cut first if the recording runs long, and the edit retimes from the real recording.
- **A video gets longer before it gets faster.** When a launch film runs past its length, cut the scenes that say too much or are not needed, rather than speeding everything up.

### Realism

Realism comes from controlled imperfection. Prompt for a phone-camera look: natural light, slight grain, real-time pace. Drop the words "cinematic", "8K" and "perfect", because they trigger a waxy, plastic look. Put real pauses and breaths in the voice. Keep talking clips short so faces do not warp.

**Generated clips carry no words.** Video models misspell almost any text they render, so a video prompt never asks for words on screen. Every caption, hook line and CTA is added in the edit or in Remotion. Asking for no text is not enough on its own, because Veo still burns captions in, so every frame of every clip is checked and any burned-in text is covered with an insert or a plain brand card. Start frames for video carry no text either. Still-image models such as GPT Image, Ideogram and Nano Banana render text well, so text in a static image or thumbnail is fine.

### Writing shot prompts

Build every video prompt from the shot's row in SCENES, in this order: subject, action, camera movement, look, light, then specs.

- Keep each prompt to 50 to 100 words. Longer prompts make the model drop details.
- Always name the camera movement, or say "static". Video models understand these terms: static, pan, tilt, dolly in or out, slow push, orbit, tracking shot, crane, handheld, zoom.
- Start from the approved start frame (image-to-video), so the face, product and setting carry over.
- The setting the prompt names matches the start frame. A prompt that names a kitchen over a sofa still makes the model change rooms mid-shot, so a new location needs its own start frame.
- Anyone talking to camera keeps their eyes on the lens: "She keeps her eyes on the lens the whole time." Stage directions that point the eyes elsewhere ("nods toward the window") send the gaze off camera for the rest of the clip.
- A phone in a character's hand faces them: "she holds her phone with the screen facing her, away from the camera". The real screen is cut in during the edit.
- Every prompt carries "No music, no captions, no subtitles, no on-screen text."
- End with the anti-warp line: "No morphing, no warping, no melting, no jelly motion, no slow motion."
- Speaking shots also carry the "Dialogue accuracy" section lines.

Common mistakes: a vague subject ("a person"), asking for text on screen, asking it to "make it viral", prompts over 200 words, and no camera direction.

### Dialogue accuracy

Video models mangle lines, cut them short and add filler words. Every speaking prompt carries this line, word for word:

"Ensure each word is pronounced correctly and you do not add any extra words."

- **End on a still finish**, so the model does not fill spare seconds with glances, smirks and mouth sounds: "After the last word she stays still, looking into the lens with her mouth closed, and makes no other sound."
- **Short lines.** Each clip is generated at 8 seconds and carries one spoken line of 3 to 9 words, or two short lines with a beat between, and the edit trims it to its speech. Never use the 10 second option on a face. Merge two short lines into one clip when they share the same framing.
- **Keep names and local words plain**, and never let one hard word carry the line. Phonetic spellings often fail ("Aunty Bose sent" came back as "Antibose scent", and "Tick" as "take"). When a word keeps failing, cut it in the edit and let the caption or the on-screen tool carry it.
- **A voice line per character** in every prompt: age, pitch, accent and pace, for example "Nigerian English, Lagos, warm low voice, steady pace". Write "steady pace", never "calm". Two characters in one video get clearly different voices.
- **Dialogue runs one speaker per clip.** The other character is out of frame, or in frame with "the other woman stays silent, facing away, mouth closed". Each speaker change is a cut to the other person's close-up at the same height, eyeline and light.

### Google Flow

Flow is the video tool for every generated shot. These settings and habits come from real productions.

- **Settings that work:** Frames to video, the approved still as the Start frame, Veo 3.1 Fast, 720p, 8 seconds, 9:16, one output (x1). That costs 20 credits a clip, and a 60 second talking or dialogue video takes about 200 credits.
- **Which model for which shot.** Veo 3.1 Fast (20 credits) for talking clips, background footage behind text and cheap tests. Veo 3.1 Quality (about 100 credits) only for the one close-up people will really look at, such as hands or the product. Gemini Omni Flash (about 25 credits) when an exact person or product has to be recreated from reference images and kept consistent across shots. Name the model in every step, because "Flow" alone does not say which model runs.
- **Before each submit,** check the Start frame thumbnail, because the picker's list order changes between uses.
- **Wait, never resubmit.** A clip takes two to four minutes, sometimes ten. Poll every 60 to 90 seconds for up to ten minutes, and count a clip as failed only on an explicit error. Never submit a scene again while one is generating, and log every submission.
- **The prompt log.** Every prompt goes into the brief verbatim, scene by scene, with the clip file, the start frame, the Flow edit ID, what came back and how the edit uses it.
- **Listening clips.** For each dialogue, generate one silent listening clip per character: "listens, nods once, mouth closed the whole time, says nothing". The silent seconds after a speaking clip's last word also work.
- **Risky shots go last.** A two-shot with two faces fails most often, so it is generated last, used once and silent, and replaced with a cutaway if it fails.
- **Accounts.** Before starting a video, check the account's balance and add up its clip costs. Start only a video that account can finish, because clips join only inside one Flow project. When credits run out, the owner signs in to another Google account. Claude never switches accounts. Exported stills can be reused in any account.

### Captions

- The caption style copies the reference each time: font, size, colour, highlight and words per screen.
- The safety rules always apply on top of the reference's style:
  - captions never cover a face;
  - nothing sits in the bottom fifth of a 9:16 frame, where the app's buttons are;
  - captions are timed word by word from the Whisper transcript.
- Remotion renders captions from `words.json`. The local ffmpeg build cannot burn captions in.

### Editing generated clips

Generated clips are never shipped joined end to end. They arrive as fixed 8 second takes with dead air, glances off camera and mouth sounds at every join. The edit fixes this, and most fixes cost no credits. The full method, with the ffmpeg settings, is the `remotion` skill's `rules/generated-clip-edits.md`.

- **Transcribe before cutting.** Run whisper.cpp on every raw clip, set each cut from the transcript and the loudness curve, then transcribe the cut again so no word is clipped and no stray word stays.
- **Trim to the words**, about 0.1 seconds either side, and drop the glance away and any trailing word at the end of most clips.
- **Speed every clip up 1.15 times** (1.1 to 1.2) with the pitch kept, and level every clip to the same loudness.
- **Leave about 0.1 seconds between speakers** over one room tone bed, so no gap is digital silence.
- **Punch in to about 112%** on the second cut from the same take, so a jump cut reads as an edit.
- **Keep the listener on screen.** On a video call the other person sits in a small window in the corner. In a room, cut to the listener's silent face while the speaker's voice carries on (an L cut). End on a reaction before the end card.
- **Cut to the real screen.** When a character lifts a phone, cut to the real product on a phone, built from its own code, with each tap landing on the spoken words, then back to the face.
- **Cut around what is broken.** A mispronounced word is cut and carried by the caption or the tool. A room change or burned-in text is covered with an insert, a cutaway or a plain brand card. Fix faults here before anyone spends credits on a reshoot.

### Brand colours

Colours always come from the product's own screens or the brand kit. For a software product, sample the colours from its screenshots, so the video looks like the app. For a client, use their brand kit. A reference's palette never overrides the brand.

### Brand asset library

Each brand keeps one asset library, gathered once and reused for every video. It holds the logo as SVG, the colours and fonts, the product screens or the capture job that makes them, the brand's motion library (see the "Motion library" section of `05-launch-videos-and-recording-edits.md`), the cast, and the music and sound picks with their licences. Without these, Claude fills the gaps with its own colours and fonts, which is why so many AI videos look alike.

- **From Figma.** When a client's designs live in Figma, connect Figma's official MCP server (it needs a full or Dev seat). Claude then reads colours, fonts and screens from a frame link.
- **Without the product's code.** When we cannot build screens from the product's code, the client sends a screen recording of the flow, or signs in to a test account in Chrome so Claude can capture the session. Claude never types the password.
- **Low-resolution files** are upscaled before use.

### Real product screens

A product, tool or website on screen is built from the product's own code, never redrawn. A React product's components are imported into Remotion. A plain HTML site goes through the site motion kit, which captures the live page's real HTML at each step and rebuilds it in Remotion with the site's own CSS and fonts. Every result shown is one the live tool produced. The method is in the "Type A: Launch and Product Videos" section of `05-launch-videos-and-recording-edits.md` and Site Motion Kit — Code & How It Works.

### Audio and licensing

- **Voice for ads:** use a paid voice plan or a paid API. Gemini text to speech (TTS) with billing on is the default for narration and host voices, because it takes an accent, pace and register instruction in plain words. OpenAI gpt-4o-mini-tts is the comparison provider. The ElevenLabs free tier carries no commercial licence and requires attribution, so it never goes in an ad. Google Cloud TTS Studio voices (`en-US-Studio-Q` male, `en-US-Studio-O` female) are a low-cost option for long narration. Check the provider's commercial terms before ad use, and read keys from the shared keys file without printing them.
- **Music for ads:** use Mixkit (check each item's licence tag), Freesound or Openverse tracks licensed CC0 or CC BY, or original music from a paid Suno plan. Avoid the YouTube Audio Library for Meta ads, because its licence covers YouTube. A recurring series rotates its music beds (see step 1).
- **Sound by video type.** Each type gets its own sound rule.

  | Video type | Music | Sound effects |
  | --- | --- | --- |
  | Voiced launch or product video, recording edit | One bed, ducked under the voice (about 55% under a narrator, about 40% under short host stings, with a quick dip in and a slower release) | One on each cut and graphic entrance, quieter than the voice |
  | Launch film with no voice over | One bed carries the pace | Soft and muted, on the key moments only, never on every element |
  | UGC, dialogue and talking head | A mood bed about 4 to 6 LUFS under the speech, dipped under each line and lifted on the end card | Room tone plus the real sounds of the scene, each placed on its action (footsteps, a cup set down, a car horn outside, a message pop) |
  | Tool short | An upbeat bed | A soft tap or pop on each interaction |

- **Real sound files.** Effects come from Mixkit, Freesound or Openverse, never sounds Claude invents, except simple tones (a hum, a thump, a whoosh, call tones), which ffmpeg can generate. On Freesound and Openverse each sound carries its own licence: CC0 needs no credit, CC BY needs a credit logged in SOUNDS, and CC BY-NC (non-commercial) never goes in an ad.
- **Log every source** in the asset's SOUNDS note: the track, where it came from, and its licence.
- **Loudness:** master at about -16 LUFS (loudness units relative to full scale).

### AI disclosure

- Turn on the platform's AI label at posting wherever it offers one. A synthetic voice is AI-generated audio, so the label goes on for a voiced film even when nothing in the picture is generated. Burn an "AI-generated" label into the picture only where the platform has no label and the ad policy requires one. Otherwise the picture carries no AI tag, and post captions never mention AI.
- An AI person never poses as a real customer giving a testimonial. AI creators in ads are presented as presenters or actors.
- Testimonials come only from real, published customers with permission.

### Credits and retries

- Fix the script, the storyboard and the start frames before generating any video. Those are cheap, and video is not.
- Generate one output at a time. Draft at 720p and render the final at full resolution.
- Reuse the last prompt that worked, and change only the start frame and the line.
- **Credits go on new scenes, not repeats.** Get a clip right the first time with the prompt rules above, then fix faults in the edit (trims, cutaways, real-screen inserts, cards). A clip is reshot only when the edit cannot save the video, only after it has been watched and found unusable, and only with the owner's go-ahead. Each clip gets at most one retry, with one thing changed. If it fails again, give the failed output to the assistant to rewrite the prompt, or change the start frame.
- Allow one or two rounds of changes per approval point. A third round means the brief or the reference is wrong, so go back to step 1.

### Review stills

Every video the owner reviews before the full render comes as a stills sheet. A generated video shows its start frames. A coded video is built in full, rendered only as stills, and stopped there.

- **The sheet:** one still per beat, in order, with the end card last. Each still is taken at the moment its line has finished typing and its highlight has filled, so every line shows complete. Tile the stills four across at half size into `Frames/[Name] stills.png` in the work folder, and fill any empty tiles with the background colour.
- **Claude checks the sheet first** and fixes every frame that fails, before the owner sees it. On a 1920 by 1080 frame:
  - every line matches the approved script word for word, and no line ends on a single orphan word;
  - on-screen lines are 56px or larger, page text the viewer needs to read is 28px or larger, and the end-card name pill shows the name at about 36px and the address at about 28px;
  - everything sits at least 120px from every edge, and nothing is clipped or runs off the frame;
  - highlight boxes cover whole words;
  - backgrounds and accents are brand colours used as they are or as a gradient between two accents. An accent mixed with black or ink turns into a grey slate, so it is never used;
  - all text has strong contrast, and the end-card pill is solid, never see-through;
  - nothing the gate or the brief excludes appears in any frame;
  - the sheet reads as the reference's style.
- **Storyboards for story scripts.** A story script is reviewed with a storyboard: one frame per shot, in order, with the seconds, the line or sound and the beat's emotional trigger under each frame, and the product shot last. It is drawn in code with no image generation: stand-in figures, real product screens captured locally and the real mockup. A small script captures the real screens and builds the sheet into the brief. You approve the script and the storyboard together. Faces and generated start frames are made only after that, and no image or video credits are spent on storyboards.
- **the owner reviews the batch** as one list of sheet paths. The full render, the loudness pass and the contact sheet come only after his approval.

### Final check

Run this check before anything is posted. Each item is a yes or a no.

- Stills of the export, one per scene, match the storyboard and the reference.
- The length matches the script.
- The audio is present on every shot, and the loudness is about -16 LUFS.
- No caption covers a face, and nothing sits in the bottom fifth on 9:16.
- The AI label is set or burned in where required.
- Every claim matches the brief, and the compliance rules for the platform are met.
- Someone has watched it once, start to finish, in a normal player such as VLC or the phone's own player.

### Folders and files

- **In your notes:** one brief per video, in the project's notes folder. The REFERENCE, SCRIPT, SCENES and SOUNDS outputs become sections of the brief, or separate notes linked from it on a large project. The brief's status runs brief, approved, in production, draft, final, and nothing is generated until it is approved.
- **The brief's sections,** in order:
  - **In one line:** what the video is, who it is for, and what they do after watching.
  - **The job:** who watches it, the moment they are in, the one action we want, the market, and whether it is organic only or can run as an ad.
  - **Reference it copies:** the link, its numbers, and exactly what we copy (opening, pacing, structure, shot type).
  - **Hooks:** three, best first, drafted or reviewed by Codex and passed through the voice scan.
  - **Script, shot by shot:** a table of time, on screen, what we see and audio, within the "Pace" section caps.
  - **Storyboard:** for a story script, the code-drawn sheet from the "Review stills" section.
  - **Who appears:** the character and their persona sheet, or no people, with outfit, setting and props.
  - **Inputs and real output:** for a product or tool on screen, the exact inputs and the exact result the live tool showed.
  - **How it gets made:** the method, the style, and each step's credit cost.
  - **Audio:** the music bed, and a cue list of real sounds with each sound's moment, file, source and licence.
  - **Formats and destination:** ratios, length, where it posts first and the address the end card shows.
  - **Post caption:** ready to paste between two horizontal rules. It never mentions AI.
  - **Compliance check:** each item marked pass or to check.
  - **Build checklist.**
  - **Flow generation, scene by scene:** the prompt log from the "Google Flow" section.
  - **The finished edit:** file, length and any reshoot still open with its credit cost.
  - **Open questions:** numbered, each with a recommendation.
  - **the owner's feedback:** read before any change to the brief.
  - **Revision log.**
- **Outside your notes:** heavy media lives in a work folder linked from the hub, with `Reference/`, `Frames/`, `Voice/`, `Clips/` and `Renders/` inside.
- **Names the owner reads** use title case and readable words, with no dates, slugs or dashes, and the version at the end: a folder `Acme Launch Video`, a file `Acme Launch Video v1.mp4`. Clips are named by shot (`Shot 01.mp4`). Scratch and intermediate files stay in the session scratchpad.
- **Templates:** after the first slow run of a new format, turn it into a template (a Remotion composition, a saved prompt set, or saved anchors), so the next run is fast.

---

## Tools and prices

Prices verified 2026-10-07. Check the source link before buying. Items marked (s) rest on secondary sources.

| Tool | Job | Price and free tier | OK in ads? | Source |
| --- | --- | --- | --- | --- |
| Claude (Fable, Opus, Sonnet, Haiku) | Scripts, teardowns, coding agent | Plans per Anthropic | Yes | [anthropic.com](https://www.anthropic.com/pricing) |
| ChatGPT (GPT Image) | The default for every image of a person or character (cast, personas, clone anchors, start frames), plus ad images and thumbnails with text | Free (limited), Go $8, Plus $20 (s) | Yes | [OpenAI](https://openai.com/chatgpt/pricing/) |
| Gemini with Nano Banana | Fallback for stills when ChatGPT falls short. Never remake a character ChatGPT already made | Free in the app (about 20 a day) (s) | Yes (s) | [felloai.com](https://felloai.com/is-nano-banana-free/) |
| Google Flow | Directs Gemini Omni and Veo 3.1 shots | Free 50 credits a day at 720p; Pro $19.99 for 1,000 credits (s) | Paid plans yes; treat the free tier as no | [costgoat.com](https://costgoat.com/pricing/google-flow) |
| Gemini Omni 1.1 Flash | Quick, consistent clips of 3 to 10 seconds with sound; conversational edits | Free in Google Vids and YouTube Shorts; paid in the Gemini app | Check Google's terms before ad use | [Google blog](https://blog.google/products-and-platforms/products/workspace/gemini-omni-in-google-vids/) |
| Veo 3.1 | Cinematic and 4K shots | API $0.05 to $0.60 per second by tier | Yes on the paid API | [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| Google Vids | Free AI clips, slides to video | Free for any Google account | Treat as not for ads | [Google blog](https://blog.google/products-and-platforms/products/workspace/gemini-omni-in-google-vids/) |
| Kling 3.0 | Low-cost volume video | Free 66 credits a day with a watermark; Standard $8.80 a month (s) | Paid plans only | [crixpix.com](https://crixpix.com/kling-ai-free/) |
| Seedance 2.0 and 2.5 | Video with strong prompt following | About $0.15 a second at 720p on the API (s) | Yes on paid routes | [framesurfer.com](https://framesurfer.com/blogs/seedance-2-0-pricing) |
| Runway | Gen-4.5, plus Kling and Seedance | 125 free credits once; from $15 a month | From Standard | [runwayml.com](https://runwayml.com/pricing) |
| Midjourney | The best-looking stills | From $10 a month, no free trial (s) | Yes; companies over $1M revenue need Pro | [Midjourney](https://www.midjourney.com/account) |
| Ideogram | Text inside images, fallback to GPT Image | Free 10 slow credits a week; Plus $20 (s) | Yes (s) | [eesel.ai](https://www.eesel.ai/blog/ideogram-pricing) |
| ElevenLabs (Eleven v4) | Voiceover, voice clone, Voice Changer | Free 10,000 credits; Starter $6; Creator $22 | Paid plans only | [elevenlabs.io](https://elevenlabs.io/pricing) |
| Gemini text to speech (Flash TTS) | Narrator and host voices that take an accent, pace and register instruction in plain words | Billed per use on the Gemini API, billing on | Check Google's terms before ad use | [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| OpenAI text to speech (gpt-4o-mini-tts) | Comparison voices from a second provider; takes the same kind of style instruction | Billed per use on the OpenAI API | Yes on the paid API; disclose that the voice is AI | [OpenAI pricing](https://openai.com/api/pricing/) |
| Google Cloud TTS (Studio, Chirp 3 HD) | Low-cost narration | 1M free characters a month each, then $160 or $30 per million; billing must be on | Yes | [cloud.google.com](https://cloud.google.com/text-to-speech/pricing) |
| HeyGen | Avatars and clones of you | Free 3 videos a month; Creator $29 | Paid yes | [heygen.com](https://www.heygen.com/pricing) |
| Arcads | AI UGC actors | About $110 a month for 10 videos (s) | Yes (s) | [ugcgen.ai](https://ugcgen.ai/arcads-pricing) |
| Remotion | Code-built video, captions, motion graphics | Free for up to 3 people | Yes within the licence | [remotion.pro](https://www.remotion.pro/license) |
| whisper.cpp | Transcripts and word timings | Free | Yes | [GitHub](https://github.com/ggml-org/whisper.cpp) |
| ffmpeg | Cutting, joining, pulling frames | Free | Yes | [ffmpeg.org](https://ffmpeg.org) |
| CapCut | Manual edits | Free; Pro $19.99 (s) | Pro for ad assets (s) | [eesel.ai](https://www.eesel.ai/blog/capcut-pricing) |
| Mixkit | Music and sound effects | Free | Yes for online ads; check each item's tag | [mixkit.co](https://mixkit.co/license/) |
| Freesound | Sound effects and ambience | Free with an account | CC0 and CC BY sounds only; never CC BY-NC | [freesound.org](https://freesound.org/) |
| Openverse | Search across openly licensed audio and images | Free | CC0 and CC BY items only; never CC BY-NC | [openverse.org](https://openverse.org/) |
| Suno | Original music | Free has no commercial rights; Pro $8 a month annual | Pro and Premier only | [suno.com](https://suno.com/pricing) |

**Default picks.** ChatGPT for every image of a person. Flow for every generated clip, with the model chosen per shot in the "Google Flow" section. Remotion for every edit that can be built in code. Gemini text to speech for a coded film's voice. We do not use Higgsfield. Kling, Seedance and Runway stay listed for reference.

**Start lean.** Free tiers are enough to test. Pay for one tool per layer only when an ad or volume needs it. Sora is discontinued.

### How the tools are named

Three kinds of tools share the spotlight:

- **Assistants** are where you type: ChatGPT, Gemini, Claude.
- **Wrappers** put one interface over several models: Google Flow, Runway.
- **Models** do the generating, one layer each (text, image, video or voice): Veo 3.1, Gemini Omni, Nano Banana, Kling, Seedance.

Google's family: Gemini is the assistant, Nano Banana the image model, and Veo 3.1 and Gemini Omni the video models. OpenAI's: ChatGPT is the app and GPT Image the image model. Anthropic's: Claude is the assistant, with Fable, Opus, Sonnet and Haiku as the model tiers from most capable to fastest.

To place a new tool, ask two questions. Is it an assistant, a wrapper or a model? And which layer does it work on? Then put it in the matching row.

---

## Appendix: Google's low-cost on-ramp

**Google Flow.** The free tier gives 50 credits a day at 720p, enough for two Veo 3.1 Fast clips. Paid Google AI plans add monthly credits. Flow can also build an avatar of you: start a project, click the plus icon in the prompt box, choose Avatar, and scan your face with your phone. Work image-first, because a still costs far fewer credits than a clip.

**Google Vids.** Vids is free for any Google account and runs Gemini Omni 1.1 Flash at 1080p. Open vids.new to generate a clip, or use File, then Convert Slides, to turn a Google Slides deck into a narrated video. Treat Vids output as not cleared for ads until Google's terms say otherwise. The Gemini app's free plan makes no video.

---

Related: `reference-teardown.md` · `01-faceless-influencer.md` · `02-ai-clone-talking-head.md` · `03-ai-ad-creative.md` · `04-faceless-youtube.md` · `05-launch-videos-and-recording-edits.md`

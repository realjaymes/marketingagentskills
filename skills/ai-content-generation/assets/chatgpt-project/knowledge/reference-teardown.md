# Reference Teardown

Every AI creation starts here. Before writing a script, a carousel, an ad or a page, we take one proven example apart and copy its structure. We never copy its words, product, claims, footage, music or brand marks.

This note sets one REFERENCE format. It is used in step 1 of every AI content playbook (the "Workflow" section of the 00-workflow-and-rules knowledge file) and for every swipe file, so a swipe captured today can be rebuilt in any format later.

## When to use it

- **Before any AI video, ad, carousel or landing page.** The reference is the concept.
- **For every swipe file.** Each saved video or post gets a REFERENCE note, so swipes are ready to rebuild.
- **To copy a style.** Add the style-in-numbers section when we want a creator's edit style or a brand's motion style (the 05-launch-videos-and-recording-edits knowledge file).

## Picking a reference

- It does the same job as the thing we are making: the same goal, a similar audience and the same format.
- It is proven. That means strong engagement for its account, a long-running ad in an ad library, or a launch that clearly worked.
- One to three references are enough. With more than one, take the structure from the strongest and note what each of the others adds.

## Capturing it

Claude reads frames and transcripts. It cannot watch motion, so we capture what it needs:

1. **The file.** Download the video, or save the post's images.
2. **Frames.** Use ffmpeg scene detection to find every cut, and save one still from the middle of each shot. To measure motion, pull frames densely (10 to 30 a second) around each transition.
3. **Words.** Run whisper.cpp with word-level timestamps into `words.json`.
4. **Numbers.** Record the length, dimensions and frame rate.
5. **Comments and stats** when they exist. For Instagram and TikTok swipes, a bulk capture tool can save comments, stats and contact sheets in bulk.

Raw files go in the asset's work folder outside your notes (the "Folders and files" section of the 00-workflow-and-rules knowledge file). The REFERENCE note goes in your notes.

## The REFERENCE format

Write only from what was seen and heard. Mark anything uncertain as "unclear" instead of guessing.

**Summary:** one line covering who is on screen, what is sold, and to whom.

**Labels:** the Creative Strategy Framework layers, using only its vocabulary: angle, Content Structure, Creative Format, Style and hook trigger.

**Numbers:** length, size, shot count, average shot length, and words per minute.

**Shot list:** one row per shot with:
- start and end times;
- what is on screen (person, framing, graphics, cutaways);
- the exact words;
- the on-screen caption;
- the shot's job: hook, problem, proof, how it works, offer or call to action.

**Hook:** the first three seconds word for word, plus the move it makes. Common moves are saying what was built and for whom, asking a question, stating a surprising number, or showing the result first.

**Narrative:** the story arc in one line.

**Sentences:** every sentence written out, with the shot it starts and ends in. New sentences often begin on new shots.

**Beats:** four to seven parts of the argument, each with its job, length in seconds and word count. The script copies these word counts.

**Captions:** position, words per group, font weight, colours and highlighted words.

**Graphics:** every card, screenshot and text pop-up, with timing, position, and how it enters and exits.

**Look:** light, palette, camera movement, texture and composition.

**Sound:** music or none, sound effects or none, and where the effects land.

**Style in numbers** (only when copying a style):
- cuts per minute;
- zoom size and how often it happens;
- caption words per screen;
- animation length and easing;
- how long text holds on screen;
- sound effects per minute and what triggers them.
- three to five signature moves: the edit choices that make the style recognisable, such as a punch-in on every claim or a whoosh before each new idea.

**Why it works:** three lines, grounded in the structure.

## Non-video references

The same format works for other outputs. Keep the sections that apply:

- **Carousel:** one row per slide in place of the shot list, with the headline, body text, visual and job of each slide.
- **Static ad:** the hook text, offer, proof, visual, layout and call to action.
- **Landing page:** one row per section, with its headline, job, proof and call to action, plus the design notes `design-taste` uses.

## Rules for the rewrite

- Keep the same hook move, narrative and beats, in the same order, doing the same jobs.
- Each beat stays within about five words of the reference beat, so the length matches.
- Every claim comes from our brief. A missing fact is flagged for the owner, never invented.
- Captions copy the reference's style, and the safety rules in the "Captions" section of the 00-workflow-and-rules knowledge file still apply.
- Colours come from our product or brand kit (the "Brand colours" section of the 00-workflow-and-rules knowledge file).

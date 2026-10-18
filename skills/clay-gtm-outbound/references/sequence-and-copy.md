# Outbound Sequence and Copy Standard

This file sets the sequence structure, the copy rules and the pre-send checks for outbound that Clay data feeds. The rules come from outbound practice: copy craft (subject lines, structure, follow-ups, personalization depth) and batch checks (what a batch may and may not share). If you keep a dedicated cold-email skill or a send lint, keep it consistent with this file.

## Division of work

- Clay holds the facts. It finds, enriches, verifies and scores, then writes plain merge-field columns.
- The sequence text lives in the sequencer or a template document, with merge fields and conditionals in it. Clay does not write the whole email.
- A Clay AI column writes one bounded merge field at most (an opener line, a segment label). One call, one field, one job.
- The sequencer resolves variation (spintax and conditionals). Clay output carries no braces, no pipes and no placeholders.

## Merge fields built in Clay

Precompute every field into its own plain column at generation time:

- `greeting`: "Hi {first}," when the first name is verified (confirmed on LinkedIn or from a provider-verified direct address), otherwise "Hi {company} team,". Never greet by a scraped name that has not been verified. A wrong guess produces "Hi Chat," or "Hi Toggle,".
- `gap` (or `opener`): one sentence built from the signal the team chose, framed as an opportunity and written in plain language.
- `segment`, `company`, `city` and any proof or traction line the sequence uses.
- A variant column that records which signal produced the opener, so a preview tool can filter by it.

Resolve every fallback into its own column. Do not leave a live `{{field|fallback}}` tag in send copy. Smartlead does not support the pipe syntax and renders the field blank whether or not it has data. Bare `{{field}}` tags and single-brace spintax both work. Smartlead does support real Liquid conditionals (`{{#if var}}...{{else}}...{{/if}}`, with `==` and `!=`), and a blank field is then the signal the `{{else}}` branch keys on.

Required inputs and fallbacks:

| Input | If missing |
|-------|-----------|
| Verified deliverable address | Drop the row from the send list |
| Company name | Drop the row |
| First name | Use the company greeting |
| Signal data | Fall back to the next opener in the order the team chose |
| Stack, funding, headcount | Use neutral phrasing that claims no fact ("At your stage" in place of "With a team of 200+") |

Opener fallback order: a signal if one exists, then a stack observation, then an industry and title insight, then a plain pain statement. Missing-data phrasing never states a fact that the data does not hold. "Teams in your market often rely on testing tools" replaces "I noticed you use Optimizely" when the tool is unknown.

### Prompt skeleton for a bounded opener column

```
Role: You write one sentence for the opening of a cold email.
Evidence: {{signal_fact}}, {{company}}, {{source_url}}
Task: State the fact and the opportunity it creates for the reader, in one sentence of 25 words or fewer.
Rules: Use only the evidence above. If the evidence is empty, return an empty string.
Write plain words and full sentences. Frame an opportunity and never a criticism.
Use no dashes, no questions, no jargon and no claim about the reader's performance.
Output: the sentence only.
```

Test it on 10 rows, read every output and check the empty case before scaling. Clay's plugin skills `campaigns-sequence-writing` and `campaigns-sequence-reviewing` apply the same discipline inside Clay's own Sequencer: one role per snippet, explicit evidence, an output bound, grounding over variation, and a review from the recipient's seat that asks why they would not respond.

## Sequence structure

The default for a campaign is a reply-first sequence of three emails:

| Email | Day | Job |
|-------|-----|-----|
| 1 | 0 | The opener: `gap`, the offer and a low-friction close |
| 2 | 3 | A new angle with new value. Never "did you see my last email" |
| 3 | 7 | A clean exit: acknowledge timing, restate the offer in one line, close with an easy way out and no guilt |

Three to five touches are fine with widening gaps (days 0, 3, 7 to 8, 14, 21 to 28) when the offer needs more education. Each follow-up adds a distinct reason to respond, such as new value, fresh proof, a different angle or a useful resource, and stands alone. The last touch is a breakup that honors the silence.

Subject lines belong to Email 1 and its variants only. Follow-ups thread as replies to Email 1. When contacts at one company are in a campaign, set the sequencer to stop the whole company domain when any one of them replies.

Match the sequence to the objective:

| Objective | Email 1 | Email 2 | Email 3 |
|-----------|---------|---------|---------|
| Product signup | Signal and product in one line | Proof and the link | Is the problem still live |
| Meeting or demo | Signal, problem, offer | Proof from a similar company | Specifics and an easy time suggestion |
| Content or insight | The finding | The data behind it | Ask for their view |
| Partnership | Shared audience and mutual value | An example that worked | A simple next step |
| Re-engagement | What changed since | Proof | Is the timing right now |
| Referral | The ask and who | Why them | Make it easy to forward |

## Copy rules

- Length: a templated sequencer send stays under 120 words. A one-to-one research pitch to a named person runs about 200 words and may run longer when the finding earns it. Length is a copy judgment and does not cause spam classification.
- Voice: a peer who noticed something relevant. Use contractions, say "you" more than "I", read the email aloud, and cut every sentence that does not move the reader toward replying.
- Structure: choose from observation, problem, proof, ask; question, value, ask; trigger, insight, ask; or story, bridge, ask. One proof point beats ten features. Keep a library of worked examples for each framework.
- Opener: the personalization must connect to the problem. If you remove the personalized line and the email still makes sense, the personalization is not doing its job.
- Offer: sell the outcome and not the mechanism for service offers, and put the outcome word early in the sentence. "If I mapped out a plan for turning more of {{company}}'s free users into paying customers" opens on the outcome and stays a hypothesis. A presumed diagnosis stated as fact does not.
- Close: one ask, interest-based, with no meeting request and no calendar link in the first touch. End on one plain closing line: "What do you think?", "What do you say?", "Would you like to chat about this?", "I'm interested in your thoughts." or "I'd like your feedback." When the close asks them to say yes or no to something you would send (an audit, a plan, a teardown), a full-sentence yes or no question fits: "Would you want it?", "Is it worth a look?", "Would you like me to send it?". Vary the closing line across contacts at one company. Clipped fragments ("Worth a look?", "Want it?", "Interested?") read as templated and curt.
- Never quote a price in a pitch. Name the value and invite a conversation. Scope and price are set on the call.
- Subject lines: two to four plain lowercase words, under 30 characters, naming the topic itself, the noun phrase a colleague would type. A riddle that withholds the topic fails even when it passes the word count. Write two options per company and let open rate decide: Option A names the buying question or the page it concerns, and Option B names a competitor or a comparison (the higher-risk half). No first name in the subject line, no urgency words, no punctuation tricks.
- Full sentences with a subject. Fix three patterns in every clause and not only at the start of a sentence: verb-first openers ("Sounds like..."), bare closing questions, and trailing clauses with no subject of their own.
- A comparison claim has to survive the deliverable. When copy says a prospect resembles named competitors, that claim becomes the thesis of whatever free deliverable they accept. Re-read the live pages at deliverable time, and hold the named competitors to the same standard as the prospect.
- Never pitch a hiring company the work its open role owns (see `signals-and-audiences.md`).
- Format: plain text, no formatted markup, no images, one link at most, no markdown. Do not track opens or link clicks. A reply is the metric that matters.

## Batch checks before anything sends

A batch fails as a whole, because the failure is a batch-level fingerprint. Gmail spam-foldered a sender with the reason "similar to messages that were identified as spam in the past" when 26 pitches shared one opening clause, one closing line and two URLs. Mean pairwise similarity was only 30%, so varied middles do not save a batch. The classifier reads what does not change.

Run a pre-send lint over the full batch and fail it on any of these:

- Unsubscribe or opt-out language in one-to-one mail ("reply no thanks", "if this isn't relevant", "won't follow up"). Mail from a personal mailbox carries no list-unsubscribe header, so the line is the most bulk-looking line it can send.
- Unfilled template syntax in the assembled message (a spin group, a liquid variable or a placeholder). Check the assembled message and not only the source body, because machine-appended text is never inspected by a check that reads the source.
- Any body sentence that appears in more than a quarter of the companies in the batch, or any URL in more than half.
- A sender domain and a link domain that disagree.

Count companies and not recipients, because two contacts at one company are one pitch sent in parallel. Warn when two recipients at a company receive byte-identical prose. The signature is exempt and stays identical on every email, because a stable sign-off is what a real correspondent has. A proof link may be reused where it genuinely fits the angle. Match the proof page to the pitch angle.

Bulk sends run on a sequencer and a sending domain with a real list-unsubscribe header. Check the sending tool's opt-out setup and the local law for the audience. One-to-one mail from a personal mailbox carries no opt-out line.

Spintax and liquid variables are sequencer features and never go into a draft built outside a sequencer. Such a draft has no template engine and would mail the braces literally.

## Timing

Send in the recipient's local morning (8 to 10), lunch (12 to 1) or late afternoon (3 to 5). Avoid weekends, evenings and Friday afternoons for first touches. Tuesday to Thursday performs best. Identify the recipient's time zone before sending and record the send window in your own time.

## Quality check

Before a sequence goes live: read each email aloud, preview every email and every variant with real lead data (nothing blank, no raw `{{field}}` tag), confirm a human would reply to it, confirm the ask is single and low-friction, and run your own quality check. For bulk work, review the rendered emails in a preview tool that shows merge fields highlighted, blank variables flagged and each opener variant with its count.

---
name: outbound-engine
description: The campaign half of cold outbound. Turns an enriched, scored prospect list (from prospect-scraper) into a personalized, deliverability-safe, reply-first email campaign, reviewed in a self-built HTML QA and preview tool, sent through Smartlead, with every reply filed and real prospects handled through to close. Use when the user wants to build a cold-email sequence, personalize outbound with {{gap}} or signals, add spintax or fallback-resolved merge fields, build or standardize the HTML email preview tool, prepare a Smartlead-ready list, run or scale an outbound campaign, check a campaign's replies, or file and triage a prospect who replied. NOT for finding or enriching leads (that is prospect-scraper) or writing standalone copy (use a cold-email copy skill).
---

# Outbound Engine

The campaign half of cold outbound. It takes the enriched, scored prospect list from `prospect-scraper` and runs it to booked calls: personalize → assemble the sequence → QA in the preview tool → warm the sending infrastructure → send through Smartlead → measure → **file every reply and handle real prospects through to close**.

`prospect-scraper` owns FIND, ENRICH, VERIFY, SCORE and signal detection. This skill owns PERSONALIZE, QA, WARMUP, SEND, MEASURE and reply filing. They meet at the common record schema.

## When to use

- Build or personalize a cold-email sequence (`{{gap}}`, signals, spintax, Liquid).
- Build or regenerate the **HTML preview and QA tool**, the review surface.
- Prepare a Smartlead-ready list and run or scale a campaign.
- Check a live or completed campaign's replies, file them, or handle a prospect who replied.

Use a different skill for finding and enriching leads (`prospect-scraper`), standalone copy, or Clay-specific work.

## Where things live

- **Runnable code** (generators, the preview builder, verifiers) lives in a version-controlled repo.
- **Lead lists and the preview tool** live in one local folder per campaign. The master `*-leads.csv` is Smartlead-ready, and the `* Email Preview.html` file is the review surface.
- **Your notes system** (Obsidian, Notion, a docs folder) holds the logic: the offer, the `{{gap}}` logic, and the **sequence templates with `{{}}` and spintax**. It never holds individually filled emails. Once a campaign is live, it also holds the campaign's `Replies` file and each real prospect's own file (see Reply filing below), because those track decisions.
- **The preview tool shows the final rendered emails.** You review there, not in the notes.
- **Flow:** enriched list → `{{gap}}` and variant → master CSV → preview tool (QA) → export cleaned → Smartlead → run → file replies and handle prospects. Push to Smartlead when the batch reaches the campaign's target size.

Keep every note current. When a fact changes, rewrite the affected section in place instead of appending dated updates. A sequence template doc always shows only the current copy. The `Replies` file is the one designated log, with one row per reply.

## Personalization method

- **Collect broadly, decide narrowly, and never default to one signal.** `prospect-scraper` hands over every signal detected per lead. Never auto-pick which signal leads `{{gap}}` or a batch's variant scheme. Before writing any copy: (1) summarize the signal landscape (which signals are present and roughly how common each is), (2) present two or three candidate angles this makes possible, and (3) get a human decision on which signals lead and how they map to variants. This stops you from over-indexing on one signal early and closing off angles that a different signal, or a combination, would have opened. Only then apply a mechanical rule across the batch (for example, first match wins within the chosen priority order, or a stacked variant for leads with two signals).
- **Never pitch a hiring company the open role's own work.** This applies to every freelance, fractional, contractor or services pitch. When a lead has an open or just-filled go-to-market role, drop every signal that role would own before you build the landscape. A paid-media role owns paid gaps, a content or SEO role owns content and search gaps, a sales or GTM-engineering role owns outbound gaps, and a broad growth or founding-marketer role owns nearly all of them. Banned framings include "set up the system your new hire will run," "cover the work while you recruit," and the job description repackaged as a contract. The hire tells you there's budget. The pitch should be a different service, backed by evidence on their live pages. When nothing outside the role's remit is left, take the lead out of the campaign. It goes to a one-to-one manual pitch only after someone finds a gap by hand.
- **Named people, never role inboxes, and at least two per company.** `info@`, `contact@`, `hello@`, `support@`, `service@`, `sales@` and similar never count as a lead's email. Every company in a send list needs at least two verified emails for named decision-makers: the founder or CEO first, then the function head who owns the problem, then the hiring manager or a senior peer. "Verified" means a second, independent source confirmed the address. A single tool's own result is a candidate until another source confirms it. A catch-all domain never verifies a mailbox by itself. A firstname-style address for the right person on a catch-all domain can still go on the list, flagged `catch_all_accepted`. Personal, university and old-company addresses count toward the two only for a separate low-volume fallback send. They belong in `fallback_email`, never in the main `email` column. Run the full `prospect-scraper` waterfall before settling for less, and park a company that can't reach two named contacts instead of sending to a role inbox.
- **Multiple contacts per company are allowed, and preferred when a company has several real decision-makers.** Early-stage startups usually have two to four cofounders. Keep the list to one row per contact, with company fields repeated. Keep it to people who could buy: published cold-email benchmarks show reply rates around 7.8% at one or two contacts per company against 3.8% at ten or more, so never pad a company with junior staff. The campaign must stop sending to the whole company domain the moment any contact replies (see the setup checklist). Contacts at one company share the same `{{gap}}` because it describes the company, but `{{greeting}}` stays personal. Copy never implies each person is the only one contacted, and never names the cofounders as also emailed. Where practical, stagger starts so cofounders don't open an identical Email 1 on the same morning: upload the lead founder first and the others a few days later.
- **`{{gap}}`** is the chosen signal (or signals), written as a one-line opener. Frame it as an **opportunity, never a criticism** ("you'd normally...", not "you're failing"), in plain language, with no em dashes. At scale it's a signal-to-template engine: a keyword match on the chosen signal picks a `{{gap}}` template, following the priority order set for that batch. Hand-write it only for a small first batch.
- **Signal-keyed Email 1 variants.** When leads carry different signals, Email 1 gets variants keyed to which signal fired (for example hiring → H, recent post → P, both → HP, DNS issue → D, none → B), chosen per lead using the agreed variant scheme. Clean raw signal fields into natural sentence fragments before merging. A role note becomes "a Sales Director role", not the whole research blob.
- **Spintax and merge variables.** Use spintax `{a|b|c}` on most sentences for deliverability variation. It works in Smartlead. Merge variables such as `{{company}}`, `{{city}}`, `{{gap}}`, `{{greeting}}`, `{{segment}}` and `{{inbound}}` each get their fallback **resolved into a plain CSV column at generation time**. Precompute `greeting` as "Hi {first}," or "Hi {company} team,". **Smartlead does not support `{{field|fallback}}` pipe syntax.** It renders blank whether or not the field has data. Bare `{{field}}` tags and single-brace spintax both work. Any sequence doc with a `|` inside `{{ }}` has this bug. Smartlead does support real Liquid conditionals: `{{#if var}}...{{else}}...{{/if}}` with `==`, `!=`, `>`, `<`, `gte` and `lte` (single-quoted values). It documents no date or `now` function, so don't build time-of-day copy ("Good morning") on a guess.
- **Sell the outcome, not the mechanism**, for service offers (say "client acquisition", not "outbound"). Keep it reply-first, offer-first, with a low-friction CTA. Put the outcome early in the sentence, not after a presumed diagnosis. "If I mapped out exactly where {{company}} is losing free users before they upgrade..." opens on a problem stated as settled fact. "If I mapped out a free plan for turning more of {{company}}'s {{installs}}+ free users into paying customers..." opens on the outcome and stays a hypothesis.
- **Never quote a price in a pitch.** Emails, LinkedIn messages, follow-ups and pitch files name the value and invite a conversation. Scope and price get set on the call.
- **A comparison claim has to survive the deliverable, not just the send.** When `{{gap}}` says a prospect resembles named competitors ("your homepage reads like X's and Y's"), that claim becomes the thesis of the free deliverable they say yes to, so it has to hold up weeks later. Run two checks before writing it into copy. First, re-read the prospect's live page when you build the deliverable, not just at scrape time, because homepages change and a hero you scored can be gone by then. Second, hold the named competitors to the same standard as the prospect. Naming a competitor implies they do the thing better. If they don't, say the specific thing all of them share, so the claim stays defensible whichever way the pages change.
- **No dropped-subject fragments, anywhere in the copy.** Watch for three shapes. Verb-first openers: "Sounds like..." becomes "It sounds like...". Bare CTA questions: "Worth a look?", "Want it?" and "Interested?" become full questions ("Is it worth a look?", "Would you like me to send it?") or a simple close ("What do you think?"). Comma-tacked trailing clauses: "...3 spots this month, a free Blueprint included" becomes its own sentence, "You'll get a free Blueprint." This applies to every channel, LinkedIn messages included. Self-check for it on every draft.

## The reply-first sequence (3 emails)

Templates live in your notes and the campaign config, never as filled copy in this skill.

- **Email 1:** opener (`{{gap}}`, the offer, and a low-friction CTA).
- **Email 2 (about 3 days later):** a new angle, never "did you see my last email".
- **Email 3 (about 4 days later):** a clean exit. Acknowledge timing, restate the offer in one line, make it easy to close, no guilt.

Use a pool of subject lines for Email 1 to A/B test. Follow-ups thread as `re:` replies.

## The HTML preview and QA tool

This is the review surface. **Don't hand-build a new one per campaign.** Build one reference implementation, then copy it per campaign and change only its CONFIG block. Full spec and config schema: `references/preview-tool-standard.md`.

Required features: a dark header with suspicious, flagged and clean counts; a searchable, filterable sidebar with a severity dot per contact; a detail panel with merge fields highlighted; blank or broken variables flagged red; spintax choices underlined; a QA severity banner with reasons; one filter option per `{{gap}}` signal with its count (driven by a `gap_variant` column that every gap generator must write); an Opener select that swaps each Email 1 variant's subject and body together, with `re:` threading on follow-ups; keyboard navigation (↑/↓/r/f); flags that persist; and **Export cleaned CSV**, which drops flagged rows. An optional LinkedIn config adds steps, character limits and a test arm for campaigns with a LinkedIn track. Status columns in the leads CSV (request_sent, accepted, dm_sent, followup_sent, replied, or sent and replied for email) automatically turn on status chips, header stats and a Pending filter.

## QA rules (per lead, computed in the generator)

Standard checks that set severity and reasons: email domain doesn't match the website domain (high), a blank required merge variable (high, marked "broken"), a free or personal email on a company lead (medium), and any disqualify or exclude tags the campaign defines. Suspicious rows surface in the sidebar, and Export cleaned removes flagged ones.

## Deliverability and send

- Use fresh secondary domains and inboxes, warmed for two to three weeks before real sending. For client work, the client funds them. Never send from a client's primary domain.
- Verify SPF, DKIM, DMARC and MX records with `dig` before sending.
- Send through Smartlead or Instantly (warmup pools, a daily-cap ramp, A/B testing, cadence).
- Measure reply → positive reply → call → opportunity. Reply rate is the first conversion event.

**Smartlead through the API.** If you have a Smartlead CLI or API wrapper, use it to bulk-add leads from the master CSV. Map standard fields (`email`, `first_name`, `company` → `company_name`, `website`, `city` → `location`) and route everything else (`greeting`, `gap`, `segment`, `inbound`, `contact_source`, `quality`) into `custom_fields`. Always do a dry run first to check the mapping. This mapping is more reliable than the Smartlead UI's fuzzy CSV header matching.

## Smartlead campaign setup checklist

Once a lead list and sequence are QA'd, set up every campaign in Smartlead with this checklist, then report what was set before anyone launches.

- **Map custom fields manually, never trust auto-mapping.** Auto-mapping on CSV upload can silently break variables, so a merge field renders blank or wrong. Check and map every custom field the sequence uses during upload.
- **Choose verification by send path.** For Smartlead campaigns, Smartlead's built-in verification after upload is usually enough. Read its valid, catch-all, risky and invalid split before judging list quality. For one-to-one sends from a regular inbox (Gmail, for example) that never touch Smartlead, run a verification API such as MillionVerifier before every batch and refuse to send on an invalid or disposable result. A self-built SMTP probe won't work if your network blocks port 25, because it returns "unknown" for every address, dead ones included. A vendor's "verified" flag means the address existed, not that the mailbox is alive today.
- **Add a blank line after every line when pasting sequence copy** into Smartlead's editor, so the sent spacing matches the draft.
- **Only Email 1 and its variants get a subject line.** Later steps thread as `re:` replies.
- **Preview every email and every variant, every time. Never sample.** For every step and every A/B/C variant, open the rendered preview with real lead data. Confirm nothing is blank, no raw `{{field}}` tag shows, and nothing reads as garbled. In Smartlead's current UI, the "Inbox Preview" snippet near the top of the editor is a static summary, not a real preview. The real one is under the step's **⋮ More actions → Preview Template** menu, which opens a modal with a lead selector and the fully rendered email. Judge broken copy in that modal, not the raw editor. The raw editor can render a spintax `|` so it looks like a capital "I" ("interested.|I'll" reads as "interested.II'll"), even zoomed in. That's a font artifact, not a bug. Check Preview Template, or the underlying CSV text, before reporting anything as broken.
- **Use every account in the sending pool**, not a subset.
- **Set one standard timezone** for your campaigns, matched to where most of your prospects are, unless a campaign needs a different one.
- **Set the start date to the next day.** A placeholder date left weeks out from campaign creation silently blocks every send.
- **Delivery optimization:** plain text mode, send to all email providers.
- **Reputation protection:** turn on High Bounce Rate Auto-Protection and pause the campaign when bounces pass 5%.
- **Stop on reply at the company level** whenever a campaign has more than one contact per company. Turn on the setting that stops all leads on the same company domain once any one replies, alongside the standard stop-on-reply. Check it before launch. A missed toggle means a cofounder gets Email 2 after their partner already answered.
- **Wire a reply-alert webhook on every campaign** (Email Reply and Campaign Status Changed events) to your automation tool (n8n, Zapier, Make), which forwards alerts to email or Slack. See the reply-filing standard.

## Reply filing and prospect handling (required for every campaign)

**Every campaign gets a `Replies — [Campaign Name]` file from launch.** Full standard: `references/reply-filing-standard.md`. In short:

- **Pipeline:** Smartlead's Master Inbox (the record of what was sent) → the `Replies` file (triage) → a per-prospect file for anything real → the campaign hub (rollup and status).
- **Categorize every reply** with the standard labels: Interested, Hot, Yes to [named offer], Declined, False positive (auto-replies and wrong contacts), Confused or not primed, and Unsubscribe or complaint (handle immediately: mark Do Not Contact and add the address to Smartlead's block list).
- **Move anything Interested, Hot or Yes-to-offer** into its own prospect file.
- **The reply-check cadence is what actually catches misses**, because alert workflows can fail silently. Check at launch (confirm the alert fires), periodically while the campaign is active, and always run a full reconciliation the moment Smartlead marks the campaign Completed. Compare Smartlead's reply count against the file's row count.
- The reply-alert webhook speeds things up. It never replaces the manual cadence.

## Related

- `prospect-scraper`: the data half (find, enrich, verify, score, detect signals).
- A cold-email copy skill: writes the copy this personalizes and sequences.
- `references/preview-tool-standard.md`: the preview and QA tool spec.
- `references/reply-filing-standard.md`: the reply-filing and prospect-handling standard.

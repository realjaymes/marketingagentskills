# Reply Filing and Prospect Handling: Standard

The standard for what happens to a campaign's replies once it's live. It exists because the common failure is quiet: real replies sit unfiled across several concurrent campaigns, a drafted response never gets sent, and a campaign gets marked Completed with replies that were never pulled into your notes. **Every campaign gets this from launch, not after replies start piling up.**

## The pipeline

**Smartlead's Master Inbox (the record of what was sent and each thread) → `Replies — [Campaign Name]` (the triage file, in your notes system) → a per-prospect file for anything real (research, drafts, next actions) → the campaign hub (rollup and status).**

Smartlead stays the source of truth for what was sent and when. Your notes are for deciding what to do about a reply and tracking that decision. Don't re-record thread state that already lives in Smartlead.

## The `Replies — [Campaign Name]` file (one per campaign)

Create it the moment a campaign launches. Empty is fine, and "0 replies so far" is a valid first state. Keep it in the same folder as the campaign's offer brief. Give it the same project tags as the rest of the campaign, plus a `last_touch_date` field you update every time you touch the file.

Required sections, in order:

1. **A header line** naming the campaign, its source (Smartlead's Master Inbox), and the division of labor: "Smartlead stays the system of record for send and thread state. This file is the triage and decision layer."
2. **Current count**, taken from Smartlead's own campaign analytics (leads, sent, reply %, positive, bounced), never a manual tally. Pull it live each time you touch the file, because a stale count is exactly how replies go unfiled.
3. **A reply summary table:** `# | Company | Contact | Status | Prospect file`. One row per thread. A contact who replied four times is one row.
4. **Full reply threads:** one subsection per row, with the reply quoted verbatim, a `**Read:**` line giving your interpretation (why the reply reads the way it does and what the person likely means, not a restatement), and a link to the prospect file if one exists.
5. **Next actions:** live forward tasks only. Check off or prune old ones before adding new ones.
6. **Related:** links to the prospect files, the offer brief and the sequence doc.

## Reply categories (use these labels, don't invent new ones per campaign)

- **Interested:** engaged and asking a real question, not yet asking for a call.
- **Hot:** explicitly asking for a call or meeting, or asking a direct qualifying question a decision-maker would ask (for example "full-time or fractional? send your LinkedIn").
- **Yes to [named offer]:** said yes to a specific thing the copy offered (a free breakdown, a lead sprint, a walkthrough). Name the offer in the label so the next action is obvious without re-reading the thread.
- **Declined:** a clean "not interested" or equivalent. Closed, with no prospect file and no follow-up.
- **False positive:** an auto-reply (out of office, ticket confirmation, careers redirect) or a wrong contact (enrichment grabbed a website builder's inbox or a franchise parent's inbox instead of the business's). No human read the pitch. Close it with no prospect file, but log the failure if it's a data-quality bug worth fixing upstream, and spot-check other leads for the same wrong-contact pattern.
- **Confused, not primed:** a real business and a real reply, but they clearly haven't absorbed the earlier emails ("I don't know who you are"). They need a plain re-introduction, not a repeat of the pitch.
- **Unsubscribe or complaint:** handle it immediately. Mark the lead Do Not Contact and add the exact address to Smartlead's block list (the whole domain only if they asked for that). No prospect file and no reply. Honoring the request is the whole action.

A thread only ever gets **one** row and one category, even across several messages. Update the category as the thread develops (Interested becomes Hot once they ask for a call) instead of adding a second row.

## Moving replies into prospect files

The moment a reply is categorized **Interested, Hot or Yes to [offer]**, it gets its own prospect file. Research, drafts and next actions move there. The `Replies` file keeps only the verbatim reply as the source record, plus a link. Never edit an active draft in both places, because they will drift apart.

Where the prospect file lives depends on what the campaign sells. A simple rule is one `Prospects/` folder per niche when you sell your own services into a specific niche, and one shared `Prospects/` folder for campaigns that cut across niches. Give every prospect file a `type` and `status` field so a dashboard or database view can list all open prospects. An unfiled reply is invisible to that view, which is the whole reason this step exists.

## Building a free research deliverable

Many outbound offers lead with a free, prepared deliverable (a teardown, a lifecycle or monetization plan, an audit) sent once a prospect says yes. Build it only from live research on that prospect, never a templated write-up reused across leads.

**Screenshots are part of the research step, not a follow-up fix.** Capture a screenshot of every piece of evidence the deliverable cites (a review, a pricing page, an FAQ answer, a listing description) at the moment you find it. It's easy to build the deliverable text-only and only realize at the end that the evidence isn't shown.

Once captured:

1. **Save each screenshot alongside the prospect file** in an `attachments/[company-slug]/` folder, numbered with descriptive names (for example `02-reviews-not-free-cluster.jpg`), and embed each one in the deliverable section with a one-line caption.
2. **Keep a copy in a local folder** for pasting into whatever document you send (a Google Doc, Notion page or PDF), since some document APIs create text only and the images have to go in by hand.
3. **Put the deliverable's real URL** in the prospect file, both in the deliverable section and next to the drafted email, as soon as the document exists.

## Reply-check cadence (what actually catches misses)

Wire a reply-alert workflow (Smartlead webhook → n8n, Zapier or Make → email or Slack) as standard launch infrastructure for every campaign. Alerts can fail silently, though. A bug in the workflow can make Smartlead show the webhook as sent while no alert ever arrives. Treat the alert as a speed boost and never the only check. Do a manual pass through Smartlead's Master Inbox, filtered to the campaign, at each of these points regardless of alerts:

1. **At launch**, to confirm the alert actually fires on a real reply.
2. **Periodically while active.** Every few days is enough at normal volumes, and daily if a hot lead is mid-conversation.
3. **The moment Smartlead marks the campaign Completed.** This full reconciliation is mandatory. Compare Smartlead's reply count with the `Replies` file's row count. Any gap means something was missed, and this is the check that finds replies left behind on a campaign that finished days ago.

## Using it for a new campaign

1. When the campaign goes live in Smartlead, create `Replies — [Campaign Name]` in the campaign's folder with the structure above, even with a "0 replies so far" placeholder.
2. Wire the reply-alert workflow if it isn't already standing infrastructure for that sending identity.
3. On each reply-check pass, pull the current count from Smartlead's analytics, compare it with the file's row count, add any missing rows, categorize them, and move anything Interested, Hot or Yes-to-offer into its own prospect file.
4. Update the campaign hub's `last_touch_date` and add a one-line status note whenever the replies file changes materially, such as a new hot lead or a completed-campaign reconciliation. The hub needs to show current reality, not just send-side numbers.

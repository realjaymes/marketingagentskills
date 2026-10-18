# Sequencer Handoff and Sending Setup

Clay finds, enriches and verifies. A sequencer sends. This file covers the handoff from a Clay table to a sequencer, and the sending setup that decides whether the email lands. For authentication and reputation checks on a domain, use the domain-health skill if you have it. For copy and batch rules, see `sequence-and-copy.md`.

## Choosing where mail goes

| Path | Use it for |
|------|-----------|
| A sequencer on dedicated sending domains (Smartlead, Instantly, Lemlist) | Templated campaigns that reach tens or hundreds of people |
| Clay's own Sequencer (HubSpot Sequencer from 2026-01-16, sequencer forwarding from 2026-06-15, Sequencer in the plugin since 2026-09-15) | Campaigns managed inside Clay, written and reviewed with the plugin skills `campaigns`, `campaigns-sequence-writing` and `campaigns-sequence-reviewing` |
| A personal mailbox | One-to-one mail to a named person with a real finding, such as an application, a reply or a researched pitch |

Never send a templated batch from a personal mailbox. Its reputation is shared with every reply and application the owner sends, and a content-similarity classifier can file a clean reply in spam after one templated batch. Templated volume belongs on dedicated domains that carry a real list-unsubscribe header.

## Sending infrastructure

- Buy fresh secondary domains and inboxes. Never send cold mail from a primary domain, and for client work the client funds the domains and never loses the primary.
- Warm each inbox for two to three weeks before real sending.
- Verify Sender Policy Framework (SPF), DomainKeys Identified Mail (DKIM), Domain-based Message Authentication, Reporting and Conformance (DMARC) and mail exchange (MX) records with `dig` before the first send. A missing or failing record is a blocker.
- Send 10 emails per inbox per day on dedicated domains, ramping up gradually. Spread volume across every inbox in the pool.
- Schedule weekdays only, in the recipient's working hours.
- Do not track opens or link clicks. Send in plain text mode and measure replies.
- Test placement before a batch with a seed test to a mailbox you own, and use a spam-score checker such as mail-tester.com for the named rules that fired. Run it on the assembled message.
- A personal mailbox carrying one-to-one mail only: 5 sends a day while its reputation recovers, 8 to 10 after three clean placement tests. Cold mail as a share of the mailbox's normal volume matters more than the daily number, and a step change from near zero to a dozen in an afternoon is what a classifier reads. Order the queue so the likeliest repliers go first.
- Keep a kill switch. A single file or flag that blocks every send, whoever runs the batch, stops a mistake from compounding.
- Verify every address with an address-level checker before the send (see `prospecting-and-enrichment.md`). A bounce damages reputation, and the damage lands on the next batch. A tolerable bounce band is 2 to 5%. Pause a campaign above 5%.

## Variables and field mapping

- Clay writes one column per merge field (`greeting`, `gap`, `segment`, `company`, and so on). Map the columns to the sequencer's custom fields during import and check every one by hand. Auto-mapping can silently break a field so that it renders blank or wrong. Standard fields auto-map (`email`, `first_name`, `last_name`, `company_name`, `website`, `location`) and everything else arrives as a custom field.
- Smartlead's command-line interface imports a master comma-separated values (CSV) file with explicit mapping (`leads add-bulk`). Run `--dry-run` first to check the mapping before anything reaches the sequencer.
- Spintax uses single braces in Smartlead and works. Liquid conditionals use `{{#if var}}...{{else}}...{{/if}}`. A pipe fallback inside double braces does not work (see `sequence-and-copy.md`).
- In Lemlist, the Clay column mapping uses custom variables such as `subject1`, `email1`, `subject2` and `email2` (two fields per step). Lemlist supports Liquid and spin syntax. Create a dummy campaign with as many steps as the sequence, define the variables, and map the Clay columns on import. Leave the subject blank on follow-ups so they stay in the thread.
- Send one campaign and not one per variant. Use a Liquid conditional on a variant field so every lead receives a complete sequence under one set of sending limits and one reply inbox.
- Do not drop a lead for an unknown title. Drop only a positive not-a-buyer verdict.

## Campaign setup checklist

1. Map every custom field manually. Check each against the sequence copy.
2. Let the sequencer verify addresses after upload when it offers verification, and read its valid, accept-all, risky and invalid split before judging the list.
3. When pasting copy into the sequencer's editor, add a blank line after every line so the sent email matches the draft.
4. Only Email 1 and its variants carry a subject. Follow-ups thread as replies.
5. Preview every email and every variant with real lead data, using the sequencer's template preview and not the raw editor. Confirm nothing is blank, no raw `{{field}}` tag shows, and nothing reads garbled.
6. Select every inbox in the pool.
7. Set the time zone and a start date of the next day. A placeholder date left weeks out silently blocks every send.
8. Use plain text delivery to all providers.
9. Turn on automatic bounce protection and pause the campaign when the bounce rate exceeds 5%.
10. Stop on reply for the lead, and stop on reply for the whole company domain whenever a campaign has more than one contact per company.
11. Wire a reply webhook to an alert (a workflow that emails or posts to a channel). Check at launch that an alert fires, because alert workflows fail silently.

## Replies and measurement

- Read replies in the sequencer's inbox, categorize each (interested, hot, yes to a named offer, declined, false positive, confused, unsubscribe or complaint), and file anything real as its own prospect record. Handle unsubscribes at once: add to the do-not-contact list and the sequencer's block list.
- Reconcile at launch, periodically, and when the campaign completes: the sequencer's reply count against the reply log's row count.
- Measure reply, positive reply, call, opportunity. Reply rate is the first conversion event.

## Multi-channel steps

LinkedIn actions (profile visit, connection request) and phone tasks can sit in the sequence. Keep automated LinkedIn actions to about 20 a day per account, and use reply-based branch conditions because open tracking is off.

# Clay Sequencer and Campaigns

Clay's Sequencer sends email campaigns from inside Clay. "Campaigns" and "Sequencer" name the same product surface, and a sequence is the message flow inside a campaign. Facts come from Clay's official plugin skills `campaigns`, `campaigns-interview`, `campaigns-sequence-writing` and `campaigns-sequence-reviewing` (plugin version 2.33.0), Clay's University pages "Table-based campaigns" and "Sequencer FAQs and best practices", and Clay's pricing page, all checked 2026-10-18. Command names are in `clay-cli-commands.md`. Copy rules for this skill are in `sequence-and-copy.md`, and sending infrastructure for an outside sequencer is in `sequencer-handoff.md`.

## When to use Clay's Sequencer

Use it when the lead data already lives in Clay (a table or an Audience segment) and the team wants one tool for enrichment, copy and sending. Use an outside sequencer on dedicated, warmed domains when the team already runs one, needs more than four emails per lead, or wants its own deliverability controls. Clay sends through Smartlead infrastructure underneath, and each email address can connect to only one Smartlead account.

Plans that include the Sequencer: Launch, Growth and Enterprise (and legacy Explorer and Pro). Growth adds buying domains and inboxes for the Sequencer. Clay's pricing page and its FAQ disagree on whether Free includes it, so treat Free as not included until Clay's page says otherwise. Clay now recommends segment-based (People) campaigns for new work, and table-based campaigns remain supported. A table-based campaign is created from a table through Tools, Exports, Create Clay email sequence.

## Limits and costs (Clay's documentation)

- Up to four emails per lead per campaign. Each lead can be sequenced once per campaign. A campaign holds up to 500,000 leads, and enrollment is capped at 100,000 new sequence starts a day across the platform.
- Message text is capped at 8 KB per message. Plain text is the default. HTML unlocks formatting, open and click tracking and an unsubscribe link, and Clay warns that each adds deliverability risk for cold mail.
- Each lead enrolled costs 1 Action. Each AI snippet run costs 1 Action plus Data Credits that depend on the model. Relaunching a paused campaign does not charge leads already sequenced.
- Sending: Clay's default minimum gap between emails from one account is 20 minutes (a custom schedule can set 3 to 30). The "Optimized for deliverability" schedule runs Monday to Friday, 9 AM to 5 PM in the chosen time zone. "As fast as possible" sends around the clock within account limits. Steady state is about 20 emails a day per inbox with three inboxes per domain and five at most. A third-party summary and Clay documentation pull requests cite 30 a day for Clay-purchased inboxes and an adjustable 10 to 500 for self-connected inboxes, so read the cap in the Email accounts tab before planning volume. Add accounts instead of raising one account's limit. Clay documents no per-company daily cap, and the closest control is the setting that pauses leads at the same company when one replies.
- Warm-up: accounts bought in Clay take about three weeks to warm up and warm-up stays on. On accounts connected by the user, warm-up is opt-in. Personal Gmail and Hotmail accounts are not supported for OAuth, and Google Workspace OAuth needs admin approval.
- Out-of-office replies do not end a sequence unless the return date is more than 30 days away. Out-of-office replies count toward reply rate and not toward positive reply rate.
- Open and click tracking are not recommended for cold email, and replies are the metric to optimize. Events reach Clay within five minutes for 99% of sends on purchased accounts, and reply events can take 15 to 30 minutes to show in a campaign events table.
- Cooldown: set a cooldown window on every campaign and keep trigger cooldowns on. New campaigns have none by default. Wait a couple of months before sequencing the same person again, and only with a different offer.
- After launch, copy and step timing can be edited while paused, steps cannot be added, removed or reordered, and settings lock. Complete ends a campaign for good and freezes analytics.
- Spintax is not tracked as a test. Use an A/B variant test to learn which copy wins. AI snippet output is generated and frozen at enrollment, so later data changes do not touch leads already enrolled.
- Plaintext unsubscribe handling goes through the `Add email to blocklist` action or the Blocklist tab.

## What the CLI can and cannot do

The CLI can create a blank campaign, read settings, the audience, analytics and resolved AI context, edit settings and the sequence, run Clay's spam check, preview a saved variant for one sample lead (free) and send one test email (free, one real email). It cannot launch, pause, resume, complete or delete a campaign, replace its provider, or change a non-draft campaign's lead source. Those changes happen in the Campaigns screen in the Clay app. Clay's plugin treats these as hard boundaries and forbids working around them through other commands.

Reading and mutation rules from the plugin's `campaigns` skill:

- Resolve the target from a fresh `list` or `get`, state its exact name, make one mutation, then report from the response. Do not batch two mutations in one call.
- Show people readable placeholders (`[First name]`) and never campaign, step, variant or field ids. Keep raw tokens only inside the command.
- Before using a lead field in copy, run `clay campaigns audience <id>` and use the exact field id and label. `reliablyPopulated` describes only the sampled preview leads.
- Token grammar: `{{lead:<fieldId>|<label>}}` is required by default and a lead missing a required value is excluded from enrollment, while a non-empty `fallback` makes it optional. `{{sender.senderFirstName}}`, `senderFullName` and `senderSignature` fill sender details. `{{spintax:a|b}}` takes two to five unique variants. `{{ai:<snippetId>|<label>|<brief>}}` is an AI snippet.
- Body text is markdown, so a bracketed phrase with no following `(url)` fails validation. Separate paragraphs with a blank line.
- `addStep`, `deleteStep` and `reorder` need a draft campaign, and `updateStep` works on draft and paused campaigns. A subject or body edit on a non-baseline variant removes its link to the baseline, so check what will propagate before editing a linked field.
- A sequence with AI snippets runs one generation per lead for the whole snippet set. Keep a snippet's brief grounded, with the raw lead-field token inside the brief and a fallback that implies no research the data does not support.

## Clay's interview, writing and review method

Plugin skill `campaigns-interview` applies when a campaign has no real copy. It reads the campaign goal, the resolved AI context (workspace skills, My Business Context, attached files), the audience and the settings first, asks only about gaps that would change the draft, and states its assumptions. It proposes a goal only when the goal is empty or conflicts with the audience, and never replaces a non-empty goal without consent. In a non-draft campaign the settings are locked.

Plugin skill `campaigns-sequence-writing` sets these rules: one primary purpose and one response path per email, fix strategy before polishing lines, omit proof the context does not support, and give every follow-up a distinct reason to respond. For dynamic copy, use fixed text when the language is shared, a lead-field token when one value changes, spintax for variation that does not depend on lead facts, and a short bounded AI snippet only when useful lead data must be interpreted into natural prose. Never add a snippet to clear a personalization warning or to meet a quota.

Plugin skill `campaigns-sequence-reviewing` reviews copy as the recipient. It asks one question, "Why wouldn't I respond?", reviews strategy before execution, raises only material concerns, and stops when the remaining problem needs missing facts or a different offer. It reports those as Unresolved and does not rewrite around them. The draft, review and amend loop stays private. The user sees one concise update before each amendment and the final copy once.

## Where Clay's guidance differs from this skill's rules

This skill's rules in `sequence-and-copy.md` and `sequencer-handoff.md` are the default. Clay's guidance is context, and it never overrides them.

| Topic | Clay's guidance | This skill's default |
|-------|-----------------|----------------------|
| Who writes the email | The Sequencer holds the sequence text, and AI snippets can generate bounded parts per lead | Same division. Clay writes plain merge-field columns and each snippet or AI column writes one bounded field. Never generate a whole email in one call |
| Fallback syntax | Tokens with a `fallback` are valid in Clay's own Sequencer | Resolve every fallback into its own column, because other sequencers render pipe fallbacks blank. Use Clay's fallback tokens only inside Clay's Sequencer |
| Daily volume | About 20 a day per inbox, 3 inboxes per domain, 5 at most | 10 a day per inbox on dedicated warmed domains, ramping gradually. Use the lower number |
| Sequence length | Up to 4 emails | Three emails on days 0, 3 and 7 by default. A fourth is allowed in Clay when the offer needs it, and a fifth touch needs an outside sequencer |
| Word count and punctuation | No limit beyond 8 KB, and punctuation chosen for the recipient | Templated sends stay under 120 words, one ask, a plain closing line, no dashes in the prose |
| Subject lines | Per step, with subject edits allowed on new threads | Subject lines belong to Email 1 only, two to four plain lowercase words under 30 characters, two options |
| Personalization | Per-lead AI snippets are encouraged where they help relevance | A snippet is allowed only when it is grounded in a signal the team chose, tested on 10 rows and checked for the empty case. Batch checks still apply (no sentence shared by more than a quarter of companies) |
| Tracking | Off by default for cold email | Off, always. Measure replies |
| Deliverability checks | Clay's `spam-check` is a copy-quality signal and not a delivery guarantee | Also run a seed test and authentication checks before a batch, and read the bounce rate. Pause above 5% |
| Time window | Weekdays 9 AM to 5 PM in the chosen time zone | Recipient's local morning, lunch or late afternoon, Tuesday to Thursday first, no Friday afternoons |
| Reply handling | Out-of-office replies tagged neutral. Stop the sequence on reply | Same, plus stop on reply for the whole company domain and file every real reply as a prospect record |

## Checklist for a Clay Sequencer campaign

1. Confirm the workspace, the plan and the connected sender accounts (`clay campaigns options sender-accounts`).
2. Resolve the audience and check each lead field the copy uses.
3. Write the sequence under the copy rules in `sequence-and-copy.md`, then review it from the recipient's seat.
4. Run `spam-check` on each variant and preview with at least three real leads, including one with missing data.
5. Send one test email only on the user's explicit request to an address the user names.
6. Launch in the Clay app. The CLI cannot do it. State the daily limits, the cooldown window and the expected spend (1 Action per lead) before the user launches.
7. After launch, read `clay campaigns analytics <id>` for replies and `list --with-analytics` to compare campaigns.

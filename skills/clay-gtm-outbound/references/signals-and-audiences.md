# Signals and Audiences in Clay

A signal watches a set of records and writes an event when something changes in the real world: a job change, a promotion, a funding round, a job posting, a new topic of interest. Signals decide when to write. The ideal customer profile (ICP) decides whom to write to. Clay's plugin skill `signals` is the authority on commands and current limits, so read it before creating or changing a signal.

## The four signal categories

| Category | What it means | Examples | Timing |
|----------|---------------|----------|--------|
| Intent | The company is researching your category | Visits to competitor pages, content downloads, Web Intent (2025-11-26) | Late. They are probably comparing vendors already |
| Growth | The company is scaling | Funding, aggressive hiring, new offices, traffic increases | Early. New budget and new needs |
| Change | A transition reopens vendor decisions | New CMO, CTO or VP, a technology migration, a restructure, a new business line | Early. The new owner has no vendor loyalty yet |
| Distress | A visible problem creates urgency | Reviews that name a pain point, compliance failures, public vendor complaints, outages | Immediate, and the most sensitive to write about |

Rank candidate signals on two axes: how often the signal fires in your market, and how often it leads to a sale. Build the ones that score high on both first.

## Signal types

The CLI knows these types (plugin skill `signals`, plugin version 2.33.0, checked 2026-10-18).

| Type | Fires when | Watches by | Billing |
|------|-----------|------------|---------|
| `JobChange` | A tracked person's employer changes | Person LinkedIn URL | Per record checked |
| `Promotion` | A tracked person's title advances at the same company | Person LinkedIn URL | Per record checked |
| `NewHire` | A tracked company hires someone matching your criteria | Company identifier | Per record checked |
| `JobPost` | A tracked company opens a posting matching your filters | Company identifier | Per record checked |
| `News` | A tracked company appears in news, including funding rounds | Company identifier | Per result emitted |
| `PersonTopicIntent` and `CompanyTopicIntent` | A tracked person or company researches your topics | LinkedIn URL or company identifier | Per record checked, multiplied by each provider's selected topics |
| `Custom` | An enrichment you configure returns a change | Any action output | Per result emitted. Built in the app only |
| `WebsiteVisitorTracking` (web intent) | A de-anonymized visit hits your site | A tracking script | Built and managed in the app only |
| `LinkedinPostMentions` | Discontinued | | A workspace may still hold old ones, and new brand-mention signals are not possible |

Start with the built-in types for the common triggers, and build a `Custom` signal in the app only when no type carries the data point you need. Fundraising is a `News` topic and has no type of its own.

## Where signals live now

- The Signals hub lists every signal with its status, schedule, credit use and results. A signal can also be started from a table (Actions) or from a new workbook.
- A table-based signal writes events into a destination table. An Audiences-based signal writes each event back onto the person or company as a signal activity, and the derived `signal_summary` field shows them. Nothing appears in a table for an Audiences signal. For existing records, query the events already captured before creating a watch (`clay audiences signals get|summary`, or the `signals.<type>.exists(...)` clause in an Audiences query). An empty trigger list or `signal_summary` does not prove that no events were captured.
- In the command-line interface (CLI), `id` in `clay signals` output is the trigger definition (`td_...`), the only id the commands accept. The underlying watch is `sig_...`. The Audiences event commands and the Workflow `audience_signal` trigger use that one. Commands: `list`, `get`, `create`, `update`, `pause`, `resume`, `delete` and `search-topics`.
- A created signal starts Paused and neither runs nor spends until `resume` (or `create --activate`). Read it back, confirm what it watches, then resume.
- Pausing stops running and spending and is reversible, so pause before deleting. Deleting keeps the captured events but loses the baseline.
- What a signal watches (table, view, identifier field) is fixed at creation. Changing it means a new signal. Name, schedule and event filter can always change.
- Check for a duplicate before creating one, because two signals over the same records are each charged in full.
- Job change and promotion signals start with a default event filter of `confidence >= 90`. That can make a healthy signal look quiet. A signal that detects changes only sees changes after monitoring starts, apart from a one-time lookback at setup (three months for job change).
- A person-based signal tracks the LinkedIn URL on each record. A record with a missing or stale URL is silently not monitored, so measure fill rate on the watched view or segment first (`search-count` with a `NotEmpty` filter on the identifier).
- An Audience signal with a credit limit pauses itself when the limit is used up and stays paused until someone resumes it. Do not promise it restarts next cycle.
- Topic intent signals fix their provider set at creation, and `topicIds` come from `clay signals search-topics`. Never guess or copy ids. A provider config with no topics watches every topic and bills for each.
- Clay's Audiences and Sequencer work together: a signal event can enrol a contact in a campaign through a Workflow (plugin skill `workflows-campaign-enrollment`). Plugin skill `workflows` explains how to pick between a signal trigger and a segment trigger, which are not interchangeable.

### Pricing a signal

Per-record types charge for every record examined on every run, whether or not an event appears. Size one as records in the watched set times runs per month, and narrow the watched set before slowing the cadence. Per-result types charge for events, so a large quiet audience costs little and a small noisy one costs more. The CLI has no cost, health or test command, so diagnose a silent signal from `get` in this order: `runStatus` (only Active and Preview run), the event `filter`, the `error`, the `schedule` and last run, then where the output goes.

## Setting up the common signals

Job change. Monitor champions who have bought before, decision-makers at target accounts and competitors' customers. Required fields: the LinkedIn profile URL (find it first with an enrichment if missing) and the company domain or company LinkedIn URL. The company field lets Clay tell a move to a new company from a promotion at the same one.

New hire. Set company size, title keywords, locations and a time window. Keep the window tight enough to be fresh and wide enough not to miss hires. Give it company domains or LinkedIn company URLs from your ICP list only, because every extra account adds noise and cost.

Job postings. A posting says what a company plans to build or buy. Read the role, not only the title. Sales and marketing hiring signals budget and growth. Technical roles signal technology plans.

Add enrichments to the signal output so an alert arrives ready to act on: a contact email and phone, company enrichments (stack, funding, headcount) and AI research on the company's site and recent news. Gate each added step with a run condition so only qualified events spend credits.

## Routing the output

Options: a new table per signal type (easy to measure by type), rows added to an existing table, a Slack alert (add a human approval for sends), a webhook, or a CRM push. Run frequency trades speed against credits. Run job changes and critical accounts daily. Run slow-moving signals weekly.

## Rules for using a signal in outreach

- Collect broad and decide narrow. Detect every applicable signal per lead, then summarise which signals are present and how common each is across the batch. Pick the signal that leads the message after reviewing the options, and not before. Letting the first signal found become the default angle closes off messages another signal would have opened.
- Stack signals for intent. A funded company with a matching hiring pattern and a recent leadership change is a stronger reason to write than any one of them alone. Track the timing between signals, because the gap between two events tells you how fast the account is moving.
- A signal is a reason to write and not a diagnosis. Phrase the observation as an opportunity ("you would normally...") and never as criticism ("you are failing at...").
- Never pitch a hiring company the work its open role owns. A paid-media role owns paid gaps, a content role owns content and search gaps, a sales or go-to-market (GTM) engineering role owns outbound gaps, and a broad growth role owns most of them. The hire is the budget signal. Pitch a different service, evidenced on their live pages.
- Re-read the live page before the claim goes into copy and again before any deliverable built on it. Homepages change, and a claim built on a scraped hero can be stale within weeks.
- Distress signals about named companies or people need extra care. Quote only what is public and verifiable, such as a review the person posted on a public page.

## Audiences as account data

Audiences hold the workspace's own people, companies and deals. They can be fed from Salesforce (including Opportunities, 2026-04-20, and Salesforce Object Query Language imports, 2026-08-17), HubSpot Deals, BigQuery, Snowflake, Attio and comma-separated values (CSV) imports, with lookalike generation (2026-06-15), a sources and exports view on All people and All companies (2026-10-12) and a Reporting view that follows Clay-sourced accounts from pipeline to closed-won revenue (2026-08-03). An audience (saved segment) is a named filter that selects records live, so membership moves as records change. Deals are read-only.

How to work with them (plugin skill `audiences`):

- Reading is free and fast, so start here for any question about the workspace's own records. Count with `clay audiences records search-count --query 'count from people where email is_not_null'`, fetch ids with `search-ids --query 'select from companies where ...'`, and hydrate with `records get` (at most 100 ids per call). A top-N question ranks server-side with `order by` and a small `--limit`.
- Use one spelling per surface: the CLI flag takes `people`, `companies` or `deals`, a filter or action takes `CONTACT` or `ACCOUNT`, and the query language roots are `people`, `companies` and `opportunities`.
- Discover categorical values with `fields list-values` before filtering, and check fill rate with a `is_not_null` count before proposing an enrichment.
- Prefer dynamic segments. Keep a fixed cohort for when the user asks for one. A segment's `update` replaces the whole filter.
- Rate limits are per command and per workspace (60 calls a minute by default), and `records get` carries a second hourly budget of 100,000 record ids. Budget a full walk with `search-count` first, and narrow the scope or label the answer a sample instead of grinding through it.
- The CLI cannot write a field value onto a record. A Workflow does that with the `upsert-audiences-record` action.
- Default field ids: people `name`, `first_name`, `last_name`, `email`, `linkedin_url`, `phone`, `title`, `signal_summary`. Companies `org_name`, `domain`, `headquarters_location`, `linkedin_url`, `sfdc_owner_id`, `signal_summary`, `technographics`. Other fields are workspace-defined, so list them and never guess an id from a display name.
- Use Audiences as the account list for named-account work and to suppress existing customers before outbound. A Search can exclude the whole Audiences dataset with `@audience_segment("ALL")`.
- The connector's `query-objects` and `ask-question-about-accounts` tools read Audiences data and need that data and CRM owner data to be present.

## Account-based marketing (ABM) workflow

A three-table design still works, and Audiences can replace the first table:

1. Named account list with contacts, imported from the CRM on a schedule, carrying the ABM stage and a contact grade.
2. A mention or intent table that monitors domain mentions daily, classifies each post with AI and scores engagement.
3. A lookup and stage-update table that cross-references mentions with the account list, updates stages from engagement and writes the change back to the CRM.

Stages: Aware (build the relationship), Interested (nurture curiosity), Evaluating (high-touch tactics to close).

Clay Ads (plugin skill `ad-syncs`, Ads in the stable CLI since 2026-10-05) pushes an Audience segment to LinkedIn, Meta, Google, Bing, Reddit or Vibe as a custom audience. Company syncs go to LinkedIn only. A segment can have one ad sync. A sync is ONE_TIME or RECURRING, and a recurring company sync now runs every 7 days while people syncs run every 3 days (CLI 1.10.0 release notes, 2026-10-15). The enrichment tier (PREMIUM or STANDARD, people syncs only) costs credits and cannot change once set. The CLI creates and edits drafts and paused syncs, and the user starts or resumes a sync in the Clay app. Audience size and match rate follow each platform's own reporting (2026-10-12), and `runs list` needs `--limit 100` to show every destination's latest run. Earlier releases added exclusion lists, retargeting and lookalikes (2026-02-25) and LinkedIn syncs (2026-09-28).

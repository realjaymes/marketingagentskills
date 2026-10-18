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

## Default and custom signals

Default signals are pre-built monitors for common triggers: career movements (job changes, new hires, promotions), news and fundraising, job postings, LinkedIn brand mentions and website intent. Custom signals combine a scheduled source, AI analysis and a condition to watch anything Clay can enrich: technology changes, certifications, geographic expansion, website content changes, social activity, filings and engineering activity.

Start with default signals for the common triggers. Build a custom signal only when no default carries the data point you need.

## Where signals live now

- The Signals hub lists every signal in the workspace with its status, schedule, credit use and results. A signal can also be started from inside a table (Actions) or from a new workbook.
- Signals write their events onto a table or onto an Audience. Audiences are the workspace's own people, companies and deals, imported from a customer relationship management (CRM) system, a warehouse or a comma-separated values (CSV) file, and Audiences have their own signal runs (see the release table in `clay-interfaces-and-releases.md`). For existing records, query the events already captured before creating a new watch. An empty trigger list does not prove that no events were captured.
- In the plugin's command-line interface (CLI), `id` in `clay signals` output is the trigger definition (`td_...`), and it is the only id the commands accept. The commands are `list`, `get`, `create`, `update`, `pause`, `resume`, `delete` and `search-topics` (to find topic ids for a topic-intent signal).
- Pausing a signal stops it running and stops it spending. Deleting one keeps the events it captured.
- Web Intent is outside the plugin's `signals` skill. Read that skill's limitations section before telling someone a change cannot be made through the CLI.
- Clay's Audiences and Sequencer work together: a signal event can enrol a contact in a campaign through a Workflow (plugin skill `workflows-campaign-enrollment`).

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

Audiences hold the workspace's own records and can be fed from Salesforce (including Opportunities, 2026-04-20), HubSpot Deals, BigQuery, Attio and CSV imports, with lookalike generation (2026-06-15) and a sources and exports view (2026-10-12). The connector's `query-objects` and `ask-question-about-accounts` tools read Audiences data, and they need that data and CRM owner data to be present. Use Audiences as the account list for named-account work and for suppressing existing customers before outbound.

## Account-based marketing (ABM) workflow

A three-table design still works, and Audiences can replace the first table:

1. Named account list with contacts, imported from the CRM on a schedule, carrying the ABM stage and a contact grade.
2. A mention or intent table that monitors domain mentions daily, classifies each post with AI and scores engagement.
3. A lookup and stage-update table that cross-references mentions with the account list, updates stages from engagement and writes the change back to the CRM.

Stages: Aware (build the relationship), Interested (nurture curiosity), Evaluating (high-touch tactics to close).

Clay Ads can sync Audience segments to LinkedIn and Meta as exclusion lists, retargeting audiences and lookalikes (2026-02-25) and as LinkedIn syncs (2026-09-28). Plugin skill `ad-syncs` covers the commands.

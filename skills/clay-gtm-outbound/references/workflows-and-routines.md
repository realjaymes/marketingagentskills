# Workflows, Routines, Searches, Schedules and the Public API

This file covers the Clay surfaces that run outside a table: Routines, Workflows, Searches, Schedules and the Public application programming interface (API). Facts come from Clay's official plugin (version 2.33.0), Clay's developer documentation and the Sculpt 2026 recap, all checked 2026-10-18. Command names and safety classes are in `clay-cli-commands.md`. Read a plugin skill's `SKILL.md` before running it, because the plugin skills carry the full rules.

## Which surface to reach for

Clay's plugin gives an escalation order for any task. Take the earliest option that fits.

1. Audiences (plugin skill `audiences`): questions about the workspace's own people, companies and deals. Reading is free, and searching or enriching first would spend credits to rediscover data the workspace already holds.
2. Searches (skill `searches`): net-new people or companies from Clay's database.
3. Routines (skill `routines`): run a saved Clay-managed function, custom function or Workflow.
4. Workflows (skill `workflows`): build a new automation only when no routine fits. Clay names the reasons as embedded custom code, batches over 100,000 rows, step-by-step run inspection, and inputs stitched from several sources.
5. Tables (skill `tables-cli`): read an existing table the user names. The CLI cannot create one.

## Routines

A routine is a saved function or Workflow that already exists in the workspace and can be run asynchronously.

- Clay-managed functions (`source: managed`) cover standard enrichment such as work email, company domain, enrich person, job openings, latest funding and technology stack. They are the first choice. Match a routine by its input schema and not by its name. The managed Work Email function, for example, needs full name, company name and company domain, so resolve the domain first with the managed Company Domain function.
- Custom functions carry team-specific logic and cannot be built from the CLI. The CLI can only run them and wrap them as routines.
- An inline run takes 1 to 100 items. A bulk run takes a JSONL file (one `{ "id", "inputs" }` object per line). Clay's documentation describes a 50,000 row cap on runs that Workflows avoid.
- Every response carries `mode: inline` or `mode: bulk`. A finished bulk run returns a `resultUrl` that lives for minutes, and results stay retrievable for about a day.
- `clay routines get <id>` returns `estimatedCreditCost`. Workflow estimates count each node once, so they can miss branching and per-item repeats. `containsVariablePricing: false` does not prove the total is complete. Treat the number as a floor.
- Call the plugin skill `routines` for the run flow.

## Workflows

Clay describes Workflows as an orchestration platform for automations that run on triggers or schedules. Status is stated differently in different places. Clay's Sculpt 2026 recap (2026-10-08) says beta now for all Clay users with a full launch planned for fall 2026. Clay's developer documentation still labels them Alpha. Pricing for Workflows was not stated in either place.

**When a Workflow beats a table.** Use a Workflow for unattended or triggered work (inbound lead routing, scoring and assignment, signal handling, scheduled enrichment), for flows with branches or code, for runs above 50,000 rows and for anything where per-run observability matters. Use a table for exploration, one-off pulls and first prototypes. A table cannot be migrated automatically. Rebuild its logic and leave the data where it is. Search is not yet a supported Workflow source, so send a search to Audiences and act on it from a Workflow, or use a Find leads trigger. Plugin skill: `workflows-vs-tables`.

**Node types.** Agent (a Claygent that reasons, drafts or classifies), tool (one Clay action or function), conditional (rules, agentic or code mode, with a mandatory default route), code (Python standard library only, no network, stopped after 1 second), merge (coalesce fallback values from converging branches) and delay (1 to 86,400 seconds). Map, reduce and collect nodes are retired. For per-record work over a list, turn on list mode (the Repeat toggle). It runs the node once per item. Published Workflow functions can be called as nodes.

**Triggers.** Signals, Audience segments (live or scheduled, with an optional batch size so each pass processes the next batch only), schedules, webhooks, CSV uploads, Find leads searches and Clay tables (wired from inside the table only). One trigger can have at most one direct outgoing edge. A webhook takes a JSON object, and a top-level array lands under `payload`. For a signal trigger, bind to the underlying `sig_...` id and not to the `td_...` trigger definition id.

**Draft and live.** Edits change the draft. `clay workflows publish` makes the draft a numbered live version and activates triggers. Restoring a snapshot changes the draft only. A Find leads trigger always runs the published version. Test runs use the draft unless `--live` is passed.

**Testing and recovery.**
- Test on a small set first. Each trigger's test dataset holds up to 50 rows (`clay workflows test-data`).
- Where enabled, Free and trial workspaces have a lifetime allowance of 100 runs per workflow. Paid plans do not. Successful and unfinished runs count, and failed and cancelled runs do not.
- To recover failed runs, use `clay workflows runs rerun` (CLI 1.10.0 or later). It restarts each run at the node that failed. Run `--dry-run` first and read `rerunCount` and `estimatedCredits`. The estimate counts a repeating node once, so the real cost can be much higher. Re-runs use the published version, so publish a fix first. The `--from node` and `--from trigger` modes repeat steps that already succeeded, including emails and CRM writes.
- Never use `nodes test` to recover runs. It runs one node and ends the run, so every later node is skipped while the run reports completed.
- The runs dashboard has a bulk re-run that shows the run count and estimated credits before it starts and deduplicates by record (2026-10-05).

**Observability.** `clay workflows analysis` answers where runs fail, which node costs most and what a step really received. Start with `traffic`, then `aggregate`, then `steps`. Every run pins the snapshot it started on, so default to the latest version that has run when diagnosing current behavior. Snapshots (`clay workflows snapshots`) are the undo history, and `clay workflows versions list` is the complete index of published versions.

**Cost levers.** Plugin skill `workflows-optimize-credits` reviews a Workflow. The main levers are code nodes in place of model nodes for deterministic work, smaller models for extraction and classification, merging sequential model nodes, pre-mapping action inputs so the model call that maps parameters is skipped, conditionals that skip enrichment for records that do not need it, and a code node ahead of a repeating node that drops items needing no work. Skill `workflows-simplify` applies the same checks for reliability. Workflow credit budgets (admin setting, 2026-10-05) cap what automated runs spend, and `clay budgets list` reads them.

**Discovering actions.** Plugin skill `workflows-discover-actions`: search the live catalog (`clay workflows actions search "<capability>"`), inspect the schema, prefer a Clay waterfall function over a single provider, and check `requiresApiKey` before asking for a connection. Catalog `creditCost` is a base price, and a missing price means unknown and not free.

**Claygent nodes.** Plugin skill `workflows-claygent`. Put every prompt variable in the node's input schema, give every output field a description, test on one record, then bound the full run. Account agents (agents with account context from Audiences) are the default for research, scoring and personalized outreach under an Audiences trigger. One agent with several output tasks beats a chain of agents.

**Audience enrichment.** Plugin skill `workflows-audience-enrichment`. The shape is: save an Audience of records missing a field, trigger a Workflow on it, enrich, and write back with the `upsert-audiences-record` action. Run `clay workflows ensure-audience-writeback` instead of hand-wiring the final write. Test 10 segment records on the draft (`--audience-segment <id> --limit 10`) before publishing.

**Inbound lead routing.** Plugin skill `workflows-inbound-lead-routing`. The standard path is webhook trigger, enrichment, a scoring code node, conditional tiers, then route (rep alert in Slack or a CRM task, a sequence, or a disqualified branch). Establish the CRM, the scoring model, the rep notification channel, the sequencer and the disqualification handling before building.

**Campaign enrollment.** Plugin skill `workflows-campaign-enrollment`. The `enroll-lead-in-sequence` action enrols one Audiences person in one campaign, and a successful run sends a real email, so get an explicit go before publishing or test-running it. The campaign id must be a static value from `actions dynamic-fields`, and only active campaigns that take leads from a Workflow appear. A person created by an upstream upsert has no linked account yet, so company merge fields render blank on that first enrollment. Two failure codes (`provider_result_indeterminate` and `enrollment_persistence_unavailable`) mean the person may already be enrolled, so do not retry them.

## Searches

Plugin skill `searches`. A search is a forward-only iterator: read the query reference, create the search, then run it page by page. There is no cursor, so a page cannot be replayed. Rules worth keeping:

- Exclude what the workspace already has with `@audience_segment("ALL")` inside `clay.exclude_people_identifiers(...)` or `clay.exclude_company_identifiers(...)`.
- Searches return people or companies only. Job criteria are nested filters (`jobs.exists(...)`, `company.jobs.any(...)`).
- When a criterion is not a native filter, search on the nearest filters and send the results through a routine that enriches or scores the missing attribute.
- Before a generic, large search, narrow it first (size, title and seniority, open roles, technology, named domains or a small `limit`).
- Stop and ask before a pull that would leave under 15% of the period quota. `quota_exceeded` is a plan limit and not a transient fault, so do not retry. Only a per-request cap allows one retry with a smaller `--limit`.
- The Free plan allows 100 results per rolling 30 days, so a Free workspace cannot run a real prospecting search.
- NAICS code filtering for companies shipped on 2026-08-31, and Advanced Search (companies, people and jobs in one query, with OR filters) reached the Clay connector on 2026-09-07.
- Clay does not offer X (formerly Twitter) data sourcing, scraping or enrichment.

## Schedules

Plugin skill `schedules`. A schedule runs Clay's GTM Agent on a cadence, and each occurrence starts a fresh agent task with the schedule's prompt, so the prompt must stand alone. The limits are at most once a day, at most 20 schedules per workspace (pausing does not free a slot) and a prompt of at most 4,000 characters. Write the prompt as Objective, Goal and Instructions, keep cadence out of the prompt and in `scheduleConfig`, and name every Audience, field and Workflow by id. A goal that can be measured should name the measure (`clay audiences records search-count`, `activities summary` or `signals summary`). An occurrence runs only while the GTM Agent is enabled and the creator is still a workspace editor. Schedules are distinct from Workflow schedule triggers.

## Public API

Plugin skill `public-api`. Base address `https://api.clay.com/public/v0`, authenticated by a dedicated key from `clay api-keys create` (shown once). It offers Searches, structured table queries (Enterprise) and asynchronous routine and batch runs, plus a workflow-run query (beta). Rate limits are per workspace, and a 429 carries `Retry-After`. The documentation does not publish the numbers. Use the CLI for one-off agent tasks and the API for services that call Clay. Full reference: https://developers.clay.com/llms.txt.

## Cost and confirmation policy from Clay's plugin

Clay's plugin applies this policy to every paid step, and it fits the go rule in this skill.

- Keep Data Credits, Actions, search quota and model spend separate.
- Ask before an operation that would use at least 10% of the remaining Data Credit balance, for the whole intended run and not per page.
- Before a run over 100 records, run about 10 first, report the results, then ask about the rest. Use fewer when each record is expensive.
- Only quote a number a tool returned. Catalog base prices are not configured-run prices, and missing pricing means unknown.
- When an estimate is incomplete, probe one record, then run in chunks small enough that a several-fold miss stays inside the approved spend.
- Runs held for approval (`approval_required`) are decided with `clay approvals`, and only the user's own answer approves.

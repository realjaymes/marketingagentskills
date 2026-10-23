# Clay Interfaces, Limits and Releases

Facts in this file were checked on 2026-10-18 against Clay's changelog, blog and documentation, Clay's official plugin repository (files on disk and commit history), the installed command-line interface (CLI) and the live connector. Items marked UNVERIFIED rest on one third-party source or on a page that did not show the detail. Clay ships weekly, so re-check anything that decides a purchase or a build.

## The four ways to work with Clay

| Interface | What it does | What it cannot do |
|-----------|--------------|-------------------|
| Clay app (human or Chrome automation) | Everything: create and edit tables, columns, run conditions, runs, Functions, Audiences, Workflows, Signals, and launch campaigns | Chrome automation is slower and breaks more easily than the CLI |
| Official plugin and `clay` CLI | Read tables (structure, rows, cell status), run ClayQL queries, build and edit Workflows, run Searches, routines and Functions, manage Signals, Audiences, ad syncs, campaigns, schedules and credits | Create tables or columns, write cells, insert rows, trigger enrichments on a table, launch or pause a campaign, create a Function |
| Clay connector in claude.ai (Model Context Protocol, MCP) | Search companies and people, enrich with named data points, run the workspace's Functions, query Audiences, ask questions about accounts | List, read, create or edit tables, workbooks, columns or runs |
| Clay public application programming interface (API) | Searches, structured table queries (Enterprise), routine and batch runs, workflow-run queries (beta) | Same read limits as the CLI for tables |

Command names, flags and safety classes are in `clay-cli-commands.md`.

## The official plugin and CLI

- Clay announced the API and CLI on 2026-07-09 (open beta, no added cost) and the Agent Plugin for Claude Code, Codex and Cursor on 2026-09-15. The CLI reached 1.0.0 with plugin 2.23.0 on 2026-09-15.
- State on 2026-10-18: plugin version 2.33.0 (commit `b9952b6`, 2026-10-15) with a minimum CLI of 1.9.0, and Clay's latest CLI release is 1.10.0 (2026-10-15). Releases arrive almost daily, and the plugin's release commits are the changelog. CLI release notes are at https://github.com/clay-run/agent-plugins/releases.
- Install in Claude Code (version 2.1.91 or later): `/plugin marketplace add clay-run/agent-plugins`, then `/plugin install clay@clay-plugins`. The CLI installs on its own, by default as a native binary at `~/.local/bin/clay` (or through npm as `@clay-run/cli` where Node is required), and `clay update` updates it. Run the plugin's `setup` skill, then `clay login` (or `clay login --device` in a headless shell).
- Inside the Clay app's own managed sessions, `clay login`, `logout`, `update`, `workspaces` and the `setup` and `update` skills are unavailable, and the session is fixed to one workspace.
- The plugin has no MCP server of its own. Its manifests (Claude Code, Codex and Cursor) declare skills and hooks only, and its `clay` skill tells the agent to ignore a separately connected `clay-for-reps` connector. Clay's July blog wording about bundling MCP refers to Clay's whole developer offering and not to files in this plugin.
- Its hooks do two things. A session-start check reads `cli-min-version` and reports a missing or old CLI. A pre-tool hook auto-approves plain `clay` calls (optionally piped through `jq`, `grep` and similar read-only helpers) except `feedback`, `login`, `logout`, `api-keys`, `webhooks` and `credits top-up`. Read the plugin's `SKILL.md` files before enabling it.
- Clay says every plugin action is recorded in its audit trail and the data stays on Clay's platform.
- Table limits: `clay tables query` (joins and paging) needs Enterprise API table sync. Without it the call returns `auth_forbidden`, an account limit. `query-live` (ClayQL) needs no sync and returns at most 100 rows per call.

### Plugin skills (35 in version 2.33.0)

| Skill | Use it to | Reference file here |
|-------|-----------|---------------------|
| `clay` | Start here. Index of surfaces and the escalation order (Audiences, Searches, Routines, Workflows, Tables) | `workflows-and-routines.md` |
| `setup`, `update`, `onboard` | Install, sign in, update, first-run tour | This file |
| `cli`, `public-api`, `clay-docs`, `clay-feedback` | CLI conventions, HTTP access, answering product questions from live Clay documentation, bug reports | `clay-cli-commands.md` |
| `tables-cli`, `tables-analyze`, `tables-trace`, `tables-value-trace`, `tables-error-sweep`, `tables-capacity` | Read, audit and debug a table | `table-audit-and-debug.md` |
| `credits-quotas-plans` | Balance, plan limits, top-ups | `credits-and-cost-control.md` |
| `workflows`, `workflows-vs-tables`, `workflows-claygent`, `workflows-optimize-credits`, `workflows-simplify`, `workflows-snapshots`, `workflows-discover-actions`, `workflows-campaign-enrollment`, `workflows-inbound-lead-routing`, `workflows-audience-enrichment` | Build, review and cost-check Workflows | `workflows-and-routines.md` |
| `routines`, `searches`, `schedules` | Run functions, find net-new records, recurring agent prompts | `workflows-and-routines.md` |
| `signals`, `audiences`, `ad-syncs` | Watches, the workspace's own records, and pushing segments to ad platforms | `signals-and-audiences.md` |
| `campaigns`, `campaigns-interview`, `campaigns-sequence-writing`, `campaigns-sequence-reviewing` | Clay Sequencer campaigns and copy | `sequencer-and-campaigns.md` |

## The connector in claude.ai

- Clay launched "Clay in Claude" on 2026-01-26. New connections receive 500 free credits. Version 2 shipped in the week of 2026-03-23 with custom Functions that an operations lead builds and reps run in chat, per-rep access toggles ("Enable for MCP"), and a global plus per-rep credit budget on an "MCP Users" settings page. Advanced Search (companies, people and jobs in one query, with cross-entity and OR filters) reached the connector in the week of 2026-08-31. If the new tools do not show, reconnect the connector, because the assistant may cache tool definitions. Clickable links in connector results shipped in the week of 2026-08-24.
- Tools: `search-companies`, `search-contacts`, `search-contacts-by-name`, `load-more-search-results`, `add-company-data-points`, `add-contact-data-points`, `get-task`, `get-task-context`, `list_subroutines`, `run_subroutine`, `run_subroutine_direct`, `query-objects`, `ask-question-about-accounts`, `get-current-workspace`.
- `run_subroutine_direct` takes up to 1,000 input sets and each set consumes credits. `query-objects` returns at most 100 records per call and depends on Audiences data. `ask-question-about-accounts` answers across 1 to 10 accounts.
- The connection is pinned to one workspace. Call `get-current-workspace` and confirm the workspace id before any enrichment. Clay's guide does not say how access is scoped across workspaces (UNVERIFIED beyond the pin).
- In a terminal host such as Claude Code the result widget does not render, so call `get-task-context` to read enrichment results.
- Clay's guide scopes the connector to rep-scale work, roughly 1 to 20 contacts, and sends larger volume and deep customer relationship management (CRM) syncs to the Clay app. Enrichment through the connector costs the same credits as in the app.
- UNVERIFIED (one competitor review): search is free, a role limited to the connector cannot view tables in the app, writing to a sequencer needs an operations-built Function, there is no published rate limit, and an interaction costs 20 to 100 credits.
- UNVERIFIED: the endpoint address. A search snippet gave `https://api.clay.com/v3/mcp`, and Clay's MCP guide page does not state any address. Use the connector's own sign-in and do not hand-configure an endpoint.
- The connector also works in OpenAI Codex (2026-06-02) and ChatGPT (2026-01-16).

## Plans and credits

Clay's own pricing page and credits documentation are the source for plans, allowances, rollover and top-ups, and `credits-and-cost-control.md` carries the figures with their sources. In short: Free, Launch ($167 a month billed annually or $185 monthly), Growth ($446 or $495) and Enterprise since March 2026, with Data Credits and Actions as the two meters. Actions have no top-up. Launch and Growth have usage tiers above the entry allowance. Clay's page and FAQ conflict in places, so confirm in the app before quoting.

## Releases since July 2025

Source for every row: https://www.clay.com/changelog and its roundup pages, unless a row names another.

| Date | Release |
|------|---------|
| 2025-07-03 | Natural language company search, Ad Intel, The Org |
| 2025-07-21 | Slack approvals for enrichments, visual workflow builder |
| 2025-08-26 | Claygent Navigator, metaprompter-built AI columns |
| 2025-11-26 | Bulk enrichment, Web Intent |
| 2025-12-12 | Sumble technographics, Gong Engage actions, exact match search |
| 2026-01-16 | Clay in ChatGPT, HubSpot Sequencer, Gemini 3 Pro, credit dashboards |
| 2026-01-26 | Clay in Claude |
| 2026-01-30 | Credit limits and warnings, HyperText Transfer Protocol (HTTP) API source, saved searches, Salesforce Object Query Language (SOQL) source |
| 2026-02-25 | Ads: exclusion lists, retargeting, lookalikes (LinkedIn and Meta) |
| 2026-03 | Pricing overhaul: Free, Launch, Growth, Enterprise; Data Credits and Actions |
| 2026-03-23 | Table Versioning and Changelog (see who changed what, restore) |
| 2026-03-27 | Delay Runs (up to 10 minutes before an enrichment runs) |
| 2026-03-30 | Clay in Claude and ChatGPT version 2, Sculptor for search, email waterfall controls |
| 2026-04-15 | Functions: reusable logic across tables, Audiences and Workflows (https://www.clay.com/changelog/functions) |
| 2026-04-20 | Salesforce Opportunities in Audiences, table columns as enrichment inputs |
| 2026-05-11 | Table alerting, sensitive connection controls |
| 2026-05-25 | Sculptor sandbox mode |
| 2026-06-08 | Navigation rebuild, Sculptor chat history |
| 2026-06-15 | Company and people lookalikes, sequencer forwarding |
| 2026-06-22 | Sandbox Mode for all users, credit attribution dashboard, HTTP API pagination |
| 2026-07-09 | Clay API and CLI (open beta) |
| 2026-07-13 | Inbox as a source through AgentMail, function observability |
| 2026-07-16 | Open-weight models Kimi K2.6 and GLM 5.2 in Claygent and Use AI columns |
| 2026-08-03 | Audiences Reporting (pipeline and revenue from Clay-sourced accounts), credit usage graphs by day, hour and minute, `clay login --device`, Claygent refresh |
| 2026-08-10 | New Enrich tab (provider catalog, most popular, favorites, For You page), Nooks integration (push and pull sequence data both ways) |
| 2026-08-17 | Skills in the Claygent Builder, SOQL imports into Audiences, AI-generated Snowflake SQL, credit spike alerts |
| 2026-08-24 | Credit budgets and pre-run testing for Functions |
| 2026-08-31 | NAICS filtering in company search, prorated refunds on mid-period upgrades, rewritten enrichment action descriptions, webhook auto-delete warnings, faster signal results in Audiences, clickable links in connector results |
| 2026-09-07 | Advanced Search in the Clay connector, Pardot (Salesforce Account Engagement) integration |
| 2026-09-15 | Clay Plugin for Claude Code and Codex, with Audiences, Sequencer and Query Tables |
| 2026-09-21 | Functions take over from legacy Recipes (Save as Function, one-click Recipe migration, managed functions installed in every workspace), self-serve sign-in changes, auto top-ups |
| 2026-09-28 | Clay Ads LinkedIn syncs (company lists, pause and edit recurring syncs, sync history), IP access restrictions, clickable connection usage traces |
| 2026-09-29 | Integrations roundup: 24 new or upgraded providers (regional coverage Lunar, Pipecorn, Enrich CRM, Vainu, Leadfeeder, SMARTe, Pubrio, Forager, Meer and HG Insights v2; public sector Pursuit and GovSpend; Actovia for commercial real estate; Magellan Data for private equity; signals from G2, Crunchbase, Adyntel and Sequel.io; actions through Canva, Nooks, ClickHouse, Company URL Finder, HubSpot and Twain) |
| 2026-10-05 | Workflow credit budgets, bulk re-runs, one-click trusted-domain joining, Ads in the stable CLI, redesigned Audiences record view |
| 2026-10-08 | Sculpt 2026: agent-first building (rolling out to early access), Clay Workflows beta for all users, Inbound SDR Agent preview (https://www.clay.com/blog/sculpt-2026-recap) |
| 2026-10-12 | New home page (workflows and a chat composer that opens Sculptor, or the global agent where enabled), Audiences sources and exports tabs, Ads match rates that follow each platform's reporting |
| 2026-10-15 | Plugin 2.33.0 and CLI 1.10.0 (workflow re-runs, batch size for audience-scheduled triggers, 7-day recurring company ad syncs) |

Notes on conflicts and gaps:

- Sculptor is Clay's in-table AI builder. The changelog confirms it for Search (March), sandbox (May) and chat history (June), and the October home page opens it from the composer. UNVERIFIED: general availability on all plans.
- The global agent (the agent-first builder) is available to Sculpt attendees on paid plans with early access rolling out. Clay's showcase labels it Beta and one newsletter calls it alpha, so the stage is unclear. No pricing has been published for it, for Workflows or for the Inbound SDR Agent.
- Workflows are called beta in Clay's recap and Alpha in its developer documentation. Treat them as pre-general-availability. They have no 50,000 row ceiling. Search as a source is not supported yet.
- Sequencer 2.0 and Ads 2.0 appear as highlighted features on the changelog page without dates.

## Other Clay tooling, and what to do with it

| Tool | Verdict |
|------|---------|
| Clay's official plugin repository (`clay-run/agent-plugins`) | Adopt. Best source for the audit method and current product facts. |
| `clay-run/clay-skill-creator` | Borrow its determinism notes and function reference for failure traps. |
| `clay-run/public-docs` | Borrow to ground answers in current documentation. Pull requests there show documentation changes before they publish. |
| Clay's developer documentation (https://developers.clay.com/llms.txt) | Adopt for CLI, API, routines and search reference. |
| Community skill packs (workbench routers, enrichment-debugger packs) | Borrow ideas only. Low adoption, written before Functions, advice without table access. |
| Community MCP servers and CLIs that ask for a Clay API key or credentials file | Skip. They would hold access to workspace data and credits. Use the official Open Authorization (OAuth) connector or `clay login`. |
| Third-party go-to-market (GTM) skill repositories that run on another vendor's CLI | Not Clay-native. Do not adopt for Clay work. |

Several search results describe a different product also named "Clay" (a personal relationship manager and a self-hosted agent workspace). Do not mix them up with the go-to-market platform.

# Clay Interfaces, Limits and Releases

Facts in this file were checked on 2026-10-18 against Clay's changelog and blog, Clay's official plugin repository and the live connector. Items marked UNVERIFIED rest on one third-party source or on a page that did not show the detail. Clay ships weekly, so re-check anything that decides a purchase or a build.

## The four ways to work with Clay

| Interface | What it does | What it cannot do |
|-----------|--------------|-------------------|
| Clay app (human or Chrome automation) | Everything: create and edit tables, columns, run conditions, runs, Functions, Audiences, Workflows, Signals | Chrome automation is slower and breaks more easily than the CLI |
| Official plugin and `clay` command-line interface (CLI) | Read tables (structure, rows, cell status), run ClayQL queries, build and edit Workflows, manage Signals, Audiences, campaigns and credits | Create tables or columns, write cells, insert rows, trigger enrichments on a table |
| Clay connector in claude.ai (Model Context Protocol, MCP) | Search companies and people, enrich with named data points, run the workspace's Functions, query Audiences, ask questions about accounts | List, read, create or edit tables, workbooks, columns or runs |
| Clay public application programming interface (API), open beta since 2026-07-09 | Programmatic access for services built on Clay, no added cost | Same read and list limits as the CLI for tables |

## The official plugin and CLI

- Clay announced the API and CLI on 2026-07-09 (open beta, no added cost) and the Agent Plugin for Claude Code, Codex and Cursor on 2026-09-15.
- Install in Claude Code (version 2.1.91 or later): `/plugin marketplace add clay-run/agent-plugins`, then `/plugin install clay@clay-plugins`. Run the bundled `setup` skill, then `clay login`.
- Repository state on 2026-10-18: plugin version 2.33.0, CLI 1.9.0, last commit 2026-10-15.
- Read commands: `clay tables list`, `get`, `columns list|get`, `rows list|get`, `query-live` (ClayQL, 100 rows per call). The synced `clay tables query` (joins, paging) needs Enterprise API table sync.
- It cannot create tables or columns, write cells, insert rows or trigger enrichments on a table. Workflows are the only object it can build.
- Clay says every plugin action is recorded in its audit trail and the data stays on Clay's platform.
- The plugin's hooks auto-approve `clay` CLI commands, so read the plugin's `SKILL.md` files before installing.
- UNVERIFIED: whether the plugin bundles the MCP connector. Clay's July blog says it bundles "API, CLI, MCP, and skills", while one third-party review says it does not.

### Plugin skills and what each is for

| Skill | Use it to |
|-------|-----------|
| `clay` | Start here. Index of every Clay skill and the order to escalate (search, managed function, custom function, workflow, table) |
| `setup` | Install and authenticate the CLI |
| `tables-cli` | Read and query an existing table |
| `tables-analyze` | Explain what a table does: dependency graph, stages, narrative |
| `tables-trace` | Locate a record by identifier and snapshot each cell |
| `tables-value-trace` | Explain one cell by walking back through inputs and the run gate |
| `tables-error-sweep` | Find errored rows and group them by root cause |
| `tables-capacity` | Check the 50,000 row ceiling when imports stall |
| `credits-quotas-plans` | Read the credit balance and plan limits, and handle top-ups |
| `workflows-vs-tables` | Decide between a table and a Workflow |
| `workflows`, `workflows-claygent`, `workflows-optimize-credits`, `workflows-simplify`, `workflows-snapshots`, `workflows-discover-actions`, `workflows-campaign-enrollment`, `workflows-inbound-lead-routing`, `workflows-audience-enrichment` | Build, review and cost-check Workflows |
| `signals` | List, create, pause and resume Signals |
| `audiences`, `ad-syncs` | Work with the workspace's own people, companies and deals, and push segments to ad platforms |
| `campaigns`, `campaigns-sequence-writing`, `campaigns-sequence-reviewing`, `campaigns-interview` | Create, write and review Clay Sequencer campaigns |
| `searches`, `routines` | Find net-new people and companies, and run Clay-managed or custom functions |

## The connector in claude.ai

- Clay launched "Clay in Claude" on 2026-01-26. New connections receive 500 free credits. Version 2 shipped in the week of 2026-03-23 with custom Functions that an operations lead builds and reps run in chat, per-rep access toggles, and a global plus per-rep credit budget on an "MCP Users" settings page.
- Tools: `search-companies`, `search-contacts`, `search-contacts-by-name`, `load-more-search-results`, `add-company-data-points`, `add-contact-data-points`, `get-task`, `get-task-context`, `list_subroutines`, `run_subroutine`, `run_subroutine_direct`, `query-objects`, `ask-question-about-accounts`, `get-current-workspace`.
- `run_subroutine_direct` takes up to 1,000 input sets and each set consumes credits. `query-objects` returns at most 100 records per call and depends on Audiences data. `ask-question-about-accounts` answers across 1 to 10 accounts.
- The connection is pinned to one workspace. Call `get-current-workspace` and confirm the workspace id before any enrichment. Clay's guide does not say how access is scoped across workspaces (UNVERIFIED beyond the pin).
- In a terminal host such as Claude Code the result widget does not render, so call `get-task-context` to read enrichment results.
- Clay's guide scopes the connector to rep-scale work, roughly 1 to 20 contacts, and sends larger volume and deep customer relationship management (CRM) syncs to the Clay app.
- Enrichment through the connector costs the same credits as in the app. There is no connector surcharge.
- UNVERIFIED (one competitor review): search is free, a role limited to the connector cannot view tables in the app, writing to a sequencer needs an operations-built Function, there is no published rate limit, and an interaction costs 20 to 100 credits.
- UNVERIFIED: the endpoint address and the Cross-entity search and clickable-link additions in the August 2026 roundups (the August 31 detail page returned an error).
- The connector also works in OpenAI Codex (2026-06-02) and ChatGPT (2026-01-16).

## Plans and credits

- In March 2026 Clay replaced the Starter, Explorer and Pro plans with Free, Launch and Growth plus custom Enterprise, and split usage into two meters: Data Credits and Actions.
- Clay's official plugin confirms two balances on action-execution plans: `clay credits balance` returns `balance` (the data-credit pool) and `actionExecutionBalance`. Plenty of one does not cover the other, and there is no top-up for action executions, only a plan change.
- Plan prices and allowances come from third-party blogs and conflict with each other (one source reports Growth actions as unlimited). Reported figures, to be verified on Clay's pricing page before quoting: Launch about $185 per month with 2,500 data credits and 15,000 actions, Growth about $495 per month with 6,000 data credits and 40,000 actions.
- Steps that were free under the old model (formulas, lookups, writing to tables) may now consume Actions. Read the estimate before a run and never assume a step is free.
- Credit controls that exist now: credit limits and warnings (2026-01-30), credit dashboards (2026-01-16), credit attribution dashboard (2026-06-22), spike alerts (2026-08-17), credit budgets and function testing (2026-08-24), workflow credit budgets (2026-10-05), auto top-ups (2026-09-21).

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
| 2026-08-17 | Skills in the Claygent Builder, credit spike alerts |
| 2026-08-24 | Credit budgets, function testing |
| 2026-09-15 | Clay Plugin for Claude Code and Codex, with Audiences, Sequencer and Query Tables |
| 2026-09-21 | Functions take over from legacy Recipes, auto top-ups |
| 2026-09-28 | Clay Ads LinkedIn syncs, IP access restrictions |
| 2026-10-05 | Workflow credit budgets, bulk re-runs, Ads in the CLI |
| 2026-10-08 | Sculpt 2026 event: agent-first building, Clay Workflows beta, Inbound SDR Agent preview (https://www.clay.com/blog/sculpt-2026-recap) |
| 2026-10-12 | New home page, Audiences sources and exports view |

Notes on conflicts and gaps:

- Functions launched in April and took over from legacy Recipes in September. The April page was read directly.
- Sculptor is Clay's in-table AI builder. The changelog confirms it for Search (March), sandbox (May) and chat history (June). UNVERIFIED beyond a search summary: general availability on all plans, and the October home page composer opening Sculptor.
- Sequencer 2.0 and Ads 2.0 appear as highlighted features on the changelog page without dates.
- Workflows are in beta with a full launch announced for the fall of 2026, and they have no 50,000 row ceiling. Search as a source is not supported in Workflows yet, so send a search to Audiences and act on it from a Workflow, or use a table.

## Other Clay tooling, and what to do with it

| Tool | Verdict |
|------|---------|
| Clay's official plugin repository (`clay-run/agent-plugins`) | Adopt. Best source for the audit method and current product facts. |
| `clay-run/clay-skill-creator` | Borrow its determinism notes and function reference for failure traps. |
| `clay-run/public-docs` | Borrow to ground answers in current documentation. |
| Community skill packs (workbench routers, enrichment-debugger packs) | Borrow ideas only. Low adoption, written before Functions, advice without table access. |
| Community MCP servers and CLIs that ask for a Clay API key or credentials file | Skip. They would hold access to workspace data and credits. Use the official Open Authorization (OAuth) connector or `clay login`. |
| Third-party go-to-market (GTM) skill repositories that run on another vendor's CLI | Not Clay-native. Do not adopt for Clay work. |

Several search results describe a different product also named "Clay" (a personal relationship manager and a self-hosted agent workspace). Do not mix them up with the go-to-market platform.

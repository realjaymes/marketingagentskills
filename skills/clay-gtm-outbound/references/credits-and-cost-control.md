# Clay Credits and Cost Control

Clay bills on two meters since March 2026: Data Credits and Actions. Per-step Data Credit prices change often and depend on the provider, so this guide gives the habits that hold across pricing changes and the structure Clay documents, and it sends you to the live estimate for numbers. Run `clay credits balance` (plugin skill `credits-quotas-plans`) or read the estimate in the app before any paid run.

## What each meter charges for (Clay's documentation, checked 2026-10-18)

Source: https://university.clay.com/docs/actions-data-credits and https://www.clay.com/pricing.

- Actions cost "a few tenths of a penny" each, and each record counts as one Action whatever its source. Actions are charged for every enrichment (including enrichments that use your own API keys), every AI run, signals, each lead added to a Clay Sequencer campaign (1 per lead), each record exported to an outside sequencer, CRM and warehouse exports and syncs, HyperText Transfer Protocol (HTTP) API calls and ad audience exports.
- Actions are free for sourcing lists, CRM, warehouse and webhook imports, manual entry, formulas, filters, scoring and normalization, Sculptor, creating Audiences (only exporting counts), Send Table Data, Lookup Single Row, Lookup Multiple Rows and CSV export. The older advice to test whether formulas and lookups cost Actions is settled for now. Clay documents them as free. Still read the estimate on the first run, because the page may change.
- Actions do not roll over and cannot be topped up. More Actions need a higher plan tier.
- Data Credits cost "a few pennies" each and vary by data type. Clay's guide is 6 to 20 Data Credits per fully enriched record. Sourcing from Clay's database and validator providers are free under current pricing. Its worked example: 100 contacts with LinkedIn profiles (0.5 each) and emails (0.5 each, 90% success) used 95 credits, and using the user's own email key cut that to 50.
- Using your own API key removes the Data Credit cost for that provider and leaves the Action cost in place. Model costs billed through your own provider do not show in Clay.
- Credits are refunded when a provider refunds Clay for invalid data. A stopped run still pays for requests already sent.

## Plans as Clay's pricing page shows them

| | Free | Launch | Growth | Enterprise |
|---|---|---|---|---|
| Price | $0 | $167 a month billed annually, or $185 billed monthly | $446 a month billed annually, or $495 billed monthly | Custom |
| Actions | 500 a month | 15,000 a month up to 200,000 | 40,000 a month up to 200,000 | Custom (100,000 and up per Clay's documentation) |
| Data Credits | 100 a month | 2,500 a month up to 50,000 | 6,000 a month up to 50,000 | Custom (100,000 and up) |
| Rows per table | 200 | 50,000 | Not stated | Not stated |
| Search | Not included (100 results per rolling 30 days) | Unlimited search and CSV upload | Adds up to 250,000 CRM or warehouse imports | Unlimited |
| Adds | Waterfalls, Claygent, own API keys | Custom functions, scheduled enrichment, signals, phone enrichment, email campaigns | CRM auto-sync, HTTP APIs, webhooks, web intent signals, buying domains and inboxes for the Sequencer | Groups, role-based access, 15-minute source sync, 6-month table history |

Clay's page and FAQ conflict in places (Launch Data Credits shown as 3,000 and 2,500, Free Sequencer access, the Growth Action allowance), so confirm the tier the user is on in the app before quoting anything. Plan tiers move in steps, and prices above are starting points and not quotes.

Rollover and top-ups: on monthly plans unused Data Credits accumulate up to twice the monthly amount. On annual plans 15% of unused credits roll over when the plan renews at the same tier or higher, and trials roll over 100. A one-time top-up carries a 30% premium and starts at 250 credits. Auto top-up is for admins on paid self-serve plans (not Free, trial or Enterprise), needs a threshold of at least 15% of the plan's cycle allowance, and charges the moment the balance reaches that threshold, repeating within an optional daily limit. Clay caps a single top-up at $1,000 and top-ups at $5,000 across any rolling seven days, and top-ups together add at most four times the monthly allowance. A failed payment grants nothing and turns auto top-ups off. A shortfall in Data Credits is fixed by a tier upgrade (no premium) or a top-up. A shortfall in Actions is fixed only by a plan change.

## The rules

1. Read the estimate before every run and write it down. If Clay shows no estimate, run one row and read the credits used.
2. Do not assume a step is free beyond what Clay documents as free (above). Enrichments, AI runs, signals, exports, HTTP calls and Sequencer leads all cost Actions. Test one row before building a design that depends on a cost you have not seen.
3. Never run "all rows" on a column you have just changed.
4. Spend credits only after the user gives an explicit go for that run, with the row count and the estimate stated.
5. Check both balances. `balance` is the data-credit pool and `actionExecutionBalance` is the action meter on action-execution plans. A short action balance is fixed by a plan change, not a top-up.

## Filter upstream

Clay refines a list, and the list should be mostly right before it arrives. Filter by title, seniority, company size, industry and country in the source (Clay's own search, a customer relationship management (CRM) system, a database, a scrape) before enrichment. Deduplicate by domain and by person before the first paid column. Drop rows that fail the ideal customer profile (ICP) in a formula column that gates every paid action below it.

## Gate every paid column with a run condition

A run condition ("only run if") is the first control on spend. Typical gates: the email is empty, the domain is present, the title matches the persona, the previous provider found nothing. Check what a gate does with an empty value and with text where a number is expected, because a gate that evaluates false silently shows as empty and hides a bug (see `table-audit-and-debug.md`, step 6).

## Test, then expand

- Start with 10 rows and auto-update off. Read every output.
- Expand to 100 or 200 rows. Compare cost per row with the estimate.
- Turn auto-update on only after the output and the cost both hold.
- Use Sandbox Mode (all users since 2026-06-22) for experiments, Delay Runs (2026-03-27) for a chance to stop a bad run, and table versioning (2026-03-23) to restore a table after a bad edit.
- Set a credit budget or alert on the table, the Function, the Workflow and the workspace (credit budgets 2026-08-24, spike alerts 2026-08-17, workflow credit budgets 2026-10-05, usage graphs by day, hour and minute 2026-08-03) so a mistake caps itself. `clay budgets list` reads the budgets a user can assign.

## Enrich once, use many times

Split the work by grain. Person-level actions belong in a people table and company-level actions in a company table. Write unique companies to the company table, enrich each once, and bring the result back with a lookup. Three contacts at one company should cost one company enrichment. Deduplicate before enriching, not after. Whether the write and the lookup themselves consume Actions is a per-plan question to test on one row.

## Waterfall enrichment

Stack providers and stop at the first accepted result. Order them from cheapest to most expensive and from fastest to slowest. Each provider after the first has a run condition that checks the previous result is empty. End every email waterfall with verification from a different source than the one that found the address (see `prospecting-and-enrichment.md`). Clay shipped email waterfall controls on 2026-03-30, so check the order and stop settings in the app.

Waterfalls multiply cost on rows that no provider can resolve. Gate the whole waterfall on the persona and the domain, and cap the rows per run.

## Own keys and outside calls

Using your own key on a native integration removes the Data Credit charge for that provider, and the Action still applies. Calling a provider's own application programming interface (API) from an HTTP column costs an Action per call. Run one row and read the estimate before relying on either. The HTTP API source gained pagination on 2026-06-22. Never paste a key into a header or body that other users can read. Use a stored connection, and treat any pasted key found in a table as exposed.

## Choosing the AI model

- Match the model to the task. Extraction and classification need a small, fast model. Multi-step reasoning needs a more capable one. Drafting that must read naturally needs the most capable.
- Test the prompt on 10 rows and compare cost per row across two models before choosing.
- Claygent Navigator and the metaprompter-built AI columns arrived in August 2025, and Use AI is one consolidated action. Model options change quickly (Gemini 3 Pro on 2026-01-16, the open-weight Kimi K2.6 and GLM 5.2 on 2026-07-16), so pick from the options the app lists today and read the cost estimate for each.
- Skills in the Claygent Builder shipped on 2026-08-17.
- Use code or a formula for deterministic work. A formula costs nothing in model spend and returns the same answer every time.
- In Workflows, put a code node before a repeating AI node to filter rows that need no processing. The plugin skill `workflows-optimize-credits` reviews a workflow for these savings.

## Scrape outside, enrich and trigger inside

Clay suits structured enrichment and Signals. For high-volume scraping (websites, reviews, directories, social monitoring), run the scrape in a dedicated tool or your own scripts, clean the result, and import it for qualification and enrichment. Importing is also the way to move data when an HTTP or webhook column is not available on the plan.

## Reusable logic

Put logic you use in more than one table into a Function (2026-04-15). A Function can be tested (2026-08-24), observed (2026-07-13) and reused from tables, Audiences and Workflows, so one tested version replaces many copies that drift. Functions took over from legacy Recipes on 2026-09-21.

## Clay's own confirmation policy for agents

Clay's plugin asks for confirmation before any operation that would use at least 10% of the remaining Data Credit balance (judged for the whole run and not per page), runs about 10 records before any run over 100 records, quotes only numbers a tool returned, and treats a missing price as unknown. When an estimate may be incomplete (variable pricing or per-item repeats), it probes one record and then runs chunks small enough that a several-fold miss stays inside the approved spend. This matches the go rule above, and it never replaces it. The go for a run still comes from the user.

## Row ceilings

A table stops accepting rows at its ceiling. The default is 50,000, plans can set it lower (Free shows 200 rows per table), and per-table overrides can raise it. The CLI does not return the effective value. The table is constrained when its own `rowCount` or any source's `numSourceRecords` reaches the ceiling, so check every source. A count pinned at a round number below 50,000 while an import runs points at a lower plan ceiling. Archive tables are not subject to the ceiling. Proximity is not urgency, so measure the fill rate and report time to ceiling when asked. When an import stalls, run the plugin skill `tables-capacity` before assuming the import is broken. Tables with a webhook source show a banner when auto-delete is off, because the table can hit its record limit and stop processing webhooks (2026-08-31). Rebuild a table that is outgrowing the ceiling as a Workflow (skill `workflows-vs-tables`).

## Credit governance in a shared or client workspace

- Give each user a budget where the plan allows it, and watch the attribution dashboard.
- Record credits before and after each test in the audit findings.
- Put a spend note in the handover: which columns cost credits, the cost per row, and which are gated.

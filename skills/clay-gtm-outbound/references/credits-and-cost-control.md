# Clay Credits and Cost Control

Clay bills on two meters since March 2026: Data Credits and Actions (see `clay-interfaces-and-releases.md`). Per-step credit prices change often, so this guide gives the habits that hold across pricing changes and sends you to the live estimate for numbers. It does not carry a cost table. Run `clay credits balance` (plugin skill `credits-quotas-plans`) or read the estimate in the app before any paid run.

## The rules

1. Read the estimate before every run and write it down. If Clay shows no estimate, run one row and read the credits used.
2. Do not assume a step is free. Formulas, lookups and writes to other tables were free under the old model and may now consume Actions. Test one row before building a design that relies on them.
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
- Set a credit budget or alert on the table and the workspace (credit budgets 2026-08-24, spike alerts 2026-08-17, workflow credit budgets 2026-10-05) so a mistake caps itself.

## Enrich once, use many times

Split the work by grain. Person-level actions belong in a people table and company-level actions in a company table. Write unique companies to the company table, enrich each once, and bring the result back with a lookup. Three contacts at one company should cost one company enrichment. Deduplicate before enriching, not after. Whether the write and the lookup themselves consume Actions is a per-plan question to test on one row.

## Waterfall enrichment

Stack providers and stop at the first accepted result. Order them from cheapest to most expensive and from fastest to slowest. Each provider after the first has a run condition that checks the previous result is empty. End every email waterfall with verification from a different source than the one that found the address (see `prospecting-and-enrichment.md`). Clay shipped email waterfall controls on 2026-03-30, so check the order and stop settings in the app.

Waterfalls multiply cost on rows that no provider can resolve. Gate the whole waterfall on the persona and the domain, and cap the rows per run.

## Own keys and outside calls

Calling a provider's own application programming interface (API) from a HyperText Transfer Protocol (HTTP) column, or using your own key on a native integration, can move the cost off Data Credits. The old advice that this "costs nothing in Clay" is no longer safe, because Actions now count. Run one row through the column and read the estimate before relying on it. The HTTP API source gained pagination on 2026-06-22. Never paste a key into a header or body that other users can read. Use a stored connection, and treat any pasted key found in a table as exposed.

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

## Row ceilings

A table stops accepting rows at its ceiling, 50,000 by default. When an import stalls, check capacity with the plugin skill `tables-capacity` before assuming the import is broken. Rebuild a table that is outgrowing the ceiling as a Workflow (skill `workflows-vs-tables`).

## Credit governance in a shared or client workspace

- Give each user a budget where the plan allows it, and watch the attribution dashboard.
- Record credits before and after each test in the audit findings.
- Put a spend note in the handover: which columns cost credits, the cost per row, and which are gated.

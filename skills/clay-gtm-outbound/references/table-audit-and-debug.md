# Auditing and Debugging an Existing Clay Table

Use this method when a table already exists and something is wrong with it: errors, empty columns, bad values, runaway credit spend, or a handover from someone else. It follows the method in Clay's official plugin skills and adds the safeguards that client work needs. Every read in steps 1 to 7 is free. Credits are only at stake from step 8 onward.

The plugin skills named below come from Clay's official plugin (see `clay-interfaces-and-releases.md` for install and limits). Read a skill's `SKILL.md` before running it, and prefer calling the skill over re-deriving its commands.

## Tool routing for this method

| Job | Tool |
|-----|------|
| Read structure, rows and cell status | The `clay` command-line interface (CLI) through the plugin skills. Read-only. |
| Duplicate a table, edit a column, change a run condition, turn auto-run off, re-run rows | The human in the Clay app, or Chrome browser automation driving the Clay app. The CLI cannot create tables or columns, write cells, insert rows or trigger enrichments. |
| Read column settings when no CLI access exists | Chrome browser automation reading the column settings, run conditions and error messages in the app. Slower and more fragile than the CLI, so use it only as the fallback. |
| Anything the connector in claude.ai could help with | Nothing in this method. The connector cannot open tables. |
| Any action that spends credits | Only after the user gives an explicit go for that run, with the estimate shown first. |

## The method

### 1. Get access safely and confirm the workspace

Ask for a Clay seat with edit rights (not Viewer) in the workspace, or a screen share. Sign in with `clay login` and run the plugin's `setup` skill if the CLI is missing. Then confirm the workspace id with `clay whoami` and compare it with the workspace id in the table's URL before reading anything. A wrong workspace is the commonest way to audit the wrong table, and in a client workspace it also means reading data you have no brief to read.

If the plan does not include application programming interface (API) table sync (an Enterprise feature), `clay tables query` fails with `auth_forbidden`. That is an account limit. Fall back to `clay tables columns`, `clay tables rows` and `clay tables query-live`. Those three need no sync. `query-live` returns at most 100 rows per call.

### 2. Duplicate the table and work only on the copy

Reads can target the original because they cannot change it. Every edit and every run happens on a duplicate. The human or Chrome creates the duplicate in the Clay app. Name the copy with the date and the word "audit". Confirm before touching anything that the copy has not started running on open, because a duplicate can carry live auto-run settings and live connections.

Check table versioning on the original (shipped 2026-03-23) so the structural history shows who changed what and when, and confirm restore is available. Record the row count, the source count and each source's `numSourceRecords`.

### 3. Turn auto-run off on the copy and inspect every action that touches the outside world

Before any run, switch auto-run off on the copy. Then list every column that sends something out and read its settings:

- HyperText Transfer Protocol (HTTP) API columns: the URL, the method, the headers and the body. A header or body that holds a pasted key is a hardcoded secret.
- Slack and email columns.
- Customer relationship management (CRM) write columns (Salesforce, HubSpot) and sequencer columns (Smartlead, Instantly, Lemlist, Clay's Sequencer).
- Any column that pushes to an ad platform or a webhook.

For each one, note the connected account, the run condition and whether it would fire on existing rows when the copy is switched on. Add a run condition that blocks the column, or delete it from the copy, before anything runs. A duplicated table that auto-runs can write to a live CRM, post to a live Slack channel or enrol real people in a live sequence.

### 4. Map the columns and the dependency graph

Call the plugin's `tables-analyze` skill. It runs `clay tables get` and `clay tables columns get`, builds one entry per column with its type, integration, run gate and the columns it depends on, and orders the columns into stages. Keep the result as the column map:

| Column | Type (source, formula, action) | Integration and auth account | Inputs | Run condition | Stage |
|--------|-------------------------------|------------------------------|--------|---------------|-------|

A reference that resolves to a bare `f_` id means a deleted or renamed column. Note each one, because it is a candidate root cause. Run a sample of 10 rows for a rough status per column and say it is a sample.

### 5. Group errors by root cause

Call `tables-error-sweep`. It scans the table, reads the full error messages and reports the errors grouped by cause, not row by row. Only action columns can error. The usual groups are provider throttling, an expired or wrong connected account, a bad or missing input from an upstream column, and the provider rejecting the request. Two further results from the sweep matter for the next step:

- A gated skip is not a failure. A run condition that evaluates false usually shows as empty, and sometimes as an error whose message names the condition. Keep these out of the failure count.
- A table with no errored cells but rows that are not arriving points at capacity. Call `tables-capacity`. Clay tables stop accepting rows at a ceiling that defaults to 50,000 (plan and table dependent), and a full table looks like a broken import.

### 6. Separate the four empty states

For each action column, split the rows into four groups and count them:

1. Error: the action ran and failed.
2. Empty after a run: the action ran and found nothing.
3. Run condition not met: the gate evaluated false, so the action was skipped on purpose.
4. Never run: an upstream column has not produced, or auto-run was off, or the row arrived after the last manual run.

The four groups have different fixes. Mixing them is the reason most audits recommend the wrong change. For a gate, check whether it references a column that can be empty, whether it compares text with a number, whether auto-update runs on new rows, and whether any column is set to run on all rows.

### 7. Value-trace the worst cells to the first wrong column

Pick 5 to 10 bad rows and 5 good rows. Find each row by its identifier with `tables-trace` (locate the record and snapshot every cell), then call `tables-value-trace` on each bad cell. It walks the cell backward through its inputs and its run gate until it reaches the first column where the value goes wrong. Compare against a good row to see where the two diverge.

Root causes that recur in tables built by others: a column named for revenue that holds headcount, size bands arriving as text where a number is expected, a plural action fed a single item, a dead company that still enriches without error, and a waterfall whose stop condition checks the wrong column. The failure often surfaces three columns downstream of the cause, so fix the first wrong column and not the one that errored.

### 8. Fix one cause at a time

Change one thing on the copy, then test it. Fixing two causes in one pass makes the result unreadable. Order the fixes by rows affected and credits at stake, highest first. Where the fix is a run condition or a formula, write the new text out in full in the findings so the human can paste it.

### 9. Re-run only the affected rows

Read the cost estimate before every run and write it down. Run the changed column on the affected rows only, never on all rows. Sandbox Mode (all users since 2026-06-22) and Delay Runs (2026-03-27) exist for safe testing, and the app can run individual rows with a cost estimate. Keep auto-update off until the test in step 10 passes. Check that a table-level credit budget or alert is set (credit budgets shipped 2026-08-24, spike alerts 2026-08-17) so a mistake stops itself.

Every run in this step spends the owner's credits. Ask for the go first, state the number of rows and the estimate, and wait.

### 10. Test on a fixed row set

Freeze a test set of about 10 rows before changing anything, covering each case: a good row, a bad row for each root cause found, an edge row (missing input, wrong type, dead company) and an empty row. Write the expected result for each row first. After each fix, run only those rows and compare the output with the expected result. For waterfalls, include rows that exercise the stop condition at each provider. Record the credits before and after each test.

### 11. Write the findings

Deliver one document with these sections, in this order:

1. The column map from step 4.
2. A failure table grouped by root cause, with the count of rows in each of the four empty states.
3. Credit cost per row for each paid column, taken from the live estimate and not from memory.
4. A ranked fix list. Each entry states the issue, the root cause, the fix, the test row set and the result, with one evidence row cited for each.
5. A list of hardcoded secrets and live side effects found in step 3, described without copying any secret value.

## Client workspace etiquette

- Read first. Do not edit, run, rename, move or delete anything on an original table.
- Work on the copy for every change, and tell the owner where the copy lives.
- Never spend the client's credits without permission for that specific run. A read is free, and a run is not.
- Never write to the client's CRM, Slack, sequencer or ad accounts from a copy. Block those columns first.
- When you find a pasted API key, token or password in a column, a header or a body, flag the column by name and say a secret is exposed. Never copy the value into notes, chat or findings.
- Do not give a community tool or server the client's Clay credentials or API keys. Use Clay's own sign-in.
- Plan access limits are real: synced queries need Enterprise API table sync. Say what you could not read and why.
- Record which version of the table you audited (the version history entry) so the findings stay tied to a state of the table.

## When the audit says rebuild

If a table is outgrowing its design (the row ceiling, branching logic, unattended schedules), rebuild the logic as a Clay Workflow and leave the data where it is. The plugin's `workflows-vs-tables` skill gives the decision and `workflows-optimize-credits` reviews a workflow's cost. The CLI can build and edit Workflows but cannot create or edit tables.

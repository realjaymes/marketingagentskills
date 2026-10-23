# Email Preview and QA Tool: Standard

The standard for a self-built HTML email preview and QA tool. **Don't hand-build a new tool per campaign.** Build one reference implementation (a Python script that writes a self-contained HTML file, with the campaign CONFIG at the top and the fixed app at the bottom), then copy it per campaign and change only the CONFIG block.

## Naming convention

Both the generator script and its output HTML name the niche in the filename. Never rely on the folder alone, because browser tabs, Spotlight and a flat `ls` all lose folder context.

- **Script:** `<niche_slug>_build_preview.py`, where `niche_slug` is the niche's own short name (the same name its campaign folder uses). Never name it after a data source or a signal. If "github" is a signal inside a Tech Startups niche, the script is `techstartups_build_preview.py`, because "github" would misstate the scope.
- **Output HTML:** `NN - [Niche Short Name] Email Preview (open in Chrome).html`, for example `08 - Clay Experts Email Preview (open in Chrome).html`. The niche name belongs in the filename itself, not only the `<title>` tag, which only helps once the file is open.

## What it is

A single self-contained HTML file (no build step, opens in a browser) that renders **every lead's full sequence exactly as it will send**, with merge fields, spintax and fallbacks resolved. You review the real emails, not a spreadsheet. Your notes hold the templates and logic, this tool shows the output, and Smartlead sends it.

## Required features (every build needs these)

1. **A dark header** with the brand, the lead count and live stats: `N suspicious`, `N flagged`, `N clean`.
2. **A toolbar** with an **Opener `<select>`** that covers every Email 1 variant as one unit. Subject *and* body swap together. A subject-only select fails this item, because a variant is a full alternate email, and if only the subject changes you can't see what an alternate opener looks like with real merge data. Follow-ups thread as `re:` off whichever subject is selected. The toolbar also has Random, **Re-roll spin**, **Export cleaned** (downloads the CSV minus flagged rows) and a Highlight toggle.

   Two layouts satisfy this. A **dropdown swap** (an `OPENERS` list plus swap logic in `render()`) fits mutually exclusive Email 1 openers. **Always-visible stacking**, where every alternate opener renders below the main sequence for each contact, fits parallel offer tracks you want to compare side by side.
3. **A sidebar** with search (company, city, email), a filter `<select>` and a scrollable contact list. The filter always offers **one option per `{{gap}}` signal, with its count** (for example "Gap: under 15 Google reviews (235)"), so you can read every opener as a group. The detail panel names each lead's signal in plain words. This is presence-driven: any leads CSV with a `gap_variant` column gets these options, labelled from a `GAP_SIGNALS` map (an unmapped code still appears under its raw code). Each row has a **severity dot** (high = red, medium = amber, otherwise green for a named contact and grey for a generic one), the company, a warning icon if suspicious, and a meta line.
4. **A detail panel** with a meta card (company, city, email, website, and chips for tier, size, budget and status), a **QA severity banner** with the reasons, then the sequence as day-badged email cards (subject, body and a `To:` line).
5. **Rendering:** merge fields wrapped in `<mark>` for highlighting, **blank or broken variables in red** (`<mark class=blank>[blank X]</mark>`), and spintax choices underlined (`<span class=spin>`). Re-roll re-randomizes the spin.
6. **QA per lead**, computed in the generator: `{s: severity, r: [reasons], b: broken, x: suspicious}`.
7. **Keyboard navigation:** ↑/↓ to browse, `r` for random, `f` to flag. Flags persist in localStorage.
8. **Signal-keyed Email 1 variants** when leads carry different signals. The tool picks the variant matching each lead's signals and shows which one it picked.
9. **Self-contained and responsive**, with no external requests.

## The config block (all a campaign changes)

Everything else (CSS, UI, and the render, QA and export JavaScript) stays fixed. A campaign supplies:

- **`OPENERS`**: the Email 1 variant list. Each entry is `{label, subject, body}` as one unit, never a subject-only list. The Opener select swaps subject and body together for Day 0. Follow-up days keep their own bodies but thread `re:` off the selected subject.
- **Sequence bodies** for Email 2 and Email 3 (Email 1 lives in `OPENERS`). Use spintax `{a|b|c}`, merge tags `{{token}}` and a precomputed `{{greeting}}`.
- **`pick_variant(lead)`** (optional, for signal-based campaigns): returns which `OPENERS` entry to default to from the lead's signals (for example hiring → B, recent post → C, none → A). The reviewer can still switch the Opener select per lead.
- **`merge_map(lead)`**: maps lead columns to `{{tokens}}`, with fallbacks and any cleanup of raw data (for example turning a messy hiring note into "a Sales Director role"). Precompute `greeting` as "Hi {first}," or "Hi {company} team,".
- **`qa(lead)`**: returns severity and reasons (see rules below).
- **`COLS`** (display and export columns), **chips** (which fields show as chips) and **filters** (the sidebar dropdown options). Filter on any column with an option value of `field:<column>:<value>`, which a generic branch in `applyFilter()` handles. Any new option prefix needs its own branch in `applyFilter()`, or it shows in the dropdown and filters nothing.
- **The gap generator writes `gap_variant`.** Every script that fills `{{gap}}` also writes the code of the signal that produced it, and every new code gets a plain-English label in `GAP_SIGNALS`. Without the column, the preview can't show which signal each lead got.
- **`LINKEDIN`** (optional, off by default) turns on a campaign's LinkedIn track. It takes `{enabled, per_day, steps}`, where `steps` is an ordered list of `{key, field, label, char_limit?, arm_field?, blank_label?}`. `key` is the step ID used for tracker column names (such as `request`, `dm`, `followup`). `field` is the CSV column holding that step's message. `char_limit` shows an "X of N characters" count (LinkedIn connection notes cap at 200). `arm_field` and `blank_label` handle a test arm on that step, such as a note versus no-note split: when the lead's `arm_field` value isn't `"note"`, the tool shows `blank_label` instead of the text. When `LINKEDIN.enabled` is true, a per-lead `channel` column ("email", "linkedin" or "email + linkedin") decides which cards render, a "LinkedIn only" filter appears, and an arm filter appears automatically if a step's `arm_field` exists in the data. An email-only campaign leaves it off, and nothing about its output changes.

## Status tracking (presence-driven, no config change needed)

If the leads CSV has any recognized tracker columns (`request_sent`, `accepted`, `dm_sent`, `followup_sent`, `replied` for LinkedIn, or `sent` and `replied` for email), the tool detects them from the header at build time and turns on per-lead status chips (in the sidebar row and the meta card), header stats (`N sent`, `N accepted`, `N replied`, `N pending`), and a "Pending" filter for leads whose next step isn't done. A CSV without these columns renders as before. To track a campaign that's already sending, add the columns, fill them as sends, accepts and replies happen, and re-run the generator.

## Known CSS and filter bugs to avoid

- **Sidebar search font size.** A shared rule like `select,input,button{font:inherit;...}` leaves `input` without an explicit `font-size`, so the search box inherits the browser default (about 16px) instead of the sidebar's 12 to 13.5px scale. In a narrow sidebar (around 322px), a 16px placeholder such as "Search company / city / email" can overflow the box. Add `font-size:13px` to the shared rule and an explicit `input::placeholder{font-size:13px}` rule.
- **Dead filter options.** A filter option that `applyFilter()` never checks silently shows every contact. The generic `field:<column>:<value>` branch fixes it. Test every new filter option by choosing it and watching the count change.

## QA rule patterns (compose per campaign)

- **Email domain doesn't match website domain** → high ("email domain X does not match website Y"). This catches enrichment that grabbed the wrong site.
- **Blank required merge variable** (company, gap, email) → high, and marked `broken`.
- **Free or personal email** on a company lead (gmail, yahoo, aol and so on) → medium.
- **Disqualify or exclude tags** defined per campaign (for example acquired, defunct, no sales leader) → high or exclude.
- Suspicious rows surface in the sidebar, and Export cleaned removes flagged rows.

## Copy sanity rules (write them into the templates, check them in the preview)

- **No internal phrasing in sendable copy.** Never a literal label like "one more angle", "new angle", "[opener]" or "value prop here". Every spintax option must read naturally to the recipient. A spin option reading "One more angle." is the kind of thing that slips through.
- **Source and platform names must be true per lead, never hardcoded.** A sentence like "you depend on referrals and Clutch inbound" is only true if that lead came from Clutch. Drive any platform reference from a per-lead field (such as `{{inbound}}`, set from the lead's `source` column), with a generic fallback ("referrals and inbound"). Do the same for the audience noun: use a per-lead `{{segment}}` ("software teams", "IT firms") instead of a hardcoded "dev shops".
- **No em dashes** in the copy. Use plain language and frame observations as opportunities, never as "you're failing".
- **Every `{a|b}` option must be sendable on its own.** Read each branch by itself, and fix any branch that reads wrong. The re-roll button exists to surface exactly this.
- **Red marks mean an empty merge variable** for that lead. Fix the data or add a fallback before sending.

## Using it for a new campaign

1. Copy your reference script to `<niche_slug>_build_preview.py` and point it at the campaign's master leads CSV.
2. Edit only the CONFIG block: `OPENERS`, the Email 2 and 3 bodies, `merge_map`, `qa`, `COLS`, and `LINKEDIN` if the campaign has a LinkedIn track.
3. Set the output filename to `NN - [Niche Short Name] Email Preview (open in Chrome).html`.
4. Run it, open the HTML, and review every lead. Watch the stats, red blanks and suspicious dots, re-roll the spin, and check LinkedIn cards and status chips if enabled.
5. Flag bad rows, then Export cleaned. That CSV goes to Smartlead.

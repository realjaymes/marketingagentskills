# Prospecting, Enrichment and Verification with Clay

## The four-step data workflow

1. Find: identify companies and people that fit the ideal customer profile (ICP). Sources are Clay search, third-party databases, LinkedIn, Google Maps, CRMs (customer relationship management systems), fundraising databases and your own scrapes.
2. Enrich: add the missing attributes (firmographics, technology stack, titles, emails). Use a waterfall across providers and order the steps from cheapest to most expensive.
3. Transform: score, filter, segment, apply conditional logic and run AI analysis.
4. Export: push the result to a CRM, a sequencer or an Audience.

Clay refines a list and should not be where list building starts. Anything that scrapes at volume belongs outside Clay (see `credits-and-cost-control.md`).

## Building the company list

- Define the ICP filters: industry (self-reported categories are noisy, so test keywords too), company size, public or private (funding signals matter for private companies), geography and keywords in the description.
- Preview and iterate. Refine the filters until the count is workable, and do not stop at the first search. Clay has offered natural language company search since 2025-07-03, and Sculptor for search since 2026-03-30.
- While learning or testing, run on about 50 companies.
- Save the search (saved searches, 2026-01-30) so the filter can be re-run and audited.

## Enriching companies

Start from the anchor fields: domain, LinkedIn company URL and company name. Run the company enrichment for size, locations, specialties and funding. Where one provider covers only part of the list, add a second and third provider for the same field in a waterfall, cheapest first. Check coverage after each provider and stop adding providers when the gain per provider is small.

## Finding and enriching people

1. Find people at each company with title keywords and seniority filters. Use exact-match keywords when precision matters (exact match search, 2025-12-12).
2. Run the email waterfall (below), then LinkedIn profile enrichment.
3. Add phone enrichment only when the outreach plan uses phone.
4. Gate every paid step on the persona and the domain so rows that fail the ICP never spend credits.

## The contact standard

These rules decide whether an address goes into a send list.

- Use named decision-makers. For software, software-as-a-service (SaaS) and agency prospecting, `info@`, `contact@`, `hello@`, `support@` and `sales@` route to support or a low-attention queue and never count as a lead's email. For local owner-operated businesses (trades, home services, restaurants), a role inbox is usually the owner's own inbox and is an acceptable target. Prefer a named owner when enrichment returns one, and precompute the greeting so the email reads correctly with or without a first name.
- Aim for at least two verified named contacts per software company: the founder or chief executive first, then the function head who owns the problem, then a senior peer. More than a handful per company reduces replies (cold-email benchmarks show 7.8% reply rates at one or two contacts per company against 3.8% at ten or more), so never add junior staff to pad a company.
- Contacts at one company share the same company-level opener because it describes the company. Keep the greeting personal. Copy never implies each person is the only one contacted and never names the others.
- A single tool's result is a candidate. A Clay `clay_found` hit, a warning-icon address in a browser extension and a pattern guess all need a second independent source (another database, a mail-server check, the person's own LinkedIn or site) before they count as verified.
- An address counts only on the company domain, a subdomain, a second domain the company really sends from (confirmed by a redirect, published mail or a verified hit) or a domain carrying the company name. Anything else goes to a rejected column and the waterfall continues.
- A pattern address (first@, first.last@, firstl@, flast@ copied from a confirmed colleague) is labeled `pattern_unverified` and never treated as verified.
- Personal, university and old-company addresses count only as a labeled fallback column, never in the main send list.
- A vendor's "verified" flag is not a deliverability check. It confirms the address existed once, and the people worth contacting change jobs. In one live batch, two of thirteen vendor-verified addresses hard-bounced (15.4% against a tolerable band of 2 to 5%), so every send list passes an address-level check first.

## Verification

- Verify with an address-level deliverability checker (MillionVerifier or an equivalent) before sending, and use a second source such as Hunter as a backup when the first rate-limits. Treat the result classes this way: valid sends; invalid and disposable drop; accept-all (catch-all) is neither a pass nor a fail.
- Decide accept-all addresses on separate evidence, for example an address the company publishes itself, or a mailbox confirmed by a provider that checks through accept-all domains. Sending tiers that work: Tier A (send now) is a checker's good result or a provider-verified direct address, Tier B (second wave, low volume) is the remaining accept-all addresses, and Tier C (drop) is invalid. A flagged `catch_all_accepted` carve-out records each accept-all address you decided to send to.
- Pace verification calls at three seconds apart, and re-check a fresh invalid once after 20 seconds before dropping it. A burst of 29 checks against Google Workspace domains returned false rejections that came back valid on a paced re-check.
- A mail-server probe from a home or office network often cannot work because outbound port 25 is blocked. A probe that returns unknown for every address carries no information, so use an application programming interface (API) based checker instead.
- Where the sequencer verifies on import (Smartlead does), let it verify and read its valid, accept-all, risky and invalid split before judging list quality.
- Do not drop a lead for an unknown title. An unknown title means no title was scraped. That is common on guessed contacts. Drop only a positive "not a buyer" verdict.

## AI research with Claygent

Use Claygent for unstructured last-mile data that providers do not carry: what tools a company uses, hiring patterns, sales motion, positioning claims. Write a prompt that states the data point, the allowed sources and the output fields, and test it on 10 rows before scaling. Return structured fields (a value, a source URL and a confidence note) so a downstream column can gate on them. Claygent Navigator arrived on 2025-08-26, and the metaprompter formats a rough prompt into context, objective and instructions. Choose the model by task and cost (see `credits-and-cost-control.md`). In a Workflow, a Claygent is an agent node (plugin skill `workflows-claygent`).

## Advanced techniques

- Conditional runs: formulas so an enrichment runs only when criteria are met.
- Merge columns: combine outputs from several enrichments into one result column.
- Lookalikes: use customers as a seed list for company and people lookalikes (2026-06-15).
- Scheduled sources: refresh sources daily, weekly or monthly. Enrichments run on new rows when auto-run is on, so check the credit budget first.
- Table columns as enrichment inputs (2026-04-20) and Functions for reusable logic (2026-04-15).
- Signal stacking: see `signals-and-audiences.md`.

## Tables, Workflows or Functions

- A one-off pull, an exploration or a first build: use a table.
- A job that runs on a schedule or trigger without anyone watching, such as inbound lead routing, qualification and assignment, or a play with several branches that ends in outbound or assignment: use a Workflow (beta, no 50,000 row ceiling). Workflows do not take search as a source yet.
- Logic shared across tables, Audiences and Workflows: use a Function.
- A table that has outgrown its ceiling or its design: rebuild the logic as a Workflow. There is no automatic migration, and the data stays where it is.
- The plugin can build and edit Workflows. It cannot build or edit tables.

## Segmentation

Separate tables per segment are not needed. Use filters or conditional runs. Split into separate tables only when the segments need many different enrichments.

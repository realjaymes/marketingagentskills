---
name: prospect-scraper
description: Build and run the data half of cold outbound. Find, enrich, verify, score, and export prospect lists from any source (government and open data, SEC EDGAR Form D, Socrata, Yelp, business directories, membership associations, VC portfolios, Clutch), free-first. Use when the user wants to "build a scraper," "build a source adapter," "scrape leads," "pull a prospect/lead list," "find companies to pitch," "enrich these leads," "verify emails," "score prospects," or names a source like Socrata, SEC EDGAR, Form D, Yelp Fusion, Clutch, Product Hunt, a state licensing board, a chamber of commerce, or a business-license open dataset. This is the DATA half only. It feeds outbound-engine (the send half) and any cold-email copy skill. NOT for writing email copy or running deliverability or sending.
---

# Prospect Scraper

The data half of cold outbound. It turns any source into a clean, enriched, verified, scored prospect list.

This skill owns FIND → ENRICH → VERIFY → SCORE. Its companion skill, `outbound-engine`, owns PERSONALIZE → QA → WARMUP → SEND → MEASURE. The two meet at the common record schema below.

## When to use

- Build or extend a scraper or source adapter.
- Produce a prospect list (funded startups or local businesses) with enrichment, verification and scoring.
- Any time you need the list itself and not a campaign: agency prospect lists, client lead lists, GTM-engineering take-home tasks.

Use a different skill for writing the cold email, running the send, deliverability or warmup (`outbound-engine`), or Clay-specific enrichment when you work inside Clay.

## Core principles

1. **Free-first.** Prefer official free APIs, government and open data, and open-source libraries over paid per-record tools. Pay only for the hard remainder, such as some contact enrichment or an occasional Google Maps pull through Outscraper or Apify.
2. **Adapters, not monoliths.** Each source is a thin adapter that emits the one common record schema. Sites change, and the pipeline stays the same.
3. **Never lose code.** Save every adapter's runnable code to a version-controlled repo the moment it's built, and document it where your team can read it. See the preservation step below.
4. **Latent need over active hiring.** Target companies that need the capability but aren't publicly shopping for it. A company hiring for the exact role is a job lead, not a services lead.
5. **Adopt before you build.** Use the default libraries below before hand-rolling anything.

## The pipeline

```
Discover (source adapter) → normalize (common schema) → dedupe → enrich → verify → detect signals → score → export
```

## The common record schema

One record shape for every source (nulls allowed): `name`, `domain`, `description`, `category`, `motion` (sales-led, PLG or B2C for startups), `region/country`, `city/state`, `address`, `phone`, funding `stage`/`amount`/`date`, `employee_count`, `founder`, contact `name`/`role`/`email`, `email_status` (from the verifier), `tech_stack`, `live_ads` flag, `source`(s), `first_seen`, `signals`, `deliverable`, `personalization_seed`, `fit_score`, and dedupe keys (domain plus normalized name, or place ID for local businesses).

`signals` is plural. It holds every need signal detected for the lead, not just the first match (see Signal detection below). `deliverable` is the free offer matched to the lead. It gets chosen later at the human review step, not at scrape time.

A company can carry more than one contact. Collect every reachable decision-maker (all cofounders at a startup, or the owner plus a marketing or sales lead at an established business). Emit one record per contact with the company fields repeated, so `outbound-engine` can send to several people and stop on the first reply from the domain. Never add junior staff to pad a company.

## Default libraries

| Need | Use |
|---|---|
| Socrata open data (licenses, restaurant health data) | `sodapy` |
| SEC EDGAR / Form D (funded US startups) | `edgartools` |
| Email verification | A simple MX + SMTP checker, `reacherhq/check-if-email-exists` at scale, or Hunter's verifier where port 25 is blocked |
| Website to structured data, positioning read | `crawl4ai`, `firecrawl` (self-hostable) |
| Yelp (any local category) | Yelp Fusion API (free tier) |
| "Running paid" signal | Meta Ad Library API (free) |
| Product launches | Product Hunt GraphQL API |
| UK firmographics | Companies House API |
| Google Maps (only when a niche needs it) | Outscraper or Apify on demand. Don't build it in-house. |

Full source catalog, methods and compliance notes: `references/source-playbook.md`.

## How to add a new source adapter

1. **Find the source.** Check `references/source-playbook.md` first. If it doesn't cover your ICP, ask three questions: what would this business **join** to be credible, what must it **register** with, and where would its **customers look** for it. Rank candidates by the qualification ladder: paid membership beats a credential registry, which beats a statutory register, which beats a claimed self-listing. Never use derivative aggregators like Hotfrog, Cylex or Opendi. They scrape other directories and carry no signal.
2. **Run the access-check protocol** before writing a parser. Check terms and `robots.txt`, confirm the page has real content (not a JS shell), fingerprint the platform, then probe for structured data (WP REST → embedded search index → sitemap → JSON-LD → admin-ajax). Classify the source as open, needs-browser or blocked. The full protocol is in `references/source-playbook.md`.
3. **Sample 25 to 50 rows and measure field fill rates** (website, phone, email, category) before a full run. Small samples mislead in both directions. Use the sample to decide whether to proceed, then trust only the full run's numbers.
4. **Write a `pull()` that returns records in the common schema**, with a clear dedupe key. **Scope extraction to the record, not the page.** Listing pages render related listings and map popups that carry other businesses' contacts, and a page-wide regex misattributes them silently. Check it by comparing unique-value counts against row counts.
5. **Reconcile the row count against the total the source reports, and fail loudly on a mismatch.** A page count can reflect the response limit instead of the data. Algolia caps results at 1,000 and can report `nbPages: 1` next to `nbHits: 2210`, so a page-walk exits cleanly after silently dropping 45% of the directory. Assert `len(rows) == reported_total` inside `pull()`. On a mismatch, slice the query into buckets under the cap (facet first, then bisect a numeric attribute) and walk each one. A plausible-looking row count is the dangerous failure, because nothing errors.
6. **Use the right library** from the table above instead of raw HTTP where one exists.
7. **Preserve and document** (see below), and record the access verdict, including negative results.
8. **Wire it into your orchestrator** and register it as a source.

## Enrichment and verification (waterfall, cheapest first)

1. **Start with free source fields.** Open data often gives the owner's name, phone and address. Startup sources (YC company JSON, launch posts) often give founder names, LinkedIn URLs and personal addresses.
2. **Scrape the company's own contact, about and team pages** for emails, phones and every founder-level name.
3. **Run a waterfall for named contacts.** Build one script that tries every connected source in order for each contact and stops at the first work email on the company's own domain. A typical order is the email already on the row, hand exports (Clay tables, Apollo or SalesQL browser extensions), Prospeo by LinkedIn URL, SalesQL by LinkedIn URL, Prospeo by name on each company domain, SalesQL by name and company, Hunter by name, and finally the company's confirmed email pattern (first@, first.last@) for contacts still missing one, marked `pattern_unverified`. Cache every source's answers and cap paid matches per source. Add each new provider as one more step in the same script, never as a separate one-off. An optional "collect all" mode keeps querying after a hit to gather phones and extra emails for high-value contacts.
4. **Search every domain the company emails from**, not only its website. New or rebranded companies often email from a different domain (a founders@ inbox in a launch post, a pre-rebrand name). Keep those in `alt_domains`. Reject an email on a domain the company doesn't use (a founder's previous employer, a university). When two contacts at one company return the same unlisted domain, surface it in a `domain_hint` field for a human to check.
5. **Use connectors for the gaps.** If your agent has Clay or Apollo connectors (MCP), use them for contacts the scripted steps miss and for finding more decision-makers at a company. Batch Clay at 20 contacts or fewer and fall back to the scripts when it times out. Ask before any lookup that spends credits in bulk. Never use a tool's sequence or contact-creation features, because they enroll people in outreach. Write every email a connector or browser extension returns to a CSV (`full_name`, `domain`, `email`, `source`, `status`) and feed it back into the waterfall, so those results get the same domain check and labels as everything else.
6. **Collect fallback addresses separately.** New founders often have no company inbox yet but still read a personal inbox, a university address or a work address at another company. Collect these in a separate `fallback_email` field with a `fallback_type` (personal, edu, other_current, other_ended, other_unknown). Never put them in `email`, so the main send list never includes them. They go to a separate low-volume campaign where bounces are watched, because addresses at companies a person has left often bounce.
7. **Widen the surface per company.** Aim for every reachable decision-maker, each with every email and phone the waterfall found (`emails_all`, `phones`). Outreach then has more than one way into the company, plus a second channel (LinkedIn, phone) when email fails.
8. **Use Hunter.io for small businesses and for verification.** Hunter's domain search returns addresses it indexed from the open web, and its email finder resolves a name. Its verifier runs the SMTP check from Hunter's servers, so it works where port 25 is blocked on your machine. Run a control check on each domain first: a made-up address must come back invalid before any "valid" result counts.

### Contact standard: two verified named people per company

Role inboxes (`info@`, `contact@`, `hello@`, `support@`, `service@`, `sales@`) don't count. They usually reach support or a low-attention queue. Keep them in `emails_all` for reference, but a company is only send-ready once it has at least two verified emails for named decision-makers. Pick the founder or owner first, then the function head who owns the problem, then a hiring manager or senior peer.

"Verified" means a second, independent source confirmed the address. A single source's own result is only a candidate. That includes a Clay hit or a SalesQL or Apollo address with a warning icon. It becomes verified when Prospeo, an MX/SMTP check, a second database, or the person's own LinkedIn or site confirms it.

A catch-all domain never verifies a mailbox by itself. A firstname-style address for the right person on the right domain can still be used, but mark it `catch_all_accepted` so it stays a labeled risk. When Prospeo's LinkedIn lookup returns no match, retry by first name, last name and company website. Treat any address that breaks the company's verified email pattern as unverified until a second source confirms it.

If you have a browser agent, the SalesQL and Apollo extensions can close gaps the APIs miss. Reveal a single-hit result even when its pre-reveal count looks wrong, because single hits often show nothing in the count and still resolve. For brand-new founders, expect mostly personal, university and prior-company addresses, which are fallback material.

### When every enrichment tool comes back empty

Work this ladder in order before giving up:

1. **The person's public footprint.** Look at other sites they run (coaching, course or product sites often publish the founder's own address), press release media contacts, chamber of commerce and BBB listings, Instagram and Facebook email buttons, Google Business Profile, job posts, and search queries such as `"@domain.com"` (PDFs, bids, vendor lists, event pages).
2. **Find the second person.** Run a LinkedIn people search on the company name, read the company's team and about pages, and check state business registries (officers and managers) and professional license lookups.
3. **Guess and verify.** Generate the likely formats for each named person (first@, first.last@, flast@, firstl@, plus nicknames such as jackie@ for Jacqueline) and run them through a verifier, with a control check on the domain first. A guess counts as verified only when it comes back valid on a domain that rejects a made-up address. On a catch-all domain, label it risky and use it only as the second touch.
4. **Only when no second person exists anywhere** (an owner-operated business with no staff online), make the second touch a phone call or a social DM asking for the owner, and say so plainly in the file.

### Verify before hand-off

Use an MX/SMTP checker where port 25 is open, Hunter's verifier where it isn't, or the send tool's own verifier (Smartlead verifies on upload). Treat catch-all, blocked and `pattern_unverified` as risky, never valid. The one exception is the flagged `catch_all_accepted` address used to reach the two-person minimum.

## Signal detection and scoring

- **Detect every applicable need signal per lead, not just the first match.** Run every signal check that applies to the source or vertical against each lead and record all hits in `signals`. Stopping early closes off angles that a different or combined signal would have opened. Choosing which signal leads the message happens downstream, at `outbound-engine`'s human review step. This skill's job is complete detection.
- **Score** = fit (ICP match) × signal strength × reachability (verified contact) × freshness (how recent the trigger is). Score independently of which signal ends up leading the message.
- **Have a human confirm the top-scored leads** before any pitch. A small, well-fit list beats a big, misclassified one. A reply-first sequence caps the cost of a misclassification at one wrong email.

## Compliance

Prefer official APIs and government or open data over scraping. For gray-area scraping, use residential proxies and rate limits, cache responses, and never touch login-walled data. Don't scrape LinkedIn or Crunchbase behind their walls. Use their APIs, or a browser agent under your own logged-in session, as with Clutch. Store only business and public professional data. Cold-email sending law (CAN-SPAM, GDPR and PECR, CASL) is the sender's concern, so it lives in `outbound-engine`.

## Preservation and documentation (every time)

1. Save runnable code to a version-controlled repo (for example a `prospect-engine/` project folder). Never leave it in a temporary scratch folder.
2. Keep one readable doc per tool that explains what it does and shows the code in fenced blocks.
3. Keep an index of every scraper and data tool you've built, with a one-line description and its location.

The code is the asset. The CSVs are just outputs.

## Related skills

- `outbound-engine`: the send half (personalize, QA, send, file replies).
- A cold-email copy skill: writes the copy and sequences this list feeds.
- A Clay-specific skill, if you use one: an alternative for the enrichment and signal step.

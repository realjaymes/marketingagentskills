# Source Playbook

The catalog of prospect sources, the library or method for each, and where the free-versus-paid line sits. Prefer sources higher in each list (free API or government data). Load this when choosing where to pull a list from.

## Finding a source for an ICP this catalog doesn't cover

Every business worth pitching has already put itself on a list. Three questions find it: what would this business have to **join** to be credible in its category, what is it legally required to **register** with, and where would its **customers look** for it.

There's a shortcut too. Any directory-submission or local-SEO plan for a business is a source map for that business's whole category, read backwards. The places a business should get listed are the places you'll find its competitors.

## The qualification ladder (rank sources by what it cost to appear)

Sources are not interchangeable. What it cost a business to appear somewhere is what qualifies the list.

| Tier | Source type | Signal | Use for |
|---|---|---|---|
| 1 | **Paid membership bodies**: chambers, industry and trade associations, franchise bodies, professional societies | Strongest. Paid and usually verified. Membership is a decision to buy visibility and relationships. | B2B offers. The best source for firms that don't show up on maps. |
| 2 | **Credential and certification registries**: accreditation bodies, licensing boards | Capability is proven, commercial traction is not | Verticals where a credential defines the business |
| 3 | **Statutory registers**: SEC EDGAR, Companies House, ABN, FMCSA, EPA ECHO, SAM.gov, state Secretary of State | None (registration is compulsory), but authoritative, complete and free | Defining the universe, dedupe, verification, enrichment |
| 4 | **Claimed self-listings**: Google Business Profile, Yelp, LinkedIn, Clutch, G2, Product Hunt | Weak but real (claiming takes effort) | Consumer-facing local businesses. The best coverage for local verticals. |
| 5 | **Derivative aggregators**: Hotfrog, Cylex, Opendi, Bizadee, USDirectory, CallUpContact | **None.** They scrape other directories, and the business never chose to be there. | **Avoid.** Stale, duplicated, often wrong. Fine for SEO backlinks, worthless as prospect data. |

Tier 5 is where volume tempts you and where lists get quietly ruined. Size is not coverage.

## Access-check protocol (run before building any adapter)

1. **Terms and `robots.txt`.** Technical availability is not permission.
2. **Real-content check.** Check byte size and keyword density on a fetched page. A clean `robots.txt` on a JavaScript shell looks identical to an open source. This catches cloud and SaaS partner directories that render everything client-side.
3. **Platform fingerprint.** A small script that detects the directory platform (GrowthZone/ChamberMaster, WordPress, hosted SaaS) tells you which adapter to reuse. It generalizes past chambers to any directory.
4. **Structured-data probe, in order:** WP REST (`/wp-json/wp/v2/types` reveals custom post types like `at_biz_dir` or `member-directory`) → a search index embedded in the page's JavaScript (Algolia indexes are common, including on the YC directory) → `sitemap.xml` → JSON-LD → `admin-ajax.php`. One of these usually turns a 96-page crawl into a dozen API calls.
5. **Unusual markup is not a wall.** A directory whose links are `<option value>` or `<li data-cy>` blocks instead of plain `<a href>` tags is still open. It just needs a different selector.
6. **Scope extraction to the record.** Listing pages render related listings, map popups and sidebars that carry *other* businesses' contacts, and a page-wide regex misattributes them silently. Check it by comparing unique-value counts against row counts.
7. **Sample 25 to 50 rows and measure field fill rates** before a full run. In one chamber roster, a 25-row sample read 72% website and 52% phone, and the full 1,152 rows came in at 86% and 71%. Sample to decide whether to proceed, then trust only the full run.
8. **Reconcile the row count against the total the source reports.** Paginated sources report two numbers, a page count and a total record count, and the page count can reflect the response limit instead of the data. Algolia caps any result set at 1,000 records, then reports `nbPages: 1` next to `nbHits: 2210`. A page-walk collects 1,000 rows, believes it reached the last page, and exits cleanly. One association adapter did this for weeks, returning 45% of the directory with no error and a believable row count. Assert `len(rows) == reported_total` at the end of every pull. When they disagree, slice the query into buckets under the cap (facet first, then bisect a numeric attribute) and walk each one.
9. **Record the verdict** (open, needs browser, or blocked) in an access log. A negative result saves the next attempt.

## Membership and association sources (Tier 1, the B2B workhorse)

- **Chambers of commerce** work at two levels. The national chamber directory finds the chambers (the US Chamber directory lists about 7,370 chambers across 54 states and territories). Each chamber's own member roster then finds the businesses. One UK chamber roster returned 1,152 members at 86% website and 71% phone, mostly B2B (freight forwarders, professional services, manufacturing, legal, engineering).
- **The platform is the constraint, not the country.** Across a sample of 158 chambers: GrowthZone/ChamberMaster 19%, WordPress REST with a member post type 15%, WordPress needing an HTML parse 32%, custom or hosted SaaS 34%. Three adapters reach about two-thirds of them. A member-directory URL was findable on 77% of US chambers and 89% of UK chambers.
- **Country coverage.** US: about 7,370 chambers, open. UK: 61 accredited chambers through the British Chambers of Commerce store-locator REST endpoint, split cleanly into UK and international. Canada: 400+ chambers and boards of trade. The national list needs a browser, but local rosters are often open (Calgary returned 2,025 members via REST). Australia has no chamber federation, so use the eight state and territory chambers plus the national industry associations.
- **Industry and trade associations** generalize the same pattern per vertical: IFA (franchise), AESC (executive search), NFDA, ARA, NCRA, HBMA, NAID/i-SIGMA, NPA, NAA. A vertical-specific body is often the only structured list of a niche B2B category.

## Stream A: funded tech startups (global)

**Tier 1, structured and free:**

- **SEC EDGAR Form D** ⭐. Every US company raising a private round files a Form D. It's official, free and structured. Library: `edgartools` (`set_identity`, `get_filings(form="D", filing_date="start:end")`). You get company, CIK and date directly. The offering amount needs parsing from the filing XML.
- **UK Companies House.** A free API covering every UK company, its officers and filings. Good firmographics.
- **Y Combinator directory.** An Algolia-backed public search index you can query directly, no proxy. Confirm the current app ID and index name in the browser's network tab at build time.
- **VC and accelerator portfolio pages**: a16z, Sequoia, Accel, Index, Bessemer, Techstars, 500, Antler, Seedcamp. One thin adapter per firm. They want their portfolio seen.
- **Product Hunt.** A free GraphQL API. A launch is a trigger for a launch-plan offer.

**Tier 2, funding news (fetch, then LLM extraction with `crawl4ai` or `firecrawl`):**

- TechCrunch, Sifted, Tech.eu, EU-Startups, UKTN (Europe); The Big Deal, Disrupt Africa, Briter (Africa). Use RSS where it exists. Otherwise fetch the page and have an LLM extract company, amount, stage, date and investors.

**Tier 3, gated databases (enrichment only, respect their terms):** Crunchbase, Dealroom, Tracxn, Growjo, Latka. Use official APIs and free tiers. Never scrape login-walled data.

## Stream B: local US businesses and contractors (any vertical)

Category and geography are inputs, so this works for any vertical.

- **Socrata and open-data business-license datasets** ⭐. Most US cities and states publish active licenses (name, address, license type, date) on Socrata portals with free APIs. One `sodapy` adapter unlocks hundreds of datasets. Filter by license type for any vertical. For restaurants, city health-department inspection datasets (name, address, phone) follow the same pattern.
- **State contractor licensing boards.** One board usually lists HVAC, electrical, plumbing, roofing and general contractors together. Free and authoritative.
- **State Secretary of State business registries.** The legal entity, and often the owner or registered agent's name, which helps personalization.
- **Yelp Fusion API** (free tier). Any category, plus reviews, which feed the `{{gap}}` signal. Fusion does not return the business's own website, only the Yelp URL. Get the website through a search step (Serper, Google Places) or skip to phone or Instagram.
- **Licensed-profession registries per vertical**, such as NPPES or CMS Care Compare for healthcare (free API). Add one per campaign as needed. Don't build the whole engine around a single vertical.
- **Google Maps.** Paid, on demand through Outscraper or Apify, only when the free sources cover a vertical poorly. Don't build it in-house, because Maps fights scrapers hardest.

## Adjacent segment: B2B agencies and service firms (Clutch)

- **Clutch.co** covers dev shops, design and UX, marketing agencies, IT and cybersecurity, AI and data, and business services (consulting, BPO, staffing, accounting, legal, virtual assistants). It has rich firmographics for qualification: category, reviews, hourly rate, minimum project size, location.
- **Method:** use a browser agent under your own logged-in session. Filter by category and location, then export. Don't run a headless or proxy scrape. This is a manual browser pull, not a script.

## Signal sources (the hard, valuable part)

- **Weak positioning:** fetch the homepage (`crawl4ai` or `firecrawl`) and have an LLM score clarity and differentiation.
- **Running paid ads:** Meta Ad Library API (free), Google Ads Transparency Center, TikTok Ad Library.
- **Product launch:** Product Hunt, the company's changelog, blog or press page.
- **Moving upmarket:** the pricing page gains a "contact sales" or enterprise tier, or enterprise logos appear.
- **Tech stack:** self-hosted Wappalyzer or BuiltWith. **Traffic:** Similarweb (limited free tier).

## Contact enrichment ladder (cheapest first)

Free source fields (owner, phone, address) → a free scrape of the website's contact page (emails) → manual research → selective paid lookups (Prospeo, Apollo, LinkedIn, social profiles) by business type → verification with an MX/SMTP checker or `reacherhq/check-if-email-exists` at scale.

## Open-source repos worth modelling

`afeld/sodapy` (Socrata), `dgunning/edgartools` (EDGAR), `reacherhq/check-if-email-exists` (verifier), `unclecode/crawl4ai` and `firecrawl/firecrawl` (LLM fetch and extract), `mishushakov/llm-scraper` (extract to a schema), `gosom/google-maps-scraper` and `omkarcloud/google-maps-scraper` (Maps, if you ever need it), `lorien/awesome-web-scraping` (the master list). To find more: `gh search repos "<query>" --language=python`.

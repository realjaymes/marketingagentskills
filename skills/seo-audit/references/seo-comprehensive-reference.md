---
title: Comprehensive SEO Reference
purpose: Deep technical reference for the seo-audit skill. Covers SEO from first principles to senior-level execution across foundations, strategy, technical SEO, on-page and content SEO, off-page SEO, analytics, algorithm updates, AI search (GEO/AEO), engagement playbooks, scenario playbooks, cross-functional collaboration, and the complete tool stack.
tags: [seo-reference, handbook, technical-seo, on-page, off-page, analytics, geo, aeo]
---

# Comprehensive SEO Reference

**Purpose.** Deep technical depth for the seo-audit skill. Load sections on demand when an audit question needs more than SKILL.md's overview. The reference is organized as a progressive document (Part I to Part XII) so you can read end to end to build a mental model, or scan individual sections when executing a specific audit phase.

**When to reference which section:**

- **Part I (Foundations), II (Strategy)** — framing for audit kickoffs, stakeholder conversations
- **Part III (Technical SEO)** — the deepest section; reach here for crawlability, indexation, rendering, Core Web Vitals, site architecture, status codes, mobile-first, schema, international, migrations
- **Part IV (On-Page / Content SEO)** — keyword research methodology, intent mapping, clustering, topical authority, E-E-A-T, on-page optimization, content tools, programmatic SEO, refresh strategy
- **Part V (Off-Page)** — link value frameworks, digital PR, broken link building, unlinked mentions, directories, toxic links
- **Part VI (Analytics, Tracking, Reporting)** — GA4, GSC, Looker Studio, BigQuery for SEO, rank tracking, reporting frameworks
- **Part VII (Algorithm Updates)** — diagnosing traffic drops after algorithm events, recovery playbooks
- **Part VIII (GEO / AEO)** — optimizing for AI search citation (note: the dedicated `ai-seo` skill covers this more tactically; this section is for audit-context depth)
- **Part IX (Engagement Playbooks)** — day-by-day execution plans from diagnosis through scale
- **Part X (Scenario Playbooks)** — direct diagnostic workflows: traffic drop, ranking drop, new site launch, content refresh campaign, link audit, international expansion
- **Part XI (Cross-Functional Collaboration)** — developer, content, paid media, sales, and stakeholder collaboration patterns
- **Part XII (Tool Stack)** — every major SEO tool by category with when-to-use guidance

The reference ramps quickly from foundations. Each section is self-contained.

---

## Table of Contents

**Part I: Foundations**
1. [[#How Search Engines Work]]
2. [[#The SEO Mental Model]]
3. [[#The Four Pillars of Modern SEO]]
4. [[#What Good SEO Looks Like]]
5. [[#Glossary]]

**Part II: Strategy Layer**
6. [[#Defining SEO Success]]
7. [[#The Revenue-First SEO Lens]]
8. [[#Setting SEO Goals]]
9. [[#Building an SEO Roadmap]]
10. [[#Forecasting Organic Growth]]
11. [[#SEO for Different Business Types]]

**Part III: Technical SEO**
12. [[#Crawlability]]
13. [[#Indexation]]
14. [[#Rendering and JavaScript SEO]]
15. [[#Core Web Vitals]]
16. [[#Site Architecture]]
17. [[#Status Codes and Redirects]]
18. [[#Mobile-First Indexing]]
19. [[#Schema Markup]]
20. [[#International SEO]]
21. [[#Site Migrations]]

**Part IV: On-Page and Content SEO**
22. [[#Keyword Research]]
23. [[#Search Intent]]
24. [[#Keyword Clustering]]
25. [[#Content Strategy and Topical Authority]]
26. [[#Experience, Expertise, Authoritativeness, Trustworthiness (E-E-A-T)]]
27. [[#On-Page Optimization]]
28. [[#Content Optimization Tools]]
29. [[#Programmatic SEO]]
30. [[#Content Refresh Strategy]]

**Part V: Off-Page SEO**
31. [[#Link Value Frameworks]]
32. [[#Digital Public Relations (PR)]]
33. [[#Broken Link Building]]
34. [[#Unlinked Brand Mentions]]
35. [[#Directory and Citation SEO]]
36. [[#Toxic Links and Disavow]]
37. [[#Brand Building as SEO]]

**Part VI: Analytics, Tracking, Reporting**
38. [[#Google Analytics 4 (GA4)]]
39. [[#Google Search Console (GSC)]]
40. [[#Looker Studio Dashboards]]
41. [[#BigQuery for SEO]]
42. [[#Rank Tracking]]
43. [[#Reporting Frameworks]]

**Part VII: Algorithm Updates**
44. [[#Algorithm Update History]]
45. [[#Diagnosing an Algorithm Hit]]
46. [[#Recovery Strategies]]

**Part VIII: Generative Engine Optimization (GEO) and Answer Engine Optimization (AEO)**
47. [[#How AI Search Engines Work]]
48. [[#Optimizing for AI Citation]]
49. [[#Measuring AI Search Visibility]]

**Part IX: Engagement Playbooks**
50. [[#Days 1 to 14 – Diagnosis]]
51. [[#Days 15 to 30 – Quick Wins]]
52. [[#Days 30 to 90 – Roadmap Execution]]
53. [[#Month 3 to 6 – Compounding Work]]
54. [[#Month 6+ – Scale and Expansion]]

**Part X: Scenario Playbooks**
55. [[#Traffic Drop Diagnosis]]
56. [[#Ranking Drop Diagnosis]]
57. [[#New Site Launch]]
58. [[#Content Refresh Campaign]]
59. [[#Link Audit]]
60. [[#International Expansion]]

**Part XI: Cross-Functional Collaboration**
61. [[#Working with Developers]]
62. [[#Working with Content Teams]]
63. [[#Working with Paid Media Teams]]
64. [[#Working with Sales Teams]]
65. [[#Working with Stakeholders]]

**Part XII: Tool Stack**
66. [[#Complete SEO Tool Reference]]

---

# Part I: Foundations

## How Search Engines Work

Search engines operate in four sequential steps. Every SEO decision maps back to one of these.

### 1. Crawl

Search engines send automated programs called crawlers or bots (Googlebot is Google's) to discover URLs on the open web. Googlebot follows links from known URLs to new ones. It respects `robots.txt` directives and rate limits itself to avoid overloading servers. The amount of crawling Googlebot does on a given site is called the **crawl budget**.

### 2. Render

For sites that rely on JavaScript (JS) to build their content, Googlebot has to execute the page in a simulated browser to see the final HyperText Markup Language (HTML). This step is called **rendering**. Rendering is expensive, so Googlebot defers it for many pages and schedules it separately. If rendering fails or is delayed, the rendered content may not be indexed.

### 3. Index

After crawling and rendering, Googlebot parses the content and decides whether to store it in the index. The index is Google's searchable database. Being crawled does not guarantee being indexed. Pages that Google considers low quality, duplicate, thin, or blocked via `noindex` directives are excluded.

### 4. Rank and Serve

When a user submits a query, Google ranks indexed pages using hundreds of signals and serves the top results on a Search Engine Results Page (SERP). The signals fall into clusters: relevance (does this page answer this query?), authority (do other sites vouch for this page?), experience (does the page load fast, is it mobile-friendly?), and freshness (is this the most current information?).

**Mental model for SEO work:** Every tactic you deploy influences one of these four steps. A technical audit improves crawlability and indexation. Content strategy improves relevance. Link building improves authority. Core Web Vitals optimization improves experience signals.

---

## The SEO Mental Model

SEO works because search engines are two-sided markets. Users bring queries; sites bring content. Google's job is to match query to content in a way that keeps users coming back. SEO is the practice of shaping your site so that Google matches your content to the queries your customers already ask.

The practice has three enduring truths:

1. **SEO is a demand capture channel, not a demand generation channel.** People have to already be searching for something related to your business before you can rank for it. SEO rewards businesses whose customers type things into Google.
2. **SEO compounds.** Rankings built today continue paying out for months or years. A well-structured content asset that ranks on page one of Google drives traffic indefinitely without additional spend. This is why SEO outperforms paid media on cost per acquisition at scale, but only after the investment period.
3. **SEO rewards alignment, not hacks.** Long-term winners build sites that genuinely serve the query better than competitors. Short-term hacks get penalized or decay. Strategy beats tactics.

**The three questions every SEO decision answers:**

1. Can Google find this content? (Crawlability)
2. Can Google index this content? (Indexability)
3. Will Google rank this content above the alternatives? (Relevance, authority, experience)

If the answer to any of these is "no," fix that first before anything else.

---

## The Four Pillars of Modern SEO

Traditional SEO thinking grouped everything under three pillars: Technical, On-Page, and Off-Page. Modern SEO adds a fourth: Generative Engine Optimization and Answer Engine Optimization (GEO and AEO). A full-stack SEO operator works across all four.

### Pillar 1: Technical SEO

The infrastructure layer. Crawlability, indexation, rendering, site architecture, Core Web Vitals, schema markup, international configuration, security, status codes. If the technical foundation is broken, no amount of content or links will fix rankings. Technical is usually where the fastest wins live on neglected sites.

### Pillar 2: On-Page SEO (Content)

What's actually on the page. Keyword research, search intent mapping, title tags, meta descriptions, heading structure, content depth, internal linking, image optimization, content freshness. On-page is where you compete with ranking intent directly.

### Pillar 3: Off-Page SEO (Authority)

Signals from the rest of the web about your site. Backlinks, brand mentions, citations, reviews, Digital Public Relations (PR). Off-page is how Google decides your site deserves to rank above equally-optimized competitors.

### Pillar 4: GEO and AEO (AI-Search Visibility)

The newest pillar. Optimizing for citations in AI-generated answers (ChatGPT, Perplexity, Google AI Overviews, Gemini, Copilot). Shares most tactics with traditional SEO (entity clarity, structured answers, authoritativeness) but adds a layer for AI-specific levers: original data, topical comprehensiveness, schema.org entities, brand synonymy.

**Budget allocation across pillars (rough heuristic for senior SEO planning):**

| Stage | Technical | On-Page | Off-Page | GEO/AEO |
|---|---|---|---|---|
| Neglected site, new engagement | 45% | 35% | 15% | 5% |
| Healthy site, scale mode | 15% | 40% | 30% | 15% |
| Enterprise site, mature | 20% | 30% | 30% | 20% |

Adjust based on site diagnosis. No fixed formula.

---

## What Good SEO Looks Like

A strong SEO program has these traits:

1. **Diagnosis-first.** Every action follows from data, not vibes. Before fixing, measure.
2. **Commercially framed.** Rankings and traffic are leading indicators. Pipeline, qualified leads, and revenue are the real metrics.
3. **Cross-functional by default.** SEO alone can't ship anything. Developers implement, content teams execute, paid teams coordinate spend, sales teams route leads.
4. **Documented.** Frameworks, Standard Operating Procedures (SOPs), playbooks. Knowledge lives in documents, not heads.
5. **Forecasted.** Projected outcomes at 30, 90, 180 days. Leadership can't fund what it can't predict.
6. **Reported in business language.** Executives don't care about impressions. They care about pipeline value, client retention, and agency margin.
7. **Defensible.** Every tactic can be explained and justified. No shortcuts that expose the site to penalties or reputational risk.

**Anti-patterns to avoid:**

- Optimizing for metrics that don't map to revenue (position tracking without conversion tracking)
- Tactic-first thinking (chasing the latest SEO trend without a strategic frame)
- Reporting without narrative (sending a dashboard without explaining what it means)
- Hoarding audit findings without prioritization (drowning stakeholders in 200-item checklists)

---

## Glossary

Every term used in this handbook, in plain English.

**Anchor text:** The clickable text of a hyperlink. Google uses anchor text as a signal for what the linked page is about.

**Backlink:** A hyperlink from one site to another. Also called "inbound link" or "external link."

**Bounce rate:** The percentage of sessions where a user leaves without interaction. Increasingly replaced in Google Analytics 4 (GA4) by engagement rate.

**Canonical tag:** An HTML element (`<link rel="canonical" href="...">`) that tells search engines which URL is the master version when duplicate or near-duplicate content exists.

**Cascading Style Sheets (CSS):** The styling language for web pages. Affects how content looks.

**Click-Through Rate (CTR):** The percentage of users who click a search result after seeing it. CTR = Clicks / Impressions.

**Content Delivery Network (CDN):** A network of servers that caches static assets (images, CSS, JavaScript) close to end users for faster load times.

**Content Management System (CMS):** Software that manages the creation, editing, and publishing of digital content. Examples: WordPress, Webflow, Contentful, Sanity, Shopify.

**Core Web Vitals (CWV):** Google's standardized measurement of user experience. Three primary metrics: Largest Contentful Paint (LCP), Interaction to Next Paint (INP), Cumulative Layout Shift (CLS).

**Crawl budget:** The number of URLs Googlebot will crawl on your site within a given timeframe. Relevant for sites with more than 10,000 URLs.

**Crawler:** An automated program that visits web pages. Googlebot is Google's crawler.

**Cumulative Layout Shift (CLS):** A Core Web Vital. Measures unexpected layout shifts (elements jumping around as the page loads). Target under 0.1.

**Disavow file:** A file submitted to Google Search Console listing backlinks you don't want Google to consider when evaluating your site. Used to defend against toxic or spammy links.

**Domain Authority (DA):** Moz's proprietary metric for estimating a domain's authority. Scale 0 to 100. Not a Google ranking factor; useful as a comparative metric.

**Domain Rating (DR):** Ahrefs's equivalent of DA. Scale 0 to 100.

**Duplicate content:** Substantially similar content accessible at multiple URLs. Confuses search engines about which version to rank.

**E-E-A-T:** Experience, Expertise, Authoritativeness, Trustworthiness. A framework Google uses to evaluate content quality, particularly for Your Money or Your Life (YMYL) topics like health, finance, and legal.

**Entity:** A thing or concept that can be uniquely identified. Google uses entities in its Knowledge Graph. A person, place, organization, product, or event can be an entity.

**Entity optimization:** Making your brand, authors, or products clearly identifiable as entities to search engines through schema, consistent naming, and cross-web mentions.

**Experience, Expertise, Authoritativeness, Trustworthiness (E-E-A-T):** See above.

**Faceted navigation:** Filters on e-commerce or listing sites (size, color, price) that generate URLs combining multiple filter states. Can create infinite crawl waste if not controlled.

**Featured snippet:** A SERP feature that displays a direct answer at the top of results. Sourced from a ranking page.

**GA4 (Google Analytics 4):** Google's event-based analytics platform, replacing Universal Analytics (UA).

**Generative Engine Optimization (GEO):** Optimizing content for citation in AI-generated answers.

**Google Search Console (GSC):** Google's free tool showing how your site performs in Google Search. Tracks impressions, clicks, rankings, indexation status.

**Hreflang:** An HTML attribute (`<link rel="alternate" hreflang="...">`) indicating the language and region of a page. Used for international sites.

**Impressions (GSC):** The number of times a URL appeared in search results, regardless of whether it was clicked.

**Index:** The database where Google stores pages it has crawled and deemed worth ranking. Being crawled does not mean being indexed.

**Indexation rate:** The percentage of submitted URLs that are indexed by Google. Tracked in GSC Coverage report.

**Interaction to Next Paint (INP):** A Core Web Vital. Measures responsiveness to user interaction. Replaced First Input Delay (FID) in 2024. Target under 200 milliseconds.

**Internal linking:** Hyperlinks from one page on your site to another. Distributes link equity and signals page importance.

**JavaScript Object Notation (JSON):** A lightweight data format, used in structured data (JSON-LD).

**Keyword:** A word or phrase users type into a search engine. What SEO historically optimized for.

**Keyword clustering:** Grouping related keywords that share intent and SERP overlap into a single content target.

**Largest Contentful Paint (LCP):** A Core Web Vital. Measures loading speed. Target under 2.5 seconds.

**Log file:** A server-generated record of every request made to the site. Log file analysis reveals exactly which URLs Googlebot crawls.

**Meta description:** An HTML tag (`<meta name="description">`) summarizing page content. Not a direct ranking factor but influences click-through rate.

**Meta robots tag:** An HTML tag (`<meta name="robots">`) telling search engines how to handle a page (index, noindex, follow, nofollow, etc.).

**Mobile-first indexing:** Google primarily uses the mobile version of your site for indexing and ranking.

**Nofollow:** An attribute on a link (`rel="nofollow"`) telling search engines not to pass PageRank through it.

**Off-page SEO:** Signals from outside your site (backlinks, brand mentions, reviews).

**On-page SEO:** Everything on the page itself (content, title tags, headers, internal links).

**Organic traffic:** Traffic from non-paid search results.

**PageRank:** Google's original algorithm for estimating page authority based on inbound links. Still conceptually relevant, no longer publicly visible.

**Pagination:** Splitting long content across multiple numbered pages.

**Programmatic SEO:** Creating large numbers of pages from structured data templates.

**Rank tracker:** A tool that monitors your site's position for target keywords. Examples: Ahrefs, Semrush, Accuranker.

**Redirect:** An instruction from one URL to another. 301 is permanent; 302 is temporary.

**Rendering:** The process of executing JavaScript to produce the final HTML. Googlebot has a rendering queue.

**Retrieval Augmented Generation (RAG):** The architecture behind most AI answer engines. The AI retrieves relevant content from an index, then generates a response grounded in that content.

**Robots.txt:** A text file at the root of your domain telling crawlers which URLs they can or cannot access.

**Schema markup:** Structured data added to HTML (usually in JSON-LD format) that describes entities on the page to search engines.

**Search intent:** The underlying goal behind a search query (*informational* – to learn: what is, how to, *navigational* – to find: login, support, *commercial* – to research: best, top, compare, transactional – to buy: buy, price, checkout, order).

**Search Engine Results Page (SERP):** The page of results Google shows for a query.

**SERP feature:** Any non-standard element on a SERP (featured snippet, People Also Ask, knowledge panel, local pack, site links, video carousel).

**Sitemap:** An XML file listing the URLs on your site. Submitted to search engines to aid discovery.

**Soft 404:** A page that returns a 200 OK status code but tells the user the content doesn't exist. Creates crawl waste.

**Structured data:** Machine-readable markup (usually schema.org in JSON-LD) that helps search engines understand page content.

**Time to First Byte (TTFB):** The time from user request to the first byte of response from the server. Target under 800 milliseconds.

**Topical authority:** The degree to which Google considers your site an authoritative source on a specific topic.

**Universal Resource Locator (URL):** The address of a page on the web.

**XML (eXtensible Markup Language):** A structured text format. Used for sitemaps.

**Your Money or Your Life (YMYL):** Topics that can directly affect a user's health, finances, safety, or happiness. Google applies higher quality standards to YMYL content.

---

# Part II: Strategy Layer

## Defining SEO Success

Good SEO programs measure success at four layers. Weak programs report only on the first layer.

### Layer 1: Visibility

- Impressions (how often your pages appear in search)
- Keyword rankings (where you rank for target queries)
- Share of voice (your rankings vs competitors on a keyword set)
- Indexation rate (percentage of submitted URLs indexed)

**Tools:** GSC Performance report, Ahrefs Rank Tracker, Semrush Position Tracking, Accuranker.

### Layer 2: Traffic

- Organic sessions (visits from non-paid search)
- Organic sessions by landing page (which pages bring traffic)
- Organic sessions by country (for international sites)
- Returning vs new organic users

**Tools:** GA4 (Traffic Acquisition report, Landing Page report), Looker Studio Report.

### Layer 3: Conversion

- Form fills from organic
- Trial signups from organic
- Demo requests from organic
- Purchases from organic (for e-commerce)
- Engagement events (downloads, video plays, scroll depth)

**Tools:** GA4 (Events, Conversions, Exploration reports), Looker Studio Report, HubSpot, Salesforce.

### Layer 4: Revenue

- Pipeline value from organic
- Cost per lead from organic vs paid
- Customer acquisition cost (CAC) from organic
- Lifetime value (LTV) of organic customers
- Revenue attributed to organic

**Tools:** HubSpot (Marketing Attribution, Revenue Attribution), Salesforce, custom attribution models.

**Reporting rule:** Always report at Layer 4 when the audience is executive. Layer 1 and 2 are internal or operational. Most SEO reports lose their audience by staying at Layer 1.

---

## The Revenue-First SEO Lens

Every SEO action has a commercial justification. If you can't explain what a piece of work is worth in pipeline or revenue terms, deprioritize it.

### Translating SEO Tactics to Revenue

| SEO Action | Direct Revenue Justification |
|---|---|
| Fix crawl errors | Unlocks indexation for pages that can't currently rank |
| Optimize titles on position 6 to 15 pages | Captures existing demand at lower investment than new content |
| Build a new pillar page | Opens a new topic cluster capable of ranking across multiple keywords |
| Earn 10 digital PR links | Raises domain authority, lifts rankings across the whole site |
| Build a SEO-to-CRM pipeline | Converts organic traffic into qualified sales conversations |
| Speed up Core Web Vitals | Reduces bounce, improves CTR on SERPs that weight user experience |
| Implement Organization schema | Strengthens entity recognition, lifts AI citation odds |
| Refresh decaying content | Recovers lost traffic at near-zero production cost |

Every audit finding you present should answer "So what?" with a commercial rationale, not a technical one.

---

## Setting SEO Goals

Strong SEO goals are specific, timebound, and revenue-linked.

**Weak goal:** "Improve SEO."

**Stronger goal:** "Increase organic sessions by 40% in 6 months."

**Strong goal:** "Add 1,500 qualified leads from organic search in the next 180 days, at a cost per lead below $50, by ranking in the top 5 for 50 commercial-intent keywords in the CRM automation category."

### Goal-Setting Framework

1. **Business goal:** What commercial outcome does this support? (Pipeline, revenue, retention, expansion.)
2. **SEO contribution:** What percentage of the business goal can SEO realistically drive at current maturity?
3. **Leading metrics:** Which visibility and traffic metrics track progress toward the goal?
4. **Time horizon:** 30, 90, 180, 365 days.
5. **Accountability:** Who owns it, who reviews it, how often.

---

## Building an SEO Roadmap

A roadmap organizes work across three horizons: fix, grow, scale.

### Horizon 1: Fix (Weeks 1 to 8)

The "stop the bleeding" phase. Everything that's actively costing rankings or traffic.

- Technical audit findings (critical severity)
- Indexation fixes
- Redirect chain cleanup
- Core Web Vitals triage
- Missing or malformed schema
- Obvious on-page issues (missing title tags, duplicate meta descriptions, broken internal links)
- Quick-win keyword targeting on positions 6 to 15

### Horizon 2: Grow (Weeks 8 to 24)

Adding new capacity on top of a fixed foundation.

- Topical authority build (pillar and cluster architecture)
- Programmatic content
- Digital PR campaigns
- Content refresh cycle for decaying content
- Link reclamation (unlinked mentions, broken backlinks)
- Internal linking strategy overhaul
- GEO and AEO deliverables

### Horizon 3: Scale (Quarter 2+)

Compounding investments that pay off over 6 to 18 months.

- International expansion
- Advanced schema rollout
- Content operations system (templates, SOPs, editorial calendar)
- Backlink acquisition at scale
- Brand-building content
- Advanced reporting and forecasting infrastructure
- Team expansion and mentorship

**Framing line:** "Fix first, so grow has a foundation. Grow, so scale has volume. Scale, so the client has a defensible moat."

---

## Forecasting Organic Growth

Forecasting makes SEO budgetable. Without a forecast, executives treat SEO as speculative.

### Method 1: Keyword-Based Forecasting

1. Pull target keyword list (usually 100 to 500 priority keywords).
2. Get search volume **and Traffic Potential** for each (Ahrefs is the primary source for Traffic Potential; Semrush approximates via Estimated Traffic). Traffic Potential is usually the better number to forecast against — it captures the full traffic the top-ranking page actually earns from the entire keyword cluster, not just the single seed keyword's volume.
3. Estimate ranking position at 3, 6, 12 months based on current position and difficulty.
4. Apply Click-Through Rate (CTR) curve: position 1 is ~28% CTR, position 3 is ~11%, position 5 is ~6%, position 10 is ~2.5%. (Apply to search volume, or use Traffic Potential directly as the position-1 ceiling.)
5. Multiply projected impressions by projected CTR for projected clicks.
6. Apply conversion rate to projected clicks for projected leads or sales.
7. Apply lead-to-revenue ratio for projected pipeline value.

### Method 2: Trend-Based Forecasting

1. Pull last 12 months of organic sessions from GA4.
2. Apply seasonality adjustment.
3. Project forward with assumed lift percentage based on planned work.
4. Apply conversion and revenue multipliers.

### Method 3: Scenario Modeling

Build three forecasts: conservative, base, aggressive.

- **Conservative:** Assume target rankings achieved in 12 months, 70% of projected CTR.
- **Base:** Target rankings in 9 months, 100% of projected CTR.
- **Aggressive:** Target rankings in 6 months, 110% of projected CTR.

Present scenarios, not single-point forecasts. Leadership prefers ranges to point estimates.

---

## SEO for Different Business Types

### Business-to-Business (B2B) Software as a Service (SaaS)

- Focus: bottom-of-funnel (BOFU) intent keywords, comparison queries, integration pages, use-case pages
- Content: gated research, webinars, long-form playbooks
- Links: Digital PR on industry trends, directory placements (G2, Capterra, Clutch)
- Metrics: Marketing Qualified Leads (MQLs), demo requests, trial signups
- Anti-patterns: high-volume top-of-funnel (TOFU) content that doesn't convert

### E-commerce

- Focus: category pages, product pages, filter pages, comparison pages
- Content: buyer guides, size guides, review aggregations
- Links: product reviews, gift-guide placements, influencer mentions
- Metrics: revenue from organic, conversion rate by landing page, return on ad spend (ROAS) comparison to paid
- Technical priorities: faceted navigation control, Core Web Vitals (mobile-first), structured data for product schema

### Local / Services (Dental, Legal, Home Services)

- Focus: local keywords (city, neighborhood), service-specific landing pages
- Google Business Profile optimization
- Reviews management (Google, Yelp, industry directories)
- Local schema markup (LocalBusiness, ProfessionalService)
- Metrics: phone calls, form fills, local pack visibility, review volume

### Content Sites / Publishers

- Focus: topical authority across a breadth of subjects
- News SEO considerations (Top Stories, Google News, publisher schema)
- Ad revenue optimization, ad viewability
- Metrics: sessions, pageviews per session, ad revenue per 1,000 impressions (RPM)

### Marketplaces

- Focus: category pages, location pages, seller pages, product pages
- Programmatic SEO at scale
- User-generated content moderation
- Metrics: GMV (gross merchandise value), new-buyer acquisition cost, seller adoption

**Strategic heuristic:** The mix of tactics shifts; the four layers of measurement (visibility, traffic, conversion, revenue) are constant across business types.

---

# Part III: Technical SEO

## Crawlability

### How Googlebot Crawls

Googlebot discovers URLs through three mechanisms:

1. **Following links** from URLs it already knows
2. **XML sitemap submissions** via GSC
3. **Manual URL submission** via GSC URL Inspection tool or the Indexing API

Once Googlebot knows about a URL, it schedules a crawl based on the site's crawl budget, server response times, and perceived URL importance.

### Crawl Budget

Crawl budget matters for sites with more than 10,000 URLs. Small sites rarely hit crawl-budget limits. For large sites, crawl budget is a real resource.

**Factors that increase crawl budget:**

- High server response speed (low Time to First Byte)
- High-quality, frequently updated content
- High domain authority and external link signals
- Clean site architecture with efficient internal linking

**Factors that waste crawl budget:**

- Redirect chains (especially over 2 hops)
- Faceted navigation creating millions of URLs
- Infinite scroll pagination
- Soft 404s
- Duplicate content variants (HTTP vs HTTPS, www vs non-www, trailing slashes, parameter variants)
- Low-value parameter URLs (session IDs, tracking parameters indexed)
- Broken internal links

### Robots.txt

The `robots.txt` file lives at `yourdomain.com/robots.txt` and tells crawlers what they can and cannot access.

**Syntax basics:**

```
User-agent: *
Disallow: /admin/
Disallow: /cart/
Disallow: /*?sort=
Allow: /admin/public-pages/
Sitemap: https://yourdomain.com/sitemap.xml
```

**Common uses:**

- Block low-value URLs (admin, cart, internal search results)
- Block crawl-wasting parameters
- Specify sitemap location

**Common mistakes:**

- Blocking CSS or JavaScript files needed for rendering (Googlebot must render pages; blocked JS breaks this)
- Blocking entire staging or dev environments with a single `Disallow: /` line that gets accidentally deployed to production (catastrophic)
- Using `Disallow` to prevent indexation (it prevents crawling, not indexation; use `noindex` meta tag for indexation control)

**Testing:** Use the robots.txt Tester in GSC.

### XML Sitemaps

An XML sitemap is a machine-readable index of your priority URLs.

**Rules:**

- Include only canonical, indexable, 200-status URLs
- Do not include `noindex`, redirected, or blocked URLs
- Under 50,000 URLs per file; under 50 MB uncompressed
- Use a sitemap index file when you need more than one sitemap

**Sitemap types:**

- Standard XML sitemap (pages)
- Image sitemap
- Video sitemap
- News sitemap (for Google News sites)

**Best practice:** Segment sitemaps by content type (blog, products, categories, locations) to make indexation issues diagnosable by segment.

**Submission:** Submit each sitemap in GSC. Track indexation by sitemap in GSC Coverage report.

### Log File Analysis

The single most powerful crawl diagnostic. Log files record every request made to your server, including every Googlebot visit.

**What you can see from logs:**

- Which URLs Googlebot crawls, how often
- Which URLs are getting wasted crawl budget
- Which URLs Googlebot has never visited
- Response codes per crawl (200, 301, 404, 500)
- Crawl frequency per URL by bot type (Googlebot Mobile, Googlebot Desktop, Googlebot News)

**Tools:**

- Screaming Frog Log File Analyser (SEO-friendly, easy to start)
- Botify (enterprise-grade, expensive)
- Splunk, Elastic Stack, BigQuery (when logs are in a data lake)

**Workflow:**

1. Get 30 days of log files from the engineering team (or from the CDN)
2. Filter to requests from Googlebot
3. Cross-reference with your URL list to identify over-crawled and under-crawled URLs
4. Report findings: "Googlebot spent 40% of its crawl on faceted filter URLs with no indexable value. These can be blocked in robots.txt, freeing crawl for the 300 product pages that Googlebot hasn't visited in 60 days."

### Internal Linking for Crawl Discovery

Internal links are one of the strongest signals for crawl priority. A page linked from the homepage gets crawled more than one buried 5 clicks deep.

**Rules:**

- Every priority page should be reachable from the homepage in 3 clicks or fewer
- Use descriptive anchor text (not "click here")
- Avoid orphan pages (pages with no internal links pointing at them)
- Distribute link equity purposefully: high-authority pages should link to pages you want to rank

---

## Indexation

Being crawled does not guarantee being indexed. Google decides whether to include a URL in its searchable index based on perceived quality, uniqueness, and value.

### Controlling Indexation

**Meta robots tag** (in `<head>`):

```html
<meta name="robots" content="noindex, follow">
```

- `index`: (default) allow indexing
- `noindex`: block indexing
- `follow`: (default) pass link equity through links on the page
- `nofollow`: don't pass link equity

**X-Robots-Tag** (HTTP header, useful for non-HTML files like PDFs):

```
X-Robots-Tag: noindex
```

**Canonical tag** (in `<head>`):

```html
<link rel="canonical" href="https://yourdomain.com/preferred-url">
```

Tells search engines which URL is the master version. Other variants remain accessible but defer ranking signals to the canonical.

### Common Indexation Problems

**1. Duplicate content**

- Same content at multiple URLs
- Diagnosis: site search for distinctive content strings, Ahrefs Content Duplication report, Screaming Frog duplicate detection
- Fix: canonical tags pointing to the master URL

**2. Faceted navigation**

- Filters on e-commerce or listing sites generating millions of URLs (size+color+price+brand combinations)
- Diagnosis: crawl with Screaming Frog, look for URL patterns with parameters
- Fix options: `noindex, follow` on filter pages; block filter parameters in robots.txt; use canonicals pointing to the unfiltered category

**3. Soft 404s**

- Pages that return 200 OK status but display "content not found" or empty content
- Diagnosis: GSC Coverage report flags these as "Soft 404"
- Fix: either restore meaningful content or return a real 404 status code

**4. Index bloat**

- Low-value URLs accumulating in the index (thin pages, filter pages, tag pages, user-generated pages without moderation)
- Diagnosis: `site:yourdomain.com` search vs expected URL count; GSC indexed page count
- Fix: `noindex` or consolidation

**5. Canonical conflicts**

- Self-referencing canonical pointing to another URL, or multiple canonicals on the same page
- Diagnosis: Screaming Frog crawl showing Canonical Link Element column
- Fix: ensure every page has exactly one canonical, and it's self-referencing unless deliberately consolidating

**6. Paginated content**

- Pagination that incorrectly signals to Google
- Fix: remove legacy `rel="next"`/`rel="prev"` (Google no longer uses these); ensure each paginated page has unique title, canonical to itself, and `noindex` if not designed to rank independently

---

## Rendering and JavaScript SEO

Modern sites rely on JavaScript to build content. Googlebot renders JavaScript, but rendering is expensive and deferred. Rendering issues cause indexation gaps that technical SEO audits miss.

### Rendering Modes

- **Static Site Generation (SSG):** HTML is pre-rendered at build time. Fastest, simplest for SEO. Examples: Next.js SSG, Gatsby, Astro, Hugo.
- **Server-Side Rendering (SSR):** HTML is rendered on the server per request. Good for SEO; slightly slower than SSG. Examples: Next.js SSR, Nuxt SSR.
- **Incremental Static Regeneration (ISR):** Hybrid; content is generated at build time but can be regenerated on-demand. Example: Next.js ISR.
- **Client-Side Rendering (CSR):** HTML is minimal; JavaScript builds the page in the browser. Requires Googlebot to render. Most prone to SEO issues. Examples: React SPA, Angular SPA, Vue SPA without SSR.
- **Dynamic Rendering:** Serves pre-rendered HTML to bots and client-side JS to users. Deprecated by Google; not recommended for new builds but still common on legacy sites.

### Diagnosing Rendering Issues

**Tests to run:**

1. **Google URL Inspection in GSC:** View "Tested page" to see what Googlebot actually rendered.
2. **Mobile-Friendly Test tool:** Shows rendered HTML from Google's perspective.
3. **Compare "View source" (raw HTML) vs "Inspect" (rendered DOM) in the browser:** Large differences indicate heavy JS dependency.
4. **Disable JavaScript in Chrome DevTools:** If content disappears, it's rendering-dependent.

**Symptoms of rendering problems:**

- Key content not in rendered HTML
- Navigation links not crawled by Googlebot
- Low indexation rates on otherwise high-quality pages
- "Discovered – currently not indexed" status in GSC Coverage

### Fixing Rendering Issues

- Move to SSR or SSG for SEO-critical pages
- Ensure critical content is in the initial HTML (not JS-dependent)
- Use `<noscript>` fallbacks for key navigation
- Test rendering after every deploy
- Use Next.js or similar frameworks that solve this by default

### Core Web Vitals for JavaScript Apps

JS-heavy apps often fail Core Web Vitals due to large JavaScript bundles and slow hydration.

- **Code-split** routes and components
- **Lazy-load** non-critical JavaScript
- **Defer** third-party scripts
- **Optimize fonts** with `font-display: swap`
- **Reduce main thread work** (Web Workers for heavy computation)

---

## Core Web Vitals

Three primary metrics plus two supporting metrics. Measured from real user experience (Chrome User Experience Report, CrUX) and synthetic testing (PageSpeed Insights, Lighthouse).

### Largest Contentful Paint (LCP)

Measures loading speed. LCP is the time from navigation start until the largest visible content element renders.

- **Target:** Under 2.5 seconds (good). 2.5 to 4.0 seconds (needs improvement). Over 4.0 seconds (poor).
- **Common causes of poor LCP:**
  - Slow server response (high Time to First Byte)
  - Render-blocking JavaScript or CSS
  - Large image files without optimization
  - Web fonts loaded late
  - Third-party scripts delaying main content
- **Fixes:**
  - Optimize server performance or use a CDN
  - Inline critical CSS, defer non-critical
  - Serve images in WebP or AVIF format, with responsive sizes
  - Preload the hero image
  - Lazy-load below-the-fold images
  - Defer third-party tags

### Interaction to Next Paint (INP)

Measures responsiveness. INP is the time from a user interaction (click, tap, keypress) to the next visual update. Replaced First Input Delay (FID) in March 2024.

- **Target:** Under 200 milliseconds (good). 200 to 500 ms (needs improvement). Over 500 ms (poor).
- **Common causes of poor INP:**
  - Heavy JavaScript blocking the main thread
  - Large event handlers
  - Long tasks from third-party scripts
- **Fixes:**
  - Code-split and lazy-load JavaScript
  - Defer non-critical scripts
  - Use Web Workers for heavy computation
  - Optimize React or Vue re-render cycles
  - Debounce or throttle expensive event handlers

### Cumulative Layout Shift (CLS)

Measures visual stability. CLS is the sum of unexpected layout shifts as the page loads.

- **Target:** Under 0.1 (good). 0.1 to 0.25 (needs improvement). Over 0.25 (poor).
- **Common causes of poor CLS:**
  - Images or videos without explicit width and height
  - Ads or embeds that push content down as they load
  - Web fonts swapping in and causing reflow
  - Dynamically injected content above existing content
- **Fixes:**
  - Set `width` and `height` attributes on all images
  - Reserve space for ads, iframes, and embeds with `min-height`
  - Use `font-display: swap` carefully with matched fallback metrics
  - Inject new content below existing content, never above

### Supporting Metrics

**Time to First Byte (TTFB):** Time from request to first byte of response. Target under 800 ms. Fix with better hosting, CDN, server-side caching.

**First Contentful Paint (FCP):** Time to first visible content. Target under 1.8 seconds. Fix by eliminating render-blocking resources.

### Measurement Tools

- **PageSpeed Insights:** Single-page audit with field data (CrUX) and lab data (Lighthouse)
- **GTmetrix:** Independent speed audit with waterfall diagrams, video playback of page load, and historical tracking on free tier. Useful as a second opinion against PageSpeed Insights.
- **Pingdom Tools:** Quick speed test from multiple geographic locations. Free, no account required.
- **Chrome DevTools Performance panel:** Deep investigation of specific pages
- **CrUX Dashboard:** Real user metrics over time
- **Web Vitals Chrome Extension:** Inline display while browsing
- **Lighthouse CI:** Automated monitoring in CI/CD pipelines
- **SpeedCurve, Calibre, DebugBear:** Commercial continuous monitoring

---

## Site Architecture

Site architecture is how URLs are organized and how pages link to each other. Strong architecture makes every page discoverable, distributes link equity efficiently, and signals content hierarchy to search engines.

### URL Structure

**Best practices:**

- Short, descriptive URLs using lowercase and hyphens
- Include primary keyword when natural
- Reflect content hierarchy in folder structure
- Consistent trailing slash treatment (either all with, all without)
- No session IDs or tracking parameters in canonical URLs
- No file extensions in URLs (use `/page/` not `/page.html`)

**Examples:**

- Good: `yoursite.com/blog/how-to-build-a-sitemap`
- Bad: `yoursite.com/blog?p=12345`
- Good: `yoursite.com/products/running-shoes/brand-name/model-name`
- Bad: `yoursite.com/prod?cat=12&brand=45&model=789`

### Information Architecture Patterns

**1. Flat architecture:** Every important page is a few clicks from the homepage. Best for small and medium sites.

**2. Hierarchical architecture:** Content organized by topic with clear parent-child relationships. Best for large content sites.

**3. Pillar and cluster:** A central "pillar" page on a broad topic links to multiple "cluster" pages on subtopics, each linking back to the pillar. Best for topical authority building.

**4. Hub and spoke:** A landing page per segment or persona (the hub) links to supporting content (spokes). Best for B2B SaaS and agency sites.

### Internal Linking Strategy

**Priority distribution:**

- Homepage links carry the most equity
- Navigation menu links carry significant equity
- Footer links carry moderate equity (but too many footer links dilute)
- In-content links carry equity weighted by anchor text relevance and position

**Rules:**

- Every priority page should have at least 3 internal links pointing at it
- Anchor text should be descriptive, not generic ("Read the guide to schema markup" not "click here")
- Avoid linking the same page multiple times with the same anchor from the same source
- Link from high-authority pages to pages you want to rank (internal PageRank)

### Breadcrumbs

Breadcrumbs are navigational aids showing the user's location in the site hierarchy.

- Implement BreadcrumbList schema
- Every page beyond the homepage should have breadcrumbs
- Use descriptive breadcrumb labels, not just "Home > Category > Product"

---

## Status Codes and Redirects

### Key Status Codes

| Code | Meaning | SEO Impact |
|---|---|---|
| 200 | OK | Normal, indexable |
| 301 | Permanent redirect | Passes full ranking signals to target |
| 302 | Temporary redirect | Passes signals; Google may still index source |
| 307 | Temporary (strict) | Similar to 302 |
| 308 | Permanent (strict) | Similar to 301 |
| 404 | Not found | Removed from index over time |
| 410 | Gone | Removed faster than 404 |
| 500 | Server error | Crawl errors, potential indexation loss |
| 503 | Service unavailable | Use during maintenance; Googlebot retries |

### Redirect Best Practices

- Use 301 for permanent URL changes
- Avoid redirect chains (A to B to C). Redirect A directly to C.
- Update internal links to point at final URLs, not redirect sources
- Keep redirects in place for at least a year after a URL change
- Map every old URL to a new URL during migrations; never mass-redirect to homepage

### Managing 404s

- Use a custom 404 page that helps users find what they wanted (search bar, popular pages)
- Monitor 404s in GSC Crawl Stats and GA4
- Redirect 404s that receive significant traffic or backlinks
- Let truly irrelevant 404s stay as 404s (don't redirect junk to the homepage)

---

## Mobile-First Indexing

Since 2023, Google uses the mobile version of every site for indexing and ranking. If your mobile site is stripped-down, missing content, or broken, your rankings suffer regardless of desktop quality.

### Mobile-First Checklist

- Same content on mobile and desktop (not a subset)
- Same structured data on mobile and desktop
- Same meta tags on mobile and desktop
- Responsive design (not separate m.yourdomain.com)
- Viewport meta tag: `<meta name="viewport" content="width=device-width, initial-scale=1">`
- Tap targets sized at least 48 pixels
- Font size at least 16 pixels for body text
- No intrusive interstitials or popups that block content

### Testing

- Google's Mobile-Friendly Test
- Chrome DevTools Device Mode
- GSC Mobile Usability report

---

## Schema Markup

Structured data tells search engines exactly what a page is about in machine-readable form. Usually implemented as JSON-LD in the `<head>` or `<body>`.

### Key Schema Types

**Organization** (every site):

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Your Company",
  "url": "https://yourcompany.com",
  "logo": "https://yourcompany.com/logo.png",
  "sameAs": [
    "https://twitter.com/yourcompany",
    "https://linkedin.com/company/yourcompany"
  ]
}
```

**LocalBusiness** (local services):

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Your Clinic",
  "address": {...},
  "telephone": "+1...",
  "openingHours": "Mo-Fr 09:00-17:00"
}
```

**Product** (e-commerce):

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Product Name",
  "image": ["url"],
  "description": "...",
  "offers": {
    "@type": "Offer",
    "price": "99.99",
    "priceCurrency": "USD"
  }
}
```

**FAQ** (content with FAQ sections):

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "...",
      "acceptedAnswer": {"@type": "Answer", "text": "..."}
    }
  ]
}
```

**Article** (content articles and blog posts):

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "...",
  "author": {"@type": "Person", "name": "Author Name"},
  "datePublished": "YYYY-MM-DD",
  "dateModified": "YYYY-MM-DD"
}
```

**BreadcrumbList** (navigation breadcrumbs)
**Review / AggregateRating** (products with reviews)
**HowTo** (step-by-step guides)
**Event** (events with dates and locations)
**VideoObject** (video content)
**JobPosting** (job listings)

### Schema Implementation Rules

- Use JSON-LD format (Google's preferred)
- Place in `<head>` or before closing `<body>`
- Validate every implementation with Google's Rich Results Test and Schema.org Validator
- Only mark up content that's actually on the page (don't fake data)
- Keep schema in sync with visible content; stale schema creates trust issues

### Schema for GEO/AEO

Entity-heavy schema helps AI search systems understand your brand. Priority types for AI visibility:

- Organization (who you are)
- Person (authors, executives)
- WebSite (with SearchAction)
- BreadcrumbList (site structure)
- Article (content context)
- FAQPage (direct answer material)

---

## International SEO

Serving users in multiple countries or languages requires careful setup. Mistakes here cause wrong-country ranking, duplicate content, or total loss of international visibility.

### URL Structures (Pick One)

**1. Country-code Top-Level Domain (ccTLD)**

- Examples: yoursite.de, yoursite.fr, yoursite.jp
- Pros: Strongest geographic signal; complete separation of sites
- Cons: Each domain starts with zero authority; expensive to maintain; fragmented link equity

**2. Subdirectories**

- Examples: yoursite.com/de/, yoursite.com/fr/
- Pros: Consolidates authority; simpler infrastructure
- Cons: Weaker geographic signal than ccTLD
- **Default choice for most international sites**

**3. Subdomains**

- Examples: de.yoursite.com, fr.yoursite.com
- Pros: Clean separation
- Cons: Google treats as semi-separate site; partial authority inheritance; compromise between ccTLD and subdirectory

### Hreflang

Hreflang tells search engines which language/region version of a page to serve to which audience.

**Basic implementation (in `<head>` on every international page):**

```html
<link rel="alternate" hreflang="en" href="https://yoursite.com/">
<link rel="alternate" hreflang="en-us" href="https://yoursite.com/">
<link rel="alternate" hreflang="en-gb" href="https://yoursite.com/uk/">
<link rel="alternate" hreflang="de" href="https://yoursite.com/de/">
<link rel="alternate" hreflang="fr" href="https://yoursite.com/fr/">
<link rel="alternate" hreflang="x-default" href="https://yoursite.com/">
```

**Rules:**

- Every international page must include its own hreflang (self-referencing) plus all alternates
- Use `x-default` for the fallback when no language or region matches
- Use full language codes (`en-us`) when a country-specific version exists, plain language (`en`) for generic
- Hreflang is bidirectional: Page A must reference Page B, and Page B must reference Page A

**Alternative implementations:**

- XML sitemap (scales better for large sites)
- HTTP headers (for non-HTML files)

### Market-Specific Keyword Research

Never translate English keywords to other languages. Search behavior varies by market.

- Run independent Ahrefs or Semrush research per market in the native language
- Study SERPs in each market (use a VPN or local proxy)
- Work with native speakers for intent and nuance
- Validate content with native-speaker review before publishing

### Geotargeting in Google Search Console

For subdirectories and subdomains, set geotargeting in GSC (International Targeting report) to tell Google which country each folder targets.

### Currency, Payment, Shipping Localization

Critical for e-commerce. Even if SEO is clean, users won't convert if pricing, currency, and shipping options don't match their market. These are not just UX concerns; they affect return rates and, indirectly, ranking through user signals.

---

## Site Migrations

High-stakes engagements. Getting migrations wrong causes permanent ranking loss. Know the full process cold.

### Migration Types

1. **Content Management System (CMS) migration:** WordPress to Webflow, Shopify to Magento, etc.
2. **Domain migration:** olddomain.com to newdomain.com
3. **HTTPS migration:** HTTP to HTTPS
4. **URL structure migration:** Changing URL patterns without changing domain
5. **Site redesign:** New look and feel, potentially new information architecture
6. **Site consolidation:** Merging multiple domains into one

### Pre-Migration Checklist (T-30 Days)

- **Crawl existing site** with Screaming Frog or Sitebulb. Export all URLs with status, title, meta, canonical, response time.
- **Export GSC Performance data** (queries and pages) for last 16 months. This is your evidence baseline.
- **Export Ahrefs keyword rankings** (top 1,000 to 10,000 keywords). Snapshot of where you rank today.
- **Export backlink profile** from Ahrefs or Semrush. Critical for identifying pages that need redirects based on external link value.
- **Export GA4 organic sessions** by landing page for last 12 months. Traffic baseline.
- **Build URL mapping document** pairing every old URL to its new URL. Spreadsheet format. Include redirect type (301 in almost all cases). Flag pages being consolidated or removed.

### Pre-Migration Checklist (T-7 Days)

- **Staging environment audit.** Full Screaming Frog crawl against staging. Check for accidental `noindex`, correct canonicals, correct hreflang, proper schema, intact meta tags, working forms.
- **Verify 301 redirects** from old URLs to new URLs resolve correctly in staging (where possible) or prepare .htaccess/nginx redirect rules for launch.
- **Analytics continuity.** Ensure GA4 tracking, Google Tag Manager, Google Search Console verification, and all conversion events are in place on the new site.
- **robots.txt check.** Make sure staging's robots.txt (often `Disallow: /`) is NOT deployed to production.
- **Sitemap preparation.** New XML sitemap ready to submit immediately post-launch.
- **Stakeholder alignment.** Engineering, content, analytics, client services all know the launch window and emergency escalation path.

### Launch Day

- Deploy during the lowest-traffic window for the site
- Immediately submit new sitemap in GSC
- Submit URL Inspection requests for top 10 to 20 priority URLs to accelerate recrawl
- Run Screaming Frog crawl within the first hour
- Verify top 20 redirects manually
- Monitor GSC Coverage and Ahrefs rank tracker in real time

### Post-Migration Monitoring (Days 1 to 14)

- **Daily GSC Coverage report check** for indexation changes
- **Daily Ahrefs rank tracker review** for ranking movement
- **Daily GA4 organic sessions comparison** vs pre-migration baseline
- **Expected pattern:** 10 to 15% traffic dip in first 2 weeks is normal, with recovery to baseline by week 4 to 6
- **Red flags:** Over 20% traffic drop beyond week 2, large-scale de-indexation, 404 error spikes

### Post-Migration Recovery (if things go wrong)

- Identify which URL group dropped (segment by sitemap)
- Check redirect chains (A to B to C is worse than A to C)
- Check canonical tags (new pages should self-canonical)
- Check for accidental `noindex` tags
- Re-submit problem URLs via URL Inspection
- Earn fresh external signals (digital PR or social amplification) to signal authority on new URLs

**Example outcome when executed well:** WordPress to Webflow migration with full URL mapping, benchmark exports, staging audit, and 14-day daily monitoring. Rankings protected, traffic stayed within normal post-migration variance, inbound pipeline intact.

---

# Part IV: On-Page and Content SEO

## Keyword Research

Keyword research is the foundation of on-page SEO. Without understanding what your audience searches for, every content decision is a guess.

### Methodology

**Step 1: Seed keywords**

Start with the 10 to 20 obvious terms for the business. "CRM software," "marketing automation," "email marketing tool."

**Step 2: Expansion**

Use tools to find related keywords at scale.

- **Ahrefs Keywords Explorer:** Seed → Related, Questions, Also Rank For, Terms Match. Subscription-based UI tool.
- **Semrush Keyword Magic Tool:** Same concept, different data sources. Subscription-based UI tool.
- **DataforSEO Keywords Data API:** API-first programmatic keyword research. Pay-per-request, no subscription. Use when you need large volumes of keyword data feeding into custom workflows, AI pipelines, or proprietary tooling. Endpoints cover Google, Bing, YouTube, Amazon, plus related, suggestions, and ad volume data. Significantly cheaper than Ahrefs/Semrush at scale and easier to integrate into Claude Code skills, Python pipelines, or n8n workflows.
- **DataforSEO Labs API:** Advanced research workflows on top of the keyword data: keyword ideas, related keywords, search intent, competitor analysis, ranked keywords for a domain. Designed for programmatic use.
- **Google Keyword Planner:** Direct from Google; fewer features but free.
- **AnswerThePublic:** Question-based keywords
- **AlsoAsked:** "People Also Ask" scraping
- **Google autocomplete:** Type seed + letter to see common expansions
- **Reddit, forums, review sites:** Language your audience actually uses

**Step 3: Competitor keyword gap analysis**

- **Ahrefs Content Gap tool:** Enter your domain + 3 to 5 competitor domains. Ahrefs shows keywords competitors rank for that you don't.
- **Semrush Keyword Gap:** Similar function.
- **DataforSEO Labs API (Domain Intersection / Competitors):** Programmatic competitor gap. Pull every keyword a competitor ranks for, intersect with your own ranked keywords, output the delta. Best for large-scale or recurring gap analysis where you want the data in your own database, dashboard, or AI workflow rather than a vendor UI.

**For each gap keyword that survives prioritization, also analyze the SERP angle and content quality level competitors are using.** A keyword competitors rank for is only an opportunity if your team can match or exceed the angle and quality bar already in the SERP. See [[#Content Angle Framework]] (analyze the existing angles, find the underserved one) and [[#Content Quality Framework: Five Levels (Ahrefs)]] (price the production realistically — don't try to win a Level 4 SERP with a Level 1 piece). Gap analysis without angle analysis just produces a long list of keywords you'll publish against and lose to.

**Step 4: Refinement**

Filter the expanded list by:

- **Search volume:** Minimum threshold (usually 50 to 100 monthly searches for B2B; 500+ for e-commerce)
- **Keyword difficulty:** Exclude keywords too competitive for current domain authority
- **Intent:** Match to your business model
- **Relevance:** Remove keywords that don't map to buyer or funnel stages

### Keyword Metrics to Track

- **Search volume:** Average monthly searches (available from Ahrefs, Semrush, Google Keyword Planner, DataforSEO Keywords Data API)
- **Traffic Potential:** Estimates the total monthly organic traffic the top-ranking page receives, which is often more accurate than just looking at the search volume of one keyword. A page that ranks for "best CRM software" also captures traffic from "top CRM tools," "CRM software reviews," and dozens of related variants. Traffic Potential aggregates all of those into one number, giving a truer picture of the upside of ranking for the cluster. Available in Ahrefs Keywords Explorer (the canonical "Traffic Potential" metric) and approximated in Semrush via Estimated Traffic. Use TP as the primary opportunity-sizing metric for any keyword you'd build a dedicated page for.
- **Keyword difficulty (KD):** Ahrefs 0 to 100 scale, Semrush 0 to 100 scale, DataforSEO has its own difficulty score plus the raw SERP data needed to compute custom difficulty models
- **Cost Per Click (CPC):** Indicates commercial value; high-CPC keywords usually convert well
- **Search intent:** Informational, navigational, commercial, transactional. DataforSEO Labs API has a search-intent classification endpoint that returns intent per keyword programmatically (useful for clustering and prioritization at scale)
- **SERP features:** Featured snippets, People Also Ask, local pack, image pack, knowledge panel. The DataforSEO SERP API returns the full SERP feature breakdown per query, which is critical for clustering by SERP overlap (see [[#Keyword Clustering]])
- **Trend:** Rising, stable, declining (Google Trends, plus DataforSEO Keywords Data API monthly search volume history)

### Long-Tail Strategy

Long-tail keywords are specific, multi-word queries with lower search volume but higher intent and easier ranking. They usually convert better than head terms.

- Head term: "CRM software" (100,000 monthly searches, hard to rank)
- Long-tail: "best CRM software for solo consultants" (500 monthly searches, easier to rank, higher intent)

Strategy: target head terms with pillar pages. Target long-tail with cluster pages that all link back to the pillar.

---

## Search Intent

Matching content type to search intent is the single most important on-page factor. Ranking the wrong content type for a query is nearly impossible, even with perfect technical SEO.

### The Four Intent Types

**1. Informational**

- User wants to learn something
- Query patterns: "how to," "what is," "why does," "guide to"
- Best content type: blog post, guide, tutorial, video
- Example: "how to build a sitemap" → in-depth guide

**2. Navigational**

- User wants to reach a specific site or page
- Query patterns: "[brand name]," "[brand name] login," "[brand name] pricing"
- Best content type: homepage, login page, product page
- Example: "Ahrefs login" → Ahrefs login page

**3. Commercial (Investigation)**

- User is researching before buying; comparing options
- Query patterns: "best," "vs," "alternative to," "review"
- Best content type: comparison page, best-of list, review, alternatives page
- Example: "Ahrefs vs Semrush" → comparison page

**4. Transactional**

- User is ready to buy or take action
- Query patterns: "buy," "price," "discount," "sign up," "book"
- Best content type: product page, pricing page, signup page, checkout
- Example: "Ahrefs pricing" → pricing page

### Determining Intent

1. **Google the keyword.** Check the top 10 results. If they're all blog posts, intent is informational. If they're all product pages, intent is transactional.
2. **Check SERP features.** Featured snippets + People Also Ask + "Related searches" suggest informational. Shopping ads + product results suggest transactional.
3. **Study query language.** Command words ("buy," "download") signal transactional. Question words signal informational.
4. **Programmatic intent classification at scale.** For thousands of keywords, the DataforSEO Labs API search-intent endpoint returns intent labels per keyword. Pair with the SERP API for SERP-feature-based intent verification. Useful when the keyword set is too large to manually classify.

### Intent Mismatches

The single most common SEO mistake: trying to rank a blog post for a transactional query, or a product page for an informational query. Match intent to content type, or expect to not rank.

---

## Keyword Clustering

Keyword clustering groups semantically related keywords into single content targets. Prevents keyword cannibalization (multiple pages competing for the same keyword).

### SERP-Overlap Clustering Method

1. Pull SERP data for each keyword (top 10 ranking URLs). The DataforSEO SERP API is the standard programmatic way to do this at scale: one request per keyword, returns the full SERP including ranking URLs, SERP features, and metadata.
2. Compare SERPs across keywords (set intersection on the ranking URLs)
3. If two keywords share 3 or more of the same ranking URLs, they're the same cluster
4. Create one page targeting the cluster, not separate pages per keyword

### Clustering Tools

- **Ahrefs Keyword Grouping**
- **Keyword Insights** (dedicated clustering tool, runs SERP-overlap clustering as a service)
- **Semrush Keyword Cluster tool**
- **DataforSEO SERP API + custom clustering script:** The "build it yourself" path. Pull SERPs for every keyword via DataforSEO, then run a clustering script (Python with pandas, or a Claude Code skill) to compute SERP overlap and group keywords. Cheapest option at scale and integrates directly into AI-assisted content workflows.
- **Manual in spreadsheet** for smaller keyword sets

### Output

One spreadsheet with:

- Cluster ID
- Primary keyword (highest volume in cluster)
- Secondary keywords (other keywords in cluster)
- Total cluster volume
- Cluster intent
- Recommended content type
- Existing URL (if any) or "new page"

---

## Content Strategy and Topical Authority

Google rewards sites that comprehensively cover a topic, not just individual pages. Topical authority is earned by covering a subject area breadth and depth such that Google considers your site a reliable source.

### The Pillar and Cluster Model

**Pillar page:** A comprehensive guide to a broad topic (2,000+ words).

**Cluster pages:** Deeper-dive pages on subtopics (800 to 2,000 words each).

**Interlinking:** Every cluster page links to the pillar; the pillar links to every cluster.

**Example for a CRM software brand:**

- Pillar: "The Complete Guide to Customer Relationship Management"
- Clusters:
  - What is CRM software?
  - CRM software for small businesses
  - CRM features: what to look for
  - CRM implementation guide
  - CRM vs marketing automation
  - Free vs paid CRM software
  - CRM integrations with email marketing
  - How to choose a CRM
  - CRM software benefits
  - CRM software pricing guide

### Content Gap Analysis

- **Ahrefs Content Gap report:** find keywords where competitors rank but you don't
- **DataforSEO Labs API (Domain Intersection / Ranked Keywords):** programmatic gap analysis. Pull every ranked keyword for each competitor + your domain, compute the difference set. Best when the gap analysis needs to feed an automated content pipeline or recurring report rather than a one-off review.
- **Screaming Frog Custom Extraction:** pull competitor H1/H2 structures to see what they cover
- **Manual competitor audit:** list every topic major competitors have content on; identify what you're missing

### Editorial Calendar

A publishing schedule for the next 30, 60, 90 days. Includes:

- Publish date
- Title
- Target keyword cluster
- Author
- Word count
- Internal links to add
- Related pillar

Common cadence for B2B SaaS: 4 to 12 articles per month at 1,500 to 3,000 words each.

---

## Content Angle Framework

Topical authority gets you in the conversation. The **content angle** decides whether you actually rank against the pages already in it.

The angle is the unique "hook" or approach a piece of content takes. Two well-researched, similarly comprehensive articles on the same topic will rank very differently if one has a distinct angle (personal experience, expert commentary, original data) and the other reads as an undifferentiated summary.

This framework is from Ahrefs' content team, condensed for working use.

### Step 1: Analyze the SERP for Existing Angles

Search the target keyword and study the top 10 results. Identify the angle each top-ranking page is taking. Common angles:

- **Personal experience.** First-person account: "I tried X for 6 months, here's what happened."
- **Best / Listicle.** Aggregated, curated comparison: "The 12 best X for Y in 2026."
- **Expert commentary.** Insights and quotes from named industry experts.
- **For beginners.** Plain-language introduction to a complex topic.
- **Specific outcome.** Tied to a concrete, measurable result.
- **Freshness.** Up-to-date take that explicitly improves on dated information: "[Topic] in 2026: what's changed."

A single SERP often shows three or four of these angles competing. The angle that's missing or underserved is your opportunity.

### Step 2: Determine the Content Type and Format

Identify the dominant format on the SERP. Are the top results:

- Blog posts or in-depth guides?
- Product pages or pricing pages?
- Listicles or comparison tables?
- Video-first results?
- Tools or interactive resources?

Match the format to what the SERP rewards. Trying to rank a written guide for a query Google answers with video carousels and tools is fighting the SERP.

### Step 3: Pick a Better or Different Angle, Then Out-Execute

Two paths:

1. **Better.** Same angle as the top result, but executed at higher quality: more depth, better data, clearer structure, stronger expertise signals, fresher updates.
2. **Different.** Adopt an angle the SERP underserves. If five pages are listicles, ship a deeply researched personal-experience piece. If the SERP is all expert commentary, ship a beginner-friendly version.

The differentiation has to be visible from the SERP snippet (title, description, first sentence) or users won't click through to discover it.

### Combine With Topical Authority

Content angle works on top of topical authority, not instead of it. A site without topical authority and a single great-angle piece may rank short-term but won't sustain. A site with topical authority publishing undifferentiated content will rank for a long-tail keyword set but lose to better-angled competitors on the high-value head terms. Senior SEO operators do both.

---

## Content Quality Framework: Five Levels (Ahrefs)

A useful mental model for content investment decisions, also from Ahrefs. Move up the levels as topical authority and budget allow. Most B2B sites publish at Levels 1-2 and wonder why they don't outrank competitors investing at Levels 3-5.

| Level | Format | Production Cost | Defensibility |
|---|---|---|---|
| **1: Basic listicles** | Aggregated information, simple lists, surface-level comparisons. Quick to produce, easy to copy. | Low | Low. Anyone can replicate. |
| **2: Advanced listicles** | Detailed, curated lists with real evaluation criteria, in-depth explanations per item, judgment shown. | Low to medium | Medium. Requires editorial judgment. |
| **3: Deep dives / guides** | Comprehensive guides covering nearly all aspects of a topic. Authoritative reference material. | Medium to high | Medium-high. Hard to copy without significant time investment. |
| **4: Experiments and surveys** | Data-driven content based on original research, surveys, or experiments. | High | High. Original data is hard to fake. |
| **5: Original ideas / studies** | Thought leadership establishing new industry concepts, frameworks, or terminology that other operators cite. | Very high | Very high. Becomes the canonical reference once cited. |

### How to Apply the Five Levels

- **Audit the existing content portfolio** by level. Most under-performing content sites are 80%+ at Level 1-2.
- **Plan the next quarter's content with deliberate level mix.** A workable target for a B2B site investing in SEO seriously: 50% Level 2 (volume), 30% Level 3 (depth), 15% Level 4 (data), 5% Level 5 (thought leadership).
- **Price the work accordingly.** Level 1-2 can be produced fast with AI-assisted workflows. Level 4-5 requires real research time, named contributors, and editorial leadership.
- **Use Levels 4-5 for the highest-stakes pillar pages** and the topics where you most need to defend rankings against well-resourced competitors. Don't try to compete on a high-value head term with Level 1-2 content; you'll spend the production budget and not move the rankings.

### Why Level 4-5 Is the GEO/AEO Multiplier

The five-level framework also maps directly onto AI search citation behavior. Level 4-5 content (original data, surveys, frameworks) gets cited by AI answer engines disproportionately because:

- Original statistics give the AI something quotable that's not available elsewhere
- Named frameworks and concepts give the AI a discrete entity to reference
- Surveys with proprietary methodology become the de facto source on a topic
- Thought leadership defines the language the AI uses to describe the space

If GEO and AEO performance is a goal (see [[#Optimizing for AI Citation]]), Level 4-5 investment is the lever, not Level 1-2 volume.

---

## Experience, Expertise, Authoritativeness, Trustworthiness (E-E-A-T)

Google evaluates content quality using E-E-A-T signals, especially for Your Money or Your Life (YMYL) topics.

- **Experience:** Has the author personally done this? First-person details, photos, case studies.
- **Expertise:** Does the author have credentials in this field? Bios, certifications, affiliations.
- **Authoritativeness:** Is the site a recognized authority on this topic? Third-party citations, backlinks from authoritative sites, branded search volume.
- **Trustworthiness:** Can users trust this site? HTTPS, clear contact info, transparent sourcing, accurate and current information.

### Strengthening E-E-A-T

- **Named authors** with detailed bios and credentials
- **Author schema** markup on content pages
- **First-person examples** and case studies (Experience)
- **Cited sources** with links to primary research
- **About Us and Contact Us pages** with real names and addresses
- **Third-party validation:** press mentions, awards, certifications on the site
- **Regular content updates** with "Last updated" dates
- **Fact-check notices** or editorial standards pages for YMYL content
- **HTTPS and clean technical hygiene**

---

## On-Page Optimization

Tactical page-level optimization. Each element sends a signal to search engines about what the page is about.

### Title Tag

The single strongest on-page ranking signal. Appears in browser tabs, SERPs, and social shares.

- **Length:** 50 to 60 characters (pixels matter more, but this is a safe range)
- **Include primary keyword** near the front
- **Include brand name** at the end (exception: when character count is tight)
- **Unique per page**
- **Write for click-through rate:** Use numbers, power words, brackets
- **Format:** `Primary Keyword | Secondary Benefit – Brand`

Example: `Best CRM Software for Small Business (2026 Guide) | Yoursite`

### Meta Description

Summarizes the page. Not a direct ranking factor but strongly influences click-through rate.

- **Length:** 150 to 160 characters
- **Include primary keyword** (bolded in SERP when matched)
- **Action-oriented language:** Include a call to action if it fits
- **Distinct per page**
- **Write for click-through:** Test variants; GSC shows CTR per page

### H1 Tag

The main heading. Usually matches the title tag closely, but more descriptive.

- One H1 per page
- Include primary keyword
- Can be longer than title (SEO doesn't limit H1)

### H2, H3 Subheadings

Structure the page content into scannable sections.

- H2s for major sections, H3s for subsections
- Include keyword variations and related terms
- Helps Google understand content hierarchy

### URL Slug

- Short, descriptive
- Include primary keyword
- Lowercase, hyphens for spaces
- No stop words ("the," "of," "and") unless needed for clarity

### Image Optimization

- **File name:** descriptive, keyword-relevant (not IMG_2456.jpg)
- **Alt text:** describes the image for accessibility and search engines
- **File size:** compressed (use WebP or AVIF; tools like ImageOptim, TinyPNG)
- **Dimensions:** set `width` and `height` attributes to prevent layout shift
- **Responsive images:** use `srcset` for different viewport sizes
- **Lazy loading:** for below-the-fold images
- **AI-generated illustrations:** [NapkinAI](https://napkin.ai/) generates clean, brand-neutral illustrations from a text prompt — useful for content production when you need original visuals without stock-photo overhead. Always export as WebP (or convert) before publishing.

### Internal Linking

- Link from high-authority pages (homepage, top blog posts) to pages you want to rank
- Use descriptive anchor text that includes the target keyword when natural
- Every priority page should have at least 3 internal links from relevant pages
- Avoid linking the same page multiple times with the same anchor from the same source

### Content Structure

- **Lead with the answer** for informational content (good for featured snippets)
- **Use short paragraphs** (2 to 4 sentences each)
- **Use lists and tables** where content is naturally enumerable
- **Include images, videos, charts** that add genuine value
- **Length:** match the content depth of the top 5 ranking competitors

---

## Content Optimization Tools

Tools that score content against the top ranking pages for a target keyword, then suggest improvements.

### SurferSEO

- Content Editor: scores your draft against top 10 ranking competitors
- Shows recommended word count, heading count, image count, keyword usage
- Identifies related terms and questions to include
- Integrates with Google Docs

### Clearscope

- Similar functionality to Surfer, cleaner interface
- Stronger for enterprise content teams
- Higher price point

### Frase

- AI-assisted content brief generation
- Content scoring
- Includes AI content drafting (use cautiously, always humanize)

### MarketMuse

- Topic modeling and content inventory
- Enterprise-focused
- Strong for large content sites assessing topical authority

**Warning:** Content scoring tools optimize for correlation with ranking, not causation. Don't let the score override editorial judgment. A high-score thin article still won't rank; a lower-score deeply insightful article often does.

---

## Programmatic SEO

Creating large numbers of pages from structured data templates to capture long-tail volume at scale.

### Common Patterns

- **Location pages:** `[Service] in [City]` (dental clinic in Lagos, marketing agency in New York)
- **Product combination pages:** `[Brand] [Product] [Variant]`
- **Comparison pages:** `[Tool A] vs [Tool B]`
- **Integration pages:** `[Tool A] + [Tool B] integration`
- **Persona pages:** `[Tool] for [Persona]` (CRM for real estate agents, project management for freelancers)
- **Industry pages:** `[Solution] for [Industry]` (analytics for SaaS, payroll for restaurants, CRM for healthcare)
- **Use case pages:** `How to [Use Case]` or `[Use Case] templates` (how to write cold emails, abandoned cart email templates, customer onboarding workflow examples)
- **Category best-of pages:** `Best [Category] for [Use Case]` or `Best [Category] [Year]` (best CRMs for cold outreach, best project management tools 2026)
- **Industry + category pages:** `[Industry] [Category]` (SaaS pricing pages, fintech onboarding flows, ecommerce checkout examples) — useful for inspiration galleries and benchmark directories
- **Glossary pages:** `What is [Term]?`

### Execution

1. **Dataset:** Build a structured dataset with rows for each page (e.g., list of cities, products, competitors). For keyword-driven datasets at scale, the DataforSEO Keywords Data API can supply volume, CPC, and SERP data per row programmatically.
2. **Template:** Design a content template with fixed structure and variable data fields
3. **Unique value per page:** Each page must have some unique content (stats, local info, specific examples), not just swapped variables. DataforSEO SERP API can pull live competitor SERP snippets per keyword to seed unique data per page.
4. **Tech stack:** CMS that supports templating (Webflow, Next.js, Sanity + static generation), or a headless CMS with a deployment pipeline
5. **URL structure:** Predictable pattern (`/service/city/` or `/tool-a-vs-tool-b/`)
6. **Internal linking:** Auto-generate contextual internal links between related programmatic pages

### Quality Control

- **Test with 50 pages before scaling to 500 or 5,000**
- **Monitor indexation rate.** If pages aren't indexed within 30 days, quality is too thin.
- **Unique meta tags per page** (title, description)
- **Unique primary content per page** (more than just swapped variables)
- **Avoid thin pages.** Programmatic pages that fail to satisfy search intent get mass-deindexed.

**Content-at-scale platforms:** [Machined.AI](https://machined.ai/) generates and publishes hundreds to thousands of programmatic articles from a keyword list, with built-in internal linking, schema, and CMS publishing (Webflow, WordPress, Shopify, Sanity). Useful for solo operators or lean teams running programmatic plays without engineering capacity to build the dataset, template, and publish pipeline themselves. Quality still depends on keyword selection and template design, the same rules apply (test 50 before scaling, monitor indexation, ensure unique value per page).

**Success example:** Zapier's integration pages (thousands of `Tool A + Tool B` combinations), Yelp's location pages, Tripadvisor's destination pages.

**Failure example:** Mass-generated city pages with no local content, AI-generated thin comparison pages, keyword-stuffed landing pages that provide no real value.

---

## Content Refresh Strategy

Existing content can decay. Traffic drops, rankings slip, information goes stale. A refresh program recovers lost traffic at near-zero production cost.

### Identifying Refresh Candidates

- **Traffic decline:** GA4 landing page report, compare last 3 months vs prior 3 months
- **Ranking decline:** Ahrefs or GSC, flag pages that dropped in positions
- **Date-sensitive content:** Annual guides, pricing comparisons, "best-of" lists
- **Thin content:** Pages below 500 words on topics with deep competitors
- **Outdated stats:** Content citing data older than 24 months

### Refresh Workflow

1. **Audit the current page:** What is it missing vs current top-ranking pages?
2. **Update stats and examples** to current
3. **Add new sections** that competitors have but the current page doesn't
4. **Upgrade images, add new images**
5. **Improve internal links** (to and from the page)
6. **Update meta tags** if click-through rate has declined
7. **Update `dateModified` in schema** to reflect the refresh
8. **Re-submit in GSC URL Inspection**
9. **Track performance** for 30 days post-refresh

**Cadence:** Quarterly review of top 100 organic pages; monthly refresh of the most impactful 5 to 10.

---

# Part V: Off-Page SEO

## Link Value Frameworks

Not all backlinks are equal. Evaluate links across multiple dimensions.

### Quality Dimensions

1. **Topical relevance:** Is the linking site topically related to yours?
2. **Domain authority (DR or DA):** Higher-authority domains pass more value
3. **Page authority (URL Rating):** The specific page linking matters too
4. **Traffic:** Does the linking page get real traffic? Pages with no traffic often signal thin or low-value content
5. **Link type:** Dofollow passes PageRank; nofollow, sponsored, UGC don't pass ranking signals but still have brand and referral value
6. **Placement:** In-content editorial links pass more value than footer or sidebar links
7. **Anchor text:** Descriptive relevance matters; excessive exact-match anchor text triggers over-optimization signals

### Link Types by Intent

- **Editorial links:** Highest value. Earned through content worth citing.
- **Guest post links:** Medium value when on relevant, authoritative sites. Low to negative value when at scale on mediocre sites.
- **Directory links:** Situational value. Strong for local SEO (Google Business Profile, Yelp). Useful for SaaS (G2, Capterra). Generic directories are mostly wasted time.
- **Social media links:** Nofollow, but provide brand signals and traffic.
- **Forum and comment links:** Usually nofollow, low SEO value. Useful for research and relationship-building.
- **Press release links:** Low direct SEO value unless picked up by major publications.

---

## Digital Public Relations (PR)

The highest-value link acquisition strategy. Creating newsworthy content that earns editorial coverage at scale.

### Formats That Earn Links

1. **Data studies:** Original research based on proprietary data or surveys
2. **Industry benchmark reports:** Annual reports on trends, salaries, spend, behavior
3. **State-of-the-industry roundups:** Synthesize the current state of a topic with named contributors
4. **Tools and calculators:** Free interactive tools journalists cite
5. **Controversial or counterintuitive takes:** Data-backed counter-narratives

### Execution

**1. Ideation**

- What question would our audience want answered?
- What data do we have access to that others don't?
- What's a bold claim we can defend with evidence?

**2. Data collection**

- Internal data (product usage, customer behavior)
- Surveys via Pollfish, SurveyMonkey, Typeform
- Public datasets (government, industry associations, scraped)

**3. Analysis and packaging**

- Charts, tables, memorable stats
- Narrative: what did we find, why does it matter?
- Quotes and takes from subject-matter experts

**4. Pitch preparation**

- Email templates personalized to journalist beats
- Press release optional, pitch directly more effective

**5. Pitching**

- **Connectively (formerly HARO):** Respond to journalist queries
- **Qwoted:** Similar platform
- **Featured.com:** Structured Q&A pitching
- **Direct outreach:** Journalist databases (Muck Rack, Cision), manual research

**6. Amplification**

- Social media, newsletter, internal team
- Co-market with partners and customers
- Submit to aggregators (Hacker News, Product Hunt if applicable)

### Realistic Expectations

- One strong data study can earn 50 to 200+ referring domains
- Most pitches never get a response; expect 5 to 10% pick-up rate
- Journalist relationships compound over multiple campaigns
- Quality beats volume: one Wall Street Journal mention is worth 100 low-tier blog mentions

---

## Broken Link Building

Finding broken outbound links on relevant sites, then offering your content as a replacement.

### Workflow

1. **Identify relevant sites:** Topically aligned, high-authority sites in your space
2. **Find broken outbound links:** Ahrefs Broken Links report, Semrush Broken Backlinks, or DataforSEO Backlinks API (broken backlinks endpoint) for programmatic discovery across hundreds of domains
3. **Find your equivalent content:** Do you have a page that would fit as a replacement?
4. **Outreach:** Email the site owner pointing out the broken link and suggesting your content

### Template Pitch

> Hi [Name],
>
> I was reading your article on [topic] and noticed the link to [broken source] no longer works (returns a 404 error).
>
> I recently published a detailed guide on [related topic] that covers similar ground. It might fit as a replacement if you're updating the piece. Happy to share the link: [your URL]
>
> Either way, thanks for the article — great resource.
>
> [Your name]

### Expectations

- Conversion rate: 5 to 15% of well-targeted outreach earns a link
- Time investment: 10 to 30 minutes per link earned
- Best for complementing a digital PR program, not replacing it

---

## Unlinked Brand Mentions

Sites that mention your brand in copy without linking to you. Reach out, ask for the link.

### Finding Mentions

- **Google alerts** for your brand name
- **Ahrefs Content Explorer:** Filter for "mentions" of your brand without a link
- **Mention.com, Brand24:** Dedicated brand monitoring tools
- **Manual search:** `"Brand Name" -site:yourdomain.com`

### Outreach

Short, friendly email:

> Hi [Name],
>
> Thanks for the mention of [Brand Name] in your piece on [topic]. We really appreciated it. Would it be possible to add a link to our site so readers can find us more easily? The URL is: [your URL]
>
> Happy to return the favor if we cover something relevant to you.
>
> [Your name]

Conversion rate: 30 to 60%+ when the mention is genuine and the ask is polite.

---

## Directory and Citation SEO

Structured listings in industry directories. Varies widely in value.

### High-Value Directories

**For Software as a Service (SaaS):**

- G2
- Capterra
- Clutch
- GetApp
- SoftwareAdvice
- HubSpot Marketplace
- Product Hunt
- TrustRadius

**For Local Services:**

- Google Business Profile (essential)
- Yelp
- Angi (formerly Angie's List)
- BBB (Better Business Bureau)
- Industry-specific (Avvo for legal, Healthgrades for medical, etc.)

**For Agencies:**

- Clutch
- DesignRush
- Sortlist
- The Manifest

### Submission Workflow

1. **Consistent NAP** (Name, Address, Phone) across every submission. Data inconsistency hurts local SEO.
2. **Detailed profile:** Full description, categories, photos, hours, payment methods
3. **Reviews:** Encourage customers to leave reviews on priority directories
4. **Monitor:** Check listings quarterly for accuracy; update if anything changes

**Real-world example:** An early-stage SaaS brand achieved 130+ directory and review-platform placements that built domain authority and referral traffic in parallel without paid placements.

---

## Toxic Links and Disavow

Spam backlinks can hurt rankings. Disavowing tells Google to ignore specific links when evaluating your site.

### Identifying Toxic Links

- Low-authority sites linking in high volume
- Irrelevant topic areas (a finance blog suddenly getting links from casino sites)
- Link schemes visible in Ahrefs: one IP network linking from thousands of domains
- Sudden spikes in new referring domains from low-quality sites
- **Programmatic detection at scale:** the DataforSEO Backlinks API returns referring domains with rank, anchor text, link attributes, and first-seen dates. Pull the full backlink profile, run anomaly detection on referring-domain velocity and quality scores, and flag spikes from low-quality clusters automatically.

### When to Disavow

- **Clear manual action or unnatural link warning in GSC:** Disavow is mandatory
- **Visible link spam campaign against you (negative SEO):** Disavow defensively
- **Ambiguous cases:** Google's John Mueller has said most sites don't need to disavow; they ignore low-quality links automatically

### Disavow Process

1. Build list of toxic domains or URLs
2. Format as disavow file (plain text):

```
# Comment
domain:spammydomain.com
https://specific-page.com/bad-link
```

3. Upload via Google's Disavow Tool
4. Monitor over next 3 to 6 months

---

## Brand Building as SEO

Strong brands rank better. Google measures brand signals through:

- **Branded search volume:** How often people search for your brand name
- **Direct traffic:** People navigating straight to your site
- **Social mentions and engagement**
- **Press coverage**
- **Wikipedia presence and knowledge panel**

### Tactics That Build Brand (and SEO)

- Consistent content publishing across a clear editorial POV
- Named authors with personal brand development
- Podcast appearances and interviews
- Speaking at industry conferences
- Partnerships and collaborations
- Community building (Slack, Discord, forums)
- Newsletter growth

Brand SEO is the long game. Results compound over years, not months.

---

# Part VI: Analytics, Tracking, Reporting

## Google Analytics 4 (GA4)

Google's event-based analytics platform. Replaced Universal Analytics in July 2023.

### Key Concepts

- **Events:** Every user action is an event. Page views, scrolls, clicks, form submissions, purchases.
- **Parameters:** Extra context attached to events.
- **Conversions:** Marked events you care about (leads, sales).
- **Audiences:** User segments based on behavior or properties.
- **Explorations:** Custom analysis reports.

### Standard Setup

**1. Install GA4 via Google Tag Manager (GTM)**

- Create GTM container
- Add GA4 Configuration tag
- Trigger on All Pages
- Deploy

**2. Configure key events as conversions**

- `form_submit`, `generate_lead`, `purchase`, `sign_up`
- Mark each as a conversion in GA4 Admin

**3. Set up channel groups**

- GA4 has default channel groups
- Add custom channel groups for AI referrers (perplexity.ai, chat.openai.com, copilot.microsoft.com, gemini.google.com)

**4. Link to Google Search Console**

- Admin → Product Links → Search Console Links
- Enables Search Console reports within GA4

**5. Link to Google Ads**

- For unified performance reporting

**6. Link to BigQuery**

- Free for up to 10 GB per day
- Essential for log-level analysis beyond GA4's UI limits

### Key Reports

- **Acquisition → Traffic Acquisition:** Sessions by channel, source, medium
- **Engagement → Landing Page:** Top landing pages with conversion data
- **Engagement → Events:** All events, filterable
- **Explore:** Custom reports for deep-dive analysis

### Common GA4 Pitfalls

- **Data thresholding:** GA4 hides data when user counts are low. Fix: link to BigQuery for raw data.
- **Attribution model shifts:** GA4 uses data-driven attribution by default; different from UA's last-click.
- **Session definition changes:** Sessions reset after 30 minutes of inactivity; UA defaulted to midnight.

---

## Google Search Console (GSC)

The most accurate source of organic search data. Free from Google.

### Verification

- **Domain property:** Verifies the entire domain (recommended)
- **URL-prefix property:** Verifies a specific subdomain or folder

### Key Reports

**1. Performance**

- Impressions, clicks, CTR, average position per query and per page
- Filter by date range, country, device, search type
- Export to CSV or link to BigQuery for 16-month historical data

**2. Coverage (Index → Pages)**

- Indexed pages vs submitted in sitemap
- Errors: Server error, Redirect error, Soft 404, Not found, Blocked by robots.txt
- Valid with warnings
- Excluded with reasons (Crawled – currently not indexed, Discovered – currently not indexed, Duplicate without user-selected canonical, etc.)

**3. URL Inspection**

- Check index status of any URL
- Request indexing for new or updated URLs
- See last crawl date
- See rendered HTML
- Test live URL

**4. Sitemaps**

- Submit and monitor sitemap status
- Indexation by sitemap

**5. Enhancements**

- Core Web Vitals (mobile and desktop)
- Mobile Usability
- Breadcrumbs, Products, FAQs, How-to, and other schema validations

**6. Links**

- Top linking sites
- Most linked pages
- Top linking text (internal)

**7. Security and Manual Actions**

- Any penalty notifications
- Hacked content or malware warnings

### GSC Best Practices

- Check Coverage weekly
- Use Performance report to find quick-win keywords (position 5 to 15, high impressions, low CTR)
- Submit every new priority URL via URL Inspection
- Link to GA4 for combined analysis
- Export historical data regularly (GSC shows 16 months; if you need longer, export and store)

---

## Looker Studio Dashboards

Free Google tool for building shareable, live-updating dashboards.

### Recommended Data Sources

- **Google Search Console connector** (official)
- **Google Analytics 4 connector** (official)
- **Google Ads connector** (official)
- **BigQuery** (for advanced or large-scale data)
- **Supermetrics** (connects Ahrefs, Semrush, HubSpot, and more; paid)

### Dashboard Types

**1. Executive SEO Dashboard**

- High-level metrics only
- Organic sessions, organic conversions, pipeline from organic, cost per lead
- Month-over-month and year-over-year comparisons
- Projection vs target

**2. Operational SEO Dashboard**

- Detailed performance
- Rankings by keyword cluster
- Landing page performance
- Indexation health
- Core Web Vitals trends
- Backlink velocity

**3. Client Reporting Dashboard (for agencies)**

- Brand-styled, simplified
- Sessions, leads, keyword wins, published content, links earned
- Narrative commentary

### Dashboard Principles

- One click to understand what happened
- Annotations for major events (migration, campaign launch, algorithm update)
- Comparison to goal and to previous period, always
- No more than 5 to 7 KPIs on the executive view

---

## BigQuery for SEO

Google's cloud data warehouse. Used for:

- GSC bulk data export (Google provides a free Search Console Bulk Export to BigQuery)
- Log file analysis
- Custom analytics beyond GA4's UI
- Joining data across sources (GSC + GA4 + CRM)

### Setup

1. Create a Google Cloud Project
2. Enable BigQuery API
3. Set up GSC Bulk Export (Admin → Search Console → Bulk export)
4. Link GA4 to BigQuery
5. Query via SQL

### Example Query: Find Keywords with High Impressions but Low CTR

```sql
SELECT
  query,
  SUM(impressions) AS total_impressions,
  SUM(clicks) AS total_clicks,
  SAFE_DIVIDE(SUM(clicks), SUM(impressions)) AS ctr
FROM `project.dataset.searchdata_site_impression`
WHERE data_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY)
GROUP BY query
HAVING total_impressions > 1000
ORDER BY ctr ASC
LIMIT 50;
```

These are quick-win candidates: ranking, getting impressions, but not attracting clicks. Rewrite titles and meta descriptions.

---

## Rank Tracking

Commercial tools that monitor your site's position for target keywords daily or weekly.

### Major Tools

- **Ahrefs Rank Tracker:** Included in Ahrefs subscription, good UI
- **Semrush Position Tracking:** Included in Semrush subscription
- **Accuranker:** Specialized, fast, clean data
- **STAT Search Analytics:** Enterprise, very deep feature set
- **SerpRobot, ProRankTracker:** Budget options

### Best Practices

- Track 100 to 500 priority keywords per site (more becomes unmanageable)
- Segment by keyword group: brand, pillar, cluster, long-tail, competitors
- Track by device (mobile vs desktop)
- Track by location (especially for multi-market or local SEO)
- Monitor share of voice against competitor set
- Set alerts for significant ranking drops

---

## Reporting Frameworks

### The 30/90/180 Reporting Cadence

**30-day update:**

- Short (1 page)
- Key metrics, what changed, what's coming next
- Audience: account manager, client main contact

**90-day QBR (Quarterly Business Review):**

- Deep report (10 to 20 pages or live dashboard walkthrough)
- Performance vs goals, key wins, key challenges, strategic recommendations
- Audience: client leadership, internal senior team

**180-day strategy refresh:**

- Review of the roadmap, adjustments for next 6 months
- Scenario modeling for next year
- Audience: client leadership, agency leadership

### The Narrative Report

Data alone is meaningless. Every report needs:

1. **Context:** What was the goal for this period?
2. **Performance:** Did we hit it? Where are we ahead or behind?
3. **Drivers:** What specifically drove the result?
4. **Learnings:** What do we know now that we didn't before?
5. **Next actions:** What are we doing in the next period and why?

---

# Part VII: Algorithm Updates

## Algorithm Update History

Key updates that reshaped SEO. Reference for historical context and pattern recognition.

| Update | Year | Impact |
|---|---|---|
| Panda | 2011 | Penalized thin, low-quality content sites |
| Penguin | 2012 | Penalized spammy link-building |
| Hummingbird | 2013 | Shifted toward understanding query meaning, not just keywords |
| Mobilegeddon | 2015 | Boosted mobile-friendly sites |
| RankBrain | 2015 | Machine learning integrated into ranking |
| BERT | 2019 | Improved understanding of natural language queries |
| Core Updates | 2018 to present | Regular broad quality signals recalibration |
| Helpful Content Update | 2022 | Penalized content written for search engines vs humans |
| Product Reviews Updates | 2021 to 2024 | Raised quality bar for review content |
| Spam Updates | 2021 to present | Targeted specific spam patterns |
| AI Overviews rollout | 2024 | SERP real estate reduced as AI answers displace clicks |

### Google Core Updates

Happen 3 to 4 times per year. Broad recalibrations of quality signals.

- **No fixable cause.** Google doesn't announce specific targets.
- **Winners and losers across categories.** Both sides are usually present.
- **Recovery is slow.** Takes months, sometimes until the next update.
- **The fix is not a hack.** Improve overall site quality (E-E-A-T, user experience, content depth).

---

## Diagnosing an Algorithm Hit

Sites sometimes lose traffic sharply. The question: is it an algorithm update, a technical issue, or something else?

### Diagnostic Workflow

**1. Isolate the drop**

- When did it start? (GA4 or GSC shows the exact date)
- What pages dropped? (Landing page report)
- What queries dropped? (GSC Performance report, compare periods)
- What countries dropped? (for international sites)

**2. Cross-reference with known updates**

- Check Search Engine Roundtable, MozCast, Semrush Sensor
- Check Google Search Central blog for announced updates
- Ahrefs Rank Tracker "Compare" mode to see pre-vs-post update rankings

**3. Rule out technical issues**

- Was there a deploy around that date?
- Are pages still indexed?
- Did robots.txt change?
- Did canonicals break?
- Did site speed degrade?

**4. Rule out external issues**

- Backlink loss (major referring domain dropping you)
- Brand crisis affecting search volume or trust signals
- Competitor surge (someone else got much better, relatively pushing you down)

**5. Document hypothesis**

- Most likely cause
- Evidence supporting it
- Proposed next action

---

## Recovery Strategies

### For Core Updates

- **Don't panic-fix.** Small changes rarely recover core-update losses.
- **Audit content quality.** Remove or consolidate thin pages. Update outdated content.
- **Strengthen E-E-A-T.** Author bios, author schema, citations, trust signals.
- **Improve user experience.** Core Web Vitals, ad density, intrusive interstitials.
- **Wait.** Full recovery often requires the next core update (3+ months later).

### For Helpful Content Hits

- **Remove AI-generated thin content.**
- **Consolidate or improve helpful-but-thin articles.**
- **Make content demonstrably more useful than alternatives.**
- **Add real expertise signals** (named authors, first-person examples).

### For Technical Regressions

- **Fix the technical issue.**
- **Re-submit priority URLs via GSC URL Inspection.**
- **Monitor re-indexation.**
- Recovery can be days to weeks, not months.

### For Link-Based Hits

- **Disavow toxic links if manual action applies.**
- **Earn fresh high-quality links** to rebuild signal.
- **Re-request reconsideration in GSC if penalty is manual.**

---

# Part VIII: Generative Engine Optimization (GEO) and Answer Engine Optimization (AEO)

## How AI Search Engines Work

AI answer engines (ChatGPT search, Perplexity, Google AI Overviews, Copilot, Gemini) use Retrieval Augmented Generation (RAG).

### The RAG Flow

1. **User submits query**
2. **AI system decides this is a retrieval-requiring query**
3. **AI system sends query to a search index** (Google, Bing, or a proprietary index)
4. **Top 5 to 20 results are retrieved**
5. **The AI reads the retrieved content**
6. **The AI synthesizes an answer citing the retrieved sources**

### Implications for SEO

- **Traditional SEO is the prerequisite.** If you're not in the search index, you can't be retrieved.
- **Ranking well in traditional SEO correlates with being cited by AI.** Strong rankings are the first filter.
- **Content structure matters more, not less.** Clear, direct answers are easier to extract.
- **Zero-click shift.** AI answers often resolve queries without the user clicking through. Measure by share of citations, not just clicks.

---

## Optimizing for AI Citation

### Entity Optimization

Make your brand, authors, and products clearly identifiable as entities.

- **Organization schema** on every page (or at least homepage)
- **Person schema** for named authors
- **Consistent brand naming** across all web properties (same capitalization, spelling, taglines)
- **About Us page with rich entity information:** founding date, founders, location, focus areas
- **Author bios** with credentials, linked social profiles, published work
- **Wikipedia presence** if editorially warranted (high bar, don't fabricate)
- **External entity mentions** on authoritative sites with consistent descriptions

### Structured Answers

AI systems prefer content that directly answers questions in the first sentence of a section.

- **Lead with the answer** in every section
- **Use H2 and H3 headings phrased as questions** for informational content
- **Include definition-style openings:** "X is [definition]. It works by [explanation]."
- **Use tables and bullet lists** where content is naturally enumerable
- **Cite sources inline** with clear attribution

### Original Data and Research

AI systems strongly favor content with original stats not available elsewhere.

- **Annual benchmark reports**
- **Survey-based research**
- **Proprietary product data insights**
- **Case studies with specific numbers**
- **Clear methodology sections** describing how data was collected

### Topical Comprehensiveness

AI systems prefer sources that cover a topic comprehensively, not surface-level.

- **Map every subtopic and related question** within your niche
- **Build pillar-cluster architecture** with deep coverage
- **Answer every common question** about your topic area
- **Update content regularly** to stay current

### GEO-Specific Schema

- `Organization`
- `Person`
- `Article` with rich metadata
- `FAQPage` for direct answer material
- `HowTo` for step-by-step content
- `Product` with detailed attributes for e-commerce AI shopping

---

## Measuring AI Search Visibility

### AI Referrer Tracking

Create a custom channel group in GA4:

- perplexity.ai
- chat.openai.com
- chatgpt.com
- copilot.microsoft.com
- gemini.google.com
- claude.ai
- you.com

Segment analytics by this channel to measure traffic from AI sources.

### AI Citation Monitoring Tools

- **Profound:** Monitors brand mentions in AI responses
- **Otterly.ai:** Tracks AI citation frequency
- **Peec.ai:** Similar function
- **Manual testing:** Periodically query target keywords in ChatGPT, Perplexity, Gemini to see if your brand is cited

### AI Visibility Metrics

- **Citation share:** Percentage of relevant AI responses that cite your site
- **Citation position:** Is your site cited primary, secondary, or not at all?
- **Context quality:** Is the AI citing you in a positive, neutral, or negative context?
- **Referral traffic from AI sources:** GA4 custom channel group

---

# Part IX: Engagement Playbooks

## Days 1 to 14 – Diagnosis

The technical depth behind the high-level 14-day plan:

**Week 1 (Days 1 to 7): Foundation Audit**

- Day 1: Site access, tool setup (GSC, GA4, Looker Studio, Ahrefs project)
- Day 2: Full Screaming Frog crawl at desktop and mobile user agents
- Day 3: Log file analysis (if available) or crawl stats review
- Day 4: Content inventory (every indexed URL, with traffic and ranking data)
- Day 5: Keyword research baseline
- Day 6: Competitor gap analysis
- Day 7: On-page audit of top 10 revenue-linked pages

**Week 2 (Days 8 to 14): Off-Page + Roadmap**

- Day 8: Backlink profile audit
- Day 9: Link reclamation opportunities identified
- Day 10: Digital PR angles identified
- Day 11: Technical recommendations drafted
- Day 12: Content roadmap drafted
- Day 13: Roadmap review with stakeholders
- Day 14: Final roadmap delivered

**Deliverable:** Tiered roadmap (critical fixes, high-impact wins, compounding work) with commercial rationale per item.

---

## Days 15 to 30 – Quick Wins

Execution phase for fastest commercial wins.

- Technical critical fixes (redirect chains, broken canonicals, indexation blockers)
- Title tag and meta description rewrites on position 6 to 15 pages
- Internal linking audit and corrections
- Schema markup implementation on priority pages
- First digital PR pitches sent
- First content refresh cycle kicked off
- First GSC URL Inspection re-submission batch

**Expected result by Day 30:** 5 to 15% lift in clicks from existing pages, fast-win indexation recoveries, first backlink wins landing.

---

## Days 30 to 90 – Roadmap Execution

Building new capacity.

- Pillar and cluster page construction
- Content velocity ramp (4 to 12 articles per month)
- Programmatic SEO setup (if applicable)
- Core Web Vitals project execution
- International SEO setup (if applicable)
- Schema rollout across site
- Ongoing digital PR campaigns (1 to 2 data studies)
- Monthly reporting cadence established

**Expected result by Day 90:** 30 to 60% organic traffic growth, first pipeline contributions traceable to SEO, stabilized measurement infrastructure.

---

## Month 3 to 6 – Compounding Work

Scale phase.

- Topical authority rollout (full cluster architecture live)
- Backlink velocity sustained (10+ new referring domains per month)
- Content refresh cycle operationalized (monthly refresh of top 10 decaying pages)
- GEO and AEO deliverables live
- International expansion (if roadmap calls for it)
- Junior team mentorship and delegation of recurring tasks
- Automated reporting (Looker Studio dashboards for client and internal)

**Expected result by Month 6:** 60 to 150% organic traffic growth over baseline, compounding MQL growth, strong and defensible domain authority.

---

## Month 6+ – Scale and Expansion

Long-horizon investments.

- Advanced schema rollout
- Content operations system (templates, SOPs, editorial calendar, multi-contributor workflows)
- Backlink acquisition at enterprise scale (10+ referring domains per month, from DR 60+ sites)
- Brand-building content
- Team expansion
- Advanced reporting and forecasting infrastructure
- New market or new vertical expansion

**Expected result by Month 12:** 150 to 400% growth in organic traffic over starting baseline for a well-executed program.

---

# Part X: Scenario Playbooks

## Traffic Drop Diagnosis

Covered in [[#Diagnosing an Algorithm Hit]]. Short version:

1. Isolate the drop (when, what pages, what queries)
2. Rule out technical issues (deploy, robots.txt, canonicals, speed)
3. Check for algorithm updates
4. Rule out external issues (link loss, brand crisis)
5. Document hypothesis
6. Execute fix or wait (for core updates)

---

## Ranking Drop Diagnosis

For specific pages that dropped in rankings.

1. **URL Inspection in GSC:** Is the page still indexed? Any crawl errors?
2. **On-page audit:** Any recent content change? Title tag change?
3. **SERP check:** What's ranking now? Is the SERP type changing (e.g., now showing video, forum, or AI results)? **Programmatic comparison:** the DataforSEO SERP API returns historical SERP snapshots, so you can compare today's SERP against a snapshot from before the drop and see exactly which competitors moved up, what new SERP features appeared, and whether the SERP intent has shifted.
4. **Backlink profile:** Did the page lose any important backlinks? Pull the DataforSEO Backlinks API "lost backlinks" report for the URL to see exact lost links and their referring-domain authority.
5. **Competitor check:** Did a competitor publish better or earn significant links?
6. **Internal linking:** Did the page lose internal links (e.g., navigation redesign)?

**Fix options:**

- Content refresh (match or exceed current top-ranking pages)
- Re-earn backlinks if lost
- Restore internal links if removed
- Check for E-E-A-T degradation (removed author, removed sources)

---

## New Site Launch

Building a site from zero.

**Pre-launch:**

- Domain selection (avoid EMD/PMD unless brand makes sense)
- Hosting with good Time to First Byte
- CMS selection (Webflow, WordPress, Next.js SSG, etc.)
- Initial information architecture (homepage, services, about, contact, blog, 15 to 30 landing pages)
- Keyword research for all planned URLs
- Schema markup baseline (Organization, LocalBusiness if relevant)
- GSC and GA4 set up and verified

**Launch week:**

- Sitemap submitted in GSC
- URL Inspection requests for priority pages
- Internal linking between all launched pages
- First backlink outreach (directories, press release, partner mentions)
- Digital PR planned for 30 to 60 day post-launch

**Post-launch:**

- Weekly indexation monitoring
- Content velocity kicks in
- Backlink velocity kicks in
- First data snapshot at 30 days to inform next phase

---

## Content Refresh Campaign

Systematic refresh of decaying content. Quarterly cadence.

**Discovery:**

- GA4 landing page report: pages with 30%+ traffic decline last 3 months vs prior 3 months
- GSC Performance: pages dropping in average position over last 90 days
- Ahrefs Organic Keywords: track keyword loss per page

**Prioritization:**

- Revenue-weighted: pages driving leads or sales first
- Traffic-weighted: pages driving sessions second
- Authority-weighted: pages with backlinks third

**Execution (per page):**

- Full competitor SERP audit at current ranking
- Content gap analysis (what current top-rankers have that this page doesn't)
- Stat and example updates
- Image refresh
- Internal link updates (in and out)
- Meta tag rewrite if CTR has declined
- `dateModified` schema update
- GSC URL Inspection re-submission

**Measurement:**

- Track ranking and traffic for 30 days post-refresh
- Target: 20 to 50% traffic recovery within 30 days for pages previously ranking well

---

## Link Audit

Quarterly or semi-annual audit of backlink profile.

**Tools:** Ahrefs, Semrush, Majestic, GSC Links report. For programmatic recurring audits (multi-client agency, large enterprise site, automated reporting), the DataforSEO Backlinks API provides full backlink data via API: referring domains, anchor text, link attributes, first-seen / lost dates, and quality scores. Pipe into a database and run the audit as a scheduled job rather than a manual export.

**Questions to answer:**

- How many referring domains total?
- Growth trend: referring domains per month
- Quality mix: DR 60+, DR 30 to 60, DR 0 to 30
- Relevance mix: topically aligned vs off-topic
- Toxic link check: any spam patterns?
- Competitor comparison: how does our profile stack up?
- Lost links: any recent losses of high-value referring domains?

**Actions:**

- Recover lost links via outreach
- Disavow toxic links (if manual action applies)
- Double down on strategies earning quality links
- Identify gap: what kind of links are competitors earning that we aren't?

---

## International Expansion

Adding a new market to an existing site.

**Pre-expansion:**

- Market research: is there real search demand in the target market?
- Competitor analysis in target market (local competitors, established players)
- Market-specific keyword research in native language
- Content strategy: translate (rarely), transcreate (better), or original (best for high-stakes markets)
- Legal and compliance (GDPR in Europe, local data laws, etc.)

**Technical setup:**

- URL structure decision (ccTLD, subdirectory, or subdomain)
- Hreflang implementation across all markets
- Currency and payment localization for e-commerce
- Hosting considerations (CDN with edge locations in target market)
- GSC property setup and geotargeting

**Launch:**

- Sitemap submission
- URL Inspection for priority pages
- Initial content velocity in new market
- Initial backlink outreach to in-market sites
- Local directory submissions

**Monitoring:**

- Track rankings by market
- Track organic traffic by country
- Track conversions by market
- Monitor for cross-market cannibalization (wrong market ranking in SERPs)

---

# Part XI: Cross-Functional Collaboration

## Working with Developers

Developers implement technical SEO. A bad brief creates delays; a great brief unlocks speed.

### The Developer-Friendly Brief

Every SEO request to a developer should include:

- **What needs to happen** (the specific change)
- **Why it matters** (the SEO rationale, tied to a ranking or user experience outcome)
- **Where to make the change** (file, component, template)
- **How to verify** (test case, validation tool)
- **Links to documentation** (Google docs, schema.org, Ahrefs resource)

### Common Developer Collaboration Points

- Schema markup implementation
- Canonical tag logic
- Redirect handling
- Core Web Vitals optimization
- Rendering mode selection for new builds
- Internal linking in navigation or footer
- `hreflang` generation for international sites

### Anti-Patterns

- SEO sends a 200-item audit without prioritization
- SEO requests without business rationale
- SEO changes that break analytics tracking
- SEO demands without understanding engineering constraints

### Pro Moves

- Understand the CMS and framework the dev team uses
- Write changes as Jira tickets or Linear issues, not emails
- Include acceptance criteria
- Participate in sprint planning
- Offer to pair with developers on complex changes

**Example outcome when executed well:** A migration run with a clear technical brief, pre-staging review, launch-day coordination, and daily monitoring. Developers had no blockers; SEO had no surprises.

---

## Working with Content Teams

Content teams create the assets SEO ranks. The friction point: writers want creative freedom; SEO wants keyword coverage and structure.

### The Content Brief

Every SEO-driven content piece should have a brief covering:

- **Primary keyword and cluster**
- **Search intent** (informational, commercial, etc.)
- **Target audience**
- **Content outcome** (what should the reader do after reading?)
- **Competitor references** (top 3 ranking pages, what they cover)
- **Key questions to answer** (from People Also Ask, keyword research)
- **Recommended structure** (H2 and H3 outline)
- **Word count range**
- **Internal links to include**
- **Optional tone and voice notes**

### Anti-Patterns

- Briefs that are keyword lists without narrative direction
- Briefs without competitor context
- Overly rigid briefs that kill writer voice
- Briefs sent without publishing date

### Pro Moves

- Brief for outcomes, not just SEO checkboxes
- Pair with writers on first drafts (or first article with a new writer)
- Review outlines before drafting
- Edit for SEO as a final pass, not a first pass

---

## Working with Paid Media Teams

SEO and Paid are often siloed. When aligned, they multiply each other.

### Shared Opportunities

- **Keyword research sharing:** Paid has conversion data by keyword; SEO has ranking data. Together they prioritize commercial keywords.
- **Landing page testing:** Paid tests landing pages fast; SEO adapts winners for organic.
- **SERP occupation:** Running paid ads on keywords you already rank organically. Increases real estate and defends against competitors.
- **Brand term defense:** Paid on brand keywords to block competitors bidding on your name.
- **Remarketing from organic:** Capture organic visitors in remarketing lists for Paid Display.

### Coordination

- Weekly sync on performance
- Shared reporting dashboard
- Joint QBR presentations
- Coordinated testing calendar

---

## Working with Sales Teams

SEO generates leads; sales closes them. If the handoff is broken, SEO looks like it's not working.

### Lead Routing

- **Lead scoring model:** Map behaviors to priority (demo request > trial signup > content download)
- **CRM integration:** Every organic lead should enter CRM with source attribution
- **SLA for sales response:** Best practice is under 5 minutes for demo requests
- **Feedback loop:** Sales tells SEO which leads converted and which didn't

### SEO-to-CRM Pipelines

Shape:

- Organic traffic lands on a landing page
- Landing page captures lead with form
- Form submission fires event to CRM
- CRM routes to appropriate sales rep based on segment
- Sales qualification scored and returned to SEO reporting

### Sales Enablement Content

SEO content often doubles as sales enablement. Case studies, comparison pages, integration pages, use-case pages, technical documentation. Coordinate with sales on what they want to send prospects; that's often what should rank.

---

## Working with Stakeholders

Executive stakeholders pay for SEO but rarely understand it deeply. Communication is half the job.

### Framing Rules

- **Lead with business impact:** pipeline, revenue, retention. Never lead with rankings or traffic.
- **Translate jargon:** "Indexation rate" becomes "the percentage of pages Google can actually show in search." "Core Web Vitals" becomes "how fast and stable the site feels."
- **Be transparent about timeline:** SEO takes months. Don't overpromise Q1 results in October.
- **Be honest about competitive dynamics:** Sometimes a competitor moves, and it's not your fault.
- **Show the cost comparison:** Cost per lead from organic vs paid, especially over time.

### Difficult Stakeholder Patterns

- **"Why don't we rank first for [keyword]?":** Address with SERP education, competitive context, realistic timeline, specific action plan.
- **"Paid does this in a week; why does SEO take 6 months?":** Explain the compounding nature, the cost curve, and the defensibility over time.
- **"My nephew says SEO is dead.":** Engage seriously, ground the response in data, show AI search is additive not replacing, demonstrate current results.
- **"Why are we investing in this if it's not showing results yet?":** Revisit the agreed timeline, show leading indicators (impressions, rankings, indexation), preview Q2 or Q3 projections.

**Framing line (for handling pushback):** "I stay on the data and keep the conversation about outcomes. When someone pushes back, I treat it as a signal to explain my reasoning more clearly, not to retreat from it."

---

# Part XII: Complete SEO Tool Reference

Every tool a senior SEO should know, by category. Free vs paid noted.

### Technical Crawlers

- **Screaming Frog SEO Spider:** Desktop crawler. Industry standard. Free up to 500 URLs, paid £199/year after.
- **Sitebulb:** Alternative desktop crawler. Strong visual reporting.
- **DeepCrawl (Lumar):** Cloud-based, enterprise.
- **OnCrawl:** Cloud-based, technical SEO focus, integrates with logs.
- **Botify:** Enterprise crawler with log file analysis.

### Keyword Research

- **Ahrefs Keywords Explorer:** Primary keyword research tool (UI, subscription)
- **Semrush Keyword Magic:** Alternative with strong SERP features data (UI, subscription)
- **DataforSEO Keywords Data API + Labs API:** Programmatic, pay-per-request alternative. Best when keyword data needs to feed custom workflows, AI pipelines, or programmatic content generation. Significantly cheaper at scale than Ahrefs/Semrush.
  - **No-code wrapper:** [DataForSEO Google Sheets Extension](https://workspace.google.com/marketplace/) lets you query the same APIs from a spreadsheet without writing code. Useful for ad-hoc keyword pulls, quick competitor checks, or handing the data layer to a non-technical teammate while keeping cost-per-request economics.
- **Google Keyword Planner:** Free, direct from Google
- **Keyword Insights:** Keyword clustering
- **AnswerThePublic:** Question-based keywords
- **AlsoAsked:** People Also Ask scraping

### Rank Tracking

- **Ahrefs Rank Tracker**
- **Semrush Position Tracking**
- **Accuranker**
- **STAT**
- **DataforSEO SERP API:** API-first rank tracking. Pull live SERPs at any volume, store in your own database (BigQuery typical), build dashboards on top.

### Backlink Analysis

- **Ahrefs Site Explorer:** Industry leader
- **Semrush Backlink Analytics**
- **Majestic:** Deep historical data
- **Moz Link Explorer**
- **DataforSEO Backlinks API:** Programmatic backlink data. Live and historical referring domains, anchor text, link attributes, lost-and-gained reports. Pay-per-request, ideal for recurring agency-scale audits or feeding alerting pipelines.

### Content Optimization

- **SurferSEO**
- **Clearscope**
- **Frase**
- **MarketMuse**
- **SEOwallet (Chrome extension):** In-browser on-page SEO checker. Surfaces title/meta/H1, word count, headings, image alt coverage, and basic schema while you read or edit a page. Useful for quick spot-checks during content review without opening Screaming Frog or running a crawl.

### Analytics

- **Google Analytics 4:** Free
- **Google Search Console:** Free
- **Looker Studio:** Free
- **BigQuery:** Free tier up to 10 GB/day

### Log File Analysis

- **Screaming Frog Log File Analyser**
- **Botify**
- **OnCrawl**

### Schema and Structured Data

- **Google Rich Results Test:** Free
- **Schema.org Validator:** Free
- **Schema Markup Generator (technicalseo.com):** Free

### Core Web Vitals

- **PageSpeed Insights:** Free
- **Chrome DevTools:** Free
- **Lighthouse:** Free
- **CrUX Dashboard:** Free via Looker Studio connector
- **SpeedCurve, Calibre, DebugBear:** Paid, continuous monitoring

### AI Search Visibility

- **Profound**
- **Otterly.ai**
- **Peec.ai**

### Local SEO

- **Google Business Profile Manager:** Free
- **BrightLocal:** Local rank tracking and citation management
- **Whitespark:** Citation building

### International SEO

- **Hreflang Tags Generator (Sistrix):** Free
- **Sistrix International Visibility**

### Digital PR

- **Connectively (formerly HARO):** Free and paid tiers
- **Qwoted**
- **Featured.com**
- **Muck Rack, Cision:** Journalist databases, enterprise pricing

### Competitor Research

- **Ahrefs Site Explorer**
- **Semrush Domain Overview**
- **Similarweb:** Traffic estimates
- **DataforSEO Labs API (Domain Analytics + Domain Intersection):** Programmatic competitor intel. Pull traffic estimates, ranked keywords, content gaps, and SERP overlap with competitors at scale. Designed to feed custom dashboards and automated reports.
- **Wayback Machine:** Historical snapshots

### Programmatic and API-First SEO Data

A category in its own right because the workflow shape differs from UI-based tools. Use these when SEO data needs to feed custom code, AI agents, dashboards, or automated pipelines rather than a vendor UI.

- **DataforSEO:** The most comprehensive programmatic SEO data provider. APIs cover Keywords Data, Labs (advanced research), SERP, Rank Tracker, Backlinks, On-Page, Domain Analytics, Content Analysis, Business Data (local), Merchant (e-commerce), and search engines beyond Google (Bing, YouTube, Amazon). Pay-per-request, no subscription. Standard backbone for AI-assisted SEO workflows, custom dashboards, and large-scale or recurring data pulls.
- **Google Search Console API:** Free, programmatic access to GSC Performance, Coverage, and URL Inspection data. Combine with BigQuery for long-term storage beyond the GSC UI's 16-month limit.
- **Google Analytics Data API (GA4):** Programmatic GA4 reporting. Combine with GSC API and DataforSEO for unified custom dashboards.
- **Ahrefs API:** Available on enterprise tiers, more expensive than DataforSEO at most scales.
- **Semrush API:** Available on top-tier plans, similar tradeoffs to Ahrefs.

### AI-Assisted SEO

- **Claude, Claude Code:** Custom workflow automation for audit scaffolding, content brief generation, competitor analysis, schema generation
- **ChatGPT:** General AI assistance
- **Perplexity:** Research with citations
- **Custom GPTs or Claude skills:** For repeat workflows (audit templates, content briefs, etc.)

---

## How This Reference Pairs With the seo-audit Skill

This reference is organized for progressive disclosure. Load only the section you need:

- **Audit kickoff or stakeholder conversation:** Part I (Foundations), Part II (Strategy Layer)
- **Executing a technical audit:** Part III (Technical SEO), Part VI (Analytics, Tracking, Reporting), Part X (Scenario Playbooks)
- **Executing an on-page or content audit:** Part IV (On-Page and Content SEO)
- **Executing a link or authority audit:** Part V (Off-Page SEO)
- **Diagnosing a traffic drop or ranking drop:** Part VII (Algorithm Updates), Part X (Scenario Playbooks)
- **AI search positioning questions during an audit:** Part VIII (GEO / AEO) — the dedicated `ai-seo` skill covers this more tactically
- **Planning a multi-phase engagement from an audit finding:** Part IX (Engagement Playbooks)
- **Writing audit briefs for developers, content teams, stakeholders:** Part XI (Cross-Functional Collaboration)
- **Recommending tools in an audit:** Part XII (Tool Stack)

**Relationship to SKILL.md:** SKILL.md provides the audit workflow (when to check what, output format, priority order). This reference provides the depth behind the checks — *why* each check matters, *how* to diagnose more rigorously when the surface check is inconclusive, and *what to do* when you find the issue.

When the audit question is surface-level, SKILL.md is sufficient. When the audit question requires deeper diagnosis (e.g., "the site has no crawl errors but pages still aren't indexed," "traffic dropped after a core update," "a migration is planned and we need to scope the SEO risk"), reach into this reference.

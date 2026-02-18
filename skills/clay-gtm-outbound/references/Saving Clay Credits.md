# Saving Clay Credits

If you're scaling outbound with Clay, your workflows are only as good as your credit management. While Clay is a powerhouse for list building, enrichment, and AI workflows, many teams burn hundreds of credits unnecessarily, often without realizing it.

This guide covers how to operate with maximum precision and minimum waste.

---

## 1. Filtering Upstream

The first rule of saving credits: don't enrich what you don't need.

Clay isn't where list building begins. It's where you fine-tune it. Work with only the data that actually matters.

**How:**
- Use filters in Apollo, Sales Navigator, Ocean.io, or Cognism to narrow your list by job title, company size, industry, and tech stack
- Pre-clean data in Google Sheets with filters or deduplication

**Example:** Targeting VP Marketing in SaaS companies over 50 employees. Use filters in Apollo before pushing to Clay. Add a formula column in Sheets to exclude interns, founders, or sales titles.

---

## 2. Use CSV Workflows to Avoid Paid Webhooks

If you're not on Clay's $314/mo Explorer plan, webhooks and HTTP API connections may not be available. Instead of upgrading just to move data between tools, use CSV workflows.

**How:**
- Export scraped data from Apify or other tools as CSV
- Upload cleaned CSV into Clay manually
- Download your final enriched Clay table as CSV
- Upload into your sequencer (Smartlead, Instantly, etc.)

This avoids paying for webhook/API access while keeping your workflow fully functional.

**Pro Tip:** Manual CSV transfer is slower, but zero-credit and zero-plan-upgrade.

---

## 3. Test & Expand

Never run a full table without testing your enrichment flows first.

**How:**
- Start with 10-20 rows and disable auto-update
- Review outputs
- Expand to 100-200 rows
- Once confident, enable auto-update and run a full table

**Use case:** You're enriching job titles using AI to map to personas. Test the agent on 10 rows. If the output aligns, then scale. If not, tweak the prompt.

**Pro Tip:** Always keep "Auto-Update" OFF until you're 100% sure about the outcome.

---

## 4. Formulas & Conditionals

Conditionals and formulas are your first line of credit defense.

**Key tactics:**
- Use `only run if` logic to avoid enriching blank or DQ'd rows
- Use formulas to qualify/disqualify based on job title, seniority, or industry

**Example formula:**
```
only run if: email is not empty AND title includes "VP" or "Head"
```

**Use case:** You scraped 1,000 rows from Crunchbase. Use a `unique()` formula to deduplicate domains and only enrich 150 unique companies.

---

## 5. Lookups & Write to Other Tables

Avoid enriching the same company or job signal multiple times.

**The Trick:** Split enrichments into two layers:
1. Prospect-level (people table)
2. Account-level (company table)

**Workflow:**
- Push unique companies to a separate table
- Enrich company-level data (funding, tech stack, industry)
- Use lookups to bring enriched data back into the people table

**Example:** You've got 3 contacts from Notion. Instead of enriching company data 3 times, write to an account table, enrich once, then pull info back via lookup.

**Clay Feature:** Write to Table + Lookup (both credit-free)

---

## 6. Use Your Own APIs

Clay native enrichments cost credits. External APIs? Not always.

**Recommended Tools:**
- **LeadMagic** - email + LinkedIn scraping
- **Prospeo** - email enrichment
- **FullEnrich** - waterfall enrichment
- **OpenAI API** - AI personalization
- **Debounce / Neverbounce** - email verification

**Example:** Instead of using "Enrich Person from Profile" in Clay (1 credit), use LeadMagic's API via HTTP enrichment (costs nothing in Clay).

**Advanced tip:** Create enrichment templates using HTTP request once, then reuse across tables.

---

## 7. Waterfall Enrichment Strategy

Stack multiple providers to maximize email coverage.

**Typical Waterfall:**
1. LeadMagic (fast and cheap)
2. Prospeo (accurate)
3. Icypeas
4. Clay native (fallback)

**How:** Use conditional enrichments:
```
only run if: email_1 is empty → then run email_2
```

**Bonus:** Add Debounce at the end to validate emails.

---

## 8. Smart AI Usage

AI enrichments (Claygent, Agents, Helium/Neon) are powerful, but costly.

**Save like a pro:**
- Use **OpenAI's gpt-4o via custom API** (costs less than Clay models)
- For scraping or research: start with **Helium** → test → scale
- If needed, **upgrade to Neon** for deeper scraping

**Use case:** Ask GPT to analyze job title and assign a persona category. Only run contact enrichment if the title = "Marketing" or "Sales" persona.

---

## 9. Offload Heavy Scraping Outside Clay

Clay is powerful for structured enrichment and signals. It is not built to handle large-scale scraping or deep social monitoring at scale.

**For high-volume scraping, use:**
- Apify
- Phantombuster
- Outscraper
- Zenrows

**Use these tools for:**
- Website scraping
- Review scraping
- LinkedIn extraction
- Social monitoring
- Large data pulls

Then push cleaned results into Clay for qualification, segmentation, and structured enrichment.

**Clay Signals work best for:**
- Job changes
- Hiring signals
- Funding
- Tech stack detection
- Structured growth triggers

**Rule of thumb:** Scrape outside. Enrich and trigger inside.

---

## 10. Enrich Once, Leverage Many Times

Don't enrich email, phone, company data twice. Ever.

**Use Deduplication + Lookup combo:**
- Deduplicate by domain
- Enrich once
- Lookup back into multiple tables (e.g., for phone, website, social profiles)

---

## Summary: Tools That Save Your Credits

| Data Point / Action | Best Tool | Cost (Credits) | Notes |
|---|---|---|---|
| Heavy Scraping | Apify, Phantombuster, Zenrows, Outscraper | 0 in Clay | Scrape outside, import via CSV |
| Social Monitoring | Apify, Phantombuster | 0 in Clay | Use Clay for structured signals only |
| Finding Email | Prospeo, LeadMagic, Datagma (API) | 0 | Run waterfall before Clay native |
| Email Verification | Debounce (API) | 0 | Validate at end of waterfall |
| Domain Name | Serper (API), Clearbit | 0 | Avoid native lookup when possible |
| News | Serper (API) | 0 | Use template; cheaper than native enrichment |
| Gen AI | GPT-4o-mini (API) | 0 | Use Neon only when 4o-mini fails |
| CSV Data Movement | Manual CSV export/import | 0 | Avoid Explorer plan if not needed |
| Company Growth | LinkedIn | 1 | Native signal, structured and reliable |
| Website Competitors | Google Search + GPT-4o-mini | 1 | Skip paid tools unless necessary |
| Website Data | Semrush | 2 | Only run after qualification gates |
| Google Maps Scraping | Outscraper | 0 | Login via 1Pass |
| Technology Detection | BuiltWith (via Apify) or Claygent 4o-mini | 0 | Replace tech name via formula |
| Company Enrichment | LinkedIn | 1 | Employee size, founded date, industry |
| Contact Enrichment | LinkedIn | 1 | Run only after persona qualification |
| Headcount Data | LinkedIn | 1 | Total, by role, by location |
| Fundraising Data | Intellizence | 1 | Run only for funded ICP |
| Site Traffic (e-comm) | StoreLeads | 1 | Otherwise use Semrush (2 credits) |
| Reviews | G2, Capterra via Apify/Zenrows | 0-3 | Avoid native 3-credit pull when scraping works |
| Manipulate Cell Data | Clay AI Formula Writer | 0 | Use for deterministic logic |
| LinkedIn Ads Detection | Serper (API) | 0 | Template-based |
| Open Jobs | LinkedIn, PredictLeads | 1 | Structured hiring signal |

# Prospecting with Clay

James Praise | Marketing In Action
Prospecting with Clay 2
Overview 2
Key Concepts 2
What is GTM Engineering? 2
Principles of GTM Engineering 2
Core Components of Prospecting 3
GTM Building Blocks 3
The Four-Step Data Workflow 3
Prospecting Workflow 3
Core Prospecting Concepts 3
AI Concepts in GTM Engineering 4
Step-by-Step Processes 4
Building a Targeted Company List 4
Enriching Company Data 4
Finding & Enriching People 4
Using AI Enrichment (Claygent) 5
Advanced Techniques 5
Noteworthy Questions & Answers 5
Practical Applications 6
GTM Beyond Outreach 6
Key Takeaways 6
Marketing Newsletter | Marketing Resources | Marketing Services

James Praise | Marketing In Action
Prospecting with Clay
Overview
This session introduced the principles and practices of GTM (Go-to-Market) Engineering—a
systematic approach to scaling sales, marketing, and customer outreach using automation, AI, and data
enrichment.
The instructors walked through the history of GTM Engineering, its philosophical underpinnings, and
gave a hands-on demo of how to build targeted prospect lists, enrich them with data, and automate
workflows in Clay.
The structure of the session:
1. Background & Principles of GTM Engineering
2. Framework for data workflows: Find → Enrich → Transform → Export
3. Hands-on demo: building lists & enrichments in Clay
4. AI-powered enrichments (Claygent, prompting, agents)
5. Breakout exercises for participants
6. Advanced Q&A (conditional runs, segmentation, LinkedIn integrations, lookalike
companies, etc.)
Key Concepts
What is GTM Engineering?
● A modern approach to sales and marketing operations.
● Combines data engineering, automation, and AI to speed up tasks traditionally done by
BDRs/SDRs.
● Replaces repetitive manual work (prospecting, copy-pasting, enrichment) with scalable AI-driven
workflows.
● Goal: Free humans to focus on creative, strategic, and relationship-building tasks.
Principles of GTM Engineering
● Quality > Quantity – Personalized, high-quality outreach beats mass email blasting.
● Data is the foundation – Garbage in, garbage out. Success depends on CRM health and strong
enrichment pipelines.
● Computational thinking – Use database concepts (e.g., company-to-people relationships) and
conditional logic (if/then) to design efficient workflows.
● Automation + AI synergy – Machines should handle repetitive enrichment; humans focus on
personalization and creative messaging.
Marketing Newsletter | Marketing Resources | Marketing Services

James Praise | Marketing In Action
Core Components of Prospecting
● Data Clearinghouse: Access 100+ data providers in one place.
● Waterfall Enrichments: Sequential provider searches maximize coverage.
● AI Research Agent: Use AI to search web & answer custom questions.
● Personalized Messaging: Generate/send relevant emails with AI builder.
GTM Building Blocks
● Layer 1 – Data: TAM sourcing, CRM enrichment.
● Layer 2 – Automation: Account research & scoring, inbound lead enrichment.
● Layer 3 – GTM: Signals & intent, account-based marketing, GTM Copilot, AI outbound.
The Four-Step Data Workflow
1. Find – Identify companies and people that fit your Ideal Customer Profile (ICP).
○ Sources: third-party data providers, LinkedIn, Google Maps, CRMs like HubSpot and
Salesforce, fundraising databases like Crunchbase or Dealroom.
2. Enrich – Add missing attributes to records (firmographics, tech stack, emails, job titles).
○ Example: Use waterfall enrichment across multiple providers like Harmonic, Dealroom,
and Crunchbase to maximize coverage.
3. Transform – Customize or process the data to make it campaign-ready.
○ Includes scoring, filtering, segmentation, conditional logic, AI analysis.
4. Export – Push enriched and segmented lists into CRMs, sequencing tools, or outreach platforms
like Smartlead, Outreach.io, Customer.io, or Instantly.
Prospecting Workflow
● Shows how Clay Sandbox orchestrates across:
○ 1st Party Data (CRMs, warehouses like Snowflake)
○ Intent Data (job changes, funding, web visits)
○ AI Enrichments (via models like OpenAI, Anthropic, Gemini)
○ Outreach tools (Salesloft, Outreach, Instantly)
Core Prospecting Concepts
● Company list: Built on firmographics (industry, size, location, keywords).
● People list: Based on roles, seniority, keywords.
● Enrichments: Add firmographics, tech stack, social signals, contacts.
● Variables: Dynamic columns for custom research.
● Scoring: Assign points to ICP traits & enrichments.
● Prompts: Structured LLM instructions (role, context, goal, examples).
● Claygent: Clay’s native AI agent for scraping/research.
Marketing Newsletter | Marketing Resources | Marketing Services

James Praise | Marketing In Action
AI Concepts in GTM Engineering
● Zero-Shot Prompting: Design prompts that yield 90% accurate results on the first try, avoiding
multiple back-and-forth corrections.
● Agents: LLMs break prompts into multiple steps and autonomously execute tasks.
● Claygent: Clay's AI web scraper for generating custom niche data points that standard
providers miss.
● Meta-Prompting: Clay can auto-format rough prompts into structured ones with sections like
Context, Objective, Instructions.
Step-by-Step Processes
Building a Targeted Company List
1. Define ICP filters:
○ Industry (using NAICS codes, but be cautious—companies self-select categories).
○ Company size (e.g., 200–1,000 employees).
○ Public vs. private (fundraising signals more relevant for private).
○ Geography (e.g., US-based, New York/SF).
○ Keywords in descriptions (sales, marketing, GTM).
2. Preview & iterate: Don’t stop at the first search; refine filters until you hit 500–1,000 companies.
3. Limit scope during learning: Run searches on ~50 companies to save credits.
Enriching Company Data
● Use corner pieces of the puzzle: domain, LinkedIn URL, company name.
● Run Enrich Company: pull size, locations, specialties, funding rounds.
● Add fundraising enrichment with waterfall providers (Harmonic, Dealroom, Crunchbase).
○ Best practice: order enrichments from cheapest → most expensive.
○ Example: Found 100% funding stage coverage using 3 providers instead of 50–70% with
one.
Finding & Enriching People
1. Run Find People at Companies from the company table.
○ Filter by title keywords (e.g., “RevOps,” “VP,” “Director”).
○ Use exact keyword match for precision.
2. Run email waterfall enrichment:
○ Use multiple providers like FullEnrich, BetterContact, Enrow.
○ Max 10 providers per workflow (system limitation).
○ Emails are automatically validated (removes invalids, prevents spam penalties).
3. Run LinkedIn profile enrichment.
4. Optionally, add phone enrichment (blocked in trial accounts to prevent abuse).
Marketing Newsletter | Marketing Resources | Marketing Services

James Praise | Marketing In Action
Using AI Enrichment (Claygent)
● Identify custom data points not available in providers.
○ Example: What GTM tools a prospect has used, company hiring signals, sales motion
insights.
● Steps:
○ Write a prompt describing what data you want.
○ Use Meta-Prompting to auto-structure it.
○ Run tests on 10 rows before scaling.
● Output can include:
○ Reasoning steps
○ Crawled URLs
○ Extracted structured fields (e.g., URL1, URL2, URL3).
Advanced Techniques
● Conditional Runs – Apply formulas so enrichments only run when criteria are met (saves
credits).
● Merge Columns – Combine outputs from multiple enrichments into a single final result column.
● Lookalike Companies –
○ Use existing customers as a seed list.
○ Run “Company Lookalikes” via Clay’s native LLM or Ocean.io integration.
● Scheduling Sources – Automate source refreshes (daily/weekly/monthly).
● LinkedIn API Integration – Officially supported for brand mentions & posts.
○ Pull mentions, then enrich posters & engagers.
○ Use for social listening and multi-threading deals.
Noteworthy Questions & Answers
Q: Should I create separate tables for each segment (tiering strategy)?
A: Not necessary. Use filters or conditional runs instead. Separate tables only if segmentation requires
many distinct enrichments.
Q: How to filter noise from enrichment data?
A: Use wide nets initially, then refine with conditional enrichments or AI formulas (e.g., only include
companies with certain tech stacks).
Q: How does data auto-refresh?
A: Sources can be set to manual refresh or scheduled refresh (daily/weekly). Enrichments auto-run
when new data is pulled.
Marketing Newsletter | Marketing Resources | Marketing Services

James Praise | Marketing In Action
Q: What about LinkedIn scraping risks?
A: Use the official LinkedIn API for compliance (brand mentions, posts). Third-party scrapers like
PhantomBuster carry risk—follow rate-limit guidelines to avoid bans.
Practical Applications
● Automating SDR prospecting (save 40–60 sales hours/month).
● Creating hyper-personalized outreach campaigns (location, tenure, tool usage).
● Generating custom landing pages for named accounts (boosted conversion by 20–50%).
● Social listening: Identify prospects engaging with your brand on LinkedIn, Reddit, Twitter/X,
YouTube.
● Building lookalike lists based on top customers for expansion.
GTM Beyond Outreach
● GTM Engineering covers more than outreach:
○ Processing sales call notes, product data, opportunity tracking.
○ Auto-updating CRM records & creating intelligence dashboards.
○ Generating proposals, ABM docs, and POC documentation.
Key Takeaways
● GTM Engineering is about scaling human creativity with machine efficiency.
● Always follow the Find → Enrich → Transform → Export workflow.
● Iterate and test: Preview filters, run enrichments on 10 rows first, refine prompts.
● AI is most valuable for unstructured, last-mile data that databases don’t cover.
● Use conditional runs & waterfall enrichments to maximize efficiency and conserve credits.
● The foundation of success: clean data, strong CRM hygiene, thoughtful ICP design.
Marketing Newsletter | Marketing Resources | Marketing Services
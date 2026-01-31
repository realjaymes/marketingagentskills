# Clay Personalization & Sequencing on Lemlist

James Praise | Marketing In Action
Clay Personalization & Sequencing on Lemlist 2
Overview 2
Key Concepts 2
Octave as the Messaging OS 2
Clay as the Enrichment & Orchestration Layer 2
Lemlist as the Sequencing/Sending Engine 2
Where Can You Create / Write Copy? 3
1. Messaging OS (Octave) 3
2. Enrichment Layer (Clay) 3
3. Sequencing Tool (e.g., Lemlist) 3
Step-by-Step Processes 3
A. Prepare Octave + Clay 3
B. Push to Lemlist & Map Variables 4
C. Configure Lemlist Account (Deliverability & Basics) 4
D. Build Omnichannel Campaigns on Lemlist (Intermediate → Advanced) 4
Workflow Cheatsheet 5
Messaging OS (Octave) 5
Enrichment Layer (Clay) 5
Sequencing Tool (Lemlist) 6
Noteworthy Q&A & Practical Tips 6
Liquid & Spin Syntax (Lemlist) 7
Liquid & Spin Syntax (Lemlist) 7
Spin Syntax 7
Liquid Syntax 7
Best Practices 9
Practical Applications 9
Key Takeaways 9
Marketing Newsletter | Marketing Resources | Marketing Services

James Praise | Marketing In Action
Clay Personalization & Sequencing on Lemlist
Overview
This session walks you end-to-end from positioned, persona-aware messaging in Octave →
AI-enriched, row-level context in Clay → omnichannel sequencing & sending in Lemlist.
You’ll set up the Octave Sequence Agent inside Clay, enrich prospects, split outputs into reusable fields,
push leads into Lemlist with custom variables, and learn deliverability & sequencing best practices
(including Liquid/Spin syntax and conditional logic).
Key Concepts
Octave as the Messaging OS
● Create Library (Products, Personas, Use Cases, Case Studies, References, Competitors),
Playbooks (by sector/practitioner/solution, with value props & narrative), and Agents (e.g.,
Sequence Agent)
● Octave assembles persona-aware copy and lets you weave in runtime context
(prospect/company data coming from Clay) for personalization at scale.
Clay as the Enrichment & Orchestration Layer
● Build custom intelligence columns (e.g., SDR team size, job openings, awards, latest
experience) using Claygent/AI actions or LinkedIn enrichments. Then pass these into Octave’s
runtimeContext and runtimeInstructions to guide how the data should influence messaging
(examples demoed live).
● Add Octave Sequence Agent in Clay and include "outputFormat":"html" when targeting
Lemlist.
● Split Octave outputs (Emails & Subjects) into separate columns so downstream sequencers
can map them cleanly. Formula approach for arrays: data → emails → [0..3] →
subject/body.
Lemlist as the Sequencing/Sending Engine
● Create a dummy campaign with as many email steps as the Octave output (e.g., 2–4). Define
custom variables like subject1, email1, etc., and map Clay columns to these fields upon
import.
● Preview messages and (optionally) use Liquid and Spin syntax.
Marketing Newsletter | Marketing Resources | Marketing Services

James Praise | Marketing In Action
Where Can You Create / Write Copy?
We compare three different places you might generate and manage your outbound messaging:
1. Messaging OS (Octave)
Choose Octave when:
● You have structured messaging playbooks (persona → product → pain → proof).
● You want to scale message assembly using modular combinations (persona, product, use case,
etc.).
● You need centralized control over templates that sync across campaigns.
● Messaging must be systematic & consistent across reps/segments.
● Clay then acts as the final QA + enrichment layer, merging Octave outputs with
prospect-specific details.
2. Enrichment Layer (Clay)
Best suited when:
● You want to personalize at scale using enriched data fields (funding, tech stack, company
insights, etc.).
● You’re using AI to dynamically generate messaging per row.
● You need to preview, QA, or adjust content for each lead before launching.
● Conditional logic is required (different industries/titles get different copy).
● You orchestrate multi-step enrichment (e.g., LinkedIn + company info) before writing.
3. Sequencing Tool (e.g., Lemlist)
Use the sequencer itself when:
● Running micro-campaigns that don’t need complex logic or enrichment.
● Messaging is straightforward, without deep personalization (though this is becoming less
common).
● You need to launch quickly and want all copy/editing to stay inside the sequencer.
● You’re running A/B tests native to the tool.
● Your personalization fields (like {firstName}, {company}) are already prepared.
Step-by-Step Processes
A. Prepare Octave + Clay
1. Create/confirm Octave assets (Library, Playbooks, Sequence Agent). Grab your Agent ID and
API key in Octave and paste into Clay’s Octave Sequence enrichment.
Marketing Newsletter | Marketing Resources | Marketing Services

James Praise | Marketing In Action
2. In Clay, add enrichment → Octave Sequence Agent, map required fields (company
domain/name, job title, first name, LinkedIn), then Apply Template. Don’t edit the default
template—use the per-table setup.
3. Add your custom data points (LinkedIn awards/experience, SOC2 status, team size, job
openings, etc.) via AI columns or Claygent. Write runtimeContext with variables (facts) and
runtimeInstructions that explain how to use those facts across the sequence (e.g., tailor pains
to SDR team size/open roles).
Tip: You can run the Octave Sequence without context/instructions—it still uses your base
persona/product messaging—but context/instructions are the “frosting & sprinkles” that make
sequences feel handcrafted.
4. Split outputs: From the Octave result JSON, extract email1Subject, email1Body, …
email4Subject, email4Body into separate columns (array indices 0–3). This ensures clean
mapping and table hygiene.
5. Updating lookups across tables: If you add new company-level fields later (e.g., annual
revenue) and want them to appear in your People table, run Force Run on the related lookup
column and refresh to expose the new fields for extraction.
B. Push to Lemlist & Map Variables
1. In Lemlist Settings → Integrations → API keys, create/copy an API key. In Clay Settings →
Connections, add Lemlist and test account. (you can also paste a campaign ID if dropdown
doesn’t show it.)
2. In Clay, add “Add lead to Lemlist campaign” enrichment. Map Custom Fields: subject1,
email1, subject2, email2, … (two custom fields per email step). Toggle Allow duplicates
only when needed (e.g., re-adding same lead during demos), but generally not recommended.
3. Preview in Lemlist: In the campaign Sequence → Email → Preview to verify variable
substitution/HTML rendering.
C. Configure Lemlist Account (Deliverability & Basics)
● Enable AI to mark interested / not interested (used later for CRM updates via automation). Do
not track opens or link clicks to protect domain reputation; focus on replies. Confirm
timezone and send windows.
● Create a simple 3-step email sequence first; add unsubscribe link; leave subject blank on
follow-ups to keep them in the same thread (often improves reply rates).
D. Build Omnichannel Campaigns on Lemlist (Intermediate → Advanced)
● Start sequences with conditional checks (e.g., deliverable emails only). Add non-email steps:
LinkedIn profile visit, connection request, voice messages (AI-generated voice in beta), and
phone call tasks in Lemlist Outreach queue. Respect platform limits (e.g., ~20 automated
Marketing Newsletter | Marketing Resources | Marketing Services

James Praise | Marketing In Action
LinkedIn actions/day) and keep daily email send limits low (e.g., ~15 per sender while warming).
● Use branching (e.g., if accepted invite → send voice message; else → create manual task).
Prefer reply-based conditions over open-based when open tracking is off; if you do enable
opens, set a custom tracking domain first.
Outbound Workflow Cheatsheet
This summarizes the full workflow from messaging → TAM/list building → enrichment → sequencing.
Messaging OS (Octave)
● Library
○ Products
○ Personas
○ Use Cases
○ Case Studies
○ Reference Customers
○ Competitors
● Playbooks
○ By sector, practitioner, solution, milestone
○ Capture key insights, value props, narrative, and approach angles
● Agents
○ Sequence Agent
○ Content Agent (follow-ups, supporting copy)
Enrichment Layer (Clay)
● Generate Company List (“block of marble”).
● Company Enrichment
○ Firmographics (size, geography, industry),
○ B2B vs. B2C
○ Scrape website, G2, etc.
○ Signals (hiring, funding, etc.)
● Find Prospects at company (new table).
● Prospect Enrichment
○ Verified email/phone
○ Unique info from LinkedIn
○ Time in job, certifications, etc
○ Conferences, podcasts, etc.
● Scoring / conditional runs (“statue”—refine the marble).
● Octave Sequence
○ Add runtime context
○ Split into columns
● Generate subject, hooks, PS. etc.
Marketing Newsletter | Marketing Resources | Marketing Services

James Praise | Marketing In Action
● Export to Sequencing Tool
Sequencing Tool (Lemlist)
● Setup
○ Buy and configure sending domains (SPF, DKIM, DMARC)
○ Connect LinkedIn account & dialer
○ Define schedules (weekdays)
○ Define sending limits (15 emails daily, 20 LinkedIn actions daily)
● Create campaign (omnichannel campaign sequences)
○ Email sequences
○ Auto LinkedIn profile visits
○ Auto LinkedIn invites
○ LinkedIn messages/InMails
○ LinkedIn voice messages
○ In-app calling
● Design campaign flow
○ Omnichannel
○ Conditions
○ A/B tests
● Map Octave sequences
● Map custom Clay snippets into sequencer
● Fill subject & body with text/variables
● Add Liquid and Spin syntax as needed
● Test → Send → Analyze → Update CRM (via webhooks/iPaaS integrations like
Zapier/Make/N8n)
Noteworthy Q&A & Practical Tips
● No runtime context? Octave still generates solid persona-aligned copy; adding
context/instructions lifts specificity and resonance.
● HTML outputs: Set "outputFormat":"html" in the Octave action so the body renders
properly in Lemlist
● Threaded follow-ups: Leave subject empty on email #2/#3 to stay in thread; this routinely
increases reply rates.
● Column extraction at scale: Use array indices in Clay formulas
(data.emails[0].subject/body, etc.). Duplicate columns and just change the index
(0→1→2→3) for fast setup.
● Table hygiene: Prefer extracted columns over deep lookups inside templates; it keeps variables
explicit and auditable.
● Running lookups: When you add new company-level fields later, run Force Run on related
lookups to refresh downstream tables.
● Cost vs. formulas: If a task is generative or time-intensive to “hardcode,” using a low-cost
model (e.g., “mini”) via AI actions is often worth it; if it’s deterministic, formulas can be
cheaper—choose by quality, accuracy, and time (discussion in class).
Marketing Newsletter | Marketing Resources | Marketing Services

James Praise | Marketing In Action
● Protect spend: Gate expensive enrichments behind conditional formulas—e.g., don’t run
Octave/Claygent unless a verified email exists (prevent wasting credits).
● CRM push from CRM: Lemlist’s Launchpad lets reps push/enrich/remove leads directly from
HubSpot or Salesforce using the Lemlist API key—handy if reps won’t open Lemlist.
Liquid & Spin Syntax (Lemlist)
● Spin syntax rotates synonyms/phrases to keep messages unique and reduce spam patterns
(demo: rotating greetings or CTAs).
● Liquid syntax renders conditional content (e.g., time-aware greetings, gendered salutations, or
branch by title/industry).
See the dedicated segment toward the end; examples and the Notion page were referenced by
the instructor (preview and test in Lemlist before sending).
Liquid & Spin Syntax (Lemlist)
Spin Syntax
Spin syntax lets you rotate words or phrases randomly to make each email unique. This helps improve
deliverability and avoid spam patterns.
Examples:
● Greetings:
{Hi|Hey|Hello} {{firstName}},
Each email will randomly start with Hi, Hey, or Hello.
● Calls-to-Action (CTAs):
{Would you be open to a quick chat?|Can we schedule a call?|Interested in a
brief discussion?}
The CTA rotates between three variations, making outreach less repetitive.
● Closing lines:
{Looking forward to hearing from you|Excited to get your thoughts|Hope to
connect soon},
Marketing Newsletter | Marketing Resources | Marketing Services

James Praise | Marketing In Action
Liquid Syntax
Liquid syntax allows you to inject conditional logic into your messages. This ensures the right content is
shown depending on context, such as time of day, title, or location.
Examples:
● Time-aware greeting:
{% if now | date: "%H" < 12 %} Good morning {{firstName}},
{% elsif now | date: "%H" < 18 %}
Good afternoon {{firstName}},
{% else %}
Good evening {{firstName}},
{% endif %}
● Title-based personalization:
{% if job_title contains "CEO" %}
As a CEO, I thought you’d appreciate this perspective...
{% elsif job_title contains "Head of Sales" %}
Given your role leading Sales, this might resonate...
{% else %}
I wanted to share something relevant to your team...
{% endif %}
● Industry-specific messaging:
{% if industry == "SaaS" %}
We help SaaS companies like {{company}} improve retention.
{% elsif industry == "E-commerce" %}
We work with e-commerce brands to increase conversion.
Marketing Newsletter | Marketing Resources | Marketing Services

James Praise | Marketing In Action
{% else %}
Our solutions are designed to support companies across industries.
{% endif %}
● Gendered salutation (if enrichment provides gender data):
{% if gender == "male" %}
Dear Mr. {{lastName}},
{% elsif gender == "female" %}
Dear Ms. {{lastName}},
{% else %}
Hello {{firstName}},
{% endif %}
Best Practices
● Always preview/test before launching to catch broken brackets or empty variables.
● Keep it natural—don’t over-rotate synonyms (spam filters may still flag if overdone).
● Use Spin for variation and Liquid for logic. Together, they create both uniqueness and
contextual relevance.
Practical Applications
● Persona → pain mapping: Use runtime context (e.g., SDR team size + open roles) to tailor
pains (“data hygiene with many SDRs” vs. “bandwidth with few SDRs”).
● Custom PS or Subject: Generate only a PS line or subject in Clay using an AI action over the
existing Octave message; append as HTML to the body to avoid formatting issues.
● Omnichannel momentum: After email+LI steps, call quickly (tasks appear in Outreach
queue). Keep calls frequent initially (daily/every other day) to maintain sales momentum.
Marketing Newsletter | Marketing Resources | Marketing Services

James Praise | Marketing In Action
Key Takeaways
● Octave centralizes structured messaging; Clay personalizes with runtime context; Lemlist
scales sending & orchestration.
● Deliverability first: warm domains, avoid open/link tracking, add unsubscribe, thread follow-ups,
keep daily limits low while warming. Set up a custom tracking domain to safely monitor opens &
clicks.
● Guard your budget with conditional runs and verify emails early; Force Run lookups when
schema changes.
● Liquid/Spin syntax can help, but Octave-generated emails are often unique by default,
improving deliverability without heavy templating.
Marketing Newsletter | Marketing Resources | Marketing Services
# Clay Outbound Email Prompt (3 Email Sequence)

**Multi-Use Template for 3-Step Outbound Sequences**

This reference provides templates for 3-email outbound sequences across multiple use cases and copywriting frameworks. Choose the templates that match your offer type, signal strength, and buyer awareness level.

For the full library of copywriting frameworks, sequence archetypes, hook patterns, and CTA formulas, see: `Outbound Email Frameworks & Templates.md`

---

## Role

You are a senior B2B outbound copywriter creating cold email templates for {{your_company_name}}.

## Task

Generate a 3-step outbound email sequence based on Clay enrichment signals. Each sequence must include:

- **Email 1** → Signal-based cold email using one of the provided frameworks. Introduce your offer and establish relevance.
- **Email 2** → Follow-up in same thread that deepens the value prop with proof, resources, or a reframe.
- **Email 3** → Follow-up in same thread with a clear next step, content share, or explicit close/out.

## Goal

Write messaging that connects Clay enrichment signals to your value proposition, proves relevance to your target personas, and drives replies.

## Audience

Define your target personas. Examples:
- B2B SaaS demand gen leaders
- Growth/performance marketers
- RevOps and marketing ops managers
- CRO specialists
- CMOs/CROs/VPs at SMB-mid-market companies (11-500 employees)
- Engineering leaders evaluating new tools
- Founders at seed-to-Series B startups

## Enrichment Signals

### Paid Media Spend (Active Google Ads & Active LinkedIn Ads)

- High = 50+ ads across Google & LinkedIn combined
- Medium = 5-49 ads across Google & LinkedIn combined
- Low = <5 ads across Google & LinkedIn combined

### Tool Maturity (adjust category to your market)

- Advanced = 3+ tools in the relevant category
- Moderate = 1-2 tools in the relevant category
- None = 0 tools in the relevant category

### Combined Signal Matrix

| Paid Media Spend | Tool Maturity | Messaging Angle |
|------------------|---------------|-----------------|
| High/Medium | None | "Spending but not optimizing" |
| High/Medium | Advanced/Moderate | "Diminishing returns" |
| Low | None | "Efficiency matters at this scale" |
| Low | Advanced/Moderate | "Proving ROI on existing investments" |

### Growth & Change Signals

| Signal Type | Examples | Messaging Angle |
|-------------|----------|-----------------|
| Funding | Series A-C, growth equity | "Scaling requires new systems" |
| Hiring | 10+ open roles, new VP/C-suite | "Growth brings new challenges" |
| Tech adoption | New tool in stack | "Getting more from your investment" |
| Leadership change | New CMO, VP Sales, CTO | "Fresh eyes on existing problems" |
| News/PR | Product launch, partnership | "Building on momentum" |

### Detected Stack Tools (customize to your market)

- Category 1 Tools (e.g., A/B Testing: VWO, Optimizely, Convert, Adobe Target)
- Category 2 Tools (e.g., Analytics: GA4, Mixpanel, AppsFlyer, Posthog)
- Category 3 Tools (e.g., CRM: Salesforce, HubSpot)
- Category 4 Tools (e.g., Marketing Automation: Marketo, HubSpot, Pardot, Eloqua)

## Style/Tone

- Conversational, plain English, first-person tense
- Authoritative yet approachable
- Value-first, outcome-driven
- No jargon

## Constraints

### Positioning of Value

Adapt these to your specific offer type:

**For free tools/products:**
- Frame tools together with a clear category descriptor (e.g., "our free revenue optimization tools")
- **Tool 1** description: [One sentence explaining what it does and the outcome it delivers]
- **Tool 2** description: [One sentence explaining what it does and the outcome it delivers]

**For SaaS products:**
- Lead with the outcome, not the feature
- Reference time-to-value (e.g., "see results in 5 minutes," "set up in one click")

**For services/consulting:**
- Lead with the deliverable, not the process
- Reference a fixed scope or specific output

**For content/thought leadership:**
- Lead with the insight, not the brand
- Reference the specific value the content delivers

### Language Adjustments

- Do not use internal shorthand or acronyms prospects won't recognize
- If no tools detected: "no testing or optimization tools"
- If tools detected: "advanced [category] tools already in play"
- Always persona-first: "{{job_title}}s aiming for {{objective_kpi_1}} often say {{pain_1}} shows up as {{symptom_1}}."

### Offers & CTAs

- No push for meetings, demos, or calendar links in Email 1-2
- CTAs must be low-friction and soft:
  - **Email 1** → Value offer or interest check (e.g., "Would you like me to run a free [audit] for {{company_name}}?" / "Is this something your team is thinking about?")
  - **Email 2** → Feedback ask or nudge (e.g., "Would you let me know if this helped?" / "Worth testing?")
  - **Email 3** → Conversation ask or explicit out (e.g., "Would a short conversation be worth your time?" / "If not, no worries at all.")
- Do not include any footer, sign-off, or salutation. End with the CTA only.

### Terminology Consistency

- Use consistent product/tool names throughout (never abbreviate after first mention)
- For free tools: always describe as "free" and reinforce they are not gated behind a call/demo

### Missing Inputs

- Where inputs/variables are missing, generate emails based on available inputs/data
- The cell must run even if some inputs are missing

### Links

- All links must be written as full plain-text URLs (no Markdown or HTML)

### Usage of Dashes

- Avoid dashes unless absolutely necessary. Prefer commas, periods, or conjunctions
- Use en dashes (with spaces) or em dashes (without spaces) only when unavoidable, ideally no more than once per complete piece of copy

## Inputs/Placeholders

### Contact/Firmographic

```
{{first_name}}, {{last_name}}, {{job_title}}, {{company_name}}, {{linkedin_profile}}, {{work_email}}
```

### Signals

```
{{active_google_ads}}, {{active_linkedin_ads}}, {{detected_stack_tools}}, {{detected_tool_categories}}, {{paid_media_spend}} (High/Medium/Low), {{tool_maturity}} (Advanced/Moderate/None), {{active_linkedin_ads_count}}, {{tools_count}}, {{funding_signal}}, {{hiring_signal}}, {{news_signal}}, {{leadership_change}}
```

### Persona Mapping (by job title)

```
{{objective_kpi_1}}, {{pain_1}}, {{symptom_1}}
```

### Your Company (replace these)

```
{{your_company_name}}, {{your_product_name}}, {{your_product_url}}, {{your_product_description}}, {{your_tool_1_name}}, {{your_tool_1_url}}, {{your_tool_1_description}}, {{your_tool_2_name}}, {{your_tool_2_url}}, {{your_tool_2_description}}, {{your_content_url}}, {{your_content_description}}, {{your_booking_url}}
```

---

## Email 1 Templates

### Framework A: Pain-First / PAS (No Signal Reference)

Best when: Signals are weak or unavailable. Works for any offer type.

```
{Hi|Hey|Hello} {{first_name}},

{{job_title}}s at companies like {{company_name}} often tell us {{pain_1}} makes {{objective_kpi_1}} hard to prove. It usually shows up as {{symptom_1}}.

That's why they use {{your_product_description_or_offer}}. {{proof_or_mechanism}}.

Not asking for a call. {{soft_cta}}.
```

### Framework B: Ad/Tool Reference / AIDA (High/Medium Spend)

Best when: Clay shows active ad campaigns. Works for optimization, analytics, and martech offers.

```
{Hi|Hey|Hello} {{first_name}},

I noticed {{company_name}} is running {{detected_stack_tools}} campaigns. That's a strong push, but many {{job_title}}s tell me the traffic doesn't always turn into pipeline.

Clients aiming for {{objective_kpi_1}} say {{pain_1}} shows up as {{symptom_1}} when paid demand grows faster than funnel optimization.

{{your_offer_positioned_as_solution}}.

{{soft_cta}}
```

### Framework C: Stack Insight (Tools Detected)

Best when: Clay detects relevant tools in their stack. Works for complementary or competitive products.

```
{Hi|Hey|Hello} {{first_name}},

At {{company_name}}, with [category] tools already in play, I'd guess you've run into what many {{job_title}}s describe as "diminishing returns."

Even at this stage, {{pain_1}} often blocks {{objective_kpi_1}}, showing up as {{symptom_1}}.

{{your_offer_positioned_as_next_level}}.

{{soft_cta}}
```

### Framework D: No Tools + Ad Spend

Best when: Clay shows ad spend but no tools in your category. Works for any product filling a clear gap.

```
{Hi|Hey|Hello} {{first_name}},

I saw {{company_name}} is running {{detected_stack_tools}}, but no [category] tools. At this scale, every click matters, and many {{job_title}}s tell me proving ROI is a struggle.

Clients focused on {{objective_kpi_1}} often mention {{pain_1}}, which shows up as {{symptom_1}}.

{{your_offer_positioned_as_solution}}.

{{soft_cta}}
```

### Framework E: Before-After-Bridge (BAB)

Best when: Growth signals (funding, hiring, expansion) suggest the prospect is building toward a goal. Works for any offer type.

```
{Hi|Hey|Hello} {{first_name}},

Right now, most {{job_title}}s at {{company_size_or_stage}} companies are stuck {{current_state_description}}.

Imagine instead: {{desired_outcome_description}}.

That's what {{your_company_name}} helps teams achieve. {{brief_mechanism}}.

{{soft_cta}}
```

### Framework F: Insight-Led / Challenger

Best when: Targeting VP+ roles who don't respond to pain-based messaging. Works best with content, benchmarks, or original research as the offer.

```
{Hi|Hey|Hello} {{first_name}},

Most {{job_title}}s assume {{common_assumption}}. But in working with {{number}} {{industry}} teams, we've found {{counterintuitive_insight}}.

The difference usually comes down to {{root_cause}}.

We put together a {{resource_type}} that breaks this down: {{resource_url}}

{{soft_cta}}
```

### Framework G: Social Proof-Led

Best when: You have strong case studies in the prospect's industry or size band. Works for any offer type.

```
{Hi|Hey|Hello} {{first_name}},

{{similar_company_name}} was dealing with {{shared_pain}} before they {{outcome_achieved}}.

Given {{company_name}} is {{signal_based_similarity}}, I thought the approach might be relevant.

{{soft_cta}}
```

### Framework H: Question-Led

Best when: Signals are ambiguous and you need to qualify interest. Works for any offer type.

```
{Hi|Hey|Hello} {{first_name}},

Has {{company_name}} started {{activity_related_to_your_solution}} yet?

Asking because {{context_for_why_you_ask}}, and most {{job_title}}s I talk to say {{common_response}}.

Either way, {{value_offer_regardless_of_answer}}.

{{soft_cta}}
```

---

## Email 2 Templates

### Template A: Direct Resource Links

Best for: Free tools, self-serve products, or content offers.

```
{Hi|Hey|Hello} {{first_name}},

Circling back with links to {{resource_description}}:

{{resource_1_name}} → {{resource_1_url}}
{{resource_2_name}} → {{resource_2_url}}

{{job_title}}s focused on {{objective_kpi_1}} often say {{pain_1}} shows up as {{symptom_1}}. These were designed to solve exactly that.

Would you let me know if either helps at {{company_name}}?
```

### Template B: Social Proof + Links

Best for: Any offer type when you have customer proof.

```
{Hi|Hey|Hello} {{first_name}},

Just wanted to follow up. Other {{job_title}}s tell me {{your_offer}} helped reduce {{pain_1}}, which usually shows up as {{symptom_1}} in their {{function}}.

{{resource_or_link_if_applicable}}

Curious if you'd be open to trying this at {{company_name}} and letting me know if it moves the needle?
```

### Template C: Reframe the Problem

Best for: SaaS products, services, or consulting where the common approach fails.

```
{Hi|Hey|Hello} {{first_name}},

Most {{job_title}}s try to solve {{pain_1}} by {{common_approach}}. The issue is {{why_common_approach_fails}}.

What we've seen work instead is {{your_approach}}. {{brief_explanation}}.

Would it help to see how this looks in practice for a team like yours?
```

### Template D: Case Study Follow-Up

Best for: Demo/meeting booking or services when you have a relevant customer story.

```
{Hi|Hey|Hello} {{first_name}},

Quick follow-up. {{customer_name}} had the same challenge with {{pain_1}}.

After {{what_they_did_with_your_solution}}, they {{quantified_result}} in {{timeframe}}.

Given {{company_name}} is {{similarity_to_customer}}, I thought the playbook might be worth sharing.

Would you find that useful?
```

### Template E: Benchmark / Research Follow-Up

Best for: Content/thought leadership sequences or insight-led campaigns.

```
{Hi|Hey|Hello} {{first_name}},

We recently benchmarked {{metric}} across {{number}} {{industry}} companies.

The gap between top and bottom performers came down to {{key_finding}}.

I can share the full breakdown if it's relevant to what {{company_name}} is working on.

Would that be helpful?
```

---

## Email 3 Templates

### Template A: Content + Guest Invite

Best for: Thought leadership sequences. Builds relationship and positions prospect as an expert.

```
{Hi|Hey|Hello} {{first_name}},

Wanted to share something useful. Our [content type]:
{{your_content_url}}

We cover {{your_content_description}}. Recent topics: [Topic 1], [Topic 2], [Topic 3], and [Topic 4].

Would you ever be open to featuring on the [content type] to share your {{job_title}} perspective at {{company_name}}?
```

### Template B: Pain-Tied Content

Best for: Following up on a pain point from Email 1/2.

```
{Hi|Hey|Hello} {{first_name}},

Since {{pain_1}} came up in my last note, I thought you might like our [content type]: {{your_content_url}}

We break down how {{target_audience}} solve {{pain_1}} and get closer to {{objective_kpi_1}}.

Would you like me to suggest a specific [episode/resource] that's most relevant to {{company_name}}?
```

### Template C: Content + Soft CTA

Best for: Any sequence where you want to add value before closing.

```
{Hi|Hey|Hello} {{first_name}},

Quick share. Our [content type]:
{{your_content_url}}

Recent [episodes/resources]: [Topic 1], [Topic 2], [Topic 3]. It's where we share real experiments that turn demand into revenue.

Would you be interested in a guest spot to bring the {{job_title}} view from {{company_name}} into the discussion?
```

### Template D: Direct Conversation Ask

Best for: Demo/meeting booking sequences. Escalates to a call.

```
{Hi|Hey|Hello} {{first_name}},

I've shared a few things that might be relevant to {{company_name}}. Rather than keep emailing, would a 15-minute conversation make sense to see if there's a fit?

If yes, here's a link to grab time: {{your_booking_url}}

If the timing isn't right, no pressure at all.
```

### Template E: Priority Check + Explicit Out

Best for: Any sequence as a respectful close.

```
{Hi|Hey|Hello} {{first_name}},

Is {{pain_1}} still a priority for your team this quarter?

If so, {{your_offer_restatement}}.

If not, no worries. Happy to reconnect when the timing is better.
```

### Template F: Peer Proof + Next Step

Best for: Social proof-led sequences. Closes with specific evidence.

```
{Hi|Hey|Hello} {{first_name}},

One last thing. {{peer_company}} used {{your_product_or_approach}} and {{specific_result}} in {{timeframe}}.

If {{company_name}} is working on something similar, I'd be happy to share the details of what they did.

Would that be useful, or should I check back another time?
```

---

## Choosing Your Template Combination

Not all Email 1 + 2 + 3 combinations work equally well. Here are recommended pairings by use case:

### Free Tool / Product-Led Sequence

| Email | Recommended Templates |
|-------|----------------------|
| Email 1 | Framework A (Pain-First), B (Ad/Tool Reference), or D (No Tools + Ad Spend) |
| Email 2 | Template A (Direct Resource Links) or B (Social Proof + Links) |
| Email 3 | Template B (Pain-Tied Content) or E (Priority Check) |

### Demo / Meeting Booking Sequence

| Email | Recommended Templates |
|-------|----------------------|
| Email 1 | Framework B (Ad/Tool Reference), C (Stack Insight), or G (Social Proof-Led) |
| Email 2 | Template C (Reframe the Problem) or D (Case Study Follow-Up) |
| Email 3 | Template D (Direct Conversation Ask) or F (Peer Proof + Next Step) |

### Content / Thought Leadership Sequence

| Email | Recommended Templates |
|-------|----------------------|
| Email 1 | Framework F (Insight-Led) or H (Question-Led) |
| Email 2 | Template E (Benchmark/Research Follow-Up) |
| Email 3 | Template A (Content + Guest Invite) or C (Content + Soft CTA) |

### Re-Engagement Sequence (Cold Leads)

| Email | Recommended Templates |
|-------|----------------------|
| Email 1 | Framework E (BAB) or G (Social Proof-Led) |
| Email 2 | Template D (Case Study Follow-Up) or E (Benchmark/Research) |
| Email 3 | Template E (Priority Check + Explicit Out) |

### Competitive Displacement Sequence

| Email | Recommended Templates |
|-------|----------------------|
| Email 1 | Framework C (Stack Insight) |
| Email 2 | Template C (Reframe the Problem) |
| Email 3 | Template F (Peer Proof + Next Step) or D (Direct Conversation Ask) |

---

## Formatting Instructions

### General Rules

- Each email = 4 short paragraphs (hook, pain, solution, CTA)
- Use spintax for greeting: {Hi|Hey|Hello} {{first_name}},
- Subject lines = 2-4 words, lowercase, pain-focused
- In filled outputs, replace placeholders with specifics

### Email 1

- Must use one of the eight frameworks (A through H)
- Select framework based on available signals and offer type
- End with a soft ask

### Email 2

- No new subject line → reply in same thread
- Must tie back to {{pain_1}} and {{symptom_1}} from Email 1
- Include resource URLs as plain text where applicable
- End with a feedback ask or nudge

### Email 3

- No new subject line → reply in same thread
- Include content URL or booking URL where applicable
- End with a clear next step or explicit out

### Output Structure

For each contact:
1. Subject line: 2-4 words, lowercase, pain-focused
2. Email 1 (body)
3. Email 2 (body, no new subject)
4. Email 3 (body, no new subject)

Additional rules:
- Add space after each paragraph
- Apply spintax in greeting automatically. Do not write {Hi|Hey|Hello} {{first_name}} in output
- Replace placeholders in filled examples with specific detected tools or ad types
- Responses must be written as complete email drafts (not fragments)
- Do not include any footer, sign-off, or salutation. End the email with the CTA only
- All links must be written as full plain-text URLs (no Markdown or HTML)

---

## Example 1: Free Tools + Content Sequence

**Context:** SaaS company selling website optimization tools. Target is a Demand Gen Director at a mid-market company running Google and LinkedIn ads but no A/B testing tools.

**Templates used:** Framework D (No Tools + Ad Spend) → Template A (Direct Resource Links) → Template B (Pain-Tied Content)

**Subject:** proving roi

**Email 1:**

Hey Sarah,

I saw Acme Corp is running Google Search and LinkedIn Sponsored campaigns, but no A/B testing tools. At this scale, every click matters, and many Demand Gen Directors tell me proving ROI is a struggle.

Clients focused on pipeline velocity often mention attribution gaps, which shows up as Sales questioning lead quality.

That's why they use our free funnel optimization tools. Website Analyzer (finds 3 conversion leaks in 30 seconds) and FormFlow (multi-step forms that improve lead quality scores).

Would you like me to run Website Analyzer for Acme Corp, or send FormFlow to try?

**Email 2:**

Hey Sarah,

Circling back with links to both of our free funnel optimization tools:

Website Analyzer → www.example.com/analyzer
FormFlow → www.formflow.example.com

Demand Gen Directors focused on pipeline velocity often say attribution gaps shows up as Sales questioning lead quality. These tools were designed to solve exactly that.

Would you let me know if either helps at Acme Corp?

**Email 3:**

Hey Sarah,

Since attribution gaps came up in my last note, I thought you might like our Revenue Growth Podcast: www.example.com/podcast

We break down how B2B SaaS teams solve attribution challenges and get closer to pipeline velocity targets.

Would you like me to suggest a specific episode that's most relevant to Acme Corp?

---

## Example 2: Demo / Meeting Booking Sequence

**Context:** SaaS company selling an AI-powered analytics platform. Target is a VP of Growth at a Series B startup that recently raised funding and is hiring aggressively.

**Templates used:** Framework G (Social Proof-Led) → Template D (Case Study Follow-Up) → Template D (Direct Conversation Ask)

**Subject:** scaling analytics

**Email 1:**

Hi David,

Traction Labs was in a similar spot after their Series B. Growth team of 8, data scattered across GA4, Mixpanel, and three internal dashboards. Reporting took days instead of minutes.

After switching to DataPulse, they cut reporting time by 70% and caught a conversion drop within hours instead of weeks.

Given Bolt Commerce just raised your Series B and is scaling the growth team, I thought the approach might be relevant.

Would you like me to share how Traction Labs set things up?

**Email 2:**

Hi David,

Quick follow-up. Traction Labs had the same challenge with slow reporting cycles.

After consolidating their analytics into DataPulse, they went from 3-day turnaround on growth reports to same-day insights. Their VP of Growth said it changed how they allocated budget across channels.

Given Bolt Commerce is scaling fast, I thought the playbook might be worth sharing.

Would you find that useful?

**Email 3:**

Hi David,

I've shared a few things that might be relevant to Bolt Commerce. Rather than keep emailing, would a 15-minute conversation make sense to see if there's a fit?

If yes, here's a link to grab time: www.datapulse.example.com/book

If the timing isn't right, no pressure at all.

---

## Example 3: Content / Thought Leadership Sequence

**Context:** Marketing consultancy sharing original research on B2B conversion benchmarks. Target is a CMO at a mid-market fintech company.

**Templates used:** Framework F (Insight-Led) → Template E (Benchmark/Research Follow-Up) → Template A (Content + Guest Invite)

**Subject:** conversion benchmarks

**Email 1:**

Hello Rebecca,

Most CMOs assume conversion rate optimization is about testing button colors and headlines. But after analyzing 200+ B2B SaaS funnels, we found that 68% of conversion lifts come from fixing the handoff between marketing and product, not the landing page itself.

The difference usually comes down to how the first 48 hours post-signup are structured.

We put together a benchmark report that breaks this down by industry and company size: www.growthlab.example.com/benchmarks

Would you find this relevant to what NovaPay is working on?

**Email 2:**

Hello Rebecca,

We recently benchmarked signup-to-activation rates across 200+ B2B SaaS companies.

The gap between top and bottom performers came down to onboarding personalization. Companies that adapted the first-run experience by persona converted 3.2x more users within 7 days.

I can share the full fintech breakdown if it's relevant to what NovaPay is working on.

Would that be helpful?

**Email 3:**

Hello Rebecca,

Wanted to share something useful. Our Growth Lab Podcast: www.growthlab.example.com/podcast

We cover real experiments from B2B SaaS growth teams. Recent topics: activation benchmarks by vertical, the PLG onboarding playbook, pricing page experiments that actually moved revenue, and when to invest in lifecycle vs. acquisition.

Would you ever be open to featuring on the podcast to share your CMO perspective at NovaPay?

# Clay Outbound Email Prompt (4 Email Sequence)

**Multi-Use Template for 4-Step Outbound Sequences**

This reference provides templates for 4-email outbound sequences across multiple use cases and copywriting frameworks. The 4-email format is best for offers that require more education, trust-building, or multiple touches before a prospect will engage (workshops, services, SaaS demos, high-touch products, re-engagement campaigns).

For the full library of copywriting frameworks, sequence archetypes, hook patterns, and CTA formulas, see: `Outbound Email Frameworks & Templates.md`

---

## Sequence Architecture

Each email in a 4-step sequence serves a distinct strategic purpose:

| Email | Purpose | Friction Level |
|-------|---------|---------------|
| Email 1 | Open the conversation. Establish relevance using a signal or insight. Introduce your offer. | Lowest |
| Email 2 | Deepen the value prop. Reframe the problem, share proof, or provide open resources. | Low |
| Email 3 | Remove risk and objections. Clarify scope, share specifics, or address common hesitations. | Medium |
| Email 4 | Close or exit. Ask directly whether the outcome is a priority. Provide an easy next step and an explicit out. | Highest |

This architecture applies regardless of offer type. The templates below can be mixed and matched within this structure.

---

## Role

You are a senior B2B outbound copywriter creating cold email templates for {{your_company_name}}.

## Task

Generate a 4-step outbound email sequence based on Clay enrichment signals and your offer brief.

Each sequence must include:

- **Email 1** → Signal-based cold email that establishes relevance and introduces your offer. Email 1 must include a 2-5 word, lowercase subject line.
- **Email 2** → Follow-up in the same thread that deepens the value prop with proof, resources, or a reframe.
- **Email 3** → Follow-up in the same thread that removes risk, clarifies scope, or handles objections.
- **Email 4** → Final follow-up that directly asks whether the outcome is a priority and offers a low-friction path forward.

## Goal

Write messaging that connects Clay enrichment signals to the gap your offer solves, proves relevance to your target personas, positions your offer as the practical next step, and drives replies.

## Audience

Define your target personas. Examples:
- CMO / VP Marketing
- VP/Director of Growth or Demand Gen
- Marketing Ops / RevOps Lead
- Head of Engineering / CTO
- VP Sales / Head of Revenue
- Founders at seed-to-Series B startups

## Style/Tone

- Conversational, friendly, practical, and insight-led
- Plain English, first-person tense
- Simple language like speaking with a friend
- Value-first, outcome-driven
- No jargon

## Constraints

### Formatting & Email Output

- Never return a spintax output. Select one of the greeting options for each contact
- Always output a single, natural greeting:
  - Hi {{first_name}},
  - Hey {{first_name}},
  - Hello {{first_name}},
- You may vary between "Hi," "Hey," and "Hello" across emails, but never use braces or pipes
- The greeting must always end with a comma
- Never return a placeholder in the email output
- Each email should be made up of short paragraphs with clear whitespace between them
- Never use hyperlinks or bold text formatting
- Every email must be written as plain text
- Use simple language like speaking with a friend

### Messaging Constraints

Adapt these to your offer type:

**For workshops/services:**
- Always describe the offer with its full name
- Position it as a hands-on format paired with a fixed-scope deliverable
- Never position it as training only, consulting only, or open-ended work
- Reinforce that participants leave with one production-ready deliverable on real company data

**For SaaS products:**
- Lead with the outcome the product delivers, not the feature list
- Reference time-to-value and ease of setup
- Use free trial or freemium as the low-friction entry point

**For consulting/advisory:**
- Lead with the specific deliverable or outcome
- Reference a fixed scope or engagement model
- Position expertise through pattern recognition, not credentials

**For content/thought leadership:**
- Lead with the insight, not the brand
- Reference specific data, benchmarks, or findings
- Position the content as a tool for decision-making, not entertainment

### General Messaging Rules

- Use public demos, case studies, and examples as proof, not hypotheticals
- CTAs must be low-friction and soft
- Do not include any footer, sign-off, or salutation. End the email with the CTA only

## Inputs/Placeholders

### Contact/Firmographic

```
{{first_name}}, {{last_name}}, {{job_title}}, {{company_name}}, {{linkedin_profile}}, {{work_email}}, {{company_size}}, {{industry}}, {{funding_stage}}
```

### Signals

```
{{funding_signal}}, {{hiring_signal}}, {{tech_stack}}, {{news_signal}}, {{leadership_change}}, {{detected_tools}}, {{competitor_usage}}, {{growth_signal}}
```

### Your Offer (replace these)

```
{{your_company_name}}, {{your_offer_name}}, {{your_offer_description}}, {{your_video_url}}, {{your_resource_url}}, {{your_booking_url}}, {{your_topic}}, {{your_deliverable}}, {{your_product_url}}, {{your_case_study_url}}
```

## Key Resource URLs

Customize these for your offer:

- **Demo/walkthrough video:** {{your_video_url}}
- **Open resource (GitHub, guide, examples):** {{your_resource_url}}
- **Contact/booking link:** {{your_booking_url}}
- **Product/signup link:** {{your_product_url}}
- **Case study:** {{your_case_study_url}}

---

## Email 1 Templates

### Template A: Adoption Gap (Workshop/Service Offers)

Best when: Selling workshops, training, or services where the prospect has tried and failed with common approaches.

**Subject Line Options:**

- [topic] training rarely sticks
- [topic] adoption fails
- [topic] doesn't stick
- [topic] stalls
- [topic] doesn't scale
- [topic] adoption breaks down

**Body:**

```
Hey {{first_name}},

Most [target function] teams don't struggle with interest in [topic].

They struggle with turning it into something real.

Training sessions create excitement.
Solo experiments create silos.
Nothing actually ships.

We run a [format] where a team learns [topic] by building one together on their own data.

Here's one we ran recently: {{your_video_url}}

If this is relevant to what your team is exploring, would you be open to a quick follow-up conversation?
```

### Template B: Signal-Based Observation (SaaS/Product Offers)

Best when: Clay provides a strong, specific signal (funding, hiring, tech adoption, news).

**Subject Line Options:**

- scaling [function]
- [topic] at scale
- noticed something
- re: {{company_name}}

**Body:**

```
Hi {{first_name}},

I noticed {{company_name}} {{specific_signal_observation}}.

That usually means {{implication_of_signal}}, and most {{job_title}}s I talk to say {{common_challenge}} becomes the bottleneck.

{{your_product_name}} helps teams {{outcome_statement}}. {{one_sentence_mechanism}}.

Would it be worth a look to see if this applies to {{company_name}}?
```

### Template C: Social Proof-Led (Competitive Markets)

Best when: You have a strong case study in the prospect's industry or company size band.

**Subject Line Options:**

- [peer_company] did this
- [outcome] in [timeframe]
- how [peer_company] solved this

**Body:**

```
Hello {{first_name}},

{{peer_company}} was in a similar spot. {{one_sentence_about_their_situation}}.

After {{what_they_did_with_your_solution}}, they {{quantified_result}} in {{timeframe}}.

Given {{company_name}} is {{signal_based_similarity}}, I thought the approach might be relevant.

Would you like me to share how they set things up?
```

### Template D: Question-Led (Qualification)

Best when: Signals are ambiguous and you need to qualify whether the problem exists.

**Subject Line Options:**

- quick question
- curious about this
- is this a priority

**Body:**

```
Hey {{first_name}},

Has {{company_name}} started {{activity_related_to_your_solution}} yet?

Asking because {{context_from_signal}}, and most {{job_title}}s I talk to say {{common_pain}} is the thing that stalls progress.

Either way, I put together {{resource_description}} that might help: {{your_resource_url}}

Would you find this relevant to what your team is working on?
```

### Template E: Insight-Led / Challenger

Best when: Targeting senior buyers (VP+) who don't respond to pain-based messaging.

**Subject Line Options:**

- [topic] misconception
- most teams get this wrong
- counterintuitive finding

**Body:**

```
Hi {{first_name}},

Most {{job_title}}s assume {{common_assumption}}. But after working with {{number}} {{industry}} teams, we've found {{counterintuitive_insight}}.

The difference usually comes down to {{root_cause}}.

We put together a {{resource_type}} that breaks this down: {{your_resource_url}}

If this resonates with what you're seeing at {{company_name}}, I'd be curious to hear your take.
```

---

## Email 2 Templates

### Template A: Why Common Approaches Fail

Best for: Workshop/service offers where the prospect has likely tried and failed.

```
Hi {{first_name}},

We have learned something working with [target function] teams.

People don't understand [topic] after talks or slides.

They understand them after seeing the exact [components], [processes], and [outputs].

That's why we publish everything openly here:
{{your_resource_url}}

If you skim this and it looks useful for your team, would it make sense to talk about how teams turn this into something they actually use?
```

### Template B: Social Proof + Results

Best for: Any offer type when you have a relevant customer story.

```
Hi {{first_name}},

Quick follow-up. {{customer_name}} had the same challenge with {{shared_pain}}.

After {{what_they_did}}, they {{quantified_result}} in {{timeframe}}.

Their {{job_title}} said {{one_sentence_quote_or_paraphrase}}.

Given {{company_name}} is {{similarity}}, I thought the playbook might be worth sharing.

Would you find that useful?
```

### Template C: Content / Resource Share

Best for: Thought leadership or content-led sequences.

```
Hey {{first_name}},

Following up with something useful. We recently published {{content_type}} on {{topic}}:
{{your_resource_url}}

The key finding: {{key_insight}}.

{{number}} {{target_audience}} teams contributed data, and the patterns were surprising.

Would this be relevant to what {{company_name}} is working on?
```

### Template D: Stack Insight Follow-Up

Best for: SaaS offers when Clay detects relevant tools in their stack.

```
Hi {{first_name}},

I noticed {{company_name}} is using {{detected_tools}} for {{function}}.

Most teams at your stage find that {{common_limitation_of_current_tools}}.

{{your_product_name}} works alongside {{detected_tools}} to {{complementary_value}}. No rip-and-replace needed.

Would it be worth seeing how other {{industry}} teams have set this up?
```

### Template E: Benchmark / Data Follow-Up

Best for: Any offer type when you have original data or benchmarks.

```
Hey {{first_name}},

We recently benchmarked {{metric}} across {{number}} {{industry}} companies.

The gap between top and bottom performers came down to {{key_finding}}.

I can share the full breakdown for {{industry_or_segment}} if it's relevant to what {{company_name}} is working on.

Would that be helpful?
```

---

## Email 3 Templates

### Template A: Clarify Scope + Remove Risk

Best for: Workshop/service offers where "too vague" or "too open-ended" is the objection.

```
Hi {{first_name}},

Quick clarification, because this usually decides interest.

This is not an open-ended [topic] build.

The scope is fixed to one proven [deliverable type], things like [example 1], [example 2], or [example 3].

Those exact [deliverables] are documented here:
{{your_resource_url}}

If adoption has stalled before because things felt too vague or open-ended, would this kind of structure be helpful?
```

### Template B: ROI / Business Case

Best for: SaaS products or services where the buyer needs to justify the investment.

```
Hi {{first_name}},

Most {{job_title}}s I talk to ask the same question: "What's the actual ROI?"

{{customer_name}} saw {{specific_metric_improvement}} within {{timeframe}} of implementing {{your_product_or_offer}}. That translated to {{business_impact}} for a team of {{team_size}}.

For a company like {{company_name}}, the math looks similar based on {{signal_or_context}}.

Would it help to see the full breakdown?
```

### Template C: Objection Handling

Best for: Any offer where a common objection predictably kills deals.

```
Hey {{first_name}},

The most common pushback I hear from {{job_title}}s is "{{common_objection}}."

Fair concern. Here's how we address it: {{objection_response}}.

{{proof_point_that_addresses_objection}}.

If this was the thing holding you back, would it change the conversation?
```

### Template D: Peer Comparison

Best for: Competitive markets or when the prospect is likely evaluating alternatives.

```
Hi {{first_name}},

If {{company_name}} is evaluating options for {{function}}, here's what we hear from teams that have compared:

{{differentiator_1}}: {{brief_explanation}}
{{differentiator_2}}: {{brief_explanation}}
{{differentiator_3}}: {{brief_explanation}}

I'm not here to trash alternatives. Just wanted to share what teams at your stage have told us matters most.

Would it be useful to talk through how this applies to {{company_name}} specifically?
```

### Template E: Specificity Follow-Up

Best for: Any offer when previous emails were broad and need to get concrete.

```
Hey {{first_name}},

Let me be more specific about what this looks like for a {{company_size}} {{industry}} company.

{{specific_example_1}}: {{what_it_means_for_them}}
{{specific_example_2}}: {{what_it_means_for_them}}

These are based on what we've done with similar teams. Not hypotheticals.

Would any of these be relevant to what {{company_name}} is prioritizing right now?
```

---

## Email 4 Templates

### Template A: Direct Question + Easy Next Step

Best for: Any sequence where you're ready to close or move on.

```
Hey {{first_name}},

If your team is already curious about [topic], the real question is adoption.

Will this turn into shared capability, or stay with one motivated person?

We run a [format] where teams learn [topic] by shipping one real [deliverable] together.

If it's worth a short conversation to see if this fits, you can book time here:
{{your_booking_url}}

If not, no worries at all.
```

### Template B: Priority Check + Booking Link

Best for: SaaS or demo-based sequences.

```
Hi {{first_name}},

Is {{outcome}} a priority for {{company_name}} right now?

If yes, I can walk you through how teams like {{peer_company}} are approaching it in {{time_commitment}}: {{your_booking_url}}

If the timing is off, totally understand. I'll keep you on my radar for when it makes sense.
```

### Template C: Breakup Email (Final Touch)

Best for: Any sequence as a respectful close that sometimes prompts a response.

```
Hey {{first_name}},

I've reached out a few times and haven't heard back, which usually means one of three things:

1. The timing isn't right
2. This isn't a priority
3. You're the wrong person to talk to

Any of those is fine. Just let me know and I'll update my notes accordingly.

If {{pain_or_outcome}} does become a priority, I'm easy to find: {{your_booking_url}}
```

### Template D: New Angle / Reframe

Best for: When previous emails focused on one angle and you want to try another before closing.

```
Hi {{first_name}},

I've been approaching this from a {{original_angle}} perspective, but I realized there might be a more relevant angle.

{{new_angle_description}}. {{brief_explanation_of_why_this_matters}}.

{{proof_point_for_new_angle}}.

If this framing is more relevant to what {{company_name}} is working on, I'd be happy to share more.
```

### Template E: Referral Redirect

Best for: When the prospect might not be the right person but could introduce you to someone who is.

```
Hey {{first_name}},

I may have the wrong person for this. If {{topic}} isn't in your remit at {{company_name}}, would you mind pointing me to whoever handles {{function}}?

Happy to send a short blurb you can forward if that's easier.

Either way, appreciate your time.
```

---

## Choosing Your Template Combination

### Workshop / Service Offer Sequence

| Email | Recommended Templates |
|-------|----------------------|
| Email 1 | Template A (Adoption Gap) |
| Email 2 | Template A (Why Common Approaches Fail) |
| Email 3 | Template A (Clarify Scope) |
| Email 4 | Template A (Direct Question) |

### SaaS Demo / Product Sequence

| Email | Recommended Templates |
|-------|----------------------|
| Email 1 | Template B (Signal-Based) or C (Social Proof-Led) |
| Email 2 | Template B (Social Proof + Results) or D (Stack Insight) |
| Email 3 | Template B (ROI/Business Case) or D (Peer Comparison) |
| Email 4 | Template B (Priority Check + Booking) |

### Thought Leadership / Content Sequence

| Email | Recommended Templates |
|-------|----------------------|
| Email 1 | Template E (Insight-Led) |
| Email 2 | Template C (Content/Resource Share) or E (Benchmark/Data) |
| Email 3 | Template E (Specificity Follow-Up) |
| Email 4 | Template D (New Angle) or C (Breakup) |

### Re-Engagement Sequence (Dormant Leads)

| Email | Recommended Templates |
|-------|----------------------|
| Email 1 | Template C (Social Proof-Led) or D (Question-Led) |
| Email 2 | Template B (Social Proof + Results) |
| Email 3 | Template B (ROI/Business Case) |
| Email 4 | Template C (Breakup Email) |

### Competitive Displacement Sequence

| Email | Recommended Templates |
|-------|----------------------|
| Email 1 | Template B (Signal-Based) with stack reference |
| Email 2 | Template D (Stack Insight Follow-Up) |
| Email 3 | Template D (Peer Comparison) |
| Email 4 | Template B (Priority Check) or E (Referral Redirect) |

---

## Formatting Instructions

### General Rules

- Each email should be made up of short paragraphs (1-3 sentences each) with clear whitespace between them
- Do not invent new tools, URLs, or offers. Only use the links defined in Key Resource URLs
- Do not change the offer names. Use them exactly as written
- In filled outputs, replace placeholders with specifics

### Email Sequence Structure

- **Email 1:** Always contains a subject line
- **Email 2:** No new subject line → reply in same thread
- **Email 3:** No new subject line → reply in same thread
- **Email 4:** No new subject line → reply in same thread

### Output Structure

For each contact:
1. Email 1 (subject + body)
2. Email 2 (body, no new subject)
3. Email 3 (body, no new subject)
4. Email 4 (body, no new subject)

Additional rules:
- Add space after each paragraph
- Never return a spintax output. Select one greeting option per contact
- Always output a single, natural greeting
- You may vary between "Hi," "Hey," and "Hello" across emails
- The greeting must always end with a comma
- Never return a placeholder in the email output
- Responses must be written as complete email drafts (not fragments)
- Never use hyperlinks or bold text formatting
- Every email must be written as plain text
- Do not include any footer, sign-off, or salutation. End the email with the CTA only

---

## Example 1: Workshop / Service Offer Sequence

**Context:** A company selling AI/automation workshops to marketing teams. The offer is a hands-on workshop where teams build one production-ready workflow together.

**Your Offer Variables:**
- your_company_name: GrowthOps Academy
- your_offer_name: AI Workflows Workshop + Build
- your_topic: AI agent workflows
- your_deliverable: automated workflow
- your_video_url: https://youtu.be/example123
- your_resource_url: https://github.com/example/workshop-demos
- your_booking_url: https://growthops.example.com/book

**Templates used:** Template A → Template A → Template A → Template A

---

**Subject:** ai training rarely sticks

**Email 1:**

Hey Marcus,

Most marketing teams don't struggle with interest in AI.

They struggle with turning it into something real.

Training sessions create excitement.
Solo experiments create silos.
Nothing actually ships.

We run a workshop where a team learns AI agent workflows by building one together on their own data.

Here's one we ran recently: https://youtu.be/example123

If this is relevant to what your team is exploring, would you be open to a quick follow-up conversation?

**Email 2:**

Hi Marcus,

We have learned something working with growth teams.

People don't understand AI agent workflows after talks or slides.

They understand them after seeing the exact prompts, data flows, and outputs.

That's why we publish everything openly here:
https://github.com/example/workshop-demos

If you skim this and it looks useful for your team, would it make sense to talk about how teams turn this into something they actually use?

**Email 3:**

Hi Marcus,

Quick clarification, because this usually decides interest.

This is not an open-ended AI build.

The scope is fixed to one proven workflow, things like lead scoring automation, content brief generation, or campaign performance analysis.

Those exact workflows are documented here:
https://github.com/example/workshop-demos

If adoption has stalled before because things felt too vague or open-ended, would this kind of structure be helpful?

**Email 4:**

Hey Marcus,

If your team is already curious about AI agents, the real question is adoption.

Will this turn into shared capability, or stay with one motivated person?

We run a workshop where teams learn AI agent workflows by shipping one real automated workflow together.

If it's worth a short conversation to see if this fits, you can book time here:
https://growthops.example.com/book

If not, no worries at all.

---

## Example 2: SaaS Demo / Product Sequence

**Context:** SaaS company selling an AI-powered customer support platform. Target is a VP of Customer Success at a Series B company that recently posted 5 support hiring roles and is using Zendesk.

**Your Offer Variables:**
- your_company_name: SupportIQ
- your_product_name: SupportIQ
- your_product_url: https://supportiq.example.com/trial
- your_booking_url: https://supportiq.example.com/demo
- your_case_study_url: https://supportiq.example.com/case-studies/cloudbase

**Templates used:** Template B (Signal-Based) → Template D (Stack Insight) → Template B (ROI/Business Case) → Template B (Priority Check)

---

**Subject:** scaling support

**Email 1:**

Hi Rachel,

I noticed StackFlow just posted 5 support roles on LinkedIn. That kind of hiring push usually means ticket volume is outpacing the team.

Most VP of Customer Success leaders I talk to say maintaining quality at scale becomes the bottleneck. Hiring helps, but it takes months to ramp new agents.

SupportIQ handles the repetitive tickets automatically so your existing team can focus on complex cases. Most teams resolve 40% of tickets without a human within the first week.

Would it be worth a look to see if this applies to StackFlow?

**Email 2:**

Hi Rachel,

I noticed StackFlow is using Zendesk for support.

Most teams at your stage find that Zendesk handles routing and ticketing well, but struggles with intelligent deflection at volume.

SupportIQ works alongside Zendesk to auto-resolve common tickets and surface context for complex ones. No rip-and-replace needed.

Would it be worth seeing how other B2B SaaS teams have set this up?

**Email 3:**

Hi Rachel,

Most VP of Customer Success leaders I talk to ask the same question: "What's the actual ROI?"

CloudBase saw a 43% reduction in first-response time within 3 weeks of implementing SupportIQ. That translated to a 22% improvement in CSAT and 2 fewer hires needed in Q3 for a team of 15.

For a company like StackFlow, the math looks similar based on your current hiring pace.

Would it help to see the full breakdown?

**Email 4:**

Hi Rachel,

Is scaling support quality a priority for StackFlow right now?

If yes, I can walk you through how teams like CloudBase are approaching it in 20 minutes: https://supportiq.example.com/demo

If the timing is off, totally understand. I'll keep you on my radar for when it makes sense.

---

## Example 3: Re-Engagement Sequence (Dormant Leads)

**Context:** A marketing analytics company re-engaging a Head of Demand Gen who went cold 6 months ago. The company has since launched a new attribution feature and the prospect's company recently raised a Series C.

**Your Offer Variables:**
- your_company_name: MetricShift
- your_product_name: MetricShift
- your_product_url: https://metricshift.example.com/trial
- your_booking_url: https://metricshift.example.com/demo
- your_resource_url: https://metricshift.example.com/benchmarks

**Templates used:** Template D (Question-Led) → Template B (Social Proof + Results) → Template B (ROI/Business Case) → Template C (Breakup)

---

**Subject:** attribution revisited

**Email 1:**

Hey Priya,

Has Volta Analytics started tackling multi-touch attribution yet?

Asking because I saw the Series C announcement, and most Head of Demand Gen leaders I talk to say attribution becomes the top priority once you're spending at post-Series C levels.

Either way, we recently published a benchmark report on attribution accuracy across 150 B2B SaaS companies that might help: https://metricshift.example.com/benchmarks

Would you find this relevant to what your team is working on?

**Email 2:**

Hi Priya,

Quick follow-up. NexGen SaaS had the same challenge with multi-touch attribution.

After implementing MetricShift, they identified that 35% of their pipeline was misattributed to the wrong channel. Reallocating budget based on accurate data increased pipeline by 28% in one quarter.

Their Head of Demand Gen said it changed every budget conversation with the CFO.

Given Volta Analytics is scaling spend post-Series C, I thought the playbook might be worth sharing.

Would you find that useful?

**Email 3:**

Hi Priya,

Most Heads of Demand Gen I talk to ask the same question: "What's the actual ROI?"

NexGen SaaS saw a 28% increase in pipeline within one quarter of switching to MetricShift. That translated to $1.2M in additional pipeline for a marketing team of 12.

For a company like Volta Analytics at the Series C stage, the math tends to be even more favorable because spend levels amplify the impact of better attribution.

Would it help to see the full breakdown?

**Email 4:**

Hey Priya,

I've reached out a few times and haven't heard back, which usually means one of three things:

1. The timing isn't right
2. This isn't a priority
3. You're the wrong person to talk to

Any of those is fine. Just let me know and I'll update my notes accordingly.

If attribution does become a priority, I'm easy to find: https://metricshift.example.com/demo

---

## Adapting These Templates

### Step 1: Define Your Offer

Replace the offer variables with your specifics:
- **Topic:** What capability or outcome are you helping teams achieve?
- **Format:** Product, workshop, service, consulting, content, etc.
- **Deliverable:** What tangible output does the prospect get?
- **Proof assets:** Video walkthrough, open-source examples, case studies, benchmarks

### Step 2: Define Your Audience

- Which roles care most about this outcome?
- What adoption problems or objections have they experienced before?
- What signals from Clay indicate they're a fit right now?

### Step 3: Choose Your Template Combination

Use the "Choosing Your Template Combination" section above. Match your offer type to the recommended pairing.

### Step 4: Customize the Messaging

- Email 1: Name the gap or signal. Position your offer as the bridge.
- Email 2: Deepen with proof, data, or open resources.
- Email 3: Remove risk. Get specific about scope, ROI, or objections.
- Email 4: Ask directly. Provide easy next step and explicit out.

### Step 5: Implement Conditional Logic in Clay

Handle missing data gracefully:
- If signal data is missing → Fall back to pain-first or question-led opener
- If case study is in a different industry → Use pattern-based proof instead of direct comparison
- If no detected tools → Use generic phrasing about "teams at your stage"
- If job title is missing → Use company-level framing instead of persona-level

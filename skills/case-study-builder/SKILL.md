---
name: case-study-builder
version: 1.0.0
description: Creates professional case studies, engagement summaries, and project summaries. Use when the user wants to create a "case study," "client success story," "engagement summary," "project summary," or "portfolio piece."
---

# Case Study Builder Assistant

Generate structured case studies, engagement summaries, and project documentation using James Praise's frameworks.

## When to Use

- User wants to create a case study or success story
- User needs to document a client engagement
- User mentions: case study, client story, engagement summary, project summary, portfolio, results documentation

## Output Types

1. **Company Summary**: Quick company context
2. **Engagement Summary**: Challenge, Solution, Results, Testimonial format
3. **Project Summary**: Objective, Execution, Outcomes format
4. **Full Case Study**: Comprehensive client story

## Instructions

1. **Identify output type** needed
2. **Collect inputs** based on framework
3. **Generate structured output** following templates
4. **Include quantitative results** where available

## Company Summary Framework

### Format 1: Full Context
```
[Company name], [funding stage], [industry], [product category], [region], [website]
```

Example: Reform, Bootstrapped, MarTech, Lead Gen Form Builder SaaS, USA, www.reform.app

### Format 2: Short
```
[Company Name] ([Business Model], [Product/Service Category])
```

Example: FunnelEnvy (B2B, Growth Marketing Service Provider)

### Company Intro Template
```
[Company Name] is [Product/Service Category] for [persona + company type + industry + region] to [use case]
```

## Engagement Summary Framework

```markdown
## [Company Name] - Engagement Summary

**Challenge:**
[Brief summary of the primary problem the company faced]

**Solution:**
[Brief summary of the solutions implemented]

**Results:**
[One-liner about key improvements achieved]

**Testimonial:**
"[Customer quote]" - [Name], [Title], [Company]
```

### Inputs Needed
- Company name and context
- Primary challenge/problem
- Solutions implemented
- Measurable results
- Client quote (or draft one)

## Project Summary Framework

```markdown
## [Project Title]

**Objective:**
[1-2 lines, 15-30 words: short statement of goal]

**Execution:**
- [Tool/method/framework 1]
- [Tool/method/framework 2]
- [Tool/method/framework 3]

**Outcomes:**
- [Quantitative/qualitative impact 1]
- [Quantitative/qualitative impact 2]
```

### Guidelines
- Objective: 1-2 lines, 15-30 words
- Execution: 3-6 bullets, 15-25 words each
- Outcomes: 2-3 bullets, 15-25 words each

## Full Case Study Structure

1. **Company Context**: Name, stage, industry, product, region
2. **Challenge**: What problem they faced, why they engaged
3. **Solution**: What was implemented, how it worked
4. **Execution Details**: Specific actions, tools, methods
5. **Results**: Quantitative metrics + qualitative improvements
6. **Testimonial**: Client quote with attribution
7. **Key Takeaways**: Learnings or recommendations

## Output Format

Generate as Markdown with:
- Clear section headers
- Bold labels (Challenge:, Solution:, etc.)
- Bullet points for execution and outcomes
- Quoted testimonials with attribution
- Specific metrics where available

## Constraints

- Include specific numbers/percentages where available
- Use active voice
- Keep summaries concise
- Include testimonial or draft one labeled as [DRAFT]
- Avoid vague claims without supporting metrics

## Reference

See `references/case-study-examples.md` for complete examples.

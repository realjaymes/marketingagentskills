---
name: customer-segments
description: "Creates customer and user segment documents divided by traits, behaviors, and lifecycle stages with actionable criteria and messaging purposes for each group. Use when the user wants to 'segment customers,' 'customer segments,' 'user segments,' 'lifecycle segments,' 'audience segmentation,' or needs lifecycle stage definitions."
metadata:
  version: 1.0.0
argument-hint: "[product name or paste positioning docs]"
---

# Customer & User Segments Assistant

Creates customer and user segment documents for marketing, sales, and product teams.

## Instructions

1. **Gather inputs** — collect product name, industry, and target persona from the user (ask if not provided). If positioning or messaging docs are available, analyze them to inform segmentation.
2. **Analyze context** — identify segmentation dimensions relevant to the product (traits, behaviors, lifecycle stages, roles, verticals).
3. **Generate segments** — divide customers/users into distinct groups based on:

- **Traits** - Demographics, firmographics, psychographics
- **Behaviors** - Actions, engagement patterns, usage
- **Lifecycle stages** - Where they are in the customer journey

For each segment, include:
- **Segment Name** - Intuitive, business-friendly name
- **Criteria** - How they are identified
- **Purpose** - Messaging, marketing, or sales goal for that group

---

## Output Format

Output in Markdown using this structure:

### Introduction

2-3 sentences explaining the segmentation approach and how to use this document.

### Segments Table

| Segment Name | Criteria | Purpose |
|--------------|----------|---------|
| [Name] | [How identified] | [Goal for this segment] |

### Segment Details (Optional)

For complex segments, provide additional detail:

**[Segment Name]**
- **Criteria**: [Detailed identification criteria]
- **Characteristics**: [Key traits and behaviors]
- **Messaging Focus**: [What to emphasize]
- **Channels**: [Best ways to reach them]
- **Goals**: [What marketing/sales should achieve]

---

## Segmentation Approaches

### By Lifecycle Stage

| Segment | Criteria | Purpose |
|---------|----------|---------|
| Prospects | Visited site, no signup | Awareness and education |
| Leads | Signed up, not converted | Nurture and qualification |
| New Customers | Purchased <30 days | Onboarding and activation |
| Active Customers | Regular usage | Retention and expansion |
| At-Risk | Declining engagement | Re-engagement |
| Churned | Cancelled or inactive | Win-back |

### By Engagement Level

| Segment | Criteria | Purpose |
|---------|----------|---------|
| Power Users | Daily active, high feature use | Advocacy and feedback |
| Regular Users | Weekly active | Feature adoption |
| Casual Users | Monthly active | Activation |
| Dormant Users | No activity 30+ days | Re-engagement |

### By Value/Fit

| Segment | Criteria | Purpose |
|---------|----------|---------|
| Ideal Fit | Matches ICP, high LTV potential | Premium treatment |
| Good Fit | Partial ICP match | Standard nurture |
| Poor Fit | Doesn't match ICP | Deprioritize or qualify out |

### By Role/Persona

| Segment | Criteria | Purpose |
|---------|----------|---------|
| Decision Makers | C-level, VP titles | ROI-focused messaging |
| Influencers | Managers, leads | Feature/capability focus |
| End Users | Individual contributors | Ease-of-use focus |

### By Industry/Vertical

| Segment | Criteria | Purpose |
|---------|----------|---------|
| [Industry A] | Company in sector A | Industry-specific messaging |
| [Industry B] | Company in sector B | Industry-specific messaging |

---

## Constraints

- Segment names must be intuitive and business-friendly
- Do not invent unrealistic behaviors; ground everything in provided context
- Output must include the table format with columns: Segment Name | Criteria | Purpose
- Each segment should have a clear, actionable purpose
- Use en dashes (with spaces) for ranges or connections
- Use em dashes (without spaces) for breaks in thought

---

## Related Skills

- **icp-persona**: For detailed personas within segments
- **product-positioning**: For positioning that informs segmentation
- **product-messaging**: For segment-specific messaging
- **email-sequence**: For lifecycle email campaigns by segment

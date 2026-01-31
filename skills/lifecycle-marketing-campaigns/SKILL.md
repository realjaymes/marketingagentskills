---
name: lifecycle-marketing-campaigns
description: Creates lifecycle marketing campaign flows for SaaS, digital products, and service businesses. Use when the user wants to create "email sequences," "drip campaigns," "onboarding flows," "upgrade campaigns," "retention campaigns," or "lifecycle marketing."
---

# Lifecycle Marketing Campaigns Assistant

Design structured communication flows that guide prospects and customers through key journey stages.

## When to Use

- User wants to create email sequences for different user segments
- User mentions: lifecycle campaigns, drip campaigns, onboarding emails, upgrade campaigns, retention flows, win-back campaigns
- User needs segment-specific messaging strategies

## Business Types

**SaaS**: Activation, plan upgrades, feature adoption, renewals
**Digital Products**: Free to paid conversion, course completion, repeat purchases, memberships
**Service Businesses**: Lead nurturing, client onboarding, value delivery, expansion, referrals

## Instructions

1. **Identify business type**: SaaS, digital product, or service business
2. **Define segment**: Free user, trial user, paid user, churned, etc.
3. **Set campaign goals**: 2-3 specific objectives
4. **Design campaign flow**: Day-by-day messaging plan
5. **Specify channels**: Email, in-app, SMS, etc.

## Campaign Flow Structure

For each campaign, output:

```markdown
## Segment: [Segment Name]

**Campaign Goals:**
- [Goal 1]
- [Goal 2]
- [Goal 3]

**Campaign Flow:**

| Day | Messaging Focus | Description | CTA |
|-----|-----------------|-------------|-----|
| Day 0 | [Focus] | [Description] | "[CTA Text]" |
| Day 3 | [Focus] | [Description] | "[CTA Text]" |
```

## SaaS Segments

### Free Plan User
Goals: First action within 3 days, team invites, convert to paid within 14 days

| Day | Focus | Description |
|-----|-------|-------------|
| Day 0 | Welcome & Quick Start | Setup guide, highlight ease |
| Day 2 | Collaboration Value | Benefits of inviting teammates |
| Day 5 | Limit Awareness | Showcase free plan limits |
| Day 8 | Feature Spotlight | Highlight integrations |
| Day 12 | Case Study | Success story |
| Day 14 | Final Reminder | Urgency, what they lose |

### Trial User
Goals: Drive feature adoption, build urgency, convert before expiration

### Paid User
Goals: Consistent use, habit loops, drive upgrade to next tier

### Pro/Enterprise
Goals: Deep adoption, cross-team expansion, retention

## Digital Product Segments

### Free Resource Seeker
Channels: Email, retargeting, social
Goals: Build trust, demonstrate expertise, nurture to purchase

### First-Time Buyer
Goals: Course completion, engagement, upsell path

### Flagship Buyer
Goals: Completion, advocacy, premium upsell

### Repeat Buyer / Member
Goals: Retain membership, maximize value, drive referrals

## Service Business Segments

### Inbound Lead (Discovery Booked)
Goals: Reduce no-shows, establish credibility, prep for conversion

### Active Client
Goals: Smooth onboarding, early wins, trust building

### Retainer Client
Goals: Strengthen relationship, demonstrate ROI, expand scope

### Affiliate / Referral Partner
Goals: Activate referrals, reward performance, build loyalty

## Output Format

For each segment requested:
1. Segment name and description
2. Channels used
3. Funnel stage
4. Trigger event
5. 2-3 campaign goals
6. Day-by-day flow table with Focus, Description, CTA

## Constraints

- Include specific CTAs for each touchpoint
- Tie messaging to segment goals
- Include trigger events
- Specify channels per segment
- Reference case studies/success stories where relevant

## Reference

See `references/campaign-examples.md` for complete SaaS, digital product, and service business campaign flows.

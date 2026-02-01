# Growth Experiment Framework

## Overview

This framework provides a structured approach to designing, prioritizing, executing, and analyzing growth experiments. Use this to ensure experiments are hypothesis-driven, measurable, and actionable.

---

## Experiment Design Process

### 1. Observation

Begin by stating the observation that sparked the decision to run an experiment. Keep this simple, informative, and to the point.

**Example:**
> Recently, we have seen a decline in conversion rate on our content offers. Last month, we added two additional required fields to the landing page form.

### 2. Objective

Add structure by writing out what goal you are trying to accomplish, such as improving a specific metric or answering a question.

**Example:**
> Our goal is to increase the average landing page conversion rate.

### 3. Hypothesis

Create a measurable hypothesis and expected outcome using this format:

> By doing X, we believe Y will happen. If we are right, we expect Z.

**Example:**
> By reducing the number of required form fields, we believe we can reverse the recent 15% drop in conversion rate. If we are right, we expect at least a 10% increase in conversion rate over the current 18% baseline, returning us closer to the original 22%.

As experimentation maturity grows, hypotheses should become more precise and based on prior learnings.

### 4. Experiment Design

Break this into Control and Test to clearly outline the experiment's structure.

**Control:** Describe the existing setup (baseline). This is what your test will be compared against.

**Example:**
> Existing form with 6 fields including two new required ones added last month.

**Test:** Detail the changes, how they will be implemented, and for how long. Mention if using A/B testing or another method.

**Example:**
> Create a variant form with only 4 required fields and redesigned layout to appear shorter. Run an A/B test on multiple landing pages over a 30-day window.

### 5. A/B Testing Notes

Use tools like [abtestguide.com/abtestsize](https://abtestguide.com/abtestsize) to calculate:
- Sample size (e.g., 10,000 unique visitors)
- Baseline conversion rate (e.g., 4%)
- Expected uplift (e.g., 15%)
- Test duration (e.g., 4 weeks)

### 6. Considerations

List any open questions, dependencies, or cross-functional inputs that could affect execution or interpretation.

**Example questions:**
- Does the design team have bandwidth to create the new form?
- Are other teams using this form and seeing similar results?
- Could a technical issue (e.g., autofill not working) be affecting performance?

### 7. Success Criteria

Define clear, quantifiable success metrics.

**Example:**
> A statistically significant relative improvement of at least 10% in conversion rate over the control (e.g., from 18% to 19.8%).

**Traffic requirements:**
- Min 1,000 conversions/month to detect a 15% lift
- Min 10,000 conversions/month to detect a 5% lift

Target timeframe: 1-4 weeks at 95% confidence level for actionable results.

### 8. Measurement

State how you will measure results.

**Example:**
> Results will be tracked using our A/B testing tool. We'll compare control vs. test performance using conversion rate and assess statistical significance. We'll primarily track form conversion rates. In parallel, we'll monitor downstream metrics like lead quality to ensure improved conversion doesn't sacrifice value.

**Measurement checklist:**
- Compare control vs. test data points side-by-side
- Confirm statistical significance using built-in or third-party calculators
- Track both primary metric (e.g., form conversion) and secondary funnel metrics (e.g., lead quality)

### 9. Results & Learnings

After execution and analysis, document learnings.

**Example:**
> The experiment produced a 5% increase in conversion rate with 95% confidence. Although the result didn't meet our 10% target, the 5% uplift suggests that layout simplification has a positive impact. We'll incorporate this learning into future form optimizations.

---

## ICEEE Prioritization Framework

The ICEEE framework helps growth teams evaluate and prioritize experiments based on potential upside and effort required.

### Five Dimensions

| Dimension | Question |
|-----------|----------|
| **Impact** | How big of an improvement could this experiment drive? |
| **Confidence** | How confident are we in the experiment's success? |
| **Effort - Engineering** | How much engineering time will it require? |
| **Effort - Marketing** | What lift is required from the marketing team? |
| **Effort - Other** | Any additional resources needed (e.g., operations, product)? |

### Scoring Indices

**Impact Index:**
| Score | Meaning |
|-------|---------|
| 1 | Unknown or minimal |
| 2-4 | Small, 1-10% relative gain |
| 5-8 | Medium, 10-25% relative gain |
| 9-10 | Large/Huge, 25%+ relative gain |

**Confidence Index:**
| Score | Meaning |
|-------|---------|
| 1 | Not confident |
| 2 | Somewhat confident |
| 3 | Moderately confident |
| 4 | Very confident |
| 5 | Extremely confident |

**Effort Index:**
| Score | Meaning |
|-------|---------|
| 1 | Less than half day |
| 2 | Half to 1 day |
| 3 | 1-2 days |
| 4 | 2-4 days |
| 5 | 5-10 days |

### ICEEE Weighted Score Formula

```
Score = ((Impact + Confidence) * 2) - (Engineering Effort * 2) - Marketing Effort - Other Effort
```

**Why this formula:**
- Impact and Confidence are amplified (x2) to emphasize high-potential experiments with good rationale
- Engineering Effort is penalized more heavily (x2) because engineering time is usually most scarce
- Marketing and Other Efforts have lighter weight to reflect lower opportunity cost

This weighting surfaces high-leverage, low-lift experiments that can be executed quickly and confidently.

---

## Experiment Prioritization Template

| Experiment | Impact (1-10) | Confidence (1-5) | Eng Effort (1-5) | Mkt Effort (1-5) | Other Effort (1-5) | ICEEE Score |
|------------|---------------|------------------|------------------|------------------|-------------------|-------------|
| Example 1 | 7 | 4 | 2 | 2 | 1 | 15 |
| Example 2 | 5 | 3 | 3 | 1 | 1 | 8 |
| Example 3 | 9 | 5 | 4 | 3 | 2 | 13 |

---

## Best Practices

### Before Running Experiments

1. **Validate the hypothesis is testable** - Can you actually measure the outcome?
2. **Ensure sufficient traffic** - Do you have enough volume to reach statistical significance?
3. **Align on success criteria** - What constitutes a win, loss, or inconclusive result?
4. **Identify dependencies** - Who else needs to be involved?

### During Experiments

1. **Don't peek and decide early** - Wait for statistical significance
2. **Monitor for technical issues** - Ensure both variants are working correctly
3. **Document unexpected observations** - These become future experiment ideas

### After Experiments

1. **Document regardless of outcome** - Failed experiments teach as much as successful ones
2. **Share learnings broadly** - Other teams may benefit from your findings
3. **Plan next steps** - What will you do with this learning?

---

## Experiment Categories

### Acquisition Experiments
- Ad creative and copy tests
- Landing page optimization
- Channel expansion tests
- SEO experiments

### Activation Experiments
- Onboarding flow tests
- First-use experience optimization
- Signup friction reduction

### Conversion Experiments
- Pricing page optimization
- Checkout flow tests
- CTA and offer tests
- Form optimization

### Retention Experiments
- Email sequence optimization
- Feature adoption experiments
- Churn reduction tests

### Referral Experiments
- Referral program tests
- Viral loop optimization
- Share mechanism tests

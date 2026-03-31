---
name: experimentation
description: "Designs, prioritizes, executes, and reviews growth experiments using the ICEEE framework, structured hypothesis formation, A/B testing methodology, and statistical significance validation. Use when the user wants to 'design an experiment,' 'A/B test,' 'growth experiment,' 'prioritize experiments,' 'test this,' 'ICEEE,' or needs help with hypothesis formation or experiment tracking."
metadata:
  version: 1.0.0
---

# Experimentation Assistant

Designs, prioritizes, executes, and reviews growth experiments using the ICEEE framework.

## Instructions

1. **Capture the observation** — ask the user what they noticed that sparked the experiment idea
2. **Define the objective** — clarify the goal the experiment should accomplish
3. **Form a hypothesis** — use the format: "By doing X, we believe Y will happen. If we are right, we expect Z."
4. **Design the experiment** — define control vs. test, implementation method, duration, and sample size requirements
5. **Score with ICEEE** — rate Impact, Confidence, Engineering Effort, Marketing Effort, and Other Effort to prioritize
6. **Set success criteria** — define quantifiable metrics with confidence level requirements (typically 95%)
7. **Execute and measure** — track primary and secondary funnel metrics, validate statistical significance
8. **Document learnings** — record results, insights, and implications for future experiments

Slow the user down when hypotheses are vague, success criteria are unmeasurable, or experiment designs lack proper controls.

## Constraints

- Do not skip hypothesis formation
- Do not approve experiments without defined success criteria
- Avoid vanity metrics that do not tie to business outcomes
- Optimize for learning velocity, not just win rate

## Operating Framework

### Experiment Framework Steps

1. **Observation**: State the observation that sparked the experiment. Keep it simple and informative.
   - Example: "Recently, we have seen a decline in conversion rate on our content offers. Last month, we added two additional required fields to the landing page form."

2. **Objective**: Define the goal you are trying to accomplish.
   - Example: "Our goal is to increase the average landing page conversion rate."

3. **Hypothesis**: Create a measurable hypothesis with expected outcome.
   - Format: "By doing X, we believe Y will happen. If we are right, we expect Z."
   - Example: "By reducing the number of required form fields, we believe we can reverse the recent 15% drop in conversion rate. If we are right, we expect at least a 10% increase in conversion rate over the current 18% baseline."

4. **Experiment Design**:
   - Control: Describe the existing setup (baseline)
   - Test: Detail the changes, implementation method, and duration
   - Use abtestguide.com/abtestsize to calculate sample size requirements

5. **Considerations**: List open questions, dependencies, or cross-functional inputs.

6. **Success Criteria**: Define clear, quantifiable success metrics.
   - Include confidence level requirements (typically 95%)
   - Minimum conversion thresholds for different uplift detection

7. **Measurement**: Define how results will be tracked and analyzed.
   - Primary metrics and secondary funnel metrics
   - Statistical significance validation approach

8. **Results & Learnings**: Document outcomes and insights for future experiments.

### ICEEE Prioritization Framework

Score experiments across five dimensions:

| Dimension | Description |
|-----------|-------------|
| Impact | How big of an improvement could this experiment drive? |
| Confidence | How confident are we in the experiment's success? |
| Effort - Engineering | How much engineering time will it require? |
| Effort - Marketing | What lift is required from the marketing team? |
| Effort - Other | Any additional resources needed (operations, product, etc.) |

**Scoring Indexes:**

| Impact Index | Confidence Index | Effort Index |
|-------------|-----------------|--------------|
| 1: Unknown or minimal | 1: Not confident | 1: Less than 1/2 day |
| 2-4: Small, 1-10% relative gain | 2: Somewhat confident | 2: 1/2 to 1 day |
| 5-8: Medium, 10-25% relative gain | 3: Moderately confident | 3: 1-2 days |
| 9-10: Large/Huge, +25% relative gain | 4: Very confident | 4: 2-4 days |
| | 5: Extremely confident | 5: 5-10 days |

**ICEEE Weighted Score Formula:**

```
Score = ((Impact + Confidence) * 2) - (Engineering Effort * 2) - Marketing Effort - Other Effort
```

This formula:
- Amplifies Impact and Confidence (x2) to emphasize high-potential experiments
- Penalizes Engineering Effort more heavily (x2) as it's typically the scarcest resource
- Includes Marketing and Other Efforts with lighter weight

### A/B Testing Guidelines

**Sample Size Requirements:**
- Min 1,000 conversions/month to detect a 15% lift
- Min 10,000 conversions/month to detect a 5% lift

**Test Duration:**
- Shorter timeframes (1-4 weeks) at 95% confidence provide more actionable results

**Measurement Best Practices:**
- Compare control vs. test data side-by-side
- Confirm statistical significance with calculators
- Track both primary metrics and secondary funnel metrics

## Reference Materials

See the `/references` folder for:
- Experiment tracking templates (Email, SEO, YouTube)
- Prioritization framework details
- Real experiment examples with results

## Invocation

This skill should be invoked when the user:
- Wants to design a growth experiment
- Needs to prioritize experiments
- Asks about A/B testing methodology
- Wants to track or analyze experiment results
- Mentions "experiment," "hypothesis," "A/B test," "test this," "growth experiment," or "ICEEE"

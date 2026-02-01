# Experiment Tracking Template

## Overview

This template provides structures for tracking A/B tests and experiments across different channels. Use these tables to document experiments, record results, and build a library of learnings.

---

## General A/B Test Tracking

### Template Structure

| Variant | Description | Metric A | Metric B | Result vs Control | Significance | Winner? |
|---------|-------------|----------|----------|-------------------|--------------|---------|
| Control | Baseline version | [value] | [value] | - | - | - |
| Test 1 | [Change description] | [value] | [value] | [+/- %] | [p-value] | [Yes/No] |
| Test 2 | [Change description] | [value] | [value] | [+/- %] | [p-value] | [Yes/No] |

### Example: Landing Page Test

| Variant | Description | Visitors | Conversions | CVR | vs Control | Sig? |
|---------|-------------|----------|-------------|-----|------------|------|
| Control | Original page with 6 form fields | 5,000 | 200 | 4.0% | - | - |
| Test 1 | Reduced to 4 form fields | 5,000 | 250 | 5.0% | +25% | Yes |
| Test 2 | 4 fields + social proof | 5,000 | 275 | 5.5% | +37.5% | Yes |

---

## Email Experiment Tracking

### Email Subject Line Tests

| Variant | Subject Line | Sent | Delivered | Opens | Open Rate | vs Control | Sig? |
|---------|--------------|------|-----------|-------|-----------|------------|------|
| Control | [Original subject] | | | | | - | - |
| Test 1 | [New subject] | | | | | | |
| Test 2 | [New subject] | | | | | | |

### Email CTA Tests

| Variant | CTA Text/Position | Opens | Clicks | CTR | vs Control | Sig? |
|---------|-------------------|-------|--------|-----|------------|------|
| Control | [Original CTA] | | | | - | - |
| Test 1 | [New CTA] | | | | | |
| Test 2 | [New CTA] | | | | | |

### Email Sequence Tests

| Variant | Sequence Description | Emails Sent | Total Opens | Total Clicks | Conversions | vs Control |
|---------|---------------------|-------------|-------------|--------------|-------------|------------|
| Control | [Original sequence] | | | | | - |
| Test 1 | [Modified sequence] | | | | | |

---

## SEO & Content Experiment Tracking

### Content Test Template

| Variant | Change Description | Impressions | Clicks | CTR | Avg Position | vs Control |
|---------|-------------------|-------------|--------|-----|--------------|------------|
| Control | Original content | | | | | - |
| Test 1 | [Change description] | | | | | |

### Technical SEO Tests

| Variant | Technical Change | Pages Indexed | Crawl Rate | Organic Traffic | vs Control |
|---------|-----------------|---------------|------------|-----------------|------------|
| Control | Current state | | | | - |
| Test 1 | [Change description] | | | | |

---

## Social Media Experiment Tracking

### LinkedIn/Twitter Post Tests

| Variant | Post Type/Hook | Impressions | Engagements | Engagement Rate | vs Control |
|---------|---------------|-------------|-------------|-----------------|------------|
| Control | [Original approach] | | | | - |
| Test 1 | [New approach] | | | | |

### YouTube Video Tests

| Variant | Change Description | Views | Watch Time | CTR | Subscribers | vs Control |
|---------|-------------------|-------|------------|-----|-------------|------------|
| Control | Original video/thumbnail | | | | | - |
| Test 1 | [New thumbnail/title] | | | | | |

---

## Paid Media Experiment Tracking

### Ad Creative Tests

| Variant | Creative Description | Impressions | Clicks | CTR | Conversions | CPA | vs Control |
|---------|---------------------|-------------|--------|-----|-------------|-----|------------|
| Control | [Original creative] | | | | | | - |
| Test 1 | [New creative] | | | | | | |

### Audience Tests

| Variant | Audience Description | Reach | Clicks | CTR | Conversions | CPA | vs Control |
|---------|---------------------|-------|--------|-----|-------------|-----|------------|
| Control | [Original audience] | | | | | | - |
| Test 1 | [New audience] | | | | | | |

---

## Product/Feature Experiment Tracking

### Feature Tests

| Variant | Feature Change | Users | Adoption | Retention D7 | Retention D30 | vs Control |
|---------|---------------|-------|----------|--------------|---------------|------------|
| Control | [Current feature] | | | | | - |
| Test 1 | [Modified feature] | | | | | |

### Onboarding Tests

| Variant | Onboarding Flow | Users | Completion Rate | Time to Value | Activation | vs Control |
|---------|----------------|-------|-----------------|---------------|------------|------------|
| Control | [Current flow] | | | | | - |
| Test 1 | [New flow] | | | | | |

---

## Experiment Log

Track all experiments in one place for institutional learning.

| ID | Date | Category | Hypothesis | Result | Learning | Owner |
|----|------|----------|------------|--------|----------|-------|
| 001 | | | | Win/Lose/Inconclusive | | |
| 002 | | | | | | |
| 003 | | | | | | |

---

## Statistical Significance Reference

### Minimum Sample Sizes (95% confidence)

| Baseline CVR | Minimum Detectable Effect | Sample Size Needed |
|--------------|---------------------------|-------------------|
| 2% | 15% relative lift | ~25,000 per variant |
| 5% | 15% relative lift | ~10,000 per variant |
| 10% | 15% relative lift | ~5,000 per variant |
| 2% | 25% relative lift | ~9,000 per variant |
| 5% | 25% relative lift | ~3,500 per variant |
| 10% | 25% relative lift | ~1,800 per variant |

### Interpreting Results

| p-value | Interpretation |
|---------|---------------|
| < 0.01 | Very strong evidence |
| 0.01 - 0.05 | Strong evidence |
| 0.05 - 0.10 | Weak evidence |
| > 0.10 | No significant evidence |

---

## Tools for Statistical Analysis

- [ABTestGuide Calculator](https://abtestguide.com/calc/)
- [Evan Miller A/B Testing Calculator](https://www.evanmiller.org/ab-testing/)
- [Optimizely Stats Engine](https://www.optimizely.com/sample-size-calculator/)
- [VWO Sample Size Calculator](https://vwo.com/tools/ab-test-sample-size-calculator/)

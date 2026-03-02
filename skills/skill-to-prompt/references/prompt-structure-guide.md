# Prompt Structure Guide for ChatGPT Projects

Reference for converting Claude skills into ChatGPT Project prompt instructions.

Based on the 9-component universal prompt formula from AI Prompting Techniques.

## The 9 Components

### 1. Role
Define the AI's expertise and persona. Frame vocabulary, tone, and decision-making.

**Source in Claude skill:** Frontmatter `description`, intro paragraph, any "You are..." statements.

**ChatGPT format:**
```
You are [expertise/role description]. You specialize in [specific domain].
```

### 2. Task
Specific, step-by-step instructions. The core of what the AI does.

**Source in Claude skill:** Main workflow sections, numbered steps, "Instructions" section.

**ChatGPT format:** Numbered steps with clear verbs. Condense multi-paragraph steps to 1-2 sentences each.

### 3. Goal
The desired outcome. Influences tone, focus, and prioritization.

**Source in Claude skill:** "Purpose" section, output descriptions, "What This Produces" sections.

**ChatGPT format:**
```
Your goal is to [produce/create/generate] [specific deliverable] that [meets this standard].
```

### 4. Audience
Who the output is for. Shapes complexity, examples, and register.

**Source in Claude skill:** Target audience mentions, persona references, "Before Starting" context-gathering steps.

**ChatGPT format:**
```
The target audience for your output is [description]. Adjust complexity and examples accordingly.
```

### 5. Style/Tone
Voice, formatting personality, and register.

**Source in Claude skill:** Voice/tone guidance, writing style rules, "do not use" lists.

**ChatGPT format:** Direct statements about how to write.

### 6. Constraints
Hard rules and boundaries.

**Source in Claude skill:** "Rules", "Constraints", "Never/Always" statements, character/word limits.

**ChatGPT format:** Bulleted list of clear rules.

### 7. Inputs/Variables
Information that changes per use. Makes the prompt reusable.

**Source in Claude skill:** `argument-hint`, "Before Starting" questions, context-gathering steps.

**ChatGPT format:**
```
Before starting, ask the user for:
1. [Variable 1] - [why it's needed]
2. [Variable 2] - [why it's needed]
```

### 8. Example Output
1-2 model outputs showing quality and structure.

**Source in Claude skill:** "Examples" section, output templates.

**ChatGPT format:** One concise example showing the expected structure and quality. Keep short.

### 9. Formatting Instructions
How the final output should be structured.

**Source in Claude skill:** "Output Format" section, document structure specs.

**ChatGPT format:**
```
Format your output as:
- [Structure description]
- [Section ordering]
- [Specific formatting rules]
```

---

## Character Budget Allocation

Target: **7,500 characters** (500-char buffer from 8,000 limit)

| Component | Target Chars | Priority |
|-----------|-------------|----------|
| Role | 200-400 | P1 |
| Task (condensed workflow) | 1,500-2,500 | P1 |
| Goal | 150-300 | P1 |
| Constraints | 500-800 | P1 |
| Knowledge file references | 200-400 | P1 |
| Inputs/Variables | 300-500 | P2 |
| Style/Tone | 200-400 | P2 |
| Example Output | 400-800 | P2 |
| Formatting Instructions | 200-400 | P2 |
| Audience | 100-200 | P3 |
| Footer/metadata | 50-100 | P3 |

**Total P1:** ~2,550-4,400 chars (always included)
**Total P2:** ~1,100-2,100 chars (included if space)
**Total P3:** ~150-300 chars (included if space)

---

## Compression Priority Tiers

When the source skill content exceeds what fits in 8,000 characters:

### P1 — Always in instructions
- Role statement (who the AI is)
- Primary task overview (what it does)
- Core workflow as condensed bullet steps
- Critical constraints (never/always rules)
- Knowledge file reference section (what files contain, when to consult them)

### P2 — Include if space allows
- 1-2 key examples (move rest to knowledge file)
- Input variables / context-gathering steps
- Output formatting specs
- Style/tone guidance

### P3 — Always in knowledge files
- Full detailed workflow with explanations
- Complete example library
- Templates and frameworks
- Reference material and guidelines
- Edge cases and advanced scenarios
- Decision trees and detailed tables

---

## Compression Techniques

When condensing Claude skill content for the 8,000-char limit:

1. **Paragraphs to bullets:** Convert multi-sentence explanations to single-line bullets
2. **Tables to lists:** Convert wide tables to compact key-value lists
3. **Merge similar sections:** Combine overlapping guidance into one section
4. **Remove meta-content:** Strip "When to Use", trigger conditions, version info (not needed in ChatGPT instructions)
5. **Reference instead of repeat:** Write "See [Knowledge File Name] for full details" instead of including content
6. **Cut redundancy:** If a constraint is implied by the role, don't restate it
7. **Simplify examples:** Reduce example length by 60-70%, keeping only structure and key patterns

---

## Knowledge File Reference Section Template

Always end the prompt instructions with this section:

```
## Knowledge Files

This project includes [X] knowledge file(s). Consult them as needed:

1. **[Filename]** — [2-sentence description of what it contains and when to use it]
2. **[Filename]** — [2-sentence description]
3. **[Filename]** — [2-sentence description] (if applicable)

When the user asks you to perform a task, check the relevant knowledge file for detailed frameworks, templates, and examples before responding.
```

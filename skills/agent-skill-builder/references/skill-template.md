# SKILL.md Template

Copy this template when creating a new skill.

---

```markdown
---
name: your-skill-name
description: Brief description of what this skill does AND when to use it. Include keywords users would naturally say.
version: "1.0.0"
---

# Your Skill Name

[One sentence describing what this skill does.]

## Trigger Conditions

Invoke this skill when the user:
- [Condition 1 - include natural language users would say]
- [Condition 2]
- [Condition 3]

## Role

You are a [role description] that helps users [achieve outcome].

## Instructions

When this skill is invoked:

1. **[Step 1 name]**: [Description]
2. **[Step 2 name]**: [Description]
3. **[Step 3 name]**: [Description]

## Input Requirements

| Input | Required | Description | Example |
|-------|----------|-------------|---------|
| `[input1]` | Yes | What this input is | "example value" |
| `[input2]` | No | Optional input | "default" |

## Output Format

### Section 1
[Description of expected output]

### Section 2
[Description of expected output]

## Examples

### Example 1: [Scenario]

**Input:**
```
[Example input]
```

**Output:**
```
[Example output]
```

## Constraints

- [Rule 1]
- [Rule 2]
- [What NOT to do]

## References

- For detailed reference, see [reference.md](knowledge/reference.md)
- For more examples, see [examples/](examples/)
```

---

## Minimal Template

For simple skills:

```markdown
---
name: skill-name
description: What it does. Use when [trigger keywords].
---

# Skill Name

[Instructions for Claude to follow]
```

---

## Task-Based Template

For skills that perform specific actions:

```markdown
---
name: task-skill
description: Performs [task]. Use when user says "[keyword]."
disable-model-invocation: true
---

# Task Skill

Perform $ARGUMENTS:

1. [Step 1]
2. [Step 2]
3. [Step 3]
4. Report completion
```

---

## Reference-Based Template

For skills that add knowledge/context:

```markdown
---
name: reference-skill
description: [Domain] conventions and patterns for this codebase.
user-invocable: false
---

# [Domain] Reference

When working with [domain]:

## Conventions
- [Convention 1]
- [Convention 2]

## Patterns
- [Pattern 1]
- [Pattern 2]

## Anti-patterns
- [What to avoid]
```

---

## Subagent Template

For skills that run in isolation:

```markdown
---
name: research-skill
description: Deep research on [topic].
context: fork
agent: Explore
---

Research $ARGUMENTS thoroughly:

1. Find relevant files using Glob and Grep
2. Read and analyze the content
3. Summarize findings with specific references

Return a structured report.
```

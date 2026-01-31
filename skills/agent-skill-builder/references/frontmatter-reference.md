# Frontmatter Reference

Quick reference for all SKILL.md frontmatter fields.

---

## Basic Structure

```yaml
---
name: skill-name
description: What it does AND when to use it
---
```

---

## All Fields

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `name` | string | No | Directory name | Slash command name. Lowercase, hyphens, numbers only. Max 64 chars. |
| `description` | string | Recommended | First paragraph | What the skill does + when to use it. Max 200-1024 chars. |
| `version` | string | No | None | Version string (e.g., "1.0.0") |
| `argument-hint` | string | No | None | Shown in autocomplete (e.g., "[issue-number]") |
| `disable-model-invocation` | boolean | No | `false` | `true` = only user can invoke |
| `user-invocable` | boolean | No | `true` | `false` = hidden from / menu |
| `context` | string | No | inline | `fork` = run in isolated subagent |
| `agent` | string | No | general-purpose | Subagent type when `context: fork` |
| `allowed-tools` | list | No | All tools | Restrict available tools |
| `model` | string | No | Current model | Override model for this skill |
| `mode` | boolean | No | `false` | `true` = mode command |
| `hooks` | object | No | None | Skill-scoped hooks |

---

## Field Details

### name

```yaml
name: my-skill-name
```

- Lowercase letters, numbers, hyphens only
- Max 64 characters
- Becomes the `/slash-command`
- If omitted, uses directory name

**Valid:** `code-review`, `pr-summary`, `fix-issue-123`
**Invalid:** `Code Review`, `my_skill`, `skill with spaces`

---

### description

```yaml
description: Reviews code for security and performance. Use when user asks to "review code" or "audit this."
```

- **Critical for auto-invocation**: Claude uses this to decide when to load the skill
- Include both WHAT it does and WHEN to use it
- Include keywords users would naturally say
- Max 200-1024 characters depending on platform

**Bad:** `Helps with code`
**Good:** `Reviews code for security vulnerabilities and performance issues. Use when user asks to "review code," "check this code," or "security audit."`

---

### version

```yaml
version: "1.0.0"
```

- Semantic versioning recommended
- Useful for tracking changes
- Purely informational

---

### argument-hint

```yaml
argument-hint: "[issue-number]"
```

- Shown during autocomplete
- Helps users understand expected input
- Examples: `[filename]`, `[url]`, `[issue-number] [priority]`

---

### disable-model-invocation

```yaml
disable-model-invocation: true
```

| Value | You can invoke | Claude can invoke |
|-------|----------------|-------------------|
| `false` (default) | Yes | Yes |
| `true` | Yes | No |

**Use when:**
- Skill has side effects (deploy, commit, send)
- You want control over timing
- Skill is expensive/slow

---

### user-invocable

```yaml
user-invocable: false
```

| Value | Appears in / menu | Claude can invoke |
|-------|-------------------|-------------------|
| `true` (default) | Yes | Yes |
| `false` | No (hidden) | Yes |

**Use when:**
- Skill provides background knowledge
- Not meaningful as a user command
- Example: `legacy-system-context`

---

### context

```yaml
context: fork
```

| Value | Behavior |
|-------|----------|
| (omitted) | Runs inline with conversation context |
| `fork` | Runs in isolated subagent |

**Use `fork` when:**
- Skill needs isolation from conversation
- Running resource-intensive operations
- Want to use specific subagent type

---

### agent

```yaml
context: fork
agent: Explore
```

Only applies when `context: fork`.

| Agent | Best for |
|-------|----------|
| `general-purpose` | Default, full capabilities |
| `Explore` | Read-only codebase exploration |
| `Plan` | Architecture and planning |
| `Bash` | Command execution |
| `[custom]` | Your custom subagent from `.claude/agents/` |

---

### allowed-tools

```yaml
allowed-tools: Read, Grep, Glob
```

Restricts which tools Claude can use when skill is active.

**Common combinations:**
```yaml
# Read-only mode
allowed-tools: Read, Grep, Glob

# Research mode
allowed-tools: Read, Grep, Glob, WebFetch, WebSearch

# Git operations only
allowed-tools: Bash(git:*)

# Full file access, no web
allowed-tools: Read, Write, Edit, Grep, Glob
```

---

### model

```yaml
model: claude-3-opus
```

Override the model used when this skill runs.

---

### mode

```yaml
mode: true
```

Marks skill as a "mode command" that modifies Claude's behavior globally.

---

### hooks

```yaml
hooks:
  PreToolExecution:
    - command: echo "Running tool..."
```

Skill-scoped hooks that run during skill lifecycle.

---

## Common Patterns

### User-only task skill

```yaml
---
name: deploy
description: Deploy to production
disable-model-invocation: true
---
```

### Claude-only reference skill

```yaml
---
name: api-conventions
description: API design patterns for this codebase
user-invocable: false
---
```

### Research skill with subagent

```yaml
---
name: deep-research
description: Thorough research on a topic
context: fork
agent: Explore
---
```

### Read-only exploration skill

```yaml
---
name: safe-browse
description: Explore codebase without changes
allowed-tools: Read, Grep, Glob
---
```

### Skill with dynamic context

```yaml
---
name: pr-review
description: Review current pull request
context: fork
agent: Explore
allowed-tools: Bash(gh:*)
---

## PR Context
- Diff: !`gh pr diff`
- Comments: !`gh pr view --comments`
```

---

## Invocation Matrix

| Frontmatter | User `/skill` | Claude auto | In context |
|-------------|---------------|-------------|------------|
| (default) | Yes | Yes | Description |
| `disable-model-invocation: true` | Yes | No | Not loaded |
| `user-invocable: false` | No | Yes | Description |
| Both true/false | No | No | N/A |

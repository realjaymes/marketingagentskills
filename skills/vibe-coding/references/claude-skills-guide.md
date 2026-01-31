# Claude Code x Vibe Coding

**James Praise | Marketing In Action**

## Overview
This document explains how to extend Claude using **Claude Skills** (Agent Skills) to support real-world coding, workflow automation, and advanced AI-assisted development inside Claude Code.

Skills are modular, version-controlled instruction packages that Claude can automatically load or be invoked manually via slash commands.

## What Are Claude Skills
Claude Skills are self-contained capability bundles that can include:
- Instructions Claude follows
- Scripts and executable code
- Templates and examples
- Domain-specific knowledge

Key properties:
- Automatic or manual invocation
- Composable and portable
- Version-controlled
- Progressive disclosure of instructions

## Creating Your First Skill

### Step 1: Create the Skill Directory
Skills live in specific folders depending on scope:
- Personal: `~/.claude/skills/<skill-name>/`
- Project: `.claude/skills/<skill-name>/`
- Enterprise or Plugin scopes

### Step 2: Write `SKILL.md`
Every skill requires a `SKILL.md` file with:
- YAML frontmatter
- Markdown instructions

Example:
```yaml
---
name: explain-code
description: Explains code with diagrams and analogies
---
```

Instructions define how Claude should behave when the skill is invoked.

### Step 3: Test the Skill
Invoke automatically by context or manually:
```
/explain-code src/auth/login.ts
```

## Skill Structure
```
my-skill/
├── SKILL.md
├── templates/
├── examples/
└── scripts/
```

`SKILL.md` is required. Supporting files are optional.

## Frontmatter Configuration

Common fields:
- `name`
- `description`
- `version`
- `disable-model-invocation`
- `user-invocable`
- `allowed-tools`
- `context`
- `agent`

These fields control when, how, and by whom the skill can be invoked.

## Invocation Control
- `disable-model-invocation: true` → only user can invoke
- `user-invocable: false` → Claude only, background knowledge

## Passing Arguments
Arguments passed to a skill are accessible via:
```
$ARGUMENTS
```

## Advanced Patterns

### Dynamic Context Injection
Shell commands can run before invocation and inject live data.

### Subagents
Using `context: fork`, skills can run in isolated subagents like `Explore` or `Plan`.

### Tool Restrictions
Use `allowed-tools` to limit Claude’s permissions while a skill is active.

## Sharing Skills
Skills can be shared via:
- Git repositories
- Plugins
- Enterprise-managed settings

## Visual Output
Skills can generate HTML, reports, or visual artifacts by bundling scripts.

## Key Takeaway
Claude Skills turn Claude Code into a programmable, extensible development environment suitable for production workflows, not just prompting.

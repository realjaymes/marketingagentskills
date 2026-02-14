---
name: agent-skill-builder
description: Creates new Claude skills or translates ChatGPT projects into Claude skills. Use when the user wants to create a skill, convert a ChatGPT project, migrate prompts to Claude, or set up a new slash command.
version: "1.1.0"
argument-hint: "[new|translate] [skill-name or ChatGPT-project-name]"
---

# Agent Skill Builder

Creates new Claude skills from scratch or translates ChatGPT projects into the Claude skill format.

## Trigger Conditions

Invoke this skill when the user:
- Wants to "create a skill" or "make a new skill"
- Wants to "translate a ChatGPT project" or "convert a GPT Project to Claude"
- Mentions "migrate prompts" or "convert ChatGPT project"
- Asks about "slash commands" or "custom commands"
- Says "create a /command" or similar

## Two Modes

### Mode 1: Create New Skill (`/skill-builder new [name]`)

Creates a fresh Claude skill with proper structure and best practices.

### Mode 2: Translate ChatGPT Project (`/skill-builder translate [name]`)

Converts an existing ChatGPT project into a Claude skill.

---

## Core Principles (from Anthropic)

### Concise is Key

The context window is a public good. Skills share it with system prompts, conversation history, other skills' metadata, and user requests.

**Default assumption: Claude is already very smart.** Only add context Claude doesn't already have. Challenge each piece of information: "Does Claude really need this explanation?" and "Does this paragraph justify its token cost?"

Prefer concise examples over verbose explanations.

### Set Appropriate Degrees of Freedom

Match specificity to task fragility:

| Freedom Level | When to Use | Format |
|---------------|-------------|--------|
| **High** | Multiple valid approaches, context-dependent decisions | Text instructions |
| **Medium** | Preferred pattern exists, some variation OK | Pseudocode, parameterized scripts |
| **Low** | Fragile operations, consistency critical | Specific scripts, few parameters |

Think of Claude exploring a path: a narrow bridge with cliffs needs guardrails (low freedom), while an open field allows many routes (high freedom).

### Progressive Disclosure

Skills use a three-level loading system:

1. **Metadata (name + description)** - Always in context (~100 words)
2. **SKILL.md body** - When skill triggers (<5k words ideal, <500 lines)
3. **Bundled resources** - As needed (unlimited, scripts execute without loading)

**Key principle:** Keep SKILL.md lean. Move variant-specific details to reference files.

---

## Workflow: Create New Skill

### Step 1: Understand with Concrete Examples

Ask the user:

1. **Skill name**: What should the `/slash-command` be called?
2. **Purpose**: What does this skill do?
3. **Examples**: "Can you give examples of how this skill would be used?"
4. **Triggers**: "What would a user say that should trigger this skill?"

Avoid overwhelming with questions. Start with the most important ones.

### Step 2: Plan Reusable Contents

Analyze each example to identify:
- **Scripts** (`scripts/`): Code rewritten repeatedly or needing deterministic reliability
- **References** (`references/`): Documentation Claude should consult while working
- **Assets** (`assets/`): Files used in output (templates, images, fonts)

### Step 3: Create Directory Structure

```bash
mkdir -p ~/.claude/skills/[skill-name]
```

### Step 4: Write SKILL.md

Choose a structure pattern:

**Workflow-Based** (sequential processes)
```
## Overview → ## Workflow Decision Tree → ## Step 1 → ## Step 2...
```

**Task-Based** (tool collections)
```
## Overview → ## Quick Start → ## Task Category 1 → ## Task Category 2...
```

**Reference/Guidelines** (standards/specifications)
```
## Overview → ## Guidelines → ## Specifications → ## Usage...
```

**Capabilities-Based** (integrated systems)
```
## Overview → ## Core Capabilities → ### 1. Feature → ### 2. Feature...
```

Use this template:

```markdown
---
name: [skill-name]
description: [What it does AND when to use it. Include specific triggers/contexts. Max 200 chars. This is the PRIMARY triggering mechanism.]
version: "1.0.0"
---

# [Skill Name]

[Brief description - 1-2 sentences]

## Instructions

[Step-by-step guidance for Claude]

## Output Format

[Expected output structure]

## Examples

[Concrete input/output pairs]

## Constraints

[Limitations and rules]
```

### Step 5: Reference Files (if needed)

For skills with multiple domains or variants:

```
skill-name/
├── SKILL.md (overview + navigation)
└── references/
    ├── variant-a.md
    ├── variant-b.md
    └── variant-c.md
```

Reference from SKILL.md:
```markdown
## Advanced Features

- **Form filling**: See [forms.md](references/forms.md)
- **API reference**: See [api.md](references/api.md)
```

### Step 6: Test the Skill

1. Invoke directly: `/skill-name`
2. Let Claude auto-invoke by matching description keywords
3. Check `/context` to verify skill is loaded

---

## Workflow: Translate ChatGPT Project to Claude Skill

### Step 1: Extract ChatGPT Components

Request from user:
- ChatGPT system prompt/instructions
- Knowledge files (PDFs, docs, etc.)
- Conversation starters (optional)
- Actions/API configurations (if any)

### Step 2: Map ChatGPT Project → Claude

| ChatGPT Component | Claude Equivalent | Location |
|---------------|-------------------|----------|
| Name | `name` in frontmatter | SKILL.md |
| Description | `description` in frontmatter | SKILL.md |
| Instructions | Main markdown content | SKILL.md |
| Knowledge files | `references/` folder (as .md) | Subdirectory |
| Conversation starters | Document in skill or omit | SKILL.md |
| Actions (APIs) | MCP servers | Separate config |
| Custom behavior | Detailed instructions | SKILL.md |

### Step 3: Convert Instructions

| ChatGPT Pattern | Claude Equivalent |
|-------------|-------------------|
| "You are a [role]..." | "## Role" section |
| "Your task is to..." | "## Instructions" section |
| "Always/Never..." | "## Constraints" section |
| "Output format..." | "## Output Format" section |
| "Examples:" | "## Examples" section |
| Input placeholders `[text]` | Keep as-is or use `$ARGUMENTS` |

### Step 4: Convert Knowledge Files

1. **PDFs/Docs**: Convert to Markdown
2. **Large references**: Put in `references/` subfolder
3. **Templates**: Put in `assets/` subfolder
4. **Examples**: Include in SKILL.md or `references/examples.md`

If files are large (>10k words), include grep search patterns in SKILL.md.

### Step 5: Set Frontmatter

```yaml
---
name: skill-name                    # lowercase, hyphens only
description: What AND when          # PRIMARY triggering mechanism
version: "1.0.0"                    # optional
disable-model-invocation: true      # if user-only
user-invocable: false               # if Claude-only
context: fork                       # if needs isolation
agent: Explore                      # if using subagent
allowed-tools: Read, Grep, Glob     # if restricting tools
---
```

### Step 6: Update CLAUDE.md

Add entry to the skills table:
```markdown
| `skill-name` | User wants to [action]; mentions "[keyword1]," "[keyword2]" |
```

---

## ChatGPT-Specific Translation Notes

### ChatGPT "Memory" → Claude

ChatGPT memory has no direct equivalent. Options:
- Store in `~/.claude/memory.json`
- Use project-specific context files
- Include as "background" section in skill

### ChatGPT "Actions" → MCP Servers

ChatGPT Actions (API calls) require MCP server setup in `~/.claude/mcp.json`.

### ChatGPT "Code Interpreter" → Claude Tools

Claude has native access to: `Bash`, `Read`, `Write`, `Edit`, `Glob`, `Grep`

### ChatGPT Conversation Starters

Document in skill's "## Examples" section or CLAUDE.md usage hints.

---

## What NOT to Include

Do NOT create extraneous documentation:
- README.md
- INSTALLATION_GUIDE.md
- QUICK_REFERENCE.md
- CHANGELOG.md

Skills should only contain information needed for an AI agent to do the job. No auxiliary context about creation process, setup procedures, or user-facing documentation.

---

## Frontmatter Fields Reference

| Field | Required | Description |
|-------|----------|-------------|
| `name` | No | Slash command name. Uses directory name if omitted. |
| `description` | **Critical** | What + When. PRIMARY triggering mechanism for auto-invocation. |
| `version` | No | Version string (e.g., "1.0.0") |
| `argument-hint` | No | Hint shown in autocomplete (e.g., "[issue-number]") |
| `disable-model-invocation` | No | `true` = user-only invocation |
| `user-invocable` | No | `false` = Claude-only (hidden from menu) |
| `context` | No | `fork` = run in isolated subagent |
| `agent` | No | Subagent type: Explore, Plan, general-purpose |
| `allowed-tools` | No | Restrict tools: `Read, Grep, Glob` |
| `model` | No | Override model for this skill |

---

## Writing Good Descriptions

The description is the PRIMARY triggering mechanism. Claude reads it to decide when to use the skill.

**Bad:**
```
description: Helps with code
```

**Good:**
```
description: Reviews code for security, performance, and best practices. Use when user asks to "review code," "check this code," "security audit," or wants feedback on code quality.
```

Include:
- What the skill does
- When to use it (keywords, triggers, scenarios)
- Max 200 characters

---

## String Substitutions

| Variable | Description |
|----------|-------------|
| `$ARGUMENTS` | Everything after `/skill-name` |
| `${CLAUDE_SESSION_ID}` | Current session ID |
| `` !`command` `` | Dynamic injection (runs before skill loads) |

---

## Skill Locations

| Location | Path | Scope |
|----------|------|-------|
| Personal | `~/.claude/skills/[name]/` | All your projects |
| Project | `.claude/skills/[name]/` | This project only |

---

## After Creation Checklist

- [ ] SKILL.md created with proper frontmatter
- [ ] Description includes what AND when (triggers)
- [ ] Knowledge files converted to Markdown in `references/`
- [ ] SKILL.md under 500 lines (split if larger)
- [ ] CLAUDE.md updated with skill entry
- [ ] Skill tested with `/skill-name`
- [ ] Auto-invocation tested with matching keywords
- [ ] No extraneous documentation files created

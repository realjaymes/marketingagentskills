---
name: agent-skill-builder
description: "Quickly creates new Claude Code skills or translates ChatGPT projects into Claude Code skills. Handles skill scaffolding, frontmatter, directory structure, and ChatGPT-to-Claude migration. Use when the user wants to 'create a skill,' 'make a new slash command,' 'convert a ChatGPT project,' 'translate a GPT to Claude,' or 'migrate prompts to Claude Code.' For full eval/testing/benchmarking workflows, use skill-creator instead."
argument-hint: "[new|translate] [skill-name or ChatGPT-project-name]"
---

# Agent Skill Builder

Quickly scaffolds new Claude Code skills or translates ChatGPT projects into Claude Code format. This skill focuses on fast creation and correct structure. For iterative testing, benchmarking, and description optimization, use `/skill-creator`.

## Two Modes

### Mode 1: Create New Skill (`/agent-skill-builder new [name]`)

Scaffolds a fresh Claude Code skill with proper structure and best practices.

### Mode 2: Translate ChatGPT Project (`/agent-skill-builder translate [name]`)

Converts an existing ChatGPT project into a Claude Code skill.

---

## Create New Skill

### Step 1: Gather Intent

Ask the user (skip what's already clear from context):

1. **Skill name**: What should the `/slash-command` be called?
2. **Purpose**: What does this skill do?
3. **Examples**: How would this skill be used in practice?
4. **Triggers**: What would a user say that should invoke this skill?

### Step 2: Plan Resources

Analyze each example to identify what should be bundled:

- **Scripts** (`scripts/`): Code rewritten repeatedly or needing deterministic reliability. Execute without loading into context.
- **References** (`references/`): Documentation Claude should consult while working. Loaded on demand.
- **Assets** (`assets/`): Files used in output (templates, images, fonts). Not loaded into context.

### Step 3: Create Directory and SKILL.md

```bash
mkdir -p ~/.claude/skills/[skill-name]
```

Write SKILL.md following this template:

```markdown
---
name: skill-name
description: "Describes what the skill does and specific triggers for when to use it. Write in third person. Include keywords users would say. Max 1024 characters. This is the PRIMARY triggering mechanism."
---

# Skill Name

[1-2 sentence description]

## Instructions

[Step-by-step guidance — use imperative form]

## Output Format

[Expected output structure]

## Constraints

[Limitations and rules]
```

### Step 4: Add Reference Files (if needed)

For skills with multiple domains or variants, keep SKILL.md lean and split into references:

```
skill-name/
├── SKILL.md (overview + navigation, under 500 lines)
└── references/
    ├── variant-a.md
    └── variant-b.md
```

Reference from SKILL.md with clear guidance on when to read each file. Keep references one level deep.

### Step 5: Test

1. Invoke directly: `/skill-name`
2. Let Claude auto-invoke by matching description keywords
3. Check that the skill triggers when expected and stays silent when not relevant

---

## Translate ChatGPT Project to Claude Skill

### Step 1: Extract ChatGPT Components

Request from user:
- System prompt/instructions
- Knowledge files (PDFs, docs)
- Conversation starters (optional)
- Actions/API configurations (if any)

### Step 2: Map Components

| ChatGPT Component | Claude Code Equivalent | Location |
|---|---|---|
| Name | `name` in frontmatter | SKILL.md |
| Description | `description` in frontmatter | SKILL.md |
| Instructions | Main markdown body | SKILL.md |
| Knowledge files | `references/` folder (convert to .md) | Subdirectory |
| Conversation starters | Document in Examples section or omit | SKILL.md |
| Actions (APIs) | MCP servers | `~/.claude/mcp.json` |
| Code Interpreter | Native tools: `Bash`, `Read`, `Write`, `Edit`, `Glob`, `Grep` | Built-in |
| Memory | No direct equivalent. Use context files or skill background sections | Various |

### Step 3: Convert Instructions

| ChatGPT Pattern | Claude Equivalent |
|---|---|
| "You are a [role]..." | Role section or integrate into instructions |
| "Your task is to..." | Instructions section |
| "Always/Never..." | Constraints section |
| "Output format..." | Output Format section |
| Input placeholders `[text]` | Keep as-is or use `$ARGUMENTS` |

### Step 4: Convert Knowledge Files

1. Convert PDFs/docs to Markdown and place in `references/`
2. For large files (>10k words), include grep search patterns in SKILL.md
3. For files >100 lines, add a table of contents at the top
4. Templates and assets go in `assets/`

### Step 5: Write Frontmatter

The `description` field is the primary triggering mechanism. Write in third person and include both what the skill does and when to use it. Be slightly "pushy" with triggers to combat undertriggering.

---

## Frontmatter Reference

Only `name` and `description` are required. Additional fields are Claude Code-specific extensions:

| Field | Required | Description |
|---|---|---|
| `name` | Yes | Max 64 chars, lowercase letters/numbers/hyphens only |
| `description` | Yes | Max 1024 chars. What + When. Third person. Primary trigger mechanism |
| `argument-hint` | No | Hint shown in autocomplete (e.g., `"[issue-number]"`) |
| `disable-model-invocation` | No | `true` = user-only invocation (no auto-trigger) |
| `user-invocable` | No | `false` = Claude-only (hidden from slash command menu) |
| `context` | No | `fork` = run in isolated subagent |
| `agent` | No | Subagent type: `Explore`, `Plan`, `general-purpose` |
| `allowed-tools` | No | Restrict available tools: `Read, Grep, Glob` |
| `model` | No | Override model for this skill |

## String Substitutions

| Variable | Description |
|---|---|
| `$ARGUMENTS` | Everything after `/skill-name` |
| `${CLAUDE_SESSION_ID}` | Current session ID |
| `` !`command` `` | Dynamic injection (runs before skill loads) |

## Skill Locations

| Location | Path | Scope |
|---|---|---|
| Personal | `~/.claude/skills/[name]/` | All projects |
| Project | `.claude/skills/[name]/` | This project only |

## Writing Best Practices

These come from Anthropic's official skill authoring guide:

- **Concise is key.** Claude is already smart. Only add context Claude doesn't already have. Prefer concise examples over verbose explanations.
- **Description is everything.** Claude reads descriptions to decide which skill to use from potentially 100+ available skills. Be specific, include trigger keywords, write in third person.
- **Progressive disclosure.** Keep SKILL.md under 500 lines. Move detailed references to separate files. Claude loads them only when needed.
- **Match freedom to fragility.** High freedom (text instructions) for flexible tasks, low freedom (specific scripts) for fragile operations.
- **Explain the why.** Explain reasoning behind instructions rather than using heavy-handed MUSTs. Claude responds better to understanding motivation than rigid rules.
- **Consistent terminology.** Pick one term and use it throughout. Don't mix "API endpoint" / "URL" / "API route" / "path".
- **No extraneous files.** No README.md, CHANGELOG.md, INSTALLATION_GUIDE.md. Skills contain only what an AI agent needs to do the job.
- **Forward slashes only.** Use `scripts/helper.py`, never `scripts\helper.py`.

## After Creation Checklist

- [ ] SKILL.md created with `name` and `description` in frontmatter
- [ ] Description includes what AND when (triggers), written in third person
- [ ] SKILL.md under 500 lines
- [ ] Knowledge files converted to Markdown in `references/`
- [ ] References are one level deep from SKILL.md
- [ ] Large reference files (>100 lines) have table of contents
- [ ] Skill tested with `/skill-name` and auto-invocation
- [ ] No extraneous documentation files

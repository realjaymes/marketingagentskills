# GPT to Claude Skill Migration Checklist

Use this checklist when converting a ChatGPT GPT project to a Claude skill.

---

## Phase 1: Extract GPT Components

- [ ] **System prompt/instructions**: Copy the full GPT instructions
- [ ] **Knowledge files**: List all uploaded files (PDFs, docs, etc.)
- [ ] **Conversation starters**: Note any preset prompts
- [ ] **Actions/APIs**: Document any configured actions
- [ ] **Capabilities**: Note if Code Interpreter, DALL-E, or Browsing enabled

---

## Phase 2: Plan Skill Structure

### Naming
- [ ] Choose skill name (lowercase, hyphens only, max 64 chars)
- [ ] Name should reflect the action/purpose

### Directory
- [ ] Create `~/.claude/skills/[skill-name]/`
- [ ] Plan subdirectories if needed:
  - [ ] `knowledge/` for reference materials
  - [ ] `templates/` for output templates
  - [ ] `examples/` for sample outputs
  - [ ] `scripts/` for executable code

---

## Phase 3: Convert Instructions

### Map GPT Sections to Claude Format

| GPT Section | Claude Section | Status |
|-------------|----------------|--------|
| Role definition | `## Role` | [ ] |
| Task description | `## Instructions` | [ ] |
| Output format | `## Output Format` | [ ] |
| Constraints/rules | `## Constraints` | [ ] |
| Examples | `## Examples` | [ ] |
| Input placeholders | Keep or use `$ARGUMENTS` | [ ] |

### Clean Up Instructions

- [ ] Remove GPT-specific references ("As a GPT...", "ChatGPT...")
- [ ] Adapt for Claude's capabilities
- [ ] Simplify overly complex instructions
- [ ] Keep under 500 lines (move details to supporting files)

---

## Phase 4: Convert Knowledge Files

For each knowledge file:

| File | Format | Convert To | Location | Status |
|------|--------|------------|----------|--------|
| [filename] | PDF | Markdown | `knowledge/` | [ ] |
| [filename] | DOCX | Markdown | `knowledge/` | [ ] |
| [filename] | TXT | Keep as-is | `knowledge/` | [ ] |

### Conversion Notes
- [ ] PDFs: Extract text, format as Markdown
- [ ] Large docs: Split into logical sections
- [ ] Reference from SKILL.md: `See [file.md](knowledge/file.md)`

---

## Phase 5: Write Frontmatter

```yaml
---
name: [skill-name]
description: [What + When - include trigger keywords]
version: "1.0.0"
---
```

### Frontmatter Options

- [ ] `name`: Set (or use directory name)
- [ ] `description`: Write compelling description with keywords
- [ ] `version`: Set if tracking versions
- [ ] `disable-model-invocation`: Set `true` if user-only
- [ ] `user-invocable`: Set `false` if Claude-only
- [ ] `context`: Set `fork` if needs isolation
- [ ] `agent`: Set if using specific subagent
- [ ] `allowed-tools`: Set if restricting tools
- [ ] `argument-hint`: Set if skill takes arguments

---

## Phase 6: Handle Special GPT Features

### GPT Actions → MCP Servers
- [ ] Document required API endpoints
- [ ] Plan MCP server configuration
- [ ] Note: Requires separate MCP setup

### GPT Code Interpreter → Claude Tools
- [ ] Map to Bash, Read, Write, Edit tools
- [ ] Claude has native file/code access

### GPT Memory → Claude Options
- [ ] Consider `~/.claude/memory.json`
- [ ] Or include as "Background" section in skill

### GPT Browsing → Claude Options
- [ ] Use WebFetch or WebSearch tools
- [ ] Or MCP server for web access

---

## Phase 7: Create SKILL.md

- [ ] Write frontmatter
- [ ] Write main content sections:
  - [ ] Brief description
  - [ ] Trigger conditions
  - [ ] Role (if applicable)
  - [ ] Instructions
  - [ ] Input requirements
  - [ ] Output format
  - [ ] Examples
  - [ ] Constraints
  - [ ] References to supporting files

---

## Phase 8: Update CLAUDE.md

- [ ] Add skill to appropriate category table
- [ ] Include trigger keywords in description
- [ ] Add to decision tree if applicable
- [ ] Add to skill combinations if relevant

---

## Phase 9: Test

- [ ] Test direct invocation: `/skill-name`
- [ ] Test with arguments: `/skill-name [args]`
- [ ] Test auto-invocation with matching keywords
- [ ] Verify `/context` shows skill
- [ ] Test edge cases from original GPT

---

## Phase 10: Backup

- [ ] Copy to `~/Documents/Claude Skills/[skill-name]/`
- [ ] Consider git repository for version control

---

## Component Mapping Quick Reference

| GPT | Claude | Notes |
|-----|--------|-------|
| Instructions | SKILL.md content | Main skill body |
| Knowledge files | `knowledge/*.md` | Convert to Markdown |
| Conversation starters | Examples section | Optional |
| Actions | MCP servers | Separate config |
| Code Interpreter | Bash, Read, Write | Native tools |
| DALL-E | Not available | Use external API via MCP |
| Browsing | WebFetch, WebSearch | Native tools |
| Memory | memory.json or context | Manual setup |

---

## Common Issues

### Skill not auto-invoking
- Check description includes user keywords
- Verify skill appears in `/context`

### Skill too large
- Move reference content to `knowledge/`
- Keep SKILL.md under 500 lines

### Knowledge files not found
- Use relative paths: `[file.md](knowledge/file.md)`
- Reference in SKILL.md so Claude knows they exist

---
name: obsidian-ops
description: Processes meeting transcripts into structured notes and tracks projects in an Obsidian vault, keeping linked hub notes current after every edit. Use when the user mentions "meeting notes," "process this meeting," "transcript," "project status," "create a project," "update project," "what did we decide," "what's active," "Obsidian," or "vault." Modes: process, project.
version: "1.1.1"
argument-hint: "[process|project] [project-name]"
---

# obsidian-ops

An operations system that uses an Obsidian vault as the single source of truth for meetings and projects.

## Setup

Find the vault before doing anything else. Check, in order:

1. A vault path the user gives in the conversation
2. The `OBSIDIAN_VAULT` environment variable
3. A `vault:` line in the project's `CLAUDE.md`

If none of these exist, ask for the vault path once and suggest saving it to `CLAUDE.md` so later sessions find it.

The folder names below are defaults. If the vault already uses a different structure, follow the vault's structure and map each default to its nearest equivalent.

## When to Use

Use when the user mentions meeting notes, a transcript, processing a meeting, project status, creating or updating a project, past decisions, active work, Obsidian, or the vault.

## Invocation

```
/obsidian-ops process     # Process a meeting transcript
/obsidian-ops project     # Create, view, or update a project
/obsidian-ops             # Auto-detect from conversation
```

---

## Hub Freshness Rule

This rule applies to every vault edit, including edits made outside this skill.

At the end of any vault edit, update every hub note and cross-linked note the edit affects. Do the updates without asking. A hub is any note that summarizes and links a body of work, such as a project note, a client hub, a campaign hub, or an index note.

Standard updates after any edit:

- Frontmatter: `status`, `last_touch_date`, and any status-specific dates
- Milestone tables, decision logs, and outreach or export logs
- Next-action tasks
- Back-references, so every note the edit links to links back where it should

**Reconcile `## Next Actions` before adding to it.** This is the most-skipped step. Each time you open a hub's task list, check off everything completed with the date, delete obsolete or superseded tasks and dead sub-sections, and merge duplicates. Then add new forward tasks. Next Actions holds live forward work only. Completed items and abandoned tracks belong in the hub's logs. Refresh any stale status summary line so it describes today. Don't add speculative tasks nobody will return to.

**Write current-state documents.** Every note this skill creates or updates should read as if written in one pass by someone who already knew everything now known. When facts change mid-session, rewrite the affected section in place and fix anything else in the note, or in sibling notes, that the change contradicts. Never append dated addenda, `**Update:**` blocks, or change narration such as `(corrected 2026-09-11)`. History goes in one short line in the hub's log.

Ask before updating only when the update needs a fact the user has to supply, such as a price, an outcome, or a contact name. Keep those blocked items in one pending-updates note so they don't get lost.

---

## Vault Structure (defaults)

```
+Inbox/              Raw transcripts and captures waiting to be processed
Work/
  Meetings/          Processed meeting notes
  Projects/          All projects (status in frontmatter)
  Session-Logs/      AI session logs
  Archive/           Historical material
Personal/
Calendar/
  Daily/             Daily notes
  Weekly/            Weekly reviews
System/
  Templates/         Note templates
  Dashboards/        Dataview dashboards
```

## Frontmatter Standards

Every note gets YAML frontmatter with these standard fields. Consistent fields are what let Dataview dashboards query decisions, tasks, and project status across the vault.

| Field | Values | Required |
|-------|--------|----------|
| `type` | meeting, project, session, daily | Yes |
| `date` | YYYY-MM-DD | Yes |
| `status` | active, completed, on-hold, archived | For projects |
| `project` | Project name | If work-related |
| `client` | Client or company name | If client work |
| `meeting_type` | strategy, standup, planning, review, general | For meetings |
| `attendees` | List of names | For meetings |
| `priority` | critical, high, medium, low | For projects |
| `owner` | Person responsible | For projects |
| `target_date` | YYYY-MM-DD | For projects |
| `tags` | List of tags | Optional |

---

## Mode 1: Process Meeting Transcript (`/obsidian-ops process`)

### Input

Accept any of:

- A transcript pasted into the conversation
- A file path to a transcript (.txt, .md)
- A file in the `+Inbox/` folder

### Workflow

**Step 1: Parse and extract**

From the transcript, extract:

1. **Date**, from metadata, the filename, or the content
2. **Participants**, the list of attendees
3. **Meeting type**, inferred from content (strategy, standup, planning, review, general)
4. **Client or project**, if identifiable
5. **Summary**, a 2-3 sentence overview
6. **Key points**, each distinct topic with its key details
7. **Decisions**, each explicit decision with its owner if stated
8. **Action items**, covering who, what, and by when (if stated)
9. **Project references**, meaning updates on existing projects. Check `Work/Projects/` for matches.

**Step 2: Create the meeting note**

Save to `Work/Meetings/YYYY-MM-DD [Client or Project] [Type].md`.

Some meetings belong somewhere else. If the vault has a dedicated folder for a kind of call (customer testimonial calls, interviews, user research sessions), save the note there with that folder's field set, and tell the user where it went.

Use this structure:

```markdown
---
type: meeting
date: YYYY-MM-DD
meeting_type: [type]
client: [if applicable]
project: [if applicable]
attendees: [list]
tags: []
---

## Summary

[2-3 sentences]

## Key Points

[Bulleted list of distinct topics]

## Decisions

- [Decision] — [Owner, if stated]

## Action Items

- [ ] [Task] — [Owner] — [Due date, if stated]

## Project Updates

[Any updates to existing projects, each linked to its project note]
```

**Step 3: Report to the user**

After creating the note, report:

1. **Project updates found.** List each one with its matching project and ask whether to apply it to that project note.
2. **Decisions.** Give the count. They live in the meeting note, where dashboards can query them.
3. **Action items.** List each one with its owner and due date.

### Rules

- Meeting notes are fixed once processed. Do not edit them on later runs.
- Do not invent content. If part of the transcript is unclear, mark it `[unclear]` or ask.
- Keep the original meaning. Do not add interpretation beyond what was said.

---

## Mode 2: Project Management (`/obsidian-ops project`)

### Sub-commands

**`/obsidian-ops project`** (no arguments) shows active projects.

Read every file in `Work/Projects/` with `status: active` and display:

```
| Project | Owner | Priority | Target | Last Updated |
|---------|-------|----------|--------|--------------|
```

Also show the count of on-hold and completed projects.

**`/obsidian-ops project [name]`** shows one project.

Search `Work/Projects/` for a matching file and display its full contents.

**`/obsidian-ops project new`** creates a project.

Ask the user for:

1. Project name (used as the filename)
2. Objective
3. Owner (default: the user)
4. Priority (critical, high, medium, low)
5. Target date (optional)
6. Client (optional)
7. Success criteria
8. Initial tasks

Create the file at `Work/Projects/[Project Name].md` from the vault's project template if one exists in `System/Templates/`. Otherwise use the frontmatter standards above with sections for Objective, Success Criteria, Tasks, and Status Updates.

**`/obsidian-ops project update [name]`** updates a project.

Read the existing project file and ask what to update:

- Add a status update entry (what happened, what's next)
- Update task statuses (mark done, add new tasks)
- Change project status (active, completed, on-hold, archived)
- Update the target date

Status Updates is the project note's log. Add each entry newest first, in one or two lines. Every other section is current state, so when the objective, success criteria, scope, or tasks change, rewrite those sections in place. Don't describe the change in a status entry. Set `date` in the frontmatter to today.

---

## Auto-Detect Mode (`/obsidian-ops`)

When invoked without arguments, infer the mode from the conversation:

- The user pasted or mentioned a transcript: `process`
- The user asked about project status or tasks: `project`
- Unclear: ask which mode they need

---

## File Naming

- Meetings: `YYYY-MM-DD [Client or Project] [Type].md` (for example, `2026-04-16 Acme Strategy.md`)
- Projects: `[Project Name].md` (for example, `Q3 Product Launch.md`)

Link related meetings and projects with Obsidian wikilinks (the note name in double square brackets).

---

## Related Skills

- **lifecycle-marketing-campaigns**: turn launch or campaign decisions from a meeting into a campaign flow
- **product-launch-gtm**: build a launch plan from a project note

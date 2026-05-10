# Project Management Rules

This vault uses structured project notes to track all active work: Hermes, Thesis, freelance projects, etc.

## Project Note Location

All project notes go in: `Notes/Projects/`

Create one note per project:

- `Hermes.md`
- `Thesis.md`
- `Evidence & Portfolio.md`

## Project Template Frontmatter

```yaml
categories:
  - "[[Projects]]"
type: [] # e.g., "[[AI Agent]]", "[[Research]]", "[[Freelance]]"
org: [] # Client or organization (UEH, client name)
start: 2026-05-07 # Project start date
year: 2026 # Year for grouping
url: "" # GitHub, project page, etc.
status: "[[In Progress]]" # [[In Progress]], [[Completed]], [[Planned]], [[Cancelled]]
```

## Project Status Values

Use these status values (as links):

| Status            | Meaning                        | When to use                 |
| ----------------- | ------------------------------ | --------------------------- |
| `[[Planned]]`     | Not started, in planning phase | Early planning              |
| `[[In Progress]]` | Actively working on it         | Default for active projects |
| `[[Review]]`      | Ready for review/feedback      | Completed draft             |
| `[[Completed]]`   | Done, delivered                | Finished projects           |
| `[[On Hold]]`     | Temporarily paused             | Blocked or reprioritized    |
| `[[Cancelled]]`   | Abandoned/cancelled            | No longer proceeding        |

## Project Types

Use `type:` to classify projects:

| Type                 | Description                 | Examples                  |
| -------------------- | --------------------------- | ------------------------- |
| `[[AI Agent]]`       | AI/LLM-based bots or agents | Hermes, Thesis Bot        |
| `[[Research]]`       | Academic research           | Thesis, papers            |
| `[[Product]]`        | Product development         | Bot packages, skill packs |
| `[[Freelance]]`      | Client work                 | Freelance gigs            |
| `[[Infrastructure]]` | DevOps, tooling             | VPS setup, CI/CD          |
| `[[Learning]]`       | Courses, certifications     | Online courses            |

## Project Note Structure

After frontmatter, use this body structure:

```markdown
# Project Name

## Mục Tiêu

- What you're trying to achieve
- Success criteria

## Trạng Thái Hiện Tại

- Current phase
- Recent progress
- Blockers/risks

## Components/Features

- Feature 1
- Feature 2

## Tech Stack

- Frameworks
- Tools
- APIs

## Tiến Độ Phát Triển

### Ngắn Hạn (Next 2-4 weeks)

- [ ] Task 1
- [ ] Task 2

### Trung Hạn (1-3 months)

- [ ] Task 3
- [ ] Task 4

### Dài Hạn (3+ months)

- [ ] Task 5

## Liên Kết

- Related projects: [[Other Project]]
- People: [[Team Member]]
- Topics: [[AI]], [[Supply Chain]]
```

## Project Checklists

Use task checklists for tracking:

```
- [ ] Task description
- [x] Completed task
```

**Tip:** Use Obsidian's task management features:

- `Ctrl+Shift+P` > "Toggle task"
- Filter tasks across vault with Dataview

## Project Progress Updates

Update `status:` in frontmatter when:

- Starting work: `Planned` → `In Progress`
- Reaching milestones: Add checklist updates
- Completing: `In Progress` → `Completed`

Also update the note body with:

- What was accomplished
- What's next
- Any changes to timeline/scope

## Project Dashboard

View all projects via:

1. `Categories/Projects.md` - All projects table
2. Or Dataview query:
   ```dataview
   TABLE status, start, org
   FROM "Notes/Projects"
   SORT start DESC
   ```

## Evidence & Portfolio

For projects that produce portfolio pieces:

1. Create `Evidence & Portfolio.md` in `Notes/Projects/`
2. Use appropriate type (e.g., `[[Research]]`, `[[Product]]`)
3. Document deliverables with screenshots, links, metrics
4. Reference specific notes for each piece of evidence

## Multiple Projects

If managing multiple simultaneous projects:

1. **Prioritize:** Keep 2-3 active in `In Progress`, others in `Planned` or `On Hold`
2. **Link from Daily notes:** Reference project name in daily work
3. **Weekly review:** Check status of all projects weekly
4. **Archive completed:** Move to `Archive/` folder or keep with `Completed` status

## Project Handoff/Completion

When finishing a project:

1. Update `status: "[[Completed]]"`
2. Add completion date to frontmatter (custom field or in note)
3. Write brief summary in note body
4. Update any related MOC notes
5. Consider moving to archive if vault gets large

## Common Project Fields

Optional fields to add as needed:

```yaml
priority: "[[High]]" # High, Medium, Low
deadline: 2026-12-31 # Due date
estimated-hours: 160 # Time estimate
actual-hours: # Time spent (track separately)
client: "[[Client Name]]" # For freelance
team: # Team members (links)
tags:
  - thesis
  - priority
```

## Project Naming

- Use short, recognizable names: `Hermes`, `Thesis`, `Portfolio`
- Avoid dates in filename
- If duplicate project names, add suffix: `Thesis (v2)`

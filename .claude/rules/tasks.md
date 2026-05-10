# Task Management Rules

This vault uses Obsidian's built-in task system with checkboxes for tracking actionable items across notes.

## Task Syntax

Tasks use markdown checkbox syntax:

```markdown
- [ ] Not started task
- [x] Completed task
- [/] In-progress task (optional, plugin-dependent)
```

## Task Locations

Tasks can appear in:

- **Daily notes** - Today's actionable items
- **Project notes** - Project-specific todos
- **Meeting notes** - Action items from meetings
- **Evergreen notes** - Occasionally, for personal systems

## Task Management Best Practices

### 1. Use Tasks for Actions, Not Ideas

**Tasks:**

- `[ ] Email professor about thesis proposal`
- `[ ] Review paper by Friday`
- `[ ] Update Hermes documentation`

**Not Tasks (use evergreen notes instead):**

- `Think about AI ethics` (create evergreen note)
- `Research supply chain trends` (create clipping, then evergreen)

### 2. Context Matters

Always include enough context:

```markdown
- [ ] Email Dr. Nguyen about [[Hermes]] demo on Monday
```

Not:

```markdown
- [ ] Send email
```

### 3. Due Dates

Use dates in task text or link to calendar:

```markdown
- [ ] Submit thesis proposal by 2026-06-01
- [ ] Review paper [[Due: 2026-05-15]]
```

Or use Dataview with `due:` frontmatter field (if configured).

### 4. Tag Tasks

Add tags for filtering:

```markdown
- [ ] #hermes Update API documentation
- [ ] #thesis Find 5 more sources
- [ ] #ueh Register for next semester
```

### 5. Check Off and Date

When completing:

- Change `[ ]` to `[x]`
- Optionally add completion date: `[x] 2026-05-07`

### 6. Review Daily

During daily note review:

- Check off completed tasks
- Migrate unfinished to tomorrow's note or next action

## Task Queries with Dataview

### All Incomplete Tasks

````
```dataview
TASK
WHERE !completed
FROM "Notes" OR "Daily" OR "Notes/Projects"
SORT due ASC, file.name ASC
````

```

### Tasks by Tag

```

```dataview
TASK
FROM ""
WHERE contains(tags, "hermes")
SORT file.mtime DESC
```

```

### Tasks by Project

```

```dataview
TASK
FROM "Notes/Projects/Hermes.md"
```

````

## Task Organization by Note Type

### Daily Notes
Top 3 tasks (MIT):
```markdown
### 🎯 Top 3 Hôm Nay

- [ ] Task 1 (most important)
- [ ] Task 2
- [ ] Task 3
````

Then additional tasks in same section or separate:

```markdown
### 📋 Công Việc Hôm Nay

- [ ] Email Dr. Nguyen
- [ ] Read paper on demand forecasting
- [ ] Update project timeline
```

### Project Notes

Use checkboxes in development sections:

```markdown
### Tiến Độ Phát Triển

#### Ngắn Hạn

- [ ] Setup development environment
- [ ] Create API spec
- [ ] Build MVP prototype

#### Trung Hạn

- [ ] Integrate Claude API
- [ ] Write documentation
```

### Meeting Notes

Action items at the end:

```markdown
## Action Items

- [ ] [[Alice]]: Send meeting notes by EOD
- [ ] [[Bob]]: Research pricing options
- [ ] [[Charlie]]: Schedule follow-up
```

## Task Completion Workflow

1. **Check off** in original note
2. **Review** daily in daily note
3. **Archive** completed items (optional: move to `Completed/` folder)
4. **Identify blockers** for incomplete tasks

## Common Task Fields

Some use custom frontmatter on notes containing tasks:

```yaml
priority: "[[High]]"
deadline: 2026-05-15
```

Then query:

````
```dataview
TASK
WHERE file.priority = [[High]]
AND !completed
````

```

## Task Management Plugins

This vault may use:
- **Obsidian Tasks** (community plugin) - Enhanced task queries, due dates, priorities
- **Obsidian Dataview** - Query tasks across vault

If Tasks plugin is installed:
```

```tasks
not done
due before next week
```

```

## Task Review Rituals

### Daily (5 min)
- Check today's tasks from daily note
- Review overdue tasks from yesterday

### Weekly (15 min)
- Go to `Categories/Projects.md` or each project
- Review incomplete tasks
- Re-prioritize or delegate

### Monthly (30 min)
- Archive completed tasks (delete or move)
- Review stuck tasks (incomplete >30 days)
- Update project priorities

## Task vs Evergreen vs Clipping

| Type | Use for | Example |
|------|---------|---------|
| **Task** | Action you will do | `[ ] Write thesis chapter 2` |
| **Evergreen** | Idea to remember | `[[Writing Process]]` note |
| **Clipping** | Saved article | `[[AI in SCM article]]` |

## Task Quality Checklist

- [ ] Actionable verb at start (Email, Review, Create, Call)
- [ ] Clear what "done" looks like
- [ ] Has context (what/why)
- [ ] Has owner if collaborative (your name or `[[Person]]`)
- [ ] Has due date if time-sensitive
- [ ] Located in relevant note (project, not random)

## Troubleshooting

**Tasks not showing in Dataview:**
- Check syntax: `- [ ]` with space after `-`
- Verify Dataview plugin is enabled
- Check query path includes note location

**Too many tasks:**
- Review and prune
- Break large tasks into subtasks
- Archive completed

**Tasks getting lost:**
- Use tags for cross-cutting tasks (`#thesis`, `#hermes`)
- Create master task note that aggregates:
```

```dataview
TASK
WHERE !completed
SORT due ASC
```

```

```

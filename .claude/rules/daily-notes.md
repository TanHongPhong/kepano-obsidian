# Daily Notes Workflow

Daily notes are the central hub for day-to-day knowledge work. This vault follows a structured daily note system.

## Creating Daily Notes

### Automatic Creation

Daily notes are **auto-created** when you:

1. Open Obsidian
2. Use ribbon button "Open today's note"
3. Run command `Daily note: Open today's note`

### Manual Creation

If needed, create manually:

1. `Ctrl+P` > "Create daily note"
2. Or create file `Daily/YYYY-MM-DD.md`

### Template

Daily notes use `Templates/Daily Note Template.md`:

```markdown
## 📅 Daily Notes - {{date}}

### 🎯 Top 3 Hôm Nay

- [ ]
- [ ]
- [ ]

### 📚 Học Tập & Nghiên Cứu

-

### 🤖 Tiến Độ Dự Án (Hermes/Thesis)

-

### 💡 Ý Tưởng Mới

-

### 📝 Ghi Chú Khác

- ***

  **Tags:** #daily
```

## Daily Note Structure

### Sections (by priority)

1. **Top 3 Hôm Nay** - MIT (Most Important Tasks) for the day
2. **Học Tập & Nghiên Cứu** - Learning, research, reading
3. **Tiến Độ Dự Án** - Project progress (Hermes, Thesis)
4. **Ý Tưởng Mới** - New insights, evergreen seeds
5. **Ghi Chú Khác** - Miscellaneous

### Checklist Usage

Use checkboxes for tasks:

```
- [ ] Task not started
- [x] Task completed
- [/] Task in progress (optional)
```

### Linking from Daily Notes

Always link to related notes:

```
- Meeting with [[Nguyen Van A]] about [[Hermes]]
- Read article on [[AI Agents]] saved in [[Clippings]]
- Progress on [[Thesis]] chapter 2
```

### Tags

Daily notes automatically get `#daily` tag (from template).

## Review Workflow

### Morning (5 min)

1. Open today's daily note
2. Fill in Top 3 tasks
3. Review yesterday's note for carry-overs

### Evening (5-10 min)

1. Return to today's note
2. Update sections with what you learned/accomplished
3. Check off completed tasks
4. Add any new ideas as evergreen notes (link them)

### Weekly Review (Sunday, 30 min)

1. Navigate to `Categories/Daily.md` or create weekly review note
2. Summarize the week
3. Identify patterns, wins, blockers
4. Plan next week's focus areas

## From Daily to Permanent Notes

When an idea in daily note deserves its own evergreen note:

1. Create new note from the idea
2. Use Evergreen Template
3. Link back to the daily note: `Source: [[2026-05-07]]`
4. Add appropriate priority tag `#0🌲`-`#3🌲`

## Monthly Notes

Monthly notes exist for broader overview:

**Creation:** `Templates/Monthly Note Template.md`
**Location:** `Daily/YYYY-MM.md` (or separate folder)

Monthly notes embed daily notes:

```markdown
![[Daily.base#Monthly]]
```

Use for:

- Monthly goals
- Quarterly review
- Tracking monthly metrics

## Journaling

For more personal journaling, use `Journal Template.md`:

- Less structured than daily notes
- `#journal` tag
- Can be daily or as-needed

## Daily Note Checklist

Every daily note should have:

- [ ] Date in title (YYYY-MM-DD.md)
- [ ] Top 3 tasks listed
- [ ] At least one entry in each relevant section
- [ ] Links to related notes (people, projects, concepts)
- [ ] `#daily` tag present

## Troubleshooting

**Daily note not auto-creating:**

- Check `.obsidian/daily-notes.json` configuration
- Verify template path is correct
- Check plugin "Daily notes" is enabled in core plugins

**Previous day's note not appearing:**

- Check `Daily/` folder for file
- Verify filename format `YYYY-MM-DD.md`

**Template not loading:**

- Check `.obsidian/templates.json` configuration
- Verify `Templates/Daily Note Template.md` exists

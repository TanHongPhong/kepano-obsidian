# Naming Conventions

This vault follows consistent naming patterns for notes, folders, and templates.

## File Naming Patterns

### Daily Notes

```
YYYY-MM-DD.md           # e.g., 2026-05-07.md
```

- Auto-created in `Daily/` folder
- No spaces, use dashes
- Zero-padded months and days

### Meeting Notes

```
YYYY-MM-DD Meeting with [Name].md
# Example: 2026-05-07 Meeting with Dr. Nguyen.md
```

### People Notes

```
Full Name.md            # e.g., Nguyen Van A.md
```

- Use full name, no titles
- No commas or special characters

### Project Notes

```
Project Name.md         # e.g., Hermes.md, Thesis.md
```

- Short, recognizable name
- No dates in filename (date goes in frontmatter)

### Book/Media Notes

```
Title: Subtitle.md      # e.g., The Phoenix Project.md
```

- Keep original title capitalization
- Remove colons if problematic (Obsidian handles them)

### Clipping Notes

```
Original Article Title.md
# Or shortened: AI in Supply Chain.md
```

- Can be long; shorten if >50 chars
- Remove URL fragments

### Evergreen Notes

```
Short Descriptive Title.md
# Examples: "Composable Notes", "SCM Needs AI", "Claude Code Workflow"
```

- 2-5 words ideal
- Declarative statement style
- No dates

## Folder Structure

```
📁 Vault Root
├── 📁 .claude/          # Claude Code rules (this folder)
│   └── 📁 rules/       # Topic-specific rule files
├── 📁 .obsidian/        # Obsidian configuration (auto-generated)
├── 📁 Attachments/      # Embedded files, images, PDFs
│   ├── 📁 [date-based subfolders optional]
├── 📁 Categories/       # Category dashboard notes
├── 📁 Clippings/        # Saved articles/resource links
├── 📁 Daily/            # Daily notes (YYYY-MM-DD.md)
├── 📁 Notes/            # Personal notes and projects
│   ├── 📁 Projects/     # Active projects only
│   ├── AI.md            # Topic notes can be at root
│   ├── Thesis.md
│   └── ...
├── 📁 References/       # People, places, organizations, media
│   ├── Nguyen Van A.md
│   ├── UEH.md
│   ├── The Phoenix Project.md
│   └── ...
└── 📁 Templates/        # Template files (do not delete!)
    ├── 📁 Bases/        # Reusable .base dashboard components
    └── *.md             # Full templates for note creation
```

## Template File Naming

### Full Templates

```
"Template Name".md       # Quotes because of spaces
# Examples:
# "Daily Note Template.md"
# "People Template.md"
# "Project Template.md"
```

### Base Templates

```
TemplateName.base        # No spaces, .base extension
# Examples:
# Daily.base
# Projects.base
# People.base
# Meetings.base
```

## Category Notes

```
Category Name.md         # e.g., People.md, Projects.md, AI.md
```

- Stored in `Categories/` folder
- Note name must match category link exactly
- Embeds corresponding `.base` file

## Date Formats

**Standard format:** `YYYY-MM-DD`

- Always 4-digit year, 2-digit month, 2-digit day
- Zero-padded: `2026-05-07` not `2026-5-7`
- Used in:
  - Daily notes filenames
  - Frontmatter `created:`, `date:`, `start:`, `published:`, `last:`

## Special Characters to Avoid

**DO NOT use:**

- `? * < > | " :` in filenames (invalid on most filesystems)
- Leading/trailing spaces
- Multiple consecutive spaces
- `/ \` in note names (folder separators)

**OK to use:**

- Spaces: `My Note.md` (Obsidian handles)
- Parentheses: `Meeting (Follow-up).md`
- Hyphens/underscores: `ai-agent.md`, `my_note.md`
- Emoji: `🚀 Project.md` (but avoid for cross-platform)

## Case Sensitivity

Obsidian on most systems is case-insensitive, but:

**Be consistent:**

- `[[AI]]` not `[[ai]]` (if note is named `AI.md`)
- Use Title Case for proper nouns
- Use lowercase for tags only

## Renaming Notes

When renaming a note:

1. **Use Obsidian's rename** (F2 or right-click > Rename)
2. **Obsidian updates links automatically** (if setting enabled)
3. **Verify:** Check backlinks pane to ensure no broken links
4. **Update category if needed:** If it's a category note, update all references

## Naming Checklist

When creating a new note:

- [ ] Follows the appropriate pattern above
- [ ] No special characters (`?*<>|`)
- [ ] Dates are `YYYY-MM-DD` format
- [ ] Template spaces preserved (if using template)
- [ ] Category note exists if referencing `[[Category]]`

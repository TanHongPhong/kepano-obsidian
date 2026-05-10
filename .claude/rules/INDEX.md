# Claude Code Rules - Index

This directory contains comprehensive rules for operating in this Obsidian vault using Claude Code. Each file covers a specific domain.

## Getting Started

1. Read [CLAUDE.md](../CLAUDE.md) first for vault overview
2. Review relevant rule files before working on specific tasks
3. Check settings in `.claude/settings.local.json` for permissions

## Rule Files

### Core Workflows

| File                             | Purpose                              | When to Read                 |
| -------------------------------- | ------------------------------------ | ---------------------------- |
| [templates.md](templates.md)     | Template selection and usage         | Before creating any new note |
| [categories.md](categories.md)   | Category organization and dashboards | When classifying notes       |
| [frontmatter.md](frontmatter.md) | YAML frontmatter standards           | When editing note metadata   |
| [linking.md](linking.md)         | Internal links and backlinks         | When connecting notes        |
| [naming.md](naming.md)           | File and folder naming conventions   | Before creating files        |

### Note Types

| File                                     | Covers                                 |
| ---------------------------------------- | -------------------------------------- |
| [daily-notes.md](daily-notes.md)         | Daily journal workflow and structure   |
| [projects.md](projects.md)               | Project note creation and management   |
| [evergreen.md](evergreen.md)             | Atomic permanent notes                 |
| [clippings.md](clippings.md)             | Saving and organizing external content |
| [people-orgs.md](people-orgs.md)         | People and organization notes          |
| [media-templates.md](media-templates.md) | Books, movies, games, music, etc.      |
| [events-trips.md](events-trips.md)       | Events and travel notes                |
| [tasks.md](tasks.md)                     | Task management with checkboxes        |

### Technical

| File                                       | Covers                             |
| ------------------------------------------ | ---------------------------------- |
| [dataview.md](dataview.md)                 | Dataview JS queries and dashboards |
| [attachments.md](attachments.md)           | File attachments handling          |
| [obsidian-config.md](obsidian-config.md)   | `.obsidian/` configuration         |
| [search-discovery.md](search-discovery.md) | Finding notes efficiently          |
| [tags.md](tags.md)                         | Tag hierarchy and conventions      |

## Quick Reference

### Creating Notes

1. **Daily:** `Ctrl+P` > "Daily note"
2. **People:** `References/` + People Template
3. **Meeting:** `Notes/` + Meeting Template
4. **Project:** `Notes/Projects/` + Project Template
5. **Clipping:** `Clippings/` + Clipping Template
6. **Evergreen:** `Notes/` + Evergreen Template

See [templates.md](templates.md) for complete decision tree.

### Common Commands

| Action          | Shortcut                                |
| --------------- | --------------------------------------- |
| Quick Switcher  | `Ctrl+P`                                |
| Global Search   | `Ctrl+Shift+F`                          |
| Insert Template | `Ctrl+P` > "Templates: Insert template" |
| Toggle Task     | `Ctrl+Shift+P` > "Toggle task"          |
| Open Graph      | `Ctrl+G`                                |

### Folder Structure

```
📁 Vault Root
├── 📁 .claude/          # Claude Code rules (this folder)
│   └── 📁 rules/       # Topic-specific rule files
├── 📁 .obsidian/        # Obsidian configuration
├── 📁 Attachments/      # Images, PDFs, etc.
├── 📁 Categories/       # Category dashboard notes
├── 📁 Clippings/        # Saved articles
├── 📁 Daily/            # Daily notes (YYYY-MM-DD.md)
├── 📁 Notes/            # Main content
│   └── 📁 Projects/     # Active projects only
├── 📁 References/       # People, places, media
└── 📁 Templates/        # Template files
```

## Permissions

This vault has auto-approval configured in `.claude/settings.local.json` for:

- Read, Edit, Write file operations
- Glob, Grep, LS searches
- WebFetch for UEH domains
- WebSearch

## Key Conventions

1. **Categories** (frontmatter `categories:`) = Note type classification
2. **Links** (`[[...]]`) = Semantic connections between notes
3. **Tags** (`#tag`) = Quick filtering, priority (`#0🌲`-`#3🌲`)
4. **Frontmatter** = Structured metadata (YAML, 2-space indent)
5. **Dataview** = Dynamic dashboards (`.base` files)
6. **Templates** = Consistent note creation

## Maintenance

### Monthly

- Review `Categories/` dashboards for completeness
- Check orphaned attachments via `Attachments.base`
- Update evergreen priorities

### Quarterly

- Audit templates in `Templates/`
- Review `settings.local.json` permissions
- Clean up unused categories

## Need Help?

- **How to create X?** → Check [templates.md](templates.md)
- **What category to use?** → See [categories.md](categories.md)
- **Dataview query not working?** → See [dataview.md](dataview.md)
- **Frontmatter format?** → See [frontmatter.md](frontmatter.md)

## Contributing

When adding new conventions or templates:

1. Document in appropriate rule file
2. Update this index if adding major new category
3. Keep examples aligned with actual vault usage

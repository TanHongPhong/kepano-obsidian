# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an **Obsidian vault** implementing a "Second Brain" / PARA (Projects-Areas-Resources-Archives) methodology for personal knowledge management. The vault uses the Minimal theme by KEPANO and follows a structured note-taking system with extensive templates.

## Repository Structure

```
kepano-obsidian/
├── .obsidian/           # Obsidian configuration (vault settings)
│   ├── appearance.json  # Theme configuration (Minimal theme)
│   ├── community-plugins.json  # Enabled community plugins
│   ├── core-plugins.json # Enabled core plugins
│   ├── daily-notes.json # Daily notes configuration
│   ├── templates.json   # Template settings
│   ├── workspace.json   # UI layout and pane configuration
│   └── plugins/         # Community plugin data
├── Attachments/         # Media and file attachments
├── Categories/         # Tag/category organization (if used)
├── Clippings/          # Web clippings and excerpts
├── Daily/              # Daily notes (journal entries)
├── Notes/              # Main content notes
│   └── Projects/       # Active project notes
├── References/         # Reference material and source notes
├── Templates/          # Note templates (50+ templates)
│   ├── Bases/          # Base template files (.base extensions)
│   └── *.md            # Individual templates by entity type
└── Templates/          # Template files

```

## Key Configuration Files

- `.obsidian/appearance.json` - Theme: Minimal, Theme mode: system
- `.obsidian/community-plugins.json` - Plugins: obsidian-hider, obsidian-minimal-settings
- `.obsidian/daily-notes.json` - Daily notes folder: `Daily/`, template: `Templates/Daily Note Template`
- `.obsidian/core-plugins.json` - Core plugins enabled/disabled configuration
- `.obsidian/app.json` - Attachment folder: `Attachments/`, auto-update links enabled

## Template System

The vault uses a comprehensive template system with:

- **Base templates** (`.base` files in `Templates/Bases/`) - Reusable template components
- **Entity templates** - Specific templates for different note types:
  - People, Places, Companies, Books, Movies, etc.
  - Projects, Meetings, Events, Tasks
  - Daily notes, Monthly notes
  - Various media types (Albums, Podcasts, Recipes, etc.)

## Notes Organization

Notes follow a **PARA-inspired** structure:

- **Projects** - Active projects in `Notes/Projects/`
- **Areas** - Life domains (likely in `Notes/`)
- **Resources** - Reference materials in `References/`
- **Archives** - Historical items (likely in `Clippings/` or organized folders)

## Common Development Tasks

### Modifying Vault Configuration

Edit files in `.obsidian/` to change:

- Theme settings (`appearance.json`)
- Core/community plugins (`core-plugins.json`, `community-plugins.json`)
- Daily notes template and location (`daily-notes.json`)
- Attachment folder behavior (`app.json`)

### Adding New Templates

1. Create a new `.md` file in `Templates/` or `Templates/Bases/`
2. For base templates, use `.base` extension
3. The template will be available in Obsidian's template picker

### Modifying Existing Templates

Edit template files directly in `Templates/`. Templates are plain Markdown with frontmatter support.

## Obsidian Plugins

### Core Plugins

File-explorer, global-search, switcher, graph, backlink, tag-pane, page-preview, daily-notes, templates, note-composer, command-palette, editor-status, markdown-importer, zk-prefixer, random-note, outline, workspaces, file-recovery, canvas, bookmarks, bases, webviewer

### Community Plugins

- **obsidian-hider** - Hide UI elements for cleaner interface
- **obsidian-minimal-settings** - Extended Minimal theme configuration

## Notes on Editing

- This is an **Obsidian vault** - not a traditional codebase
- All files are plain Markdown (`.md`) with optional YAML frontmatter
- Changes to `.obsidian/` settings sync with Obsidian app automatically
- Respect existing naming conventions and template structure
- Templates use `.base` files as reusable components

## File Naming Conventions

- Template files: `"Template Name".md` (spaces included)
- Base templates: `*.base` in `Templates/Bases/`
- Daily notes: date-based (e.g., `2025-05-10.md`)

## Important: No Build/Lint/Test Commands

This is a configuration/data repository, not an application. There are no build steps, linters, or tests. Changes are immediately reflected in the Obsidian application.

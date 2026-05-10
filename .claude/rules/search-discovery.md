# Search and Discovery Rules

This vault uses multiple strategies to find and discover notes efficiently.

## Search Methods

### 1. Quick Switcher (`Ctrl+P` or `Cmd+P`)

Fastest way to jump to any note:

- Type note name or fragment
- Fuzzy matching: `thes` finds `Thesis.md`
- `#` prefix for tags: `#ai` shows all #ai tagged notes
- `[[` shows links to that note (backlinks)

### 2. Global Search (`Ctrl+Shift+F`)

Full-text search across the vault:

- Searches all markdown files
- Supports regex
- Shows context snippets
- Use filters: `path:Notes`, `tag:#ai`

### 3. Tag Pane

Enable in core plugins → tag-pane:

- Browse all tags alphabetically
- Click tag to see all notes with that tag
- Hierarchical tags shown as tree (`#ai/llm` nests under `#ai`)

### 4. Graph View

Visual map of note connections:

- `Ctrl+G` to open
- Filter by tags, folders, dates
- Color by category or tag
- Find isolated notes (no connections)

### 5. Category Dashboards

Each category note (`Categories/*.md`) shows:

- All notes in that category
- Filtered tables (by status, date, etc.)
- Embedded Dataview queries

## Search Patterns

### By Category

```
tag:[[Projects]]    # All project notes
tag:[[People]]      # All people notes
```

OR use category dashboards.

### By Status

```
status:[[In Progress]]
status:[[Completed]]
```

### By Topic (using links)

```
[[AI]]
[[Supply Chain]]
```

### By Tag

```
#ai
#thesis
#0🌲
```

### By Date

Created this week:

```
created:>=last week
```

Modified today:

```
mtime:today
```

### Combined Queries

All AI-related projects in progress:

```
tag:[[Projects]] AND [[AI]] AND status:[[In Progress]]
```

Evergreen notes created this month:

```
tag:#evergreen AND created:>=2026-05-01
```

## Finding Related Notes

### Backlinks Pane

Enable in core plugins → backlink:

- Shows all notes linking to current note
- Found in right sidebar
- Helps discover connections

### Related Note Dashboard

Use `[[Related]]` category or embed:

```
![[Related.base]]
```

Shows notes with shared links/tags.

### Outgoing Links

See what the current note links to:

- Look for linked mentions in preview
- Use `[[` in search to see outgoing

## Discovering Content

### Unlinked Mentions

Plugin "Unlinked mentions" shows:

- Words that match note titles but aren't linked
- Helps find missed linking opportunities

### Random Note

Core plugin `random-note`:

- `Ctrl+P` > "Random note"
- Serendipitous discovery
- Good for review

### MOC Notes

Map of Content notes are indices:

```
# AI Topics MOC
## People
- [[AI Researchers]]
## Projects
- [[Hermes]]
## Concepts
- [[LLM]]
```

Create MOCs for major topics (AI, Thesis, UEH).

### Daily Notes as Discovery

Review past daily notes to find:

- Ideas that became evergreen notes
- Meeting references (check if people note exists)
- Project references (check if project note exists)

## Organizing for Discovery

1. **Use categories consistently** - Category dashboards auto-populate
2. **Link liberally** - More links = better graph/backlinks
3. **Use descriptive titles** - Makes search easier
4. **Maintain tag hierarchy** - `#ai/llm` appears under `#ai`
5. **Create MOC notes** - Manual curation for complex topics

## Search Best Practices

1. **Start specific, broaden if needed:**
   - `[[Hermes]]` → `[[AI]]` → `#ai`

2. **Use dashboards for category browsing:**
   - Go to `Categories/Projects.md` instead of searching

3. **Leverage filters:**
   - In category dashboards, use built-in views (To-watch, Favorites, etc.)

4. **Combine tag and link:**
   - `#thesis [[AI]]` finds thesis-related AI notes

5. **Search attachments:**
   - `attachment:pdf` finds PDFs
   - `attachment:image` finds images

## Keyboard Shortcuts

| Action          | Shortcut                       |
| --------------- | ------------------------------ |
| Quick Switcher  | `Ctrl+P`                       |
| Global Search   | `Ctrl+Shift+F`                 |
| Open Graph      | `Ctrl+G`                       |
| Insert Link     | `Ctrl+K`                       |
| Tag Pane Toggle | `Ctrl+Shift+T` (if configured) |

## Advanced: Dataview Search

Use Dataview for complex queries:

````
```dataview
LIST FROM #ai AND #thesis
WHERE status = "In Progress"
SORT file.mtime DESC
````

```

## Troubleshooting

**Search not finding note:**
- Check note exists and is in indexed folder
- Check spelling/case (Obsidian is case-insensitive but spaces matter)
- Verify note has correct extension (.md)

**Backlinks not showing:**
- Enable backlink pane in core plugins
- Check that note actually has links pointing to it

**Graph too cluttered:**
- Filter by tag or folder
- Group by category
- Exclude Daily notes
```

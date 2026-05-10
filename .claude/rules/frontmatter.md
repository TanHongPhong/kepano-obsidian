# Frontmatter Standards

All notes in this vault use YAML frontmatter for metadata. Follow these standards for consistency.

## Frontmatter Structure

Frontmatter is enclosed by `---` lines at the top of the file:

```yaml
---
categories:
  - "[[People]]"
created: 2026-05-07
tags:
  - ueh
  - thesis
people:
  - "[[Nguyen Van A]]"
org:
  - "[[UEH]]"
---
```

### YAML Syntax Rules

1. **Indentation:** 2 spaces (never tabs)
2. **Quotes:** Use double quotes for strings, single quotes optional
3. **Arrays:** Use `[]` with items separated by `, `
4. **Dates:** Format as `YYYY-MM-DD`
5. **Booleans:** `true` / `false` (lowercase)

## Required vs Optional Fields

### Categories (REQUIRED for most notes)

```yaml
categories:
  - "[[Category]]" # Primary category (type of note)
```

**When to include:**

- All content notes (People, Projects, Books, Meetings, etc.)
- **NOT required** for Templates, Bases, or configuration files

### Created Date (REQUIRED for most notes)

```yaml
created: {{date}}      # Template placeholder
created: 2026-05-07    # Actual date
```

**Format:** `YYYY-MM-DD`

- Use `{{date}}` in templates (auto-fills when template is inserted)
- For existing notes, use actual date or approximate

### Tags (OPTIONAL)

```yaml
tags:
  - evergreen
  - ai
  -  #0🌲
```

**Tag naming conventions:**

- Lowercase
- Hyphens for multi-word: `machine-learning`
- Emoji for priority: `#0🌲`, `#1🌲`, `#2🌲`, `#3🌲`
- Topic prefixes: `#ai`, `#scm`, `#thesis`

## Common Frontmatter Fields by Template

### People Template

```yaml
categories:
  - "[[People]]"
birthday: 1990-05-15 # optional
org: [] # linked organizations
created: { { date } }
```

### Meeting Template

```yaml
categories:
  - "[[Meetings]]"
type: [] # [[1:1]], [[Team Sync]], [[Job Interviews]]
date: { { date } }
org: # organization
loc: # location (optional)
people: [] # attendees
topics: [] # [[AI]], [[Thesis]], [[Supply Chain]]
```

### Project Template

```yaml
categories:
  - "[[Projects]]"
type: [] # [[AI Agent]], [[Research]], [[Freelance]]
org: [] # client/organization
start: # YYYY-MM-DD
year: # 2026
url: "" # project link
status: # [[In Progress]], [[Completed]], [[Cancelled]]
```

### Clipping Template

```yaml
categories:
  - "[[Clippings]]"
author: [] # linked author note(s)
url: "" # source URL (required)
created: { { date } }
published: # publication date
topics: [] # [[AI]], [[Operations]]
status: [] # [[Read]], [[Unread]], [[To-Read]]
```

### Evergreen Template

```yaml
created: { { date } }
tags:
  - 0🌲 # priority (0-3)
```

### Book Template

```yaml
categories:
  - "[[Books]]"
author: [] # linked author(s)
cover: "" # cover image path
genre: [] # Fiction, Non-fiction
pages:
isbn:
isbn13:
year:
rating: # 1-5 or 1-10
topics: []
created: { { date } }
last: # last read date
via: "" # how discovered
tags:
  - to-read
```

## Linking in Frontmatter

Always use double brackets for links in frontmatter:

```yaml
categories:
  - "[[People]]" # Correct
org:
  - "[[UEH]]"
people:
  - "[[Nguyen Van A]]"
  - "[[Tran Thi B]]"
```

**Arrays of links:**

```yaml
people:
  - "[[Alice]]"
  - "[[Bob]]"
  - "[[Charlie]]"
```

## Field Order Convention

Follow this order for consistency:

1. `categories:`
2. `type:` (if applicable)
3. `status:` (if applicable)
4. Date fields (`date:`, `start:`, `published:`, `created:`, `last:`)
5. People/Org links (`people:`, `org:`, `author:`)
6. Other fields (`url:`, `topics:`, `loc:`, `rating:`, etc.)
7. `tags:`
8. Custom fields

## Empty Values

- Empty array: `[]`
- Empty string: `""`
- Omit the field entirely if truly not applicable

## Multi-line Values

For longer text in frontmatter (rare), use `|`:

```yaml
summary: |
  This is a longer
  description that spans
  multiple lines.
```

But prefer to put lengthy content in the note body instead.

## Validation

Valid frontmatter should:

- Parse as valid YAML
- Have all category links pointing to existing notes
- Have dates in `YYYY-MM-DD` format
- Not have duplicate keys

Use online YAML validators or the Obsidian preview to check.

## Template Variables

Templates use `{{variable}}` syntax for auto-fill:

- `{{date}}` - Current date (YYYY-MM-DD)
- `{{title}}` - Note title (file name)
- Other custom variables may be defined in plugin settings

When you insert a template, Obsidian/Hotkeys replace these automatically.

## Field Conventions Summary

| Field        | Type             | Required           | Purpose             |
| ------------ | ---------------- | ------------------ | ------------------- |
| `categories` | array of links   | Yes (type)         | Note classification |
| `created`    | date             | Yes                | Creation date       |
| `date`       | date             | Meetings           | Event date          |
| `start`      | date             | Projects           | Start date          |
| `people`     | array of links   | People/Meetings    | People involved     |
| `org`        | array of links   | People/Meetings    | Organizations       |
| `topics`     | array of links   | Most notes         | Subject areas       |
| `status`     | link             | Projects/Clippings | Current state       |
| `type`       | array of links   | Projects/Meetings  | Subtype             |
| `tags`       | array of strings | Optional           | Quick search labels |
| `url`        | string           | Clippings/Projects | External link       |
| `rating`     | number           | Books/Movies       | Quality score       |

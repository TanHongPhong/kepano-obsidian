# Template Selection Rules

## When to Use Each Template

### Daily Notes

- **Trigger:** Creating a note for the current day
- **How:** `Ctrl+P` > "Daily note" or use ribbon button
- **Location:** Auto-created in `Daily/` as `YYYY-MM-DD.md`
- **Template:** `Templates/Daily Note Template.md`

### People Notes

- **Trigger:** Recording information about a person (professor, classmate, mentor, contact)
- **Where:** `References/` folder
- **Naming:** Use full name (e.g., `Nguyen Van A.md`)
- **Required frontmatter:**
  ```yaml
  categories:
    - "[[People]]"
  birthday: # optional, format: YYYY-MM-DD
  org: [] # linked organizations
  ```

### Meeting Notes

- **Trigger:** After any meeting, interview, or conversation worth recording
- **Where:** `Notes/` folder
- **Naming:** `YYYY-MM-DD Meeting with [Name].md`
- **Required frontmatter:**
  ```yaml
  categories:
    - "[[Meetings]]"
  type: [] # e.g., "[[1:1]]", "[[Job Interviews]]", "[[Team Sync]]"
  date: { { date } } # auto-filled
  org: # organization
  loc: # location (optional)
  people: [] # linked people
  topics: [] # linked topics (AI, SCM, Thesis, etc.)
  ```
- **Body:** Notes section at minimum

### Project Notes

- **Trigger:** Starting any significant project (Hermes, Thesis, freelance work)
- **Where:** `Notes/Projects/` folder
- **Naming:** Project name (e.g., `Hermes.md`, `Thesis.md`)
- **Required frontmatter:**
  ```yaml
  categories:
    - "[[Projects]]"
  type: [] # e.g., "[[AI Agent]]", "[[Research]]"
  org: [] # related organizations
  start: # YYYY-MM-DD
  year: # e.g., 2026
  url: # project URL (optional)
  status: # "[[In Progress]]" or "[[Completed]]"
  ```
- **Body:** Progress updates, risks, next actions

### Clipping Notes

- **Trigger:** Saving an article, blog post, or resource worth keeping
- **Where:** `Clippings/` folder
- **Naming:** Use article title (shortened if needed)
- **Required frontmatter:**
  ```yaml
  categories:
    - "[[Clippings]]"
    - "[[Posts]]" # if it's a blog post/article
  author: [] # linked author(s)
  url: "" # source URL (required)
  created: { { date } }
  published: # publication date if available
  topics: [] # relevant topics
  status: [] # "[[Read]]", "[[Unread]]", "[[To-Read]]"
  ```
- **Body:** Summary and key insights

### Evergreen Notes

- **Trigger:** Creating a note with an idea worth remembering long-term
- **Where:** `Notes/` folder (or subfolder)
- **Naming:** Short, declarative title (1-5 words) - "Composable notes"
- **Required frontmatter:**
  ```yaml
  created: { { date } }
  tags:
    - 0🌲 # importance level: 0🌲 (critical), 1🌲, 2🌲, 3🌲 (least)
  ```
- **Body:** Single focused idea, composable with other notes

### Book Notes

- **Trigger:** Recording book information or notes
- **Where:** `References/` folder
- **Naming:** Book title (e.g., `The Phoenix Project.md`)
- **Required frontmatter:**
  ```yaml
  categories:
    - "[[Books]]"
  author: [] # linked author(s)
  cover: # cover image path
  genre: [] # Fiction, Non-fiction, etc.
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
    - to-read # while reading
  ```

### People Template Notes

- For people without meetings: simpler than full meeting template
- Use `People Template.md` with minimal frontmatter

## Template Selection Decision Tree

```
Need a new note?
├─ Is it for today's journal?
│  └─ YES → Daily Note Template
├─ Is it about a person?
│  └─ YES → People Template
├─ Is it about a meeting/conversation?
│  └─ YES → Meeting Template
├─ Is it a project/product?
│  └─ YES → Project Template
├─ Is it an article/resource you're saving?
│  └─ YES → Clipping Template
├─ Is it a focused, lasting idea?
│  └─ YES → Evergreen Template
├─ Is it a book/media item?
│  └─ YES → Specific media template (Book, Movie, Album, etc.)
└─ Is it something else?
   └─ Create custom template or use appropriate category
```

## Important Notes

- Always include `categories:` with at least one category link `[[Category Name]]`
- Use `{{date}}` for auto-filling current date in template fields
- Templates use YAML frontmatter with 2-space indentation
- Files with spaces in name: `"Template Name".md`
- Base templates (`.base` files) are embedded, not used directly

# Linking and Backlink Rules

## Internal Links (`[[...]]`)

Internal links are the primary method of connecting notes in this vault.

### Basic Syntax

```
[[Note Name]]           # Link to note
[[Note Name|Display]]   # Link with custom display text
[[Note Name#Section]]   # Link to heading within note
```

### When to Link

**Always link when mentioning:**

- People (`[[Nguyen Van A]]`)
- Organizations (`[[UEH]]`, `[[Shopee]]`)
- Projects (`[[Hermes]]`, `[[Thesis]]`)
- Topics/Concepts (`[[AI]]`, `[[Supply Chain]]`)
- Books/Movies/Media (`[[The Phoenix Project]]`)
- Previous notes that provide context

**Do NOT link:**

- Common words (the, a, is, etc.)
- Every single mention - be selective
- When the link target doesn't exist yet

### Link Creation

1. **Create note and link simultaneously:**
   - Type `[[New Note Name]]` - red link appears
   - Click to create the note

2. **Link to existing note:**
   - Start typing `[[` - autocomplete shows matching notes
   - Select from dropdown

3. **Using Claude:**
   - Say: "Link this note to [[Project Name]]"
   - Claude will add the link to frontmatter or body

## Backlinks

Backlinks are notes that link TO the current note. Found in the right sidebar.

### Using Backlinks Effectively

1. **Discover related notes:** See what else references this note
2. **Ensure completeness:** Check if new notes should be linked from here
3. **Build graph density:** More backlinks = better connected knowledge

### Backlink Panes

The vault uses specialized backlink panes via `.base` files:

- `Related.base` - Shows notes linked to/from current note
- `Backlinks.base` - Dashboard of all notes with backlinks

## Categories vs Links

**Categories (`categories:` frontmatter):**

- Type classification (People, Projects, Books, Meetings)
- Used by Dataview to generate category dashboards
- Usually 1-2 per note

**Links (`[[...]]` in content):**

- Semantic connections between any notes
- Build the knowledge graph
- Can be many per note

**Example:**

```yaml
categories:
  - "[[Projects]]" # This is the type
  - "[[AI]]" # This is topical
```

Body content:

```
Working on [[Hermes]] with [[AI Agent]] team at [[UEH]].
Reading [[The Phoenix Project]] for inspiration.
Meeting notes: [[2026-05-07 Team Sync]]
```

## Linking Best Practices

1. **Be consistent with names:** Use exact note names
   - `[[AI]]` not `[[Artificial Intelligence]]`
   - `[[Hermes]]` not `[[Hermes Project]]` (unless that's the note name)

2. **Prefer specific links over generic:**
   - `[[Supply Chain Optimization]]` over just `[[SCM]]`
   - `[[Machine Learning]]` over `[[AI]]` when specific

3. **Use alias for display:** When display text differs from note name

   ```
   [[Nguyen Van A|Dr. Nguyen]] - see [[Thesis Proposal]]
   ```

4. **Link in frontmatter OR body, not both:**
   - People/projects: Put in frontmatter `people: [[Name]]`
   - Concepts/references: Put in body

5. **Update links when renaming:** If you rename a note, update all links to it

## Link Maintenance

### Finding Broken Links

Use the "Unlinked mentions" plugin or:

1. Open search (`Ctrl+P` > "Search")
2. Search for `[[]]` with no content (red links)
3. Decide: create the note or remove the link

### Link Density Goal

Aim for:

- Every project note: links to people, orgs, topics
- Every people note: links to meetings, orgs, projects
- Every evergreen: links to related concepts

**Minimum:** Every note should have at least 2-3 internal links.

## MOC (Map of Content) Notes

Create index notes that link to related notes:

```
# AI Topics MOC

## People
- [[AI Researchers]]
- [[ML Engineers]]

## Projects
- [[Hermes]]
- [[Thesis]]

## Concepts
- [[LLM]]
- [[Multi-Agent Systems]]
- [[Prompt Engineering]]
```

Use these as hubs for knowledge areas.

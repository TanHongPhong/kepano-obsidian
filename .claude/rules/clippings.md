# Clippings and Knowledge Capture

This vault uses a structured approach to saving and organizing external content (articles, blog posts, papers).

## What Are Clippings?

Clippings are notes that capture external content you want to keep and reference. Think of them as your personal bibliography with summaries.

## When to Create a Clipping

Create a clipping when you:

- Read an article worth saving
- Find a blog post with valuable insights
- Save a research paper or report
- Want to archive a tutorial or guide
- Capture a news article for future reference

**Do NOT clip:**

- Temporary/sensationalist news
- Low-quality sources
- Things you'll never revisit
- Content behind paywalls you can't access later

## Creating a Clipping Note

1. **Location:** `Clippings/` folder
2. **Template:** `Clipping Template.md`
3. **Naming:** Original title (shortened if >60 chars)
   - Good: `AI in Supply Chain Management.md`
   - Bad: `SomeReallyLongArticleTitleThatGoesOnAndOn.md`

### Clipping Template Frontmatter

```yaml
categories:
  - "[[Clippings]]"
  - "[[Posts]]" # Include if it's a blog post/article
author: [] # Link to author People note (if exists)
url: "" # SOURCE URL (required)
created: { { date } }
published: # Publication date (YYYY-MM-DD)
topics: [] # Topics: [[AI]], [[Supply Chain]], [[Thesis]]
status: [] # [[Read]], [[Unread]], [[To-Read]]
```

## Clipping Body Structure

```markdown
# Article Title

**Source:** [[Author Name]] | [[Publication]]
**Published:** YYYY-MM-DD
**Read:** YYYY-MM-DD

## Summary

2-3 sentence overview of the article's main point.

## Key Insights

- Key takeaway 1
- Key takeaway 2
- Key takeaway 3

## Notable Quotes

> "Direct quote from the article"
> — Author Name

## Connections

- Relates to: [[Hermes]] project
- Supports: [[Thesis]] argument about X
- Contrasts with: [[Another Article]]

## Action Items

- [ ] Apply concept X to project Y
- [ ] Follow up on research Z
```

## Author Notes

If the author doesn't have a People note:

1. Create `References/Author Name.md`
2. Use People Template
3. Link in clipping: `author: [[Author Name]]`

If no People note exists, leave `author: []` empty or just put name as string: `author: "John Doe"`

## Topics and Tags

Use `topics:` to link to topic notes:

```
topics:
  - "[[AI]]"
  - "[[Supply Chain]]"
  - "[[Machine Learning]]"
```

Add tags for quick filtering:

```
tags:
  - to-read      # While you haven't read it
  - research      # Academic/research paper
  - tutorial      # How-to guide
  - #thesis       # Related to your thesis
```

## Status Field

Track reading progress:

| Status            | Meaning             |
| ----------------- | ------------------- |
| `[[To-Read]]`     | Saved, not yet read |
| `[[Unread]]`      | Same as To-Read     |
| `[[Read]]`        | Fully read          |
| `[[In Progress]]` | Partially read      |
| `[[Archived]]`    | Read and filed away |

Update status when you complete reading.

## Published Date

If available, include the original publication date:

```yaml
published: 2024-03-15
```

If unknown, omit the field.

## URL Field

**ALWAYS include the source URL:**

```yaml
url: "https://example.com/article-title"
```

This is critical for:

- Attribution
- Revisiting the original
- Verifying content

## Finding Clippings

### Category Dashboard

`Categories/Clippings.md` shows:

- All clippings
- Sorted by creation date (newest first)
- Author, published date columns

### Search

```
tag:#clippings
categories:[[Clippings]]
author:[[Author Name]]
```

### Filter by Status

```
status:[[To-Read]]     # Read later queue
status:[[Read]]        # Already consumed
```

## Converting Clippings to Evergreen Notes

After reading a clipping, extract the core insight:

1. Create new Evergreen note
2. Write the idea in your own words (don't copy)
3. Link back to the clipping: `Source: [[Article Title]]`
4. Add priority tag `#0🌲`-`#3🌲`
5. Link clipping's `status:` to `[[Read]]` or `[[Archived]]`

## Bibliographies and Citations

For academic work (Thesis):

1. All sources should have clipping notes
2. Use Dataview to generate bibliography:

   ```dataview
   TABLE author, published, url
   FROM "Clippings"
   WHERE topics = [[Thesis]]
   SORT published DESC
   ```

3. Or manually compile from clipping notes

## Clipping Quality Checklist

When creating a clipping, ask:

- [ ] Is the source credible?
- [ ] Is the URL correct and accessible?
- [ ] Have I added `categories: [[Clippings]]`?
- [ ] Have I linked author (if People note exists)?
- [ ] Have I added relevant `topics:` links?
- [ ] Have I set appropriate `status:`?
- [ ] Did I write a summary in my own words?

## Managing Large Clipping Collections

If `Clippings/` grows large:

1. **Archive old clippings:** Move to `Clippings/Archive/` (create folder)
2. **Use tags for filtering:** `#research`, `#tutorial`, `#news`
3. **Review quarterly:** Delete low-value clippings
4. **Link to projects:** Ensure clipping is referenced somewhere

## Integration with Daily Notes

When reading something in a day:

- Mention in Daily note: "Read article [[AI in SCM]]"
- Link to the clipping
- Add brief notes or questions

## PDF Attachments

If clipping refers to a PDF you've saved:

1. Store PDF in `Attachments/PDFs/Papers/`
2. Link in clipping: `![PDF](Attachments/PDFs/Paper.pdf)`
3. Or in body: "See attached: ![[PDFs/Papers/Paper.pdf]]"

## Automated Clipping (Future)

Consider browser extensions:

- Save to Obsidian via URL
- Auto-fetch metadata (author, date)
- But always review and add proper frontmatter

## Clipping Categories

The `Categories/Clippings.md` dashboard includes:

- **All clippings** - Complete list
- **By author** - Filter when viewing author's work
- By custom filters (add as needed)

Use the embedded `Clippings.base` for views.

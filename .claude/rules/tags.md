# Tagging System Rules

## Tag Overview

Tags (`#tagname`) provide lightweight labeling for quick filtering and search. They complement categories and links.

## Tag Hierarchy

The vault uses hierarchical tags with `/` separators:

```
#ai                    # Top-level topic
#ai/llm                # Sub-topic
#ai/agent              # Sub-topic
#scm                   # Supply Chain
#scm/inventory         # Sub-area
#thesis                # Thesis-related
#0🌲                   # Evergreen priority (see below)
#hermes                # Project-specific
#ueh                   # University context
```

## Priority Tags (🌲)

Evergreen notes use emoji priority tags:

| Tag    | Meaning         | Usage                                       |
| ------ | --------------- | ------------------------------------------- |
| `#0🌲` | Critical/Core   | Foundational ideas you reference constantly |
| `#1🌲` | High priority   | Important concepts worth building upon      |
| `#2🌲` | Medium priority | Useful but not essential                    |
| `#3🌲` | Low priority    | Interesting but peripheral                  |

**Guidelines:**

- Use sparingly - most evergreen notes should be `#1🌲` or `#2🌲`
- Reserve `#0🌲` for truly foundational concepts
- Re-evaluate priorities periodically

## Topic Tags

Common topic tags used in this vault:

| Tag          | Description             | Example usage                     |
| ------------ | ----------------------- | --------------------------------- |
| `#ai`        | Artificial Intelligence | AI notes, projects using AI       |
| `#scm`       | Supply Chain Management | SCM topics, thesis area           |
| `#thesis`    | Thesis-related notes    | Notes contributing to thesis      |
| `#hermes`    | Hermes project          | All notes about Hermes            |
| `#ueh`       | UEH University context  | Notes related to studies at UEH   |
| `#daily`     | Daily notes             | Auto-added to daily notes         |
| `#evergreen` | Evergreen notes         | Evergreen content                 |
| `#clippings` | Clippings               | Auto-added from clipping template |
| `#projects`  | Projects                | Auto-added from project template  |
| `#meetings`  | Meetings                | Auto-added from meeting template  |
| `#to-read`   | To be read              | Books/articles pending            |
| `#read`      | Already read            | Completed reading                 |

## When to Use Tags

**Use tags for:**

- Quick filtering in search (`tag:#ai`)
- Priority/status indicators (`#0🌲`, `#to-read`)
- Automatic grouping (`#daily`, `#clippings`)
- Cross-cutting concerns that don't deserve full category

**Avoid tags for:**

- Primary classification (use `categories:` instead)
- Person names (use `[[Person]]` links)
- Project names (use `[[Project]]` links)
- Concepts that deserve their own note

## Tag Best Practices

1. **Lowercase only:** `#MachineLearning` → `#machine-learning` or `#ml`
2. **Hyphens for multi-word:** `#machine-learning` not `#machinelearning`
3. **Be consistent:** Pick one style and stick with it
4. **Use existing tags:** Check tag pane before creating new ones
5. **Limit per note:** 3-5 tags max (beyond that, use categories/links)

## Tag Creation

When you need a new tag:

1. Check if existing tag covers it
2. If new needed, use clear naming
3. Add to notes consistently

## Searching by Tag

- `tag:#ai` - All notes with #ai tag
- `tag:#ai AND tag:#thesis` - AI notes related to thesis
- `-tag:#daily` - Exclude daily notes
- `tag:#0🌲` - Find critical evergreen notes

## Auto-added Tags

Some templates automatically add tags:

| Template            | Auto-added tags                         |
| ------------------- | --------------------------------------- |
| Daily Note Template | `#daily`                                |
| Clipping Template   | `#clippings`                            |
| Project Template    | `#projects`                             |
| Meeting Template    | `#meetings`                             |
| Evergreen Template  | `#evergreen`, `#0🌲` (from frontmatter) |

## Tag Maintenance

Periodically:

1. Review the tag pane for duplicates (e.g., `#AI` vs `#ai`)
2. Merge similar tags using tag rename
3. Remove unused tags
4. Ensure priority tags (`#0🌲`-`#3🌲`) are only on evergreen notes

# Evergreen Notes Rules

Evergreen notes are the foundation of this Second Brain system. They are atomic, composable ideas that last.

## What Are Evergreen Notes?

Evergreen notes are:

- **Atomic:** One idea per note
- **Composable:** Can connect with other notes
- **Permanent:** Meant to last, updated over time
- **Discoverable:** Well-linked, tagged, and categorized

## When to Create an Evergreen Note

Create an evergreen note when you have:

- A concept worth remembering long-term
- An insight from reading/research
- A principle that guides your work
- A synthesized idea from multiple sources
- A "note to self" that you'll reference repeatedly

**Do NOT use evergreen for:**

- Temporary todos (use daily notes or project checklists)
- Meeting notes (use Meeting Template)
- Raw clippings (use Clipping Template first, then extract)
- People or projects (use specific templates)

## Creating an Evergreen Note

1. **Location:** `Notes/` folder (or appropriate subfolder)
2. **Template:** `Evergreen Template.md`
3. **Title:** Short, declarative (2-5 words)

### Template Frontmatter

```yaml
created: { { date } }
tags:
  - 0🌲 # Priority: 0🌲 (critical) to 3🌲 (least)
```

### Priority Tags (`#0🌲` through `#3🌲`)

| Priority | Use for                                  | Frequency               |
| -------- | ---------------------------------------- | ----------------------- |
| `#0🌲`   | Foundational concepts you use constantly | Rare (5-10 notes)       |
| `#1🌲`   | Important working principles             | Common (20-50 notes)    |
| `#2🌲`   | Useful ideas worth keeping               | Most evergreen notes    |
| `#3🌲`   | Interesting but peripheral               | Fillers, minor insights |

## Evergreen Note Title Patterns

**Good titles (atomic, declarative):**

- `Composable Notes`
- `AI Agents Reduce Manual Work`
- `Supply Chain Needs Real-Time Data`
- `Claude Code Accelerates Development`
- `Second Brain Before Building Products`

**Bad titles (too vague or specific):**

- `Notes on AI` (too broad)
- `Meeting with Dr. Nguyen May 7` (specific event)
- `Article I Read Today` (not an idea)
- `Project Hermes` (that's a project note)

## Evergreen Note Structure

After frontmatter, structure varies by content. Common patterns:

### Principle/Insight Pattern

```markdown
# Atomic Notes Are Composable

## Summary

Atomic notes are more valuable because they can be combined in novel ways...

## Reasoning

- Reason 1
- Reason 2

## Examples

- Example 1
- Example 2

## Counter-arguments

- Some argue X, but...

## See Also

- [[Composition over Inheritance]]
- [[Zettelkasten]]
- [[Note-taking Workflow]]
```

### Definition Pattern

```markdown
# Prompt Engineering

## Definition

The practice of designing effective prompts for LLMs to produce desired outputs.

## Key Techniques

- Chain-of-thought
- Few-shot prompting
- Role-based prompts

## Applications

- Code generation
- Content creation
- Data analysis
```

## Linking Evergreen Notes

Evergreen notes should link to:

- **Related concepts:** Other evergreen notes
- **Supporting evidence:** Clippings that inspired them
- **Applications:** Projects that use the idea
- **People:** Who introduced the idea

Example:

```markdown
## See Also

- [[Composable Notes]] (parent concept)
- [[Hermes]] (project using this)
- [[AI in SCM Article]] (source clipping)
- [[Claude Code Best Practices]] (related technique)
```

## Evolving Evergreen Notes

Evergreen notes are NOT static. Update them when:

1. **New evidence:** Add new examples or data
2. **Changed perspective:** Revise conclusions
3. **Better formulation:** Improve clarity and structure
4. **New connections:** Add relevant links

**Update in place** - don't create versioned copies. The note evolves.

## Evergreen Note Quality Checklist

- [ ] Title is atomic (one idea)
- [ ] Has `#0🌲`, `#1🌲`, `#2🌲`, or `#3🌲` tag
- [ ] Explains the idea clearly (not just a title)
- [ ] Links to 2-3 related notes minimum
- [ ] References source material (if applicable)
- [ ] Is discoverable via search (good keywords in content)
- [ ] No orphan notes (everything has backlinks)

## Evergreen vs Other Templates

| Feature     | Evergreen      | Clipping       | Meeting      | Project      |
| ----------- | -------------- | -------------- | ------------ | ------------ |
| Purpose     | Permanent idea | Saved article  | Event record | Work output  |
| Lifespan    | Permanent      | Until consumed | Permanent    | Until done   |
| Structure   | Flexible       | Standardized   | Standardized | Standardized |
| Frontmatter | Minimal        | Detailed       | Detailed     | Detailed     |

## MOC Notes for Evergreen

Create MOC (Map of Content) notes to group evergreen notes by topic:

```
# AI Evergreen Notes

## Concepts
- [[Machine Learning]]
- [[Deep Learning]]
- [[LLM]]

## Applications
- [[AI in Supply Chain]]
- [[Prompt Engineering]]
- [[Multi-Agent Systems]]

## Tools
- [[Claude API]]
- [[Gemini API]]
- [[OpenAI]]

## Related
- [[Hermes]]
- [[Thesis]]
```

## Reviewing Evergreen Notes

### Monthly Review (30 min)

1. Go through recent evergreen notes
2. Add missing links
3. Update tags/priority if needed
4. Check for orphaned notes (no backlinks)

### Quarterly Deep Dive (1 hour)

1. Review all `#0🌲` and `#1🌲` notes
2. Consolidate duplicates
3. Improve formulations
4. Update outdated information

## Evergreen Note Categories

Evergreen notes can be categorized:

- `[[AI]]` - AI/ML evergreen notes
- `[[SCM]]` - Supply Chain evergreen
- `[[Productivity]]` - Workflow/ productivity insights
- `[[Philosophy]]` - Principles, mental models

Use the `Categories/` system to browse evergreen by topic.

## From Daily to Evergreen

The typical flow:

1. Idea emerges in Daily note
2. Create evergreen note with proper structure
3. Link back to daily note as source
4. Add priority tag
5. Reference evergreen from other notes

This creates the knowledge graph.

## Examples from This Vault

Looking at `Notes/AI.md` - this is an evergreen note:

- Atomic topic (AI)
- Structured with sections
- Links to related notes (Hermes, Thesis)
- Gets updated over time

## Common Pitfalls

1. **Creating too many, too fast:** Quality over quantity
2. **Never updating:** Evergreen should evolve
3. **Orphaning:** No links to/from other notes
4. **Vague titles:** "Some thoughts" not useful
5. **Missing tags:** Can't find via `#0🌲`-`#3🌲`

## Tools for Evergreen

- **Template:** `Evergreen Template.md`
- **Priority tags:** `#0🌲` through `#3🌲`
- **Category:** Use appropriate topic category
- **Related dashboard:** `[[Related]]` to find connections

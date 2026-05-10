# People and Organization Rules

This vault uses structured templates for people and organizations. This document covers when and how to create these notes.

## People Notes

### When to Create a People Note

Create a `People` note for:

- Professors, lecturers, academic advisors
- Classmates and study group members
- Mentors and coaches
- Professional contacts (clients, collaborators)
- Family and close friends (if you want to track interactions)

**Do NOT create people notes for:**

- Strangers you briefly interact with
- Historical figures you read about (unless you extensively research)
- Public figures (use existing sources, not personal notes)

### Creating a People Note

1. **Location:** `References/` folder
2. **Filename:** Full name (e.g., `Nguyen Van A.md`)
3. **Template:** `People Template.md`

### People Template Frontmatter

```yaml
categories:
  - "[[People]]"
birthday: 1990-05-15 # Optional, format: YYYY-MM-DD
org: [] # Organizations they're affiliated with
created: { { date } }
```

### People Note Body

After frontmatter, typical sections:

```markdown
# Nguyen Van A

## Thông Tin

- **Vai trò:** Giảng viên tại [[UEH]]
- **Bộ môn:** Supply Chain Management
- **Email:** nguyenvana@ueh.edu.vn

## Meetings

![[Meetings.base#Person]]

## Notes

- Met on 2026-05-07 to discuss [[Hermes]] project
- Suggested focusing on [[Supply Chain Optimization]] use cases
```

**Key:**

- `org:` in frontmatter links to organization notes (`[[UEH]]`)
- Meetings section embeds `Meetings.base#Person` view (auto-lists meetings with this person)
- Notes section for free-form observations

### Linking to People

From other notes:

```yaml
people:
  - "[[Nguyen Van A]]"
```

In body:

```
Discussing with [[Nguyen Van A]] about [[Thesis]] topic.
Meeting: [[2026-05-07 Meeting with Dr. Nguyen]]
```

## Organization Notes

### When to Create an Organization Note

Create for:

- Universities (`[[UEH]]`)
- Companies (employers, clients)
- Research labs
- Non-profits you're involved with
- Projects that function as organizations

### Creating an Organization Note

**Template:** Use `Company Template.md` (works for any org)

```yaml
categories:
  - "[[Companies]]"
type: [] # [[University]], [[Client]], [[Startup]]
people: [] # People affiliated (links)
url: "" # Website
```

Body:

```markdown
# UEH

## Thông Tin

- **Loại:** Đại học
- **Website:** https://ueh.edu.vn

## People

![[People.base]]

## Projects

- [[Hermes]] - AI Bot ecosystem
```

### Organization Types

Use `type:` with appropriate link:

- `[[University]]` - Academic institutions
- `[[Client]]` - Client companies (freelance)
- `[[Employer]]` - Current/past employers
- `[[Startup]]` - Startup companies
- `[[Non-profit]]` - NGOs, non-profits

## Linking People and Organizations

**From People note:**

```yaml
org:
  - "[[UEH]]"
```

**From Organization note:**

```yaml
people:
  - "[[Nguyen Van A]]"
  - "[[Tran Thi B]]"
```

This creates bidirectional relationships visible in backlinks.

## Category Dashboards

- `Categories/People.md` - All people, sorted, with age calculation
- `Categories/Companies.md` - All organizations

## Places Notes

For geographic locations:

```yaml
categories:
  - "[[Places]]"
type:
  - "[[Cities]]" # or [[Country]], [[Venue]], [[Landmark]]
loc: # Coordinates for map view [lat, lng]
rating:
created: { { date } }
last: { { date } } # Last visit/update
```

Places support map visualization via `Map.base` dashboard.

## People Best Practices

1. **Create note first, then link:** Create `Nguyen Van A.md` before linking
2. **Use consistent name:** Stick to one format (`Nguyen Van A` not `Dr. Nguyen`)
3. **Fill basic info:** At minimum, add `org:` link
4. **Link meetings:** Meeting templates include `people:` field
5. **Birthday privacy:** Only include if comfortable; used for age calculation

## People/Org Checklist

When creating a people/organization note:

- [ ] Created in `References/` folder
- [ ] Used correct template
- `categories:` includes `[[People]]` or `[[Companies]]`
- [ ] `created:` date filled
- [ ] `org:` (for people) or `type:` (for orgs) filled
- [ ] At least one section in body with details
- [ ] Links to related notes added

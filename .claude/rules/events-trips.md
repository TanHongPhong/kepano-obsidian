# Events, Trips, and Time-Based Notes Rules

This vault has templates for events, trips, and other time-based occurrences. These notes capture experiences that happen at specific times/locations.

## Event Notes

### When to Use Event Template

Use `Event Template.md` for:

- Concerts, performances
- Conferences, workshops
- Social gatherings
- One-time occasions

**Do NOT use for:**

- Recurring meetings (use Meeting Template)
- Long-term projects (use Project Template)
- Daily activities (use Daily notes)

### Event Frontmatter

```yaml
categories:
  - "[[Events]]"
type: [] # e.g., "[[Concert]]", "[[Conference]]"
start: # YYYY-MM-DD (required)
end: # YYYY-MM-DD (if multi-day)
loc: [] # Location (links to Places notes)
```

### Event Body

```markdown
# Event Name

## Details

- **Type:** Concert / Conference / Social
- **Date:** May 15-17, 2026
- **Location:** [[Ho Chi Minh City]]

## Attendees

- [[Alice]]
- [[Bob]]

## Notes

- Key takeaways
- Memorable moments
- Photos (attach in Attachments/)

## Follow-up

- [ ] Send thank you notes
- [ ] Share photos
```

## Trip Notes

### When to Use Trip Template

Use `Trip Template.md` for:

- Vacations
- Business travel
- Multi-day journeys
- Study abroad

### Trip Frontmatter

```yaml
categories:
  - "[[Trips]]"
start: 2026-06-01 # Required
end: 2026-06-07 # Required
loc: [] # Destination (Places links)
```

### Trip Body Structure

```markdown
# Trip to [Destination]

## Overview

- **Dates:** June 1-7, 2026
- **Purpose:** Vacation / Conference / Research
- **Companions:** [[Alice]], [[Bob]]

## Itinerary

### Day 1 (2026-06-01)

- Arrival
- Check-in
- Evening activity

### Day 2 (2026-06-02)

- Morning activity
- Afternoon activity

## Highlights

- Most memorable experiences
- Photos (link attachments)

## Expenses

| Item   | Cost (VND) |
| ------ | ---------- |
| Flight | 5,000,000  |
| Hotel  | 8,000,000  |

## Notes for Future

- Tips for next visit
- Places to revisit
```

### Trip Dashboard

`Categories/Trips.md` (or use Places with trips view):

- Shows all trips sorted by end date
- Filter by location
- Duration calculated from start/end

## Event vs Trip vs Meeting

| Type        | Duration          | Primary Purpose       | Template |
| ----------- | ----------------- | --------------------- | -------- |
| **Meeting** | Usually 1-2 hours | Discussion/decision   | Meeting  |
| **Event**   | Hours to 1 day    | Experience/attendance | Event    |
| **Trip**    | 2+ days           | Travel/journey        | Trip     |
| **Project** | Weeks-months      | Deliverable output    | Project  |

## Places Integration

Both Events and Trips link to Places:

1. **Create Places note first:**

   ```yaml
   categories:
     - "[[Places]]"
   type:
     - "[[Cities]]" # or [[Venue]], [[Landmark]]
   loc: [10.762622, 106.660172] # GPS coordinates
   ```

2. **Link from Event/Trip:**

   ```yaml
   loc:
     - "[[Ho Chi Minh City]]"
   ```

3. **Benefits:**
   - Map view via `Map.base`
   - All events at a location visible in Place note
   - Geographic organization

## Type Field

Use `type:` for subcategorization:

**Events:**

- `[[Concert]]`
- `[[Conference]]`
- `[[Workshop]]`
- `[[Social]]`
- `[[Ceremony]]`

**Trips:**

- `[[Vacation]]`
- `[[Business]]`
- `[[Study]]`
- `[[Family]]`

Create these type notes in `Categories/` if needed (similar to Meeting Type Template).

## Date Fields

- `start:` - Start date/time (required)
- `end:` - End date/time (for multi-day events)

Format: `YYYY-MM-DD` or `YYYY-MM-DD HH:mm`

## Location Field

`loc:` expects an array of place links:

```yaml
loc:
  - "[[Ho Chi Minh City]]"
  - "[[UEH Campus]]" # Venue within city
```

If multiple locations (multi-city trip), list all.

## Linking Events/Trips

Link events/trips to:

- **People:** Who attended (`[[Alice]]` in body or `people:` in frontmatter)
- **Projects:** If event relates to a project
- **Clippings:** After-action reports, photos
- **Evergreen:** Lessons learned (create evergreen from experience)

Example:

```markdown
## See Also

- [[Hermes]] demo at this conference
- [[AI in Vietnam]] - topic learned about
- [[Conference Reflections]] - evergreen note on conferences
```

## Dashboard Views

### Events by Type

Use `Events.base#Type` embedded view in Event category note.

### Events by Location

Use `Events.base#Location` to see all events at a place.

### Upcoming Events

Create custom Dataview:

````
```dataview
TABLE start, loc
FROM "Notes"
WHERE categories = [[Events]]
AND start >= date(today)
SORT start ASC
````

````

## Templates Available

| Template | For | Category |
|----------|-----|----------|
| `Event Template.md` | Single events | Events |
| `Trip Template.md` | Multi-day travel | Trips |
| `Conference Session Template.md` | Conference sub-sessions | Meetings |

## Best Practices

1. **Always link Places:** Even if approximate
2. **Include date range:** For trips, both start and end
3. **Add attendees:** Link people who were there
4. **Take photos:** Store in `Attachments/` and link
5. **Write notes soon:** While experience is fresh
6. **Extract evergreen:** Convert lessons to evergreen notes

## Examples

**Concert:**
```yaml
categories:
  - "[[Events]]"
type:
  - "[[Concert]]"
start: 2026-07-15
end: 2026-07-15
loc:
  - "[[Arena HCMC]]"
````

**Conference:**

```yaml
categories:
  - "[[Events]]"
type:
  - "[[Conference]]"
start: 2026-08-01
end: 2026-08-03
loc:
  - "[[Saigon Exhibition Center]]"
```

**Vacation:**

```yaml
categories:
  - "[[Trips]]"
type:
  - "[[Vacation]]"
start: 2026-12-20
end: 2027-01-05
loc:
  - "[[Japan]]"
  - "[[Tokyo]]"
  - "[[Kyoto]]"
```

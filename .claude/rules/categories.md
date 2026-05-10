# Categories Organization Rules

## Category Structure

The vault uses category notes (in `Categories/`) to organize content using Dataview-powered dashboards. Each category is a note that embeds a `.base` file to provide a table view of all notes in that category.

## Available Categories

These categories are defined in `Categories/` and should be used as frontmatter `categories:` values:

| Category               | Purpose                    | Typical Location | Base Template         |
| ---------------------- | -------------------------- | ---------------- | --------------------- |
| `[[AI]]`               | AI/ML topics, LLMs, agents | Notes/           | N/A                   |
| `[[Albums]]`           | Music albums               | References/      | Albums.base           |
| `[[Attachments]]`      | File attachments           | Attachments/     | Attachments.base      |
| `[[Backlinks]]`        | Notes with many backlinks  | -                | Backlinks.base        |
| `[[Board games]]`      | Board game records         | References/      | Board games.base      |
| `[[Books]]`            | Books read/reading         | References/      | Books.base            |
| `[[Clippings]]`        | Saved articles/excerpts    | Clippings/       | Clippings.base        |
| `[[Companies]]`        | Organizations/companies    | References/      | Companies.base        |
| `[[Daily]]`            | Daily notes                | Daily/           | Daily.base            |
| `[[Everything]]`       | All notes overview         | -                | Everything.base       |
| `[[Events]]`           | Events/occasions           | Notes/           | Events.base           |
| `[[Evergreen]]`        | Evergreen/atomic notes     | Notes/           | Evergreen.base        |
| `[[Evidence]]`         | Portfolio/evidence         | Notes/Projects   | Evidence.base         |
| `[[Games]]`            | Video games                | References/      | Games.base            |
| `[[Genre]]`            | Media genres               | References/      | Genre.base            |
| `[[Journal]]`          | Journal entries            | Notes/           | Journal.base          |
| `[[Map]]`              | Geographic/place data      | References/      | Map.base              |
| `[[Meetings]]`         | Meeting notes              | Notes/           | Meetings.base         |
| `[[Movies]]`           | Movies                     | References/      | Movies.base           |
| `[[Partners]]`         | Romantic partners          | References/      | (custom)              |
| `[[People]]`           | Individuals                | References/      | People.base           |
| `[[Places]]`           | Locations                  | References/      | Places.base           |
| `[[Podcast episodes]]` | Individual episodes        | References/      | Podcast episodes.base |
| `[[Podcasts]]`         | Podcast shows              | References/      | Podcasts.base         |
| `[[Posts]]`            | Blog posts/articles        | Clippings/       | Posts.base            |
| `[[Products]]`         | Physical products          | References/      | Products.base         |
| `[[Projects]]`         | Active projects            | Notes/Projects/  | Projects.base         |
| `[[Quotes]]`           | Memorable quotes           | References/      | (custom)              |
| `[[Ratings]]`          | Rating scales              | -                | Ratings.base          |
| `[[Recipes]]`          | Cooking recipes            | References/      | Recipes.base          |
| `[[Related]]`          | Related notes linkage      | -                | Related.base          |
| `[[Shows]]`            | TV shows                   | References/      | Shows.base            |
| `[[Templates]]`        | Template files             | Templates/       | Templates.base        |
| `[[Thesis]]`           | Thesis/long-form research  | Notes/Projects/  | (custom)              |
| `[[Tips]]`             | Tips/quick advice          | Notes/           | (custom)              |
| `[[Trips]]`            | Travel/trips               | References/      | Trips.base            |
| `[[UEH]]`              | University specific        | Notes/           | (custom)              |
| `[[Videos]]`           | Videos/YouTube             | References/      | (custom)              |
| `[[Weekly]]`           | Weekly reviews             | Daily/           | (custom)              |

## How Categories Work

Each category note (e.g., `Categories/People.md`) embeds a `.base` file:

```markdown
---
tags:
  - categories
---

![[People.base]]
```

The `.base` file contains Dataview configuration:

- **filters:** Which files belong to this category
- **properties:** Which frontmatter fields to display
- **views:** Table/card layouts for browsing

## Using Categories in Notes

Add categories to a note's frontmatter:

```yaml
categories:
  - "[[People]]" # Primary category (required)
  - "[[UEH]]" # Secondary/topical category (optional)
```

### Multiple Categories

Notes can have multiple category links. Common combinations:

- People + Organizations: `[[People]], [[UEH]]`
- Projects + Topics: `[[Projects]], [[AI]]`
- Books + Genres: `[[Books]], [[Science Fiction]]`

## Category Rules

1. **One primary category per note** - The first category should be the "type" of note
2. **Secondary categories** are topical (AI, UEH, Thesis) or contextual
3. **Categories are notes themselves** - `[[Category Name]]` must link to an existing note
4. **Create category notes first** if they don't exist in `Categories/`
5. **Category naming** matches the template's category field exactly

## Base Templates vs Full Templates

- **Base templates** (`.base`) - Reusable dashboard components, embedded in category notes
- **Full templates** (`.md`) - Used to create new notes with complete frontmatter

When creating a note, use the Full Template, not the base. The category note embeds the base for browsing.

## Custom Categories

If you need a new category:

1. Create the category note in `Categories/` (e.g., `Categories/AI.md`)
2. Choose or create a `.base` template file in `Templates/Bases/`
3. Embed the base: `![[AI.base]]`
4. Add category to template frontmatter as needed

## Category Dashboard Access

Access category views via:

1. Navigate to `Categories/` folder
2. Click on category note (e.g., `People.md`)
3. See all notes in that category via embedded Dataview table

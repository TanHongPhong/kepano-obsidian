# Media Templates (Books, Movies, Music, etc.)

This vault includes specialized templates for various media types. Use these when cataloging entertainment media.

## Available Media Templates

| Template                      | Category               | Base Template         | Typical Location |
| ----------------------------- | ---------------------- | --------------------- | ---------------- |
| `Book Template.md`            | `[[Books]]`            | Books.base            | `References/`    |
| `Movie Template.md`           | `[[Movies]]`           | Movies.base           | `References/`    |
| `Album Template.md`           | `[[Albums]]`           | Albums.base           | `References/`    |
| `Video Game Template.md`      | `[[Games]]`            | Games.base            | `References/`    |
| `TV Show Template.md`         | `[[Shows]]`            | Shows.base            | `References/`    |
| `Podcast Template.md`         | `[[Podcasts]]`         | Podcasts.base         | `References/`    |
| `Podcast Episode Template.md` | `[[Podcast episodes]]` | Podcast episodes.base | `References/`    |
| `Recipe Template.md`          | `[[Recipes]]`          | Recipes.base          | `References/`    |
| `Board Game Template.md`      | `[[Board games]]`      | Board games.base      | `References/`    |

## Common Fields by Media Type

### Books

```yaml
categories:
  - "[[Books]]"
author: [] # Linked author notes
cover: "" # Cover image path
genre: [] # Fiction, Non-fiction, Biography, etc.
pages:
isbn:
isbn13:
year:
rating: # 1-5 or 1-10 scale
topics: [] # [[AI]], [[Supply Chain]], etc.
created: { { date } }
last: # Last read date
via: "" # How discovered (recommendation, etc.)
tags:
  - to-read # While reading
```

**Usage notes:**

- Create author notes first: `References/Author Name.md` using People Template
- Add `cover:` with relative path: `"Covers/Book Title.jpg"`
- Update `last:` when you finish or revisit

### Movies

```yaml
categories:
  - "[[Movies]]"
director: [] # Linked director note(s)
cast: [] # Linked actor notes
genre: [] # Action, Drama, Sci-Fi, etc.
year:
rating: # Personal rating 1-10
scoreImdb: # IMDb rating
scoreRT: # Rotten Tomatoes %
runtime: # In minutes
watchlist: # Date added to watchlist
last: # Date watched
plot: "" # Short summary (optional)
```

**Special views in Movies.base:**

- **To-watch:** Movies with no rating/last date
- **Favorites:** Rating > 6
- **Last seen:** Recently watched
- **Actor/Genre/Director:** Filtered by linked person/genre

### Albums (Music)

```yaml
categories:
  - "[[Albums]]"
artist: [] # Linked artist note
genre: [] # Rock, Pop, Classical, etc.
year:
rating:
created: # Date added to collection
tracks: # Track listing (optional)
```

### Video Games

```yaml
categories:
  - "[[Games]]"
maker: # Developer/Publisher
genre: [] # RPG, Strategy, Action, etc.
system: # Platform (PC, PS5, Switch)
year:
rating:
created: { { date } }
last: { { date } } # Last played
```

### TV Shows

```yaml
categories:
  - "[[Shows]]"
creator: [] # Linked creator(s)
cast: [] # Main actors
genre: [] # Drama, Comedy, etc.
year:
rating:
status: # [[Watching]], [[Completed]], [[Plan to Watch]]
last: # Last episode watched/season
episodes: # Total episodes
seasons: # Number of seasons
```

### Podcasts

**Show note:**

```yaml
categories:
  - "[[Podcasts]]"
host: [] # Linked host(s)
genre: [] # Tech, Education, Comedy
episodes: # Episode count (approximate)
last: # Date of last episode heard
```

**Episode note:**

```yaml
categories:
  - "[[Podcast episodes]]"
show: "[[Podcast Name]]" # Link to parent show
episode: # Episode number or title
guest: [] # Guest(s) if notable
topics: [] # Topics covered
date: # Publication date
duration: # Approx. minutes
```

### Recipes

```yaml
categories:
  - "[[Recipes]]"
cuisine: # Italian, Vietnamese, etc.
course: # Appetizer, Main, Dessert
prep-time: # Minutes
cook-time:
total-time:
servings:
ingredients: |
  - ingredient 1
  - ingredient 2
instructions: |
  1. Step one
  2. Step two
source: "" # URL or book reference
rating: # 1-5 stars
tags:
  - vegetarian # Dietary tags as needed
```

### Board Games

```yaml
categories:
  - "[[Board games]]"
designer: [] # Game designer
publisher: # Publishing company
genre: [] # Strategy, Party, Cooperative
year:
players: # "2-4"
playtime: # Minutes
rating:
complexity: # 1-5 (BGG scale)
```

## Creating Media Notes

1. **Create the note in `References/` folder**
2. **Select appropriate template**
3. **Fill frontmatter completely:**
   - Required fields vary by template
   - All need `categories:` with correct link
   - Link to people (directors, authors, artists) when possible
4. **Add body content:**
   - Summary/review
   - Notable quotes (books/movies)
   - Track listings (albums)
   - Personal reflections

## Linking Media

Media notes can link to:

- **People:** Directors, authors, artists, actors (link to People notes)
- **Topics:** `[[AI]]`, `[[Supply Chain]]` if relevant to your interests
- **Projects:** If media relates to a project
- **Other media:** Sequels, adaptations, related works

## Rating Consistency

Use consistent scales:

- **1-10:** Movies, Games, Albums
- **1-5:** Books, Recipes, Board Games
- Or whatever you prefer - but be consistent within each category

## Category Dashboards

Each media category has a dashboard in `Categories/`:

- `Categories/Movies.md` - All movies with filters (to-watch, favorites, by director/genre)
- `Categories/Books.md` - Reading lists, by author, by genre
- `Categories/Albums.md` - Music collection
- etc.

Access via the `Categories/` folder in Obsidian.

## Watchlists/Reading Lists

Use the category dashboards' filtered views:

- **Movies:** "To-watch" filter in Movies.base
- **Books:** Filter by `tags: to-read`
- **Games:** Custom query for "Plan to Play"

Create a MOC note for your current watchlist/backlog if needed:

```
# Entertainment Backlog

## To Watch
- [[Movie 1]]
- [[Movie 2]]

## To Read
- [[Book 1]]
```

## Attachments for Media

Store cover art, posters, etc. in:

```
Attachments/Media/Movies/[Movie Title].jpg
Attachments/Media/Books/[Book Title].jpg
```

Reference in frontmatter: `cover: "Attachments/Media/Movies/Inception.jpg"`

# Dataview Usage Rules

This vault uses the Dataview plugin extensively for dynamic dashboards and queries. All `.base` files and category notes use Dataview JS.

## Dataview Basics

### Query Types

1. **Dataview JS (inline JavaScript):**

   ````javascript
   ```dataviewjs
   dv.table(["File", "Size"], files)
     .where(f => f.extension === "md")
   ````

   ```

   ```

2. **Dataview (YAML-like):**

   ````
   ```dataview
   TABLE file.name AS File, file.size AS Size
   FROM "Notes"
   WHERE status = "In Progress"
   ````

   ```

   ```

This vault primarily uses **Dataview JS** in `.base` files.

### Common Patterns

#### Basic Table Query

```javascript
dv.table(["Column1", "Column2"], collection);
```

#### FROM with path

```javascript
dv.pages('"Notes/Projects"'); // Pages from Projects folder
dv.pages('"Notes" OR "Clippings"'); // Multiple sources
```

#### WHERE filter

```javascript
.where(p => p.type && p.type.includes("AI"))
.where(p => p.status === "In Progress")
.where(p => p.rating > 3)
```

#### SORT

```javascript
.sort(p => p.file.name, "asc")
.sort(p => p.date, "desc")
```

#### LIMIT

```javascript
.limit(10)
```

#### GROUP BY

```javascript
.groupBy(p => p.type)
```

## Standard Queries Used in This Vault

### Projects Overview (Projects.base)

```javascript
dv.table(
  ["Dự án", "Trạng thái", "Ngày bắt đầu", "Tổ chức"],
  dv
    .pages('"Notes/Projects"')
    .where((p) => p.file.name != this.file.name)
    .sort((p) => p.start, "desc"),
);
```

### People List (People.base)

```javascript
dv.table(
  ["Name", "Tags", "Birthday", "Age"],
  dv
    .pages('"References"')
    .where((p) => p.categories && p.categories.includes(link("People")))
    .sort((p) => p.file.name, "asc")
    .sort((p) => p.birthday, "desc"),
);
```

### Meetings View (Meetings.base)

```javascript
dv.table(
  ["Meeting", "Date", "Person", "Type", "Org"],
  dv
    .pages('"Notes"')
    .where((p) => p.categories && p.categories.includes(link("Meetings")))
    .where((p) => !p.file.name.includes("Template"))
    .sort((p) => p.date, "asc"),
);
```

### Clippings View (Clippings.base)

```javascript
dv.table(
  ["Title", "Author", "Clipped", "Published"],
  dv
    .pages('"Clippings"')
    .where((p) => p.categories && p.categories.includes(link("Clippings")))
    .sort((p) => p.created, "desc"),
);
```

### Related Notes (Related.base)

```javascript
const related = dv
  .current()
  .file.links.map((l) => dv.page(l.link.path))
  .filter((p) => p && !p.file.name.includes(this.file.name));

dv.table(["Name", "Tags", "Links overlap"], related);
```

## Frontmatter Properties Available

Dataview can access these fields:

| Property        | Source                         | Example                      |
| --------------- | ------------------------------ | ---------------------------- |
| `file.name`     | Filename                       | `"Hermes"`                   |
| `file.path`     | Full path                      | `"Notes/Projects/Hermes.md"` |
| `file.tags`     | YAML tags                      | `["ai", "thesis"]`           |
| `file.cTime`    | Creation time                  | `date` object                |
| `file.mTime`    | Modification time              | `date` object                |
| Category fields | `categories`, `type`, `status` | Links array                  |
| Custom fields   | Whatever's in frontmatter      | `p.rating`, `p.org`          |

## Link Functions

### `link("Note Name")`

Creates a link object for comparison:

```javascript
p.categories.includes(link("People"));
```

### `this.file.name`

The current file's name (in `.base` context).

## Creating New Queries

### Step 1: Define collection

```javascript
const pages = dv.pages('"Folder"');
// OR
const pages = dv
  .current()
  .file.links.map((l) => dv.page(l.link.path))
  .filter((p) => p);
```

### Step 2: Filter

```javascript
const filtered = pages.where(
  (p) =>
    p.categories &&
    p.categories.includes(link("Projects")) &&
    p.status === "In Progress",
);
```

### Step 3: Sort

```javascript
const sorted = filtered.sort((p) => p.start, "desc");
```

### Step 4: Display

```javascript
dv.table(["Name", "Status", "Start"], sorted).limit(20);
```

## Common Pitfalls

1. **Path must match exactly:**

   ```
   dv.pages('"Notes/Projects"')  // Correct
   dv.pages('Notes/Projects')    // Wrong - needs quotes
   ```

2. **Check for undefined:**

   ```javascript
   .where(p => p.type && p.type.includes("AI"))  // Safe
   .where(p => p.type.includes("AI"))            // May error if type is undefined
   ```

3. **Exclude templates:**

   ```javascript
   .where(p => !p.file.name.includes("Template"))
   ```

4. **Exclude self in `.base` files:**
   ```javascript
   .where(p => p.file.name != this.file.name)
   ```

## Dashboard Templates

Use these standard patterns when creating category dashboards:

```javascript
---
tags:
  - categories
---

![[Category.base]]
```

Then in `Category.base`:

```javascript
dv.table(
  ["Name", "Status", "Date"],
  dv
    .pages('"Folder"')
    .where((p) => p.categories && p.categories.includes(link("Category")))
    .where((p) => !p.file.name.includes("Template"))
    .sort((p) => p.date || p.file.mtime, "desc"),
);
```

## Debugging Queries

If a query isn't working:

1. **Check the console:** `Ctrl+Shift+I` for errors
2. **Test with `console.log`:**
   ```javascript
   console.log(dv.pages().length);
   console.log(dv.current().file);
   ```
3. **Verify paths:** Use exact folder names
4. **Check frontmatter:** Missing fields cause `undefined`

## Performance Tips

1. **Limit results:** `.limit(50)` for large vaults
2. **Filter early:** Put most restrictive `.where()` first
3. **Cache reference:** Store `dv.current()` in variable if used multiple times
4. **Avoid nested loops:** Use `map()` and `filter()` efficiently

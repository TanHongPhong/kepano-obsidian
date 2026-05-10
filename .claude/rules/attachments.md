# Attachment Handling Rules

Attachments are files embedded in notes: images, PDFs, audio, etc. This vault has specific conventions.

## Attachment Location

All attachments go in: `Attachments/`

### Subfolder Structure

Organize attachments by type/date:

```
Attachments/
├── Images/
│   ├── Covers/           # Book/movie covers
│   ├── Diagrams/         # Flowcharts, diagrams
│   └── Screenshots/
├── PDFs/
│   ├── Papers/
│   └── Forms/
├── Audio/
│   ├── Recordings/
│   └── Podcasts/
└── [date-based folders]  # Optional, e.g., 2026-05/
```

## Naming Attachments

Use clear, descriptive names:

```
Book Cover - The Phoenix Project.jpg  # Good
IMG_1234.jpg                          # Bad (unclear)
Screenshot 2026-05-07.png             # Good (with date)
```

**Avoid:**

- Spaces (use hyphens): `book-cover.jpg` not `book cover.jpg`
- Special characters: `? * < > |`
- Very long names (>50 chars)

## Inserting Attachments

### Drag and Drop

1. Drag file from file explorer into Obsidian
2. Drop into note or attachment pane
3. Obsidian copies to `Attachments/` and creates link

### Copy-Paste

1. Copy image to clipboard
2. `Ctrl+V` in note
3. Obsidian prompts for save location (default: `Attachments/`)

### Manual Copy

1. Copy file to `Attachments/` folder manually
2. Create link: `![[filename.jpg]]`

## Linking Attachments

### Embedded Display

```
![Alt text](Attachments/filename.jpg)
```

or Obsidian's native: `![[filename.jpg]]`

### As Link

```
[[Attachments/filename.pdf]]
```

## Frontmatter Attachment Fields

Many templates have attachment fields:

```yaml
cover: "Attachments/Covers/Book Title.jpg"
avatar: "Attachments/People/Name.jpg"
evidence: "Attachments/Portfolio/project-screenshot.png"
```

**Rules:**

1. Use relative path from vault root
2. Always quote the path
3. Put attachments in subfolder (not root `Attachments/`)

## Attachment Management

### Finding Unused Attachments

Use `Attachments.base` dashboard:

- Shows attachments with no backlinks
- Identify orphaned files to delete

### Cleaning Up

When deleting notes:

1. Check if attachments were only used there
2. Delete orphaned attachments manually or via plugin

### File Types Supported

Obsidian can embed:

- **Images:** PNG, JPG, GIF, WebP, AVIF, SVG
- **Audio:** MP3, WAV, OGG
- **Video:** MP4, WebM
- **PDFs:** Embedded viewer
- **Others:** Links only

## Best Practices

1. **Compress images** before inserting (use TinyPNG, etc.)
2. **Use consistent naming** across attachments
3. **Organize by project/category** if vault grows large
4. **Check attachment size** - large files bloat vault
5. **Back up attachments** separately if they're important

## Embedding in Templates

Templates can reference base template for attachment management:

```markdown
---
cover: "Attachments/Covers/{{title}}.jpg"
---

![[Attachments.base]]
```

## Troubleshooting

**Attachment not showing:**

- Check file path is correct
- Verify file exists in `Attachments/`
- Check file permissions (readable)

**Broken image after moving:**

- Obsidian doesn't auto-update attachment links
- Use find/replace to update paths

**Vault getting large:**

- Check `Attachments/` for large files
- Consider moving media to external folder or cloud storage

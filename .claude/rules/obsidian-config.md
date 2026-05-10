# Obsidian Configuration Rules

This document covers the Obsidian configuration in `.obsidian/` and how to maintain it.

## Configuration Files

The `.obsidian/` folder stores vault settings in JSON format.

### Key Configuration Files

| File                     | Purpose                    | When to Edit                         |
| ------------------------ | -------------------------- | ------------------------------------ |
| `app.json`               | General app settings       | Attachment folder, auto-update links |
| `appearance.json`        | Theme and appearance       | Theme, mode (light/dark)             |
| `core-plugins.json`      | Core plugin enable/disable | Enable/disable core features         |
| `community-plugins.json` | Community plugins list     | Add/remove community plugins         |
| `daily-notes.json`       | Daily notes config         | Folder, template, format             |
| `templates.json`         | Template settings          | Template folder location             |
| `workspace.json`         | UI layout                  | Panes, splits (usually don't edit)   |
| `zk-prefixer.json`       | ZK prefixer settings       | Note naming prefixes                 |

### DO NOT Edit These Directly

- `workspace.json` - Auto-generated UI state
- `graph.json` - Graph view settings (use UI instead)
- Plugin data in `.obsidian/plugins/` - Use plugin UI

### Safe to Edit

- `app.json`
- `appearance.json`
- `core-plugins.json`
- `community-plugins.json`
- `daily-notes.json`
- `templates.json`

## Current Configuration

### Appearance

- **Theme:** Minimal (by KEPANO)
- **Mode:** System (follows OS dark/light)

### Core Plugins (Enabled)

File-explorer, global-search, switcher, graph, backlink, outline, tag-pane, page-preview, daily-notes, templates, note-composer, command-palette, editor-status, markdown-importer, zk-prefixer, random-note, workspace, file-recovery, canvas, bookmarks, bases, webviewer

**Disabled:**

- slash-command
- word-count
- slides
- audio-recorder
- publish
- sync
- properties
- footnotes
- bases (check current)

### Community Plugins

1. **obsidian-hider** - Hide UI elements for cleaner interface
2. **obsidian-minimal-settings** - Extended Minimal theme configuration

### Daily Notes

- **Folder:** `Daily/`
- **Template:** `Templates/Daily Note Template.md`
- **Format:** `YYYY-MM-DD` (auto-generated)

### Templates

- **Folder:** `Templates/`
- **Hotkey:** `Ctrl+P` > "Templates: Insert template"

### Attachments

- **Folder:** `Attachments/`
- **Auto-update links:** `true` - When you move/rename files, links update

## Editing Configuration

### Enable/Disable Core Plugin

Edit `.obsidian/core-plugins.json`:

```json
{
  "file-explorer": true,
  "global-search": true,
  "switcher": true,
  "graph": false, // Disable graph view
  "backlink": true,
  "tag-pane": true
}
```

**Restart Obsidian** after changes.

### Change Daily Notes Location

Edit `.obsidian/daily-notes.json`:

```json
{
  "folder": "Journal", // Change from Daily/
  "template": "Templates/Journal Template.md",
  "format": "YYYY-MM-DD"
}
```

### Change Theme

Edit `.obsidian/appearance.json`:

```json
{
  "cssTheme": "Minimal", // or "Atom", "Anu-puh", etc.
  "theme": "dark" // "light", "dark", or "system"
}
```

## Plugin Management

### Install Community Plugin

1. Open Settings → Community plugins
2. Turn on "Safe mode" OFF
3. Browse → Find plugin → Install
4. Enable plugin

OR manually:

1. Download plugin to `.obsidian/plugins/`
2. Add plugin ID to `community-plugins.json`
3. Enable in Settings → Community plugins

### Configure Plugin

Each plugin has its own settings in Settings → Plugin name. Some store data in `.obsidian/plugins/[plugin-name]/`.

## Recommended Settings

### For This Vault

1. **Daily notes:** Keep enabled, configured as above
2. **Templates:** Keep enabled, folder at `Templates/`
3. **zk-prefixer:** Custom prefix for note naming (check `zk-prefixer.json`)
4. **Outline:** Enable for note navigation sidebar
5. **Bases:** Dataview plugin must be installed for `.base` files to work

### Safe to Disable

- `graph` - If you don't use graph view
- `random-note` - If not using random note feature
- `page-preview` - If previews slow down performance

## ZK-Prefixer

The `zk-prefixer.json` configures note naming prefixes:

```json
{
  "format": "YYYY-MM-DD HHmm",
  "folder": "/",
  "template": "Templates/Journal Template"
}
```

This is used for quick note creation with timestamp prefixes.

## Sync Settings

**Do not enable** Obsidian Sync or Publish for this vault (see `app.json` - sync and publish are false).

## Migrating Configuration

To move this vault to another computer:

1. Copy entire vault folder (including `.obsidian/`)
2. Install same community plugins on new Obsidian
3. Configure core plugins to match `core-plugins.json`

OR use Obsidian Sync (but note settings discourage it).

## Troubleshooting

**Templates not appearing:**

- Check `templates.json` has correct folder path
- Verify template files exist
- Restart Obsidian

**Daily notes wrong date:**

- Check `daily-notes.json` format setting
- System clock accuracy

**Community plugin not loading:**

- Check `community-plugins.json` has plugin ID
- Verify plugin folder exists in `.obsidian/plugins/`
- Check plugin compatibility with Obsidian version

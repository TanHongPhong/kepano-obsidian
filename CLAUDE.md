# CLAUDE.md

File này cung cấp hướng dẫn cho Claude Code (claude.ai/code) khi làm việc với code trong repository này.

## Tổng Quan Dự Án

Đây là **Obsidian vault** triển khai phương phápology "Second Brain" / PARA (Projects-Areas-Resources-Archives) để quản lý kiến thức cá nhân. Vault sử dụng theme Minimal của KEPANO và theo hệ thống ghi chú có cấu trúc với nhiều template.

## Cấu Trúc Repository

```
kepano-obsidian/
├── .obsidian/           # Cấu hình Obsidian (vault settings)
│   ├── appearance.json  # Cấu hình theme (Minimal theme)
│   ├── community-plugins.json  # Community plugins đã bật
│   ├── core-plugins.json # Core plugins đã bật/tắt
│   ├── daily-notes.json # Cấu hình daily notes
│   ├── templates.json   # Cài đặt template
│   ├── workspace.json   # Cấu hình UI layout và pane
│   └── plugins/         # Dữ liệu community plugins
├── Attachments/         # Media và file đính kèm
├── Categories/         # Tổ chức tag/category
├── Clippings/          # Web clippings và excerpts
├── Daily/              # Daily notes (journal entries)
├── Notes/              # Notes nội dung chính
│   └── Projects/       # Notes dự án đang hoạt động
├── References/         # Tài liệu tham khảo và source notes
├── Templates/          # Note templates (50+ templates)
│   ├── Bases/          # Base template files (.base extensions)
│   └── *.md            # Templates riêng lẻ theo entity type
└── Templates/          # Template files

```

## Các File Cấu Hình Quan Trọng

- `.obsidian/appearance.json` - Theme: Minimal, Theme mode: system
- `.obsidian/community-plugins.json` - Plugins: obsidian-hider, obsidian-minimal-settings
- `.obsidian/daily-notes.json` - Daily notes folder: `Daily/`, template: `Templates/Daily Note Template`
- `.obsidian/core-plugins.json` - Cấu hình core plugins enabled/disabled
- `.obsidian/app.json` - Attachment folder: `Attachments/`, auto-update links enabled

## Hệ Thống Template

Vault sử dụng hệ thống template toàn diện với:

- **Base templates** (`.base` files in `Templates/Bases/`) - Thành phần template có thể tái sử dụng
- **Entity templates** - Templates cụ thể cho các loại note khác nhau:
  - People, Places, Companies, Books, Movies, etc.
  - Projects, Meetings, Events, Tasks
  - Daily notes, Monthly notes
  - Các loại media khác (Albums, Podcasts, Recipes, etc.)

## Tổ Chức Notes

Notes theo cấu trúc **PARA-inspired**:

- **Projects** - Dự án đang hoạt động trong `Notes/Projects/`
- **Areas** - Life domains (thường trong `Notes/`)
- **Resources** - Tài liệu tham khảo trong `References/`
- **Archives** - Items lịch sử (thường trong `Clippings/` hoặc folders có tổ chức)

## Các Tác Vụ Phát Triển Thường Gặp

### Chỉnh Sửa Vault Configuration

Chỉnh sửa files trong `.obsidian/` để thay đổi:

- Theme settings (`appearance.json`)
- Core/community plugins (`core-plugins.json`, `community-plugins.json`)
- Daily notes template và location (`daily-notes.json`)
- Attachment folder behavior (`app.json`)

### Thêm Template Mới

1. Tạo file `.md` mới trong `Templates/` hoặc `Templates/Bases/`
2. Với base templates, dùng extension `.base`
3. Template sẽ có sẵn trong Obsidian's template picker

### Chỉnh Sửa Template Hiện Có

Chỉnh sửa template files trực tiếp trong `Templates/`. Templates là plain Markdown với frontmatter support.

## Obsidian Plugins

### Core Plugins

File-explorer, global-search, switcher, graph, backlink, tag-pane, page-preview, daily-notes, templates, note-composer, command-palette, editor-status, markdown-importer, zk-prefixer, random-note, outline, workspaces, file-recovery, canvas, bookmarks, bases, webviewer

### Community Plugins

- **obsidian-hider** - Ẩn các phần tử UI cho interface sạch hơn
- **obsidian-minimal-settings** - Cài đặt mở rộng cho theme Minimal

## Ghi Chú Về Chỉnh Sửa

- Đây là **Obsidian vault** - không phải codebase truyền thống
- Tất cả files là plain Markdown (`.md`) với optional YAML frontmatter
- Thay đổi `.obsidian/` settings đồng bộ với Obsidian app tự động
- Tôn trọng quy ước đặt tên và cấu trúc template hiện có
- Templates dùng `.base` files như thành phần có thể tái sử dụng

## Claude Code Agents

This vault includes a multi-agent system for automated vault maintenance. Agents are defined in `.claude/agents/`.

**See [`.claude/AGENTS.md`](.claude/AGENTS.md) for complete agent documentation.**

### Quick Reference

| Agent              | Skill                 | Purpose                |
| ------------------ | --------------------- | ---------------------- |
| Zoe (Orchestrator) | `orchestrator`        | Coordinates all agents |
| Athena             | `metadata-validation` | Validates frontmatter  |
| Arachne            | `link-analysis`       | Knowledge graph health |
| Sage               | `content-analysis`    | AI content review      |
| Mercury            | `task-management`     | Task tracking          |
| Janus              | `backup-recovery`     | Git & backup           |
| Hermes             | `report-generation`   | Daily reports          |

### Usage

```bash
# Run single agent
Skill run athena
Skill run arachne --fix-typos

# Run full orchestrated check
Skill run orchestrator --full
```

## Quy Ước Đặt Tên File

- Template files: `"Template Name".md` (giữ spaces)
- Base templates: `*.base` trong `Templates/Bases/`
- Daily notes: based on date (ví dụ: `2025-05-10.md`)

## Quan Trọng: Không Có Build/Lint/Test Commands

Đây là repository cấu hình/dữ liệu, không phải ứng dụng. Không có build steps, linters, hoặc tests. Thay đổi được phản ánh ngay lập tức trong ứng dụng Obsidian.

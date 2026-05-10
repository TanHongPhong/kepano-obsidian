# Hướng Dẫn Sử Dụng Multi-Agent System

## Tổng Quan

Hệ thống này gồm 7 agents tự động hóa bảo trì Obsidian vault:

- **Zoe** (Orchestrator) - Điều phối tất cả
- **Athena** - Validate metadata (frontmatter, categories, dates)
- **Arachne** - Quản lý links (broken/orphan detection)
- **Sage** - Phân tích nội dung bằng AI
- **Mercury** - Theo dõi tasks (overdue detection)
- **Janus** - Backup & Git health
- **Hermes** - Tạo báo cáo hàng ngày

## Cách Chạy

### 1. Chạy Demo Python (Nhanh để xem cách hoạt động)

```bash
cd /path/to/kepano-obsidian
python .claude/orchestrator.py full
```

Output:

```
[Zoe] Starting full orchestration...
[Zoe] Invoking agent: athena
[Zoe] Invoking agent: arachne
...
[Zoe] Report saved to: Reports/Daily/2026-05-10_orchestrator.json
```

### 2. Chạy Single Agent (Claude Code Skill)

Trong Claude Code, dùng lệnh:

```bash
# Validate metadata
Skill run athena

# Check links với auto-fix typos
Skill run arachne --fix-typos

# Content analysis (dùng Claude API)
Skill run sage --batch-size 10

# Check overdue tasks
Skill run mercury

# Backup & Git health
Skill run janus

# Generate daily report
Skill run hermes --daily
```

### 3. Chạy Tất Cả Agents (Full Health Check)

```bash
Skill run orchestrator --full
```

Hoặc:

```bash
python .claude/orchestrator.py full
```

## Kết Quả

### Agent Output (JSON)

Mỗi agent trả về JSON với kết quả. Ví dụ Athena:

```json
{
  "agent": "metadata-validation",
  "generated_at": "2026-05-10T14:30:00Z",
  "scan_stats": {
    "notes_scanned": 120,
    "valid": 115,
    "errors": 5,
    "auto_fixed": 3,
    "requires_review": 2
  },
  "errors": [...],
  "auto_fixes_applied": [...]
}
```

### Orchestrator Report

Khi chạy `orchestrator --full`, bạn nhận được báo cáo tổng hợp:

```json
{
  "orchestrator": "Zoe",
  "mode": "full_check",
  "results": {
    "total_notes": 120,
    "total_issues": 23,
    "auto_fixed": 8,
    "requires_review": 15,
    "health_score": 85
  },
  "agent_summary": { ... },
  "decisions": {
    "auto_apply": ["metadata_fixes", "broken_links"],
    "request_review": ["content_updates", "duplicate_resolution"]
  },
  "report_generated": "Reports/Daily/2026-05-10.md"
}
```

Báo cáo Markdown sẽ được tạo tại `Reports/Daily/YYYY-MM-DD.md`.

## Cấu Hình

Mỗi agent có cấu hình riêng trong `.claude/settings.json`:

```json
{
  "athena": {
    "auto_fix": true,
    "max_fixes_per_run": 10
  },
  "arachne": {
    "auto_fix_typos": true,
    "typo_confidence_threshold": 0.85
  },
  "sage": {
    "claude_model": "claude-opus-4-7",
    "batch_size": 20,
    "rate_limit_delay": 6
  },
  "orchestrator": {
    "auto_fix_limit": 10,
    "parallel_agents": true,
    "skip_unchanged": true
  }
}
```

## Workflow Đề Xuất

### Hàng Ngày

```bash
# Morning check
Skill run orchestrator --quick

# End of day full check
Skill run orchestrator --full
```

### Hàng Tuần

```bash
# Sunday review
Skill run sage          # Deep content analysis
Skill run mercury       # Task review
Skill run hermes --weekly
```

### Trước Khi Commit

```bash
Skill run janus         # Verify Git status
Skill run athena        # Check metadata
```

## Xem Kết Quả

### Báo Cáo Hàng Ngày

Mở file: `Reports/Daily/YYYY-MM-DD.md`

### JSON Logs

- Orchestrator: `Reports/Daily/YYYY-MM-DD_orchestrator.json`
- Agent-specific: Mỗi agent có thể lưu riêng

### Category Dashboards

Mở các note trong `Categories/`:

- `Categories/Projects.md` - Projects overview
- `Categories/People.md` - People list
- `Categories/Daily.md` - Daily notes
- `Categories/Backlinks.md` - Notes with many backlinks

## Troubleshooting

### Agent không chạy

```
Error: Agent not found
```

Kiểm tra:

- File agent có trong `.claude/agents/`?
- `name:` trong frontmatter đúng với tên gọi?

### Permission denied

```
Error: Permission denied for tool: Edit
```

Kiểm tra `.claude/settings.local.json`:

```json
{
  "permissions": {
    "allow": ["Edit:*", "Read:*", ...]
  }
}
```

### Sage (content-analysis) chậm

Sage dùng Claude API, có thể bị rate limit:

- Giảm `batch_size` trong config
- Tăng `rate_limit_delay`
- Chạy ít notes một lần

### Broken links nhiều

Arachne sẽ:

- Auto-fix typos (nếu confidence > 85%)
- Flag missing links để bạn tạo note

Xem `Categories/Backlinks.md` để thấy notes cần link.

## Tích Hợp Với Obsidian

### Mở Reports

Trong Obsidian, mở `Reports/Daily/` và xem báo cáo mới nhất.

### Dataview Queries

Dùng Dataview để xem issues:

```dataview
TABLE file.name, status
FROM "Notes/Projects"
WHERE status = "In Progress"
```

### Tìm Orphan Notes

Arachne sẽ liệt kê. Hoặc dùng Graph view:

- `Ctrl+G` - Mở graph
- Filter theo tag
- Look for isolated nodes

## Mở Rộng

### Thêm Agent Mới

1. Tạo file `.claude/agents/new-agent.md`
2. Define persona, mission, tools, output format
3. Add to orchestrator nếu cần coord

### Customize Output

Sửa agent `.md` file để thay đổi output format.

### Tích Hợp Với Hooks

Trong `.claude/settings.json`:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "command": "Skill run orchestrator --quick"
      }
    ],
    "Notification": [
      {
        "command": "Skill run orchestrator --full && skill run hermes --daily"
      }
    ]
  }
}
```

## Best Practices

1. **Chạy quick check hàng ngày** - phát hiện sớm
2. **Full check cuối ngày** - apply auto-fixes
3. **Backup trước khi chạy full** - Janus sẽ tự động nếu configured
4. **Review requires_review items** - đừng ignore hoàn toàn
5. **Tune thresholds** theo vault size và nhu cầu

## Liên Kết

- Agent definitions: `.claude/agents/`
- Documentation: `.claude/AGENTS.md`
- Quick start: `.claude/README.md`
- Plan chi tiết: `.claude/plans/l-n-k-e-ho-ch-vi-t-jolly-treasure-vi.md`

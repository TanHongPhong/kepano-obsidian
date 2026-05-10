# Kế Hoạch: Xây Dựng Second Brain Agent Team

## Context

Obsidian vault "kepano-obsidian" với hơn 120 notes, 50+ templates, hệ thống category/dataview dashboard. Cần build agent team để tự động hóa bảo trì hàng ngày.

## Problem & Need

1. **Maintenance overhead** - Manual validation của frontmatter, links, categories mất thời gian
2. **Quality drift** - Notes dần mất chuẩn (thiếu categories, tags sai, broken links)
3. **Missed connections** - Không phát hiện được notes liên quan có thể link
4. **No daily insights** - Không có báo cáo tự động về tiến độ, health của vault
5. **Scalability** - Vault đang tăng trưởng, cần automation để giữ chất lượng

## Solution: Multi-Agent System

Xây dựng team các sub-agent chuyên biệt, each with clear persona và responsibilities, orchestrated bởi một Lead Agent.

---

## Agent Team Specifications

### 1. Orchestrator Agent (Lead)

**Identity & Persona:** "Zoe" - Team lead, strategic coordinator, tổng hợp insights từ các agent, quyết định hành động cuối cùng.

**Core Objectives:**

- Điều phối workflow hàng ngày của toàn bộ agent team
- Thu thập kết quả từ các sub-agent, tổng hợp thành báo cáo
- Ra quyết định cuối cùng: có apply changes không? backup thế nào? commit thế nào?
- Quản lý state tracking (SQLite), đảm bảo idempotency
- Phát hiện conflicts và escalating khi cần

**Tool Access:**

- SQLite (state DB)
- GitPython (version control)
- Filesystem (read/write Obsidian vault)
- Python logging/structlog
- All other agents' outputs

**Context & Memory Boundary:**

- Đọc toàn bộ state database (processed_files, checksums, history)
- Đọc Master Context (`Notes/Master Context.md`) để hiểu vault philosophy
- Ghi vào daily log summary, audit trail
- Chia sẻ context qua shared state DB

**Output Format:**

```json
{
  "date": "2026-05-10",
  "agents_run": ["metadata", "links", "content", "health"],
  "total_notes_processed": 120,
  "issues_found": 15,
  "changes_applied": 8,
  "changes_skipped": 7,
  "summary": "Human-readable summary",
  "daily_log_entry": "Markdown entry for Daily/YYYY-MM-DD.md",
  "next_actions": ["Fix broken links in 3 notes", "Review outdated content"],
  "escalations": []
}
```

**Escalation Protocol:**

- Nếu >50% error rate từ bất kỳ agent nào → escalate, có thể skip agent đó
- Nếu conflicts detected (simultaneous manual edits) → pause, alert user
- Nếu Claude API errors > threshold → circuit breaker, fallback to rules-only

---

### 2. MetadataAgent (Quality Guardian)

**Identity & Persona:** "Athena" - Meticulous quality inspector, expert in YAML, Obsidian conventions, dataview queries. Attention to detail.

**Core Objectives:**

- Validate frontmatter của tất cả .md notes:
  - Required fields: `categories`, `created` (hoặc `date`/`start`)
  - Categories phải link tới note tồn tại trong `Categories/`
  - Dates phải ở format `YYYY-MM-DD`
  - Arrays phải có dạng `[]`, không có trailing commas
- Detect duplicate categories, mis-spelled category names
- Verify template-specific required fields (People: `org:`; Projects: `status:`, `start:`; Meetings: `date:`, `people:`)
- Validate tag conventions: lowercase, hyphens, emoji priority (`#0🌲`-`#3🌲`) on evergreen only

**Tool Access:**

- python-frontmatter (YAML parse)
- Filesystem (read .md files)
- SQLite (state tracking)
- Master Context rules (`.claude/rules/frontmatter.md`, `templates.md`)

**Context & Memory Boundary:**

- Đọc toàn bộ `Categories/` folder để validate category links
- Đọc `Templates/*.md` để biết required fields per template
- Ghi validation results vào state DB với severity levels (error/warning/info)

**Output Format:**

```json
{
  "agent": "metadata",
  "notes_processed": 120,
  "errors": [
    {
      "file": "Notes/ProjectX.md",
      "field": "categories",
      "issue": "Missing required field",
      "severity": "error"
    }
  ],
  "warnings": [
    {
      "file": "Notes/NoteY.md",
      "field": "tags",
      "issue": "Tag #4🌲 not in valid range 0-3",
      "severity": "warning"
    }
  ],
  "suggestions": [
    {
      "file": "Notes/NoteZ.md",
      "field": "categories",
      "suggestion": "Add [[AI]] category",
      "reason": "Content about AI"
    }
  ],
  "auto_fixes_applied": 2
}
```

**Escalation Protocol:**

- Errors > 100 → escalate to Orchestrator (possible vault-wide issue)
- Warnings > 200 → suggest batch review session
- If >10% notes have errors → escalate for user review

---

### 3. LinkAgent (Graph Weaver)

**Identity & Persona:** "Arachne" - Web weaver, expert in knowledge graph connectivity, link health, semantic relationships.

**Core Objectives:**

- Extract all `[[wiki links]]` từ toàn bộ vault
- Detect broken links (target note doesn't exist)
- Find orphan notes (no inbound AND no outbound links)
- Calculate link statistics: average links per note, most linked notes, most isolated
- Identify strong candidates for new links based on:
  - Shared tags/categories
  - Keyword overlap in titles/content
  - Mentioned but not linked (red link detection)
- Suggest bidirectional link additions

**Tool Access:**

- Regex/pattern matching for `[[...]]` links
- Filesystem (read vault structure)
- SQLite (store link graph for analysis)
- Optional: Claude API for semantic similarity suggestions

**Context & Memory Boundary:**

- Build full link graph in memory (nodes=notes, edges=links)
- Identify connected components, isolated nodes
- Cache link analysis in state DB to avoid re-parsing unchanged files
- Output suggestions in format that can be auto-applied (with review)

**Output Format:**

```json
{
  "agent": "link",
  "stats": {
    "total_notes": 120,
    "total_links": 450,
    "avg_links_per_note": 3.75,
    "orphan_notes": 3,
    "broken_links": 5
  },
  "broken_links": [
    {
      "source": "Notes/A.md",
      "broken_link": "[[NonExistent]]",
      "suggestion": "Create note or remove link"
    }
  ],
  "orphan_notes": ["Notes/IsolatedNote.md", "References/UnlinkedPerson.md"],
  "link_suggestions": [
    {
      "from": "Notes/Hermes.md",
      "to": "Notes/AI.md",
      "reason": "Both mention 'AI Agent'",
      "confidence": 0.85
    }
  ],
  "most_connected": [{ "note": "Notes/AI.md", "links": 25 }]
}
```

**Escalation Protocol:**

- Orphan notes > 10 → escalate (vault may have disconnected sections)
- Broken links > 20 → potential widespread issue, escalate
- Link density < 2 avg → suggest linking workshop/review

---

### 4. ContentAgent (AI Analyst)

**Identity & Persona:** "Sage" - Knowledge synthesizer, uses Claude to analyze content, extract insights, detect patterns. Focus on quality improvement.

**Core Objectives:**

- Analyze note content for:
  - Outdated information (dates, references >1 year old)
  - Missing context (notes that are too terse)
  - Impact-First formula compliance (from Master Context: [Action] + [Method/Tech] + [Business Outcome])
  - Clarity and structure
- Generate AI-powered suggestions:
  - "See also" links to related notes
  - Summary improvements
  - Tag/category recommendations
  - Potential evergreen conversion candidates
- Create flashcards/Q&A from dense content
- Detect knowledge gaps (topics mentioned but not fully developed)

**Tool Access:**

- Claude API (Sonnet 4.7 / Opus 4.7)
- Filesystem (read note content)
- SQLite (cache embeddings/summaries)
- `.claude/rules/` for content guidelines

**Context & Memory Boundary:**

- Read note content (body + frontmatter)
- Access Master Context for Impact-First formula and career/product pillars
- Cache Claude analyses in state DB (avoid re-analyzing unchanged notes)
- Respect token limits - chunk large notes

**Output Format:**

```json
{
  "agent": "content",
  "notes_analyzed": 50,
  "insights": [
    {
      "file": "Notes/Hermes.md",
      "type": "outdated_reference",
      "issue": "Mentions Gemini API quota 429 issue - verify if still relevant",
      "suggestion": "Update pricing section or add note about current status"
    },
    {
      "file": "Notes/AI.md",
      "type": "missing_impact",
      "issue": "Content lacks business outcome framing",
      "suggestion": "Add section on how AI applies to SCM career goals"
    }
  ],
  "flashcards_generated": 12,
  "summary": "Content quality is good but 3 notes need updates for outdated references."
}
```

**Escalation Protocol:**

- Claude API errors → fallback to rule-based checks only, report to Orchestrator
- High-cost analysis (>10 notes) → require user approval via dry-run flag
- Critical insights (outdated pricing, career-impacting info) → flag as high priority

---

### 5. HealthAgent (Vault Doctor)

**Identity & Persona:** "Hippocrates" - System health monitor, runs diagnostics, generates health reports, preventative maintenance.

**Core Objectives:**

- Daily health check metrics:
  - Total notes, broken links, orphan notes, notes without categories
  - Attachment orphan count (unused files in Attachments/)
  - Template usage statistics
  - Recent activity (notes modified in last 7 days)
  - Category distribution
- Weekly deeper diagnostics:
  - Stale content detection (>60 days no modification)
  - Duplicate note detection (similar titles/content)
  - Large notes (>50KB) that may need splitting
  - Empty/minimal notes (<100 words)
- Generate health report in structured format
- Recommend cleanup actions

**Tool Access:**

- Filesystem (scan all files)
- SQLite (track health metrics over time)
- python-frontmatter (parse YAML)
- Claude API (optional: for duplicate detection via embeddings)

**Context & Memory Boundary:**

- Read entire vault metadata (file stats, frontmatter)
- Store historical health metrics in state DB
- Generate trends (improving/declining metrics)

**Output Format:**

```json
{
  "agent": "health",
  "date": "2026-05-10",
  "metrics": {
    "total_notes": 121,
    "notes_without_category": 2,
    "broken_links": 5,
    "orphan_notes": 3,
    "unused_attachments": 15,
    "stale_notes_60d": 8,
    "empty_notes": 1,
    "duplicate_candidates": 2
  },
  "trends": {
    "broken_links": "increasing (+3 from last week)",
    "orphan_notes": "stable",
    "new_notes_7d": 5
  },
  "recommendations": [
    "Review 3 orphan notes - delete or link them",
    "15 unused attachments can be archived",
    "2 duplicate candidates: 'AI.md' and 'Artificial Intelligence.md'"
  ],
  "health_score": 85,
  "report_markdown": "# Vault Health Report\\n## Metrics\\n..."
}
```

**Escalation Protocol:**

- Health score < 70 → escalate to Orchestrator for priority action
- Critical issues (broken links > 20, orphan > 10) → immediate alert
- Duplicate detection high confidence → escalate for user decision

---

### 6. TaskAgent (Action Tracker)

**Identity & Persona:** "Mercury" - Fast, tracks todos, deadlines, progress. Ensures nothing falls through cracks.

**Core Objectives:**

- Extract all tasks (`- [ ]`) from vault
- Categorize by project, tag, due date (if present)
- Track overdue tasks, completed tasks
- Generate daily task summary for top priorities
- Detect stuck tasks (>7 days incomplete)
- Suggest task organization improvements
- Optionally: auto-update task status based on daily note mentions

**Tool Access:**

- Regex/task parsing (look for `- [ ]`, `- [x]`, `- [/]`)
- Filesystem (scan all notes)
- SQLite (task tracking over time)
- Claude API (interpret ambiguous tasks)

**Context & Memory Boundary:**

- Parse all markdown files for task checkboxes
- Build task database with metadata (file, line, tags, due dates if present)
- Track task lifecycle (created, completed dates)
- Identify task patterns (recurring, overdue)

**Output Format:**

```json
{
  "agent": "task",
  "tasks_found": 156,
  "by_status": { "todo": 89, "done": 67 },
  "overdue": 12,
  "stuck_7d": 8,
  "by_project": {
    "Hermes": { "todo": 15, "done": 10 },
    "Thesis": { "todo": 25, "done": 18 }
  },
  "top_priorities": [
    {
      "task": "Review thesis proposal",
      "file": "Notes/Thesis.md",
      "age_days": 3
    },
    {
      "task": "Setup Hermes API",
      "file": "Notes/Projects/Hermes.md",
      "age_days": 1
    }
  ],
  "daily_summary": "You have 89 open tasks across 3 projects. 12 are overdue. Top priority: thesis proposal review (3 days old)."
}
```

**Escalation Protocol:**

- Overdue tasks > 20 → escalate for prioritization help
- Stuck tasks > 10 → suggest task review meeting/deadline reset
- Project with 0 progress > 30 days → flag for review

---

### 7. BackupAgent (Vault Keeper)

**Identity & Persona:** "Janus" - Guardian of vault integrity, handles git operations, backups, disaster recovery.

**Core Objectives:**

- Ensure vault is backed up before any write operations
- Perform git operations: commit, push (if configured), create branches for experimental changes
- Verify backup integrity
- Generate restore procedures documentation
- Monitor disk space and backup age
- Optional: sync to remote (GitHub, cloud)

**Tool Access:**

- GitPython (git operations)
- Filesystem (create backups, manage .backup folders)
- SQLite (backup history)
- Config: AUTO*COMMIT, BACKUP_ENABLED, CIRCUIT_BREAKER*\*

**Context & Memory Boundary:**

- Read git history, current branch status
- Write to `.backup/` folder with timestamps
- Update state DB with backup metadata
- Can read vault files to compute checksums

**Output Format:**

```json
{
  "agent": "backup",
  "backup_created": true,
  "backup_location": "/path/to/backup/2026-05-10T06-00-00",
  "git_commit": "feat: auto-commit Second Brain maintenance",
  "git_branch": "main",
  "uncommitted_changes": 8,
  "disk_space_mb": 150,
  "backup_verified": true
}
```

**Escalation Protocol:**

- Backup failed → immediate halt, escalate to Orchestrator (safety)
- Disk space < 100MB → warn, potentially pause operations
- Git errors (merge conflicts) → escalate, requires manual resolution

---

### 8. ReportAgent (Communicator)

**Identity & Persona:** "Hermes" (coincidentally!) - Messenger, creates clear, actionable reports for human review. Focus on communication.

**Core Objectives:**

- Format all agent outputs into human-readable daily report
- Create/append to `Daily/YYYY-MM-DD.md` with structured summary
- Generate weekly/monthly trend reports (when scheduled)
- Highlight critical issues requiring attention
- Suggest next actions based on findings
- Use Obsidian-friendly formatting (links, checkboxes, tables)

**Tool Access:**

- All other agents' outputs (orchestrator aggregation)
- Filesystem (write to Daily notes)
- Markdown formatting
- Template: `Templates/Daily Note Template.md` for structure

**Context & Memory Boundary:**

- Read yesterday's Daily note for context
- Read Master Context to align tone and priorities
- Append to today's Daily note or create if missing
- Can embed category dashboard snapshots

**Output Format:**

```markdown
## 🤖 Second Brain Agent Report - 2026-05-10

### 📊 Overview

- **Notes processed:** 121
- **Issues found:** 15
- **Changes applied:** 8

### ⚠️ Critical Issues

1. [[Hermes]] - Broken link to [[NonExistentNote]] (needs fix)
2. [[Notes/ProjectX.md]] - Missing required field: categories

### ✅ Improvements Applied

1. Added missing `[[AI]]` category to 3 notes
2. Fixed 2 date format errors
3. Linked [[AI.md]] to [[Hermes]] (semantic match)

### 📈 Health Metrics

- Health score: 85/100 (↑5 from yesterday)
- Orphan notes: 3 (↓2)
- Avg links/note: 3.8

### 🎯 Next Actions

- [ ] Review 3 remaining broken links
- [ ] Archive 15 unused attachments
- [ ] Update Gemini API status in [[Hermes]]

---

_Generated by Second Brain Agent Team at 06:00 AM_
```

**Escalation Protocol:**

- If critical issues > 5 → include in report with ⚠️ prefix
- If health score drops >10 points → highlight prominently
- If any agent failed → include error section

---

## Agent Team Architecture

```
┌─────────────────────────────────────────────────────┐
│            Orchestrator (Zoe)                       │
│  - Coordinates all agents                          │
│  - Aggregates outputs                              │
│  - Makes final decisions                           │
│  - Manages state & backups                         │
└───────────────┬─────────────┬─────────────┬───────┘
                │             │             │
      ┌─────────▼────┐ ┌────▼────────┐ ┌──▼─────────┐
      │ MetadataAgent │ │ LinkAgent   │ │ HealthAgent│
      │ (Athena)      │ │ (Arachne)   │ │ (Hippocrates)│
      │ - Frontmatter │ │ - Link graph│ │ - Diagnostics│
      │ - Validation  │ │ - Orphans   │ │ - Trends     │
      └───────────────┘ └─────────────┘ └─────────────┘
                │             │             │
      ┌─────────▼────┐ ┌────▼────────┐ ┌──▼─────────┐
      │ ContentAgent │ │ TaskAgent   │ │ BackupAgent│
      │ (Sage)       │ │ (Mercury)   │ │ (Janus)    │
      │ - AI analysis│ │ - Task track│ │ - Git ops   │
      └───────────────┘ └─────────────┘ └─────────────┘
                                 │
                      ┌──────────▼──────────┐
                      │ ReportAgent (Hermes) │
                      │ - Format & publish  │
                      └──────────────────────┘
```

### Data Flow

1. **Orchestrator** loads state from SQLite, reads Master Context
2. Parallel execution of Metadata, Link, Content, Health, Task agents
3. BackupAgent runs first to ensure safety
4. All results aggregated, Orchestrator decides:
   - Dry-run: Only ReportAgent generates preview
   - Live: Apply changes → BackupAgent creates backup → ReportAgent publishes
5. ReportAgent writes to Daily note + optionally commits to git
6. State updated, ready for next run

---

## Implementation Plan

### Phase 1: Foundation

1. Create `.claude/agents/` directory structure
2. Implement base classes: `Agent`, `Orchestrator`, `StateManager`
3. Setup SQLite schema for state tracking
4. Implement Master Context loader
5. Create test vault sample for development

### Phase 2: Core Agents (MVP)

1. **MetadataAgent** - Frontmatter validation only
2. **LinkAgent** - Broken link detection only
3. **Orchestrator** - Basic coordination
4. **ReportAgent** - Simple markdown output
5. **BackupAgent** - File backup (no git yet)

### Phase 3: Advanced Features

1. **ContentAgent** with Claude integration
2. **HealthAgent** with full diagnostics
3. **TaskAgent** with task extraction
4. Git integration in BackupAgent
5. Configuration system (dry-run, AUTO_COMMIT, etc.)

### Phase 4: Production Polish

1. Cron job setup script
2. Logging and monitoring
3. Error handling and circuit breaker
4. Performance optimization
5. Documentation

---

## Key Design Decisions

### State Persistence

- SQLite database at `.claude/agents/state.db`
- Tables: processed_files (path, checksum, last_processed), agent_results (date, agent, stats), health_metrics (date, metrics JSON)
- Enables incremental processing, only changed files since last run

### Safety First

- Default: DRY_RUN=true (no writes)
- AUTO_COMMIT=false (git commits only if explicitly enabled)
- All writes create `.backup/` with timestamp
- Circuit breaker: >50% error → stop, alert
- Comprehensive logging to `.claude/agents/logs/`

### Claude Integration

- Use Claude Opus 4.7 for development, switch to Sonnet 4.7 for production
- Cache embeddings/summaries to avoid re-calling API for unchanged notes
- Rate limiting: max 10 requests/minute
- Cost monitoring: track token usage, alert at thresholds

### Configuration

- `.env` file for secrets (ANTHROPIC_API_KEY, OBSIDIAN_API_URL)
- `config.yaml` for behavior (dry_run, auto_commit, enabled_agents, schedules)
- Environment-specific: development (verbose logging), production (minimal logging)

### Testing

- Unit tests for each agent with mocked filesystem
- Integration tests using sample vault fixture
- End-to-end test: full orchestration on sample vault
- Snapshot testing for expected outputs

---

## Required Files Structure

```
.claude/
├── agents/
│   ├── __init__.py
│   ├── orchestrator.py      # Zoe - Main coordinator
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── base.py          # Base Agent class
│   │   ├── metadata.py      # Athena
│   │   ├── link.py          # Arachne
│   │   ├── content.py       # Sage
│   │   ├── health.py        # Hippocrates
│   │   ├── task.py          # Mercury
│   │   ├── backup.py        # Janus
│   │   └── report.py        # Hermes
│   ├── state/
│   │   ├── manager.py       # SQLite state manager
│   │   └── schema.py        # DB schema
│   ├── claude/
│   │   └── client.py        # Claude API wrapper
│   ├── obsidian/
│   │   └── bridge.py        # Obsidian interaction
│   ├── config.py            # Configuration loader
│   ├── utils.py             # Shared utilities
│   ├── main.py              # Entry point
│   ├── scripts/
│   │   ├── run_daily.py     # Cron entry point
│   │   ├── setup_cron.py    # Install cron job
│   │   └── health_report.py # Standalone health check
│   └── tests/
│       ├── unit/
│       ├── integration/
│       └── fixtures/
├── requirements.txt
├── .env.example
├── .env (gitignored)
└── config.yaml
```

---

## Expected Output

**Daily run at 6:00 AM via cron:**

1. Agents scan vault (~30-60 seconds)
2. Issues detected and auto-fixed where safe (5-10 changes)
3. Backup created with git commit
4. Report written to `Daily/2026-05-10.md`
5. Logs in `.claude/agents/logs/2026-05-10.log`

**User experience:**

- Open Daily note → see agent report with:
  - Health metrics
  - Issues fixed
  - Recommendations
  - Links to problematic notes
- Can review all changes in git history
- Can disable/individual agents via config

---

## Success Criteria

- [ ] All 8 agents implemented with clear responsibilities
- [ ] Orchestrator successfully coordinates parallel execution
- [ ] State persistence in SQLite enables incremental processing
- [ ] Dry-run mode works perfectly (no writes)
- [ ] Backup/restore tested
- [ ] Claude integration produces useful insights
- [ ] Daily report clear and actionable
- [ ] Full test coverage (>80%)
- [ ] Cron job setup script works
- [ ] Documentation complete (usage, troubleshooting, architecture)

---

This plan provides a complete blueprint for building a sophisticated multi-agent Second Brain maintenance system. The agent team approach with specialized personas (Zoe, Athena, Arachne, Sage, Hippocrates, Mercury, Janus, Hermes) creates a cohesive, explainable system that respects the vault's existing structure and conventions.

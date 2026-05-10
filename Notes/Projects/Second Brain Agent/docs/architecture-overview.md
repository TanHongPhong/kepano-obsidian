# Second Brain Agent Team - Architecture Overview

## System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                         DAILY SCHEDULE (6:00 AM)                  │
│                         ┌─────────────────┐                         │
│                         │   Cron Job      │                         │
│                         └────────┬────────┘                         │
│                                  │                                   │
│                                  ▼                                   │
│                    ┌─────────────────────────┐                      │
│                    │  SecondBrainOrchestrator│                      │
│                    │   (main.py - async)    │                      │
│                    └──────────┬──────────────┘                      │
│                               │                                     │
│                 ┌─────────────┼─────────────┐                       │
│                 │             │             │                       │
│                 ▼             ▼             ▼                       │
│    ┌──────────────────┐ ┌────────────┐ ┌─────────────┐           │
│    │  Metadata Agent  │ │ Link Agent │ │  AI Client  │           │
│    │  - Validate      │ │ - Orphans  │ │  - Claude   │           │
│    │    frontmatter   │ │ - Suggest  │ │  - Insights │           │
│    │  - Categories    │ │ - Mapping  │ │  - Content  │           │
│    │  - Tags          │ │            │ │  - Analysis │           │
│    └────────┬─────────┘ └──────┬─────┘ └──────┬──────┘           │
│              │                  │              │                    │
│              └──────────────────┼──────────────┘                    │
│                                 │                                   │
│                                 ▼                                   │
│                    ┌─────────────────────────┐                      │
│                    │    ObsidianBridge       │                      │
│                    │  (HTTP API Wrapper)    │                      │
│                    └──────────┬──────────────┘                      │
│                               │                                     │
│                               ▼                                     │
│                    ┌─────────────────────────┐                      │
│                    │   Obsidian Vault        │                      │
│                    │  (Markdown + Frontmatter│                      │
│                    │   via localhost:27123)  │                      │
│                    └──────────┬──────────────┘                      │
│                               │                                     │
│                               ▼                                     │
│                    ┌─────────────────────────┐                      │
│                    │      Git Auto-commit    │                      │
│                    │  (backup + commit)      │                      │
│                    └──────────┬──────────────┘                      │
│                               │                                     │
│                               ▼                                     │
│                    ┌─────────────────────────┐                      │
│                    │   Daily Log Summary     │                      │
│                    │   (Daily/YYYY-MM-DD.md) │                      │
│                    └─────────────────────────┘                      │
└─────────────────────────────────────────────────────────────────────┘
```

## Data Flow

```
┌─────────────┐
│ Master      │
│ Context.md  │──────┐
└─────────────┘      │
                     ▼
              ┌──────────────┐
              │  Orchestrator │
              │  Loads rules │
              └──────┬───────┘
                     │
         ┌───────────┼───────────┐
         │           │           │
         ▼           ▼           ▼
   ┌─────────┐ ┌─────────┐ ┌─────────┐
   │Metadata │ │  Link   │ │  Claude │
   │ Agent   │ │ Agent   │ │  Client │
   └────┬────┘ └────┬────┘ └────┬────┘
        │           │           │
        └───────────┼───────────┘
                    │
                    ▼
          ┌─────────────────┐
          │ ObsidianBridge  │
          │ HTTP API calls  │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │   Obsidian      │
          │   Vault         │
          └─────────────────┘
```

## Component Responsibilities

### 1. StateTracker (src/state.py)

- **Purpose:** Track processed files, timestamps, checksums
- **Storage:** SQLite (`data/state.db`)
- **Tables:** `file_state`, `processing_log`

### 2. MasterContext (src/context.py)

- **Purpose:** Load và validate against Master Context rules
- **Source:** `Notes/Master Context.md`
- **Validates:** Required frontmatter fields, tag formats, category consistency

### 3. ObsidianBridge (src/obsidian_bridge.py)

- **Purpose:** Interface với Obsidian qua HTTP API
- **Endpoint:** `http://localhost:27123` (Obsidian HTTP plugin)
- **Operations:** read_note(), write_note(), refresh_vault()
- **Safety:** Auto-backup before writes

### 4. MetadataAgent (src/metadata_agent.py)

- **Purpose:** Validate và fix YAML frontmatter
- **Checks:**
  - Required fields: categories, created, topics, tags, status
  - Tag prefix conventions (0🌲, etc.)
  - Category linking to existing categories
- **Output:** Health report + auto-fixes

### 5. LinkAgent (src/link_agent.py)

- **Purpose:** Manage wiki links [[...]]
- **Detects:**
  - Orphan notes (no inbound/outbound links)
  - Broken links (link to non-existent note)
- **Suggests:**
  - New connections dựa trên keyword overlap
  - Missing bidirectional links

### 6. ClaudeClient (src/anthropic_client.py)

- **Purpose:** AI-powered suggestions
- **Model:** Claude Opus 4.7
- **Capabilities:**
  - `validate_impact_first()` - Check impact-first formula
  - `suggest_links()` - Smart link suggestions
  - `analyze_outdated()` - Detect stale content

### 7. SecondBrainOrchestrator (src/orchestrator.py)

- **Purpose:** Coordinate all agents
- **Workflow:**
  1. Initialize all agents
  2. Scan all notes
  3. Run MetadataAgent → LinkAgent → ClaudeClient
  4. Apply changes via ObsidianBridge
  5. Auto-commit to git
  6. Append summary to Daily log
  7. Trigger vault refresh

## Schedule & Triggers

```
┌─────────────────────────────────────────────────────────────┐
│ Trigger Type              │ Frequency    │ Action             │
├───────────────────────────┼──────────────┼────────────────────┤
│ Cron Job                 │ Daily 6:00   │ Full maintenance   │
│ File System Watch (opt)  │ Real-time    │ Validate on save   │
│ Manual Trigger           │ On-demand    │ Run full check     │
│ Pre-commit Hook          │ On git commit│ Quick validation   │
└───────────────────────────┴──────────────┴────────────────────┘
```

## File Structure

```
Notes/Projects/Second Brain Agent/
├── src/
│   ├── __init__.py
│   ├── state.py              # SQLite state tracking
│   ├── context.py            # Master Context loader
│   ├── obsidian_bridge.py    # HTTP API wrapper
│   ├── metadata_agent.py     # Frontmatter validator
│   ├── link_agent.py         # Link manager
│   ├── anthropic_client.py   # Claude integration
│   ├── prompts.py            # System prompts
│   └── orchestrator.py       # Main coordinator
├── tests/
│   ├── test_state.py
│   ├── test_context.py
│   ├── test_obsidian_bridge.py
│   ├── test_metadata_agent.py
│   ├── test_link_agent.py
│   └── test_integration.py
├── scripts/
│   ├── test_local.sh         # Local test runner
│   └── setup_cron.sh         # Cron installer
├── data/
│   └── state.db              # SQLite database
├── logs/
│   └── [daily logs]
├── main.py                   # Entry point
├── requirements.txt
├── .env.example
├── README.md
└── docs/
    └── usage-guide.md
```

## Safety Mechanisms

1. **Dry-run mode:** `DRY_RUN=true` - no writes
2. **Auto-backup:** Every write creates `.backup` file
3. **Git versioning:** All changes committed
4. **Selective auto-commit:** Can be disabled per-agent
5. **Logging:** All actions logged to Daily notes
6. **Error handling:** API failures logged but don't crash

## Technology Stack

- **Language:** Python 3.11+
- **Async:** asyncio for concurrent operations
- **AI:** Anthropic Claude API (Opus 4.7)
- **Storage:** SQLite (state), Markdown files (vault)
- **Integration:** Obsidian HTTP Plugin (localhost:27123)
- **Scheduler:** cron (system-level)
- **VCS:** Git (auto-commit)

## Expected Daily Workflow

```
6:00 AM ── Cron triggers main.py
           │
           ├─> Load Master Context
           ├─> Scan all notes (~97 files)
           ├─> Run MetadataAgent
           │   └─> Fix 5-10 frontmatter issues
           ├─> Run LinkAgent
           │   └─> Find 2-3 orphans, suggest 10-20 links
           ├─> Run ClaudeClient
           │   └─> Generate impact-first suggestions
           ├─> Write changes via ObsidianBridge
           ├─> Git commit with formatted message
           ├─> Append summary to Daily/YYYY-MM-DD.md
           └─> Refresh Obsidian UI
```

## Performance Expectations

- **Scan 97 notes:** ~30-60 seconds
- **Claude API calls:** ~5-10 calls @ ~1-2s each
- **Total runtime:** ~2-3 minutes
- **Disk space:** <100MB (logs + state.db)

---

## Next Steps for Implementation

1. Setup Obsidian HTTP plugin (manual, user)
2. Create project structure (Task 2)
3. Build core infrastructure (Tasks 3-5)
4. Implement agents (Tasks 6-8)
5. Build orchestrator (Task 7)
6. Add Claude integration (Task 8)
7. Test & verify (Task 10)
8. Deploy with cron (Task 11)

---

**Key Design Principles:**

- ✅ Non-destructive (backup before write)
- ✅ Context-aware (Master Context driven)
- ✅ Observable (logs in Daily notes)
- ✅ Reversible (git versioning)
- ✅ Safe (dry-run default)

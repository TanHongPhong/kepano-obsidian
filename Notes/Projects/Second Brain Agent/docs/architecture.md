# Second Brain Agent - Architecture Specification

## Core Philosophy

The Second Brain Agent is an autonomous system that transforms an Obsidian vault into an intelligent knowledge management system. It operates on the principle of **passive enrichment** - observing note creation and automatically enhancing the knowledge graph through intelligent metadata extraction, link suggestions, and context augmentation.

**Key Principles:**

- **Zero-friction operation**: Works in the background without disrupting user workflow
- **Progressive enhancement**: Each note improves the system's understanding over time
- **Human-in-the-loop**: All suggestions are reviewable; user maintains full control
- **Local-first**: All processing happens locally; Obsidian sync handles distribution
- **Cost-aware**: Targets student/freelancer budget; uses Claude efficiently

---

## Agent Roles

### 1. Orchestrator (Orchestrator Agent)

**Purpose**: Central coordination and workflow management

**Responsibilities:**

- Initialize and monitor all agent threads
- Route new/modified notes to appropriate agents
- Aggregate agent outputs and resolve conflicts
- Manage retry logic and error handling
- Schedule periodic maintenance tasks

**Communication:**

- Receives file system events via watchdog observer
- Dispatches note content to MetadataAgent, LinkAgent, ClaudeClient
- Collects results and writes to Obsidian via ObsidianBridge
- Publishes status updates to central log

---

### 2. MetadataAgent

**Purpose**: Extract and standardize YAML frontmatter

**Responsibilities:**

- Parse existing frontmatter or infer missing fields
- Extract `categories`, `topics`, `tags`, `status`, `created` dates
- Normalize tag format (emoji prefixes: `0🌲` evergreen, `1📝` draft, etc.)
- Infer relationships from content (references, projects, people)
- Detect note type (concept, person, project, resource, daily)

**Output:**

- Updated frontmatter dictionary
- Confidence scores for inferred fields
- Suggested corrections in review mode

---

### 3. LinkAgent

**Purpose**: Maintain bidirectional link health and suggest connections

**Responsibilities:**

- Parse `[[WikiLinks]]` in content
- Validate target note existence (broken link detection)
- Generate contextual link suggestions based on:
  - Semantic similarity (embedding-based)
  - Shared tags/categories
  - Mentioned entities (people, projects, concepts)
  - Temporal proximity (daily note connections)
- Rank suggestions by relevance score
- Avoid duplicate/ circular link proposals

**Output:**

- Broken link report
- Top N link suggestions with context snippets
- Link density metrics per note

---

### 4. ClaudeClient

**Purpose**: LLM-powered analysis and generation

**Responsibilities:**

- Construct prompts from note content + context
- Apply templates (summarization, extraction, expansion)
- Manage Claude API quotas and retry logic
- Cache embeddings for similarity computation
- Parse structured responses (JSON/YAML)

**Use Cases:**

- Summarize long articles into digestible abstracts
- Extract key entities and relationships
- Generate "see also" suggestions
- Rewrite unclear passages
- Create flashcards/Q&A from content

**Safety:**

- Rate limiting per minute/hour
- Content length truncation
- Fallback to rule-based processing on API failure

---

### 5. ObsidianBridge

**Purpose**: Read/write interface to the vault

**Responsibilities:**

- Watch file system for note changes (create/modify/delete)
- Read Markdown files with proper encoding
- Write updates atomically (temp file + rename)
- Preserve formatting and user edits
- Handle Obsidian lock files appropriately
- Trigger Obsidian refresh (touch .git directory)

**Operations:**

- `get_note(path) -> Note` - read and parse
- `update_note(path, frontmatter, content) -> bool` - write safely
- `list_notes() -> List[Path]` - enumerate notes
- `search_notes(query) -> List[Path]` - grep-based search
- `get_backlinks(path) -> List[Path]` - reverse link lookup

---

## Communication Pattern

```
┌─────────────────┐
│   File System   │ ← New/Modified Note
│   (watchdog)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Orchestrator   │ ← Receives event
│                 │ ← Loads note via ObsidianBridge
└────────┬────────┘
         │
         ├─────────────────┬─────────────────┐
         ▼                 ▼                 ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ MetadataAgent│  │   LinkAgent  │ │ ClaudeClient │
│              │  │              │ │              │
│ Process      │  │ Analyze      │ │ LLM API      │
│ frontmatter  │  │ links        │ │ calls        │
└──────┬───────┘  └──────┬───────┘ └──────┬───────┘
       │                 │                 │
       └─────────────────┼─────────────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  Orchestrator   │ ← Merge results
                  │   (Conflict     │
                  │   Resolution)   │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │  ObsidianBridge │ ← Write updates
                  │                 │   (preserve edits)
                  └─────────────────┘
```

**Message Format (internal):**

```python
@dataclass
class AgentTask:
    note_path: Path
    note_content: str
    frontmatter: dict
    task_type: str  # "metadata", "links", "enrich"
    priority: int

@dataclass
class AgentResult:
    note_path: Path
    updates: dict  # {"frontmatter": {}, "content": ""}
    suggestions: list  # link suggestions, tag proposals
    confidence: float
    agent: str
```

---

## Schedule

### Real-time (Event-driven)

- On note creation: MetadataAgent, LinkAgent (broken links)
- On note modification: All agents (incremental update)

### Periodic (Async)

- **Hourly**: LinkAgent - full vault similarity scan
- **Daily** (02:00): ClaudeClient - embedding cache refresh
- **Weekly** (Sunday 03:00): MetadataAgent - orphaned tag cleanup
- **Monthly**: Full vault health report generation

---

## Safety Mechanisms

### File Safety

- **Backup before write**: Keep `.backup/` with timestamped copies
- **Atomic writes**: Write to temp file then `os.replace()`
- **Max batch size**: Process max 50 notes per cycle to limit damage
- **Dry run mode**: Preview changes without writing

### API Safety

- **Rate limits**: 10 requests/minute burst, 100/hour sustained
- **Cost monitoring**: Track token usage; alert at $5/day threshold
- **Fallback**: Rule-based processing if Claude unavailable

### User Control

- **Review mode**: All changes logged to `suggestions.log` for manual approval
- **Auto-commit toggle**: `AUTO_COMMIT=false` requires manual `git add`
- **Exclude patterns**: `ignored_paths` config for sensitive folders

### Error Recovery

- **Retry with backoff**: 3 attempts with exponential delay
- **Circuit breaker**: Pause agent if error rate > 50% over 10 notes
- **State persistence**: `logs/agent_state.json` for recovery after crash

---

## Component Responsibilities

| Component      | Primary Concern       | Outputs               | Side Effects       |
| -------------- | --------------------- | --------------------- | ------------------ |
| Orchestrator   | Workflow coordination | Task dispatch, merge  | Agent lifecycle    |
| MetadataAgent  | Frontmatter integrity | Standardized metadata | Frontmatter writes |
| LinkAgent      | Graph connectivity    | Link suggestions      | Content edits      |
| ClaudeClient   | LLM services          | Enriched content      | API costs          |
| ObsidianBridge | Vault I/O             | Note objects          | File system writes |

---

## Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        OBSIDIAN VAULT                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐      │
│  │  Note A  │  │  Note B  │  │  Note C  │  │  Note D  │ ...  │
│  │ .md file │  │ .md file │  │ .md file │  │ .md file │      │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘      │
└─────────────────────────────────────────────────────────────────┘
                              │ FS Events
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                       SECOND BRAIN AGENT                       │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              ORCHESTRATOR (async loop)                  │  │
│  │  • Event queue: Deque[AgentTask]                        │  │
│  │  • Active agents: Dict[str, AgentThread]                │  │
│  │  • State: logs/agent_state.json                         │  │
│  └────────────────────────────┬─────────────────────────────┘  │
│                               │ dispatch                      │
│       ┌───────────────────────┼───────────────────────┐      │
│       ▼                       ▼                       ▼      │
│  ┌──────────┐            ┌──────────┐            ┌──────────┐│
│  │ Metadata │            │   Link   │            │  Claude  ││
│  │  Agent   │            │  Agent   │            │  Client  ││
│  └────┬─────┘            └────┬─────┘            └────┬─────┘│
│       │                       │                       │      │
│       └───────────────────────┼───────────────────────┘      │
│                               │ results                      │
│                               ▼                               │
│                    ┌──────────────────┐                     │
│                    │  Conflict Resolver│                    │
│                    │  • Merge updates │                    │
│                    │  • Deduplicate   │                    │
│                    │  • Confidence    │                    │
│                    └────────┬─────────┘                     │
│                             │                                │
│                             ▼                                │
│                    ┌──────────────────┐                     │
│                    │  Obsidian Bridge │                     │
│                    │  • Read/Write    │                     │
│                    │  • Backup         │                    │
│                    └──────────────────┘                     │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   PERSISTED STATE                              │
│  • logs/agent_state.json - Agent checkpoints                  │
│  • logs/suggestions.log - Pending approvals                  │
│  • data/embeddings.sqlite - Cached embeddings                │
│  • data/link_index.json - Link graph                         │
│  • backups/ - Timestamped vault snapshots                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## File Structure

```
Second Brain Agent/
│
├── src/
│   ├── __init__.py
│   ├── orchestrator.py      # Main coordinator, event loop
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── metadata.py      # MetadataAgent implementation
│   │   ├── link.py          # LinkAgent implementation
│   │   ├── claude_client.py # ClaudeClient with caching
│   │   └── base.py          # BaseAgent abstract class
│   ├── bridge/
│   │   ├── __init__.py
│   │   ├── obsidian.py      # ObsidianBridge
│   │   └── file_watcher.py  # watchdog observer wrapper
│   ├── models/
│   │   ├── __init__.py
│   │   ├── note.py          # Note dataclass
│   │   ├── task.py          # AgentTask, AgentResult
│   │   └── config.py        # Config dataclass
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py        # Structured logging
│   │   ├── backup.py        # Backup utilities
│   │   └── safety.py        # Safety checks
│   └── main.py              # Entry point
│
├── tests/
│   ├── __init__.py
│   ├── test_metadata.py
│   ├── test_link.py
│   ├── test_claude_client.py
│   ├── test_bridge.py
│   └── fixtures/
│       ├── sample_notes/
│       └── vault_mock.py
│
├── scripts/
│   ├── install.sh           # Setup script
│   ├── migrate_notes.py     # Migration utility
│   └── health_report.py     # Generate vault health report
│
├── data/
│   ├── embeddings.sqlite    # Vector embeddings cache
│   └── link_index.json      # Link graph index
│
├── logs/
│   ├── agent_state.json     # Agent checkpoints
│   ├── suggestions.log      # Pending manual reviews
│   └── sba_YYYY-MM-DD.log   # Daily logs (rotated)
│
├── backups/                 # Auto-created, gitignored
│   └── backup_YYYY-MM-DD_HH-MM-SS/
│       └── (vault snapshot)
│
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── pyproject.toml (optional)
```

---

## Technology Stack

| Layer             | Technology               | Rationale                         |
| ----------------- | ------------------------ | --------------------------------- |
| **Runtime**       | Python 3.11+             | Mature ecosystem, async support   |
| **LLM**           | Anthropic Claude API     | High quality, structured output   |
| **Orchestration** | asyncio + threading      | Async I/O, parallel agent workers |
| **File Watching** | watchdog                 | Cross-platform FS events          |
| **Embeddings**    | Claude embeddings API    | Consistent with LLM provider      |
| **Storage**       | SQLite (local)           | Zero-config, thread-safe          |
| **Config**        | Pydantic + python-dotenv | Validation, env management        |
| **Markdown**      | python-frontmatter       | YAML frontmatter parsing          |
| **Logging**       | structlog                | Structured logs for debugging     |
| **Testing**       | pytest + pytest-asyncio  | Async test support                |
| **Git**           | GitPython                | Programmatic repo operations      |

---

## Configuration

### Environment Variables (.env)

```bash
# Required
ANTHROPIC_API_KEY=sk-ant-...

# Vault location (absolute path recommended)
VAULT_ROOT=/path/to/obsidian/vault

# Optional Obsidian Local REST API (for trigger refresh)
OBSIDIAN_API_URL=http://localhost:27123
OBSIDIAN_API_KEY=optional_key

# Agent behavior
DRY_RUN=false          # Preview changes without writing
AUTO_COMMIT=false      # Auto-commit to git after changes
REVIEW_MODE=auto       # "auto" (confident only), "always", "never"

# Logging
LOG_LEVEL=INFO         # DEBUG, INFO, WARNING, ERROR
LOG_FILE=logs/sba.log

# Safety
MAX_BATCH_SIZE=50      # Notes per processing cycle
BACKUP_ENABLED=true    # Create backups before writes
CIRCUIT_BREAKER_ERROR_RATE=0.5  # 50% error threshold

# Claude API
ANTHROPIC_MODEL=claude-sonnet-4-7-20250514
MAX_TOKENS_PER_REQUEST=4000
EMBEDDING_MODEL=claude-3-embedding-3
```

---

## Extension Points

Future agent additions:

- `TaggerAgent`: Machine learning-based tag recommendation
- `MentionAgent`: People/entity detection and profile creation
- `ReviewAgent`: Periodic content quality audits
- `SyncAgent`: Multi-vault synchronization

Plugin integration:

- Obsidian plugin for inline suggestion UI
- Git hook integration for pre-commit validation
- VS Code extension for vault management

---

## Development Roadmap

**Phase 1** (MVP): Orchestrator + MetadataAgent + ObsidianBridge
**Phase 2**: LinkAgent + embedding similarity
**Phase 3**: ClaudeClient + enrichment templates
**Phase 4**: Web UI for reviewing suggestions
**Phase 5**: Multi-vault support, advanced analytics

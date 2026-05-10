# Second Brain Agent

An autonomous system that transforms your Obsidian vault into an intelligent knowledge management system.

## Overview

The Second Brain Agent operates in the background, automatically enhancing your notes through:

- **Metadata standardization** - consistent YAML frontmatter
- **Smart link suggestions** - discover connections between notes
- **Intelligent enrichment** - AI-powered summaries and insights

## Project Structure

```
Second Brain Agent/
├── src/              # Source code
│   ├── agents/       # Individual agent implementations
│   ├── bridge/       # Obsidian vault interface
│   ├── models/       # Data structures
│   └── utils/        # Utilities (logging, backup, safety)
├── tests/            # Unit and integration tests
├── scripts/          # Helper scripts (migration, health reports)
├── data/             # SQLite cache and indexes
├── logs/             # Agent logs and state
└── docs/             # Documentation
```

## Setup

1. **Clone and navigate:**

   ```bash
   cd Notes/Projects/Second\ Brain\ Agent
   ```

2. **Create virtual environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment:**

   ```bash
   cp .env.example .env
   # Edit .env with your settings
   # - Add your ANTHROPIC_API_KEY
   # - Verify VAULT_ROOT path
   ```

5. **Run the agent:**
   ```bash
   python -m src.main
   ```

## Architecture

See `docs/architecture.md` for complete specification including:

- Agent roles (Orchestrator, Metadata, Link, ClaudeClient, ObsidianBridge)
- Communication patterns
- Safety mechanisms
- Data flow diagrams

## Key Features

- **Zero-friction**: Works in background without disrupting your workflow
- **Human-in-the-loop**: All changes are reviewable; you maintain control
- **Local-first**: All processing happens locally
- **Cost-aware**: Designed for student/freelancer budget

## Configuration

| Variable         | Description                         | Default |
| ---------------- | ----------------------------------- | ------- |
| `DRY_RUN`        | Preview changes without writing     | `true`  |
| `AUTO_COMMIT`    | Auto-commit to git after changes    | `false` |
| `REVIEW_MODE`    | `auto`, `always`, or `never`        | `auto`  |
| `MAX_BATCH_SIZE` | Notes processed per cycle           | `50`    |
| `LOG_LEVEL`      | `DEBUG`, `INFO`, `WARNING`, `ERROR` | `INFO`  |

## Safety

- Atomic file writes with automatic backups
- Circuit breaker for error handling
- Rate limiting on Claude API calls
- Full audit trail in `logs/suggestions.log`

## License

TBD

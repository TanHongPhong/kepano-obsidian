# Multi-Agent System - Quick Start

This vault includes a multi-agent system for automated Second Brain maintenance.

## Agents

| Agent              | Skill                 | Purpose                |
| ------------------ | --------------------- | ---------------------- |
| Zoe (Orchestrator) | `orchestrator`        | Coordinates all agents |
| Athena             | `metadata-validation` | Validates frontmatter  |
| Arachne            | `link-analysis`       | Knowledge graph health |
| Sage               | `content-analysis`    | AI content review      |
| Mercury            | `task-management`     | Task tracking          |
| Janus              | `backup-recovery`     | Git & backup           |
| Hermes             | `report-generation`   | Daily reports          |

## Usage

### Run Single Agent

```bash
Skill run athena                    # Validate metadata
Skill run arachne --fix-typos       # Check and fix broken links
Skill run sage                      # AI content analysis
Skill run mercury                   # Check overdue tasks
Skill run janus                     # Backup and Git health
Skill run hermes --daily            # Generate daily report
```

### Run All Agents (Orchestrated)

```bash
Skill run orchestrator --full       # Full health check
Skill run orchestrator --quick      # Quick check (skip heavy agents)
```

## Agent Definitions

Agent definitions are in `.claude/agents/` as markdown files with:

- **Persona**: Who the agent is (Zoe, Athena, etc.)
- **Core Mission**: What the agent does
- **Allowed Tools**: What tools the agent can use
- **Output Format**: JSON schema for results
- **Configuration**: Settings for the agent

See `.claude/AGENTS.md` for complete documentation.

## State & Reports

- State DB: `.claude/state/orchestrator.db`
- Daily reports: `Reports/Daily/YYYY-MM-DD.md`
- Orchestrator logs: `Reports/Daily/YYYY-MM-DD_orchestrator.json`

## Demo

A simple Python orchestrator demo is available:

```bash
python .claude/orchestrator.py full
```

This demonstrates the coordination flow with mock agent outputs.

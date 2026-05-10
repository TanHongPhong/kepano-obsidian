# Claude Code Agent Definitions

This directory contains agent definitions for the multi-agent Second Brain system. These are Claude Code skills that define specialized agents with specific missions, tools, and output formats.

## What Are Agent Definitions?

Agent definitions are markdown files (`.md`) with YAML frontmatter that describe:

- **name**: Agent identifier (used in `Skill run <name>`)
- **description**: One-line summary
- **Persona**: Who the agent is (Zoe, Athena, etc.)
- **Core Mission**: What the agent does
- **Allowed Tools**: Which tools the agent can use
- **Execution Model**: When and how the agent runs
- **Output Format**: JSON schema for results
- **Configuration**: JSON config options

## How Claude Code Uses These

When you invoke `Skill run <agent-name>`, Claude Code:

1. Reads the `.md` file from `.claude/agents/`
2. Extracts the frontmatter and persona
3. Loads the agent's allowed tools
4. Executes the agent's logic (defined in the document)
5. Returns JSON output in the specified format

## Agent Types

| Agent               | Name    | Role                       | Skill                 |
| ------------------- | ------- | -------------------------- | --------------------- |
| Orchestrator        | Zoe     | Coordinates all agents     | `orchestrator`        |
| Metadata Validation | Athena  | Validates frontmatter      | `metadata-validation` |
| Link Analysis       | Arachne | Manages knowledge graph    | `link-analysis`       |
| Content Analysis    | Sage    | AI-powered content review  | `content-analysis`    |
| Task Management     | Mercury | Tracks tasks and deadlines | `task-management`     |
| Backup & Recovery   | Janus   | Git, backups, integrity    | `backup-recovery`     |
| Report Generation   | Hermes  | Creates health reports     | `report-generation`   |

## Using Agents

### Standalone

```bash
# Run a single agent
Skill run athena

# Run with arguments
Skill run arachne --fix-typos
Skill run sage --batch-size 10
Skill run orchestrator --full
```

### Orchestrated

```bash
# Run all agents (orchestrated by Zoe)
Skill run orchestrator --full

# Quick check (skip some agents)
Skill run orchestrator --quick
```

## Creating New Agents

To create a new agent:

1. Copy an existing agent `.md` file as template
2. Change the `name` in frontmatter (lowercase, hyphens)
3. Update the persona and mission
4. Define allowed tools (from Read, Edit, Bash, Grep, Glob, LS, etc.)
5. Specify output JSON format
6. Add configuration section if needed
7. Save to `.claude/agents/`

## Agent File Structure

````markdown
---
name: agent-name
description: Short description
---

# Agent Name (Persona)

You are **Persona** - description.

## Core Mission

1. Task 1
2. Task 2

## Allowed Tools

- `Read` - What it can read
- `Bash` - What commands it can run

## Execution Model

ON-DEMAND or SCHEDULED

## Output Format (JSON)

```json
{
  "agent": "name",
  "key": "value"
}
```
````

## Configuration

```json
{
  "agent": {
    "option": "value"
  }
}
```

## Best Practices

- Keep agents focused (single responsibility)
- Use clear, actionable output JSON
- Document error conditions
- Specify rate limits if using Claude API
- Include examples in output format

## State Persistence

Agents can store state in:

- `.claude/state/[agent-name].db` (SQLite)
- `.claude/cache/` (JSON files)
- Git commits (for backup/recovery)

State is agent-specific, not shared.

## Integration with Orchestrator

Orchestrator (Zoe) can:

- Call any agent via Agent Tool
- Read agent JSON outputs
- Make decisions based on aggregated results
- Apply auto-fixes (with safety limits)

Orchestrator does NOT:

- Modify agent definitions
- Bypass agent tool restrictions
- Make unilateral changes without agent input

## Troubleshooting

**Agent not found:**

- Check file exists in `.claude/agents/`
- Verify `name:` in frontmatter matches invocation

**Tool permission denied:**

- Check `.claude/settings.local.json` permissions
- Add tool to `allow` list

**JSON output malformed:**

- Validate JSON syntax
- Ensure output is pure JSON (no extra text)

**Agent hangs:**

- Check for infinite loops
- Add timeout in configuration
- Review rate limiting for Claude API calls

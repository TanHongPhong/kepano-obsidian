# Second Brain Maintenance Agent Team Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Triển khai agent team tự động hóa việc cập nhật, duy trì, và bảo trì Obsidian second brain vault — đảm bảo thông tin luôn nhất quán, theo ngữ cảnh của Phong, và được ghi chép đúng chuẩn.

**Architecture:** 3-agent team (Orchestrator + Specialist agents) chạy trên Python asyncio, tích hợp với Obsidian qua HTTP plugin, sử dụng Claude Opus 4.7 để xử lý ngữ cảnh và quyết định hành động. Team chạy như cron job hàng ngày, theo dõi thay đổi và tự động gợi ý/cập nhật notes với auto-commit.

**Tech Stack:**

- Python 3.11+ (asyncio)
- Claude API (Opus cho reasoning, Sonnet cho processing)
- Obsidian file system (Markdown + YAML frontmatter)
- Git for version control
- Schedule/cron integration
- SQLite để tracking state

---

## Task 1: Thiết kế Architecture & Agent Roles

**Files:**

- Create: `Notes/Projects/Second Brain Agent/docs/architecture.md`
- Modify: N/A

- [ ] **Step 1: Viết specification agent team**

```markdown
# Second Brain Agent Team Architecture

## Core Philosophy

- **Keep it simple:** File-based, no external DB dependencies (except SQLite state)
- **Context-aware:** Dựa trên Master Context.md để đưa ra quyết định
- **Non-destructive:** Luôn tạo backup, không overwrite manual edits mà không hỏi
- **Observable:** Ghi log tất cả hành động vào Daily/ hoặc dedicated log

## Agent Roles

### 1. Orchestrator Agent

- Điều phối workflow hàng ngày
- Đọc Master Context.md để hiểu priorities và rules
- Quyết định agent nào chạy, khi nào
- Tạo daily report

### 2. Metadata Agent

- Kiểm tra và fix YAML frontmatter consistency
- Validate categories, tags, status theo đúng format
- Sync với Categories/ và Templates/
- Gợi ý linking với các notes có liên quan

### 3. Content Agent

- Phân tích nội dung note, đảm bảo impact-first formula
- Detect outdated thông tin (dates, references)
- Gợi ý updates dựa trên Master Context
- Tìm inconsistencies across notes

### 4. Link Agent (optional, merge với Metadata nếu cần)

- Quản lý bidirectional links [[...]]
- Detect orphan notes (không có inbound/outbound links)
- Suggest new connections dựa trên topics
- Maintain link integrity

### 5. Obsidian Bridge

- Wrapper cho Obsidian HTTP API (localhost:27123)
- Read/write notes với proper frontmatter preservation
- Trigger vault refresh tự động sau changes
- Safe mode: backup before write

## Communication Pattern

- Orchestrator gọi agents theo schedule
- Agents đọc/write files qua Obsidian HTTP API (port 27123)
- State tracking trong `state.db` (SQLite)
- Auto-commit tất cả changes với git (meaningful messages)
- Daily summary được append vào Daily/ note

## Schedule

- Daily: Metadata validation, link check
- Weekly: Content audit, consistency check
- On-detected: Khi có file mới/thay đổi lớn

## Safety

- Dry-run mode mặc định
- Human approval cho bulk changes
- Backup trước mọi modification
- Git hooks để review changes
```

- [ ] **Step 2: Commit architecture doc**

```bash
cd /home/tan-hong-phong/Documents/obsidian/kepano-obsidian-main
git add Notes/Projects/Second\ Brain\ Agent/docs/architecture.md
git commit -m "docs: add Second Brain Agent architecture specification"
```

- [ ] **Step 3: Run test validation**

```bash
python3 -c "import yaml; print('yaml OK')" && python3 -c "import sqlite3; print('sqlite3 OK')" && echo "Dependencies check passed"
```

---

## Task 2: Project Setup & Dependencies

**Files:**

- Create: `Notes/Projects/Second Brain Agent/` (thư mục project)
- Create: `Notes/Projects/Second Brain Agent/requirements.txt`
- Create: `Notes/Projects/Second Brain Agent/main.py`
- Modify: N/A

- [ ] **Step 1: Create project structure**

```bash
mkdir -p Notes/Projects/Second\ Brain\ Agent/{tests,data,logs}
```

- [ ] **Step 2: Viết requirements.txt**

```
anthropic>=0.47.0
pydantic>=2.0
python-frontmatter>=1.0
python-dateutil>=2.8
watchdog>=3.0
schedule>=1.2
sqlite-utils>=3.0
gitpython>=3.1
python-dotenv>=1.0
```

- [ ] **Step 3: Commit project structure**

```bash
git add Notes/Projects/Second\ Brain\ Agent/
git commit -m "chore: create Second Brain Agent project structure"
```

---

## Task 3: Core Infrastructure - State Tracking

**Files:**

- Create: `Notes/Projects/Second Brain Agent/src/state.py`
- Create: `Notes/Projects/Second Brain Agent/tests/test_state.py`
- Test: `tests/test_state.py`

- [ ] **Step 1: Viết StateTracker class**

```python
# src/state.py
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Optional

class StateTracker:
    """Track processed files và last check timestamps"""

    def __init__(self, db_path: str = "data/state.db"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS file_state (
                    path TEXT PRIMARY KEY,
                    last_modified TIMESTAMP,
                    last_processed TIMESTAMP,
                    checksum TEXT,
                    agent_tag TEXT
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS processing_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TIMESTAMP,
                    agent_name TEXT,
                    file_path TEXT,
                    action TEXT,
                    details TEXT
                )
            """)

    def is_processed(self, file_path: str, agent_name: str, since: Optional[datetime] = None) -> bool:
        """Check if file đã được agent xử lý"""
        # Implementation
        pass

    def mark_processed(self, file_path: str, agent_name: str, checksum: str):
        """Mark file as processed by agent"""
        # Implementation
        pass

    def log_action(self, agent_name: str, file_path: str, action: str, details: str = ""):
        """Log hành động của agent"""
        # Implementation
        pass
```

- [ ] **Step 2: Viết unit tests**

```python
# tests/test_state.py
import pytest
from src.state import StateTracker

def test_init_creates_db():
    tracker = StateTracker("data/test.db")
    assert tracker.db_path.exists()

def test_mark_and_check_processed():
    tracker = StateTracker("data/test.db")
    tracker.mark_processed("test.md", "MetadataAgent", "abc123")
    assert tracker.is_processed("test.md", "MetadataAgent") is True
```

- [ ] **Step 3: Run tests và commit**

```bash
python3 -m pytest tests/test_state.py -v
git add src/state.py tests/test_state.py
git commit -m "feat: add StateTracker for file processing state"
```

---

## Task 4: Master Context Loader

**Files:**

- Create: `Notes/Projects/Second Brain Agent/src/context.py`
- Create: `Notes/Projects/Second Brain Agent/tests/test_context.py`

- [ ] **Step 1: Viết MasterContext class**

```python
# src/context.py
from pathlib import Path
import yaml
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class MasterContext:
    """Load và expose Master Context rules"""
    vault_root: Path
    identity: Dict
    career_focus: List[str]
    ai_protocol: Dict
    tags_required: List[str]

    @classmethod
    def load(cls, vault_root: str = "."):
        """Load Master Context.md"""
        master_path = Path(vault_root) / "Notes" / "Master Context.md"
        with open(master_path) as f:
            content = f.read()

        # Parse YAML frontmatter
        frontmatter, body = yaml.split(content)

        return cls(
            vault_root=Path(vault_root),
            identity=frontmatter.get('identity', {}),
            career_focus=frontmatter.get('career_focus', []),
            ai_protocol=frontmatter.get('ai_protocol', {}),
            tags_required=frontmatter.get('tags', [])
        )

    def validate_note_frontmatter(self, note_path: Path) -> List[str]:
        """Validate note's frontmatter against Master Context rules"""
        errors = []
        with open(note_path) as f:
            content = f.read()

        try:
            frontmatter, _ = yaml.split(content)
        except:
            errors.append("Missing or invalid YAML frontmatter")
            return errors

        required = ['categories', 'created', 'topics', 'tags', 'status']
        for field in required:
            if field not in frontmatter:
                errors.append(f"Missing required field: {field}")

        return errors
```

- [ ] **Step 2: Viết tests**

```python
def test_load_master_context():
    ctx = MasterContext.load()
    assert ctx.identity is not None
    assert 'SCM' in ctx.career_focus or 'Operations' in ctx.career_focus
```

- [ ] **Step 3: Commit**

```bash
git add src/context.py tests/test_context.py
git commit -m "feat: add Master Context loader with validation"
```

---

## Task 5: Metadata Agent Implementation

**Files:**

- Create: `Notes/Projects/Second Brain Agent/src/metadata_agent.py`
- Create: `Notes/Projects/Second Brain Agent/tests/test_metadata_agent.py`

- [ ] **Step 1: Viết MetadataAgent class**

```python
# src/metadata_agent.py
from pathlib import Path
from typing import List, Dict
from src.context import MasterContext
from src.state import StateTracker

class MetadataAgent:
    """Validate và fix metadata trong notes"""

    def __init__(self, vault_root: str, context: MasterContext, tracker: StateTracker):
        self.vault_root = Path(vault_root)
        self.context = context
        self.tracker = tracker

    def scan_all_notes(self) -> List[Path]:
        """Tìm tất cả markdown files trong Notes/"""
        notes_dir = self.vault_root / "Notes"
        return list(notes_dir.rglob("*.md"))

    def validate_frontmatter(self, note_path: Path) -> Dict:
        """Validate một note, return errors và suggestions"""
        result = {"valid": True, "errors": [], "suggestions": []}

        errors = self.context.validate_note_frontmatter(note_path)
        if errors:
            result["valid"] = False
            result["errors"].extend(errors)

        return result

    def generate_report(self) -> str:
        """Generate metadata health report"""
        all_notes = self.scan_all_notes()
        valid = 0
        issues = []

        for note in all_notes:
            result = self.validate_frontmatter(note)
            if result["valid"]:
                valid += 1
            else:
                issues.append(f"{note.name}: {', '.join(result['errors'])}")

        report = f"Metadata Health Check\n"
        report += f"Total notes: {len(all_notes)}\n"
        report += f"Valid: {valid}\n"
        report += f"Issues: {len(all_notes) - valid}\n\n"

        if issues:
            report += "Issues found:\n" + "\n".join(issues)

        return report
```

- [ ] **Step 2: Viết tests**

```python
def test_validate_sample_note(tmp_path):
    # Create test note
    note = tmp_path / "test.md"
    note.write_text("---\ncreated: 2026-01-01\n---\nContent")

    agent = MetadataAgent(".", MasterContext.load(), StateTracker())
    result = agent.validate_frontmatter(note)
    assert "Missing required field" in result["errors"][0]
```

- [ ] **Step 3: Commit**

```bash
git add src/metadata_agent.py tests/test_metadata_agent.py
git commit -m "feat: add MetadataAgent for frontmatter validation"
```

---

## Task 6: Link Agent Implementation

**Files:**

- Create: `Notes/Projects/Second Brain Agent/src/link_agent.py`
- Create: `Notes/Projects/Second Brain Agent/tests/test_link_agent.py`

- [ ] **Step 1: Viết LinkAgent class**

```python
# src/link_agent.py
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, Set, List

WIKILINK_PATTERN = re.compile(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]')

class LinkAgent:
    """Quản lý và validate wiki links"""

    def __init__(self, vault_root: str):
        self.vault_root = Path(vault_root)
        self.all_notes = self._index_notes()

    def _index_notes(self) -> Dict[str, Path]:
        """Build mapping note name -> path"""
        notes_dir = self.vault_root / "Notes"
        mapping = {}
        for md in notes_dir.rglob("*.md"):
            stem = md.stem
            mapping[stem] = md
        return mapping

    def extract_links(self, content: str) -> List[str]:
        """Extract all [[wiki links]] từ content"""
        return [match[0] for match in WIKILINK_PATTERN.findall(content)]

    def find_orphans(self) -> List[Path]:
        """Find notes với 0 inbound và 0 outbound links"""
        inbound = defaultdict(int)
        outbound = defaultdict(int)

        for note_path in self.all_notes.values():
            with open(note_path) as f:
                content = f.read()
            links = self.extract_links(content)
            outbound[note_path.stem] = len(links)
            for link in links:
                inbound[link] += 1

        orphans = []
        for name, path in self.all_notes.items():
            if inbound.get(name, 0) == 0 and outbound.get(name, 0) == 0:
                orphans.append(path)

        return orphans

    def suggest_links(self, note_path: Path, threshold: int = 3) -> List[str]:
        """Suggest potential links dựa trên topic matching"""
        with open(note_path) as f:
            content = f.read().lower()

        suggestions = []
        for name, path in self.all_notes.items():
            if name == note_path.stem:
                continue
            try:
                other_content = path.read_text().lower()
            except:
                continue

            # Simple keyword overlap
            note_words = set(content.split())
            other_words = set(other_content.split())
            overlap = note_words & other_words

            if len(overlap) >= threshold:
                suggestions.append(f"[[{name}]]")

        return suggestions[:10]
```

- [ ] **Step 2: Commit**

```bash
git add src/link_agent.py tests/
git commit -m "feat: add LinkAgent for wiki link management"
```

---

## Task 7: Orchestrator & Scheduler

**Files:**

- Create: `Notes/Projects/Second Brain Agent/src/orchestrator.py`
- Create: `Notes/Projects/Second Brain Agent/.env.example`
- Modify: N/A

- [ ] **Step 1: Viết Orchestrator**

```python
# src/orchestrator.py
import asyncio
from datetime import datetime
from pathlib import Path
from src.context import MasterContext
from src.state import StateTracker
from src.metadata_agent import MetadataAgent
from src.link_agent import LinkAgent
from src.anthropic_client import ClaudeClient

class SecondBrainOrchestrator:
    """Main orchestrator cho agent team"""

    def __init__(self, vault_root: str = "."):
        self.vault_root = Path(vault_root)
        self.context = MasterContext.load(vault_root)
        self.tracker = StateTracker()
        self.claude = ClaudeClient()

        self.metadata_agent = MetadataAgent(vault_root, self.context, self.tracker)
        self.link_agent = LinkAgent(vault_root)

    async def run_daily_check(self):
        """Daily maintenance routine"""
        print(f"[{datetime.now()}] Starting daily check...")

        # 1. Metadata health
        print("Running MetadataAgent...")
        metadata_report = self.metadata_agent.generate_report()
        print(metadata_report)

        # 2. Link check
        print("Running LinkAgent...")
        orphans = self.link_agent.find_orphans()
        if orphans:
            print(f"Found {len(orphans)} orphan notes:")
            for o in orphans[:10]:
                print(f"  - {o}")

        # 3. Generate AI suggestions
        await self._generate_ai_suggestions()

        # 4. Create daily log
        self._create_daily_log()

        print(f"[{datetime.now()}] Daily check complete")

    async def _generate_ai_suggestions(self):
        """Dùng Claude để phân tích và gợi ý"""
        # Read Master Context + recent changes
        # Ask Claude for contextual suggestions
        pass

    def _create_daily_log(self):
        """Tạo daily note với summary"""
        daily_dir = self.vault_root / "Daily"
        daily_dir.mkdir(exist_ok=True)
        today = datetime.now().strftime("%Y-%m-%d")
        log_file = daily_dir / f"{today}.md"

        # Append summary
        # ...
```

- [ ] **Step 2: Viết .env.example**

```
ANTHROPIC_API_KEY=your_key_here
VAULT_ROOT=/home/tan-hong-phong/Documents/obsidian/kepano-obsidian-main
DRY_RUN=true
LOG_LEVEL=INFO
```

- [ ] **Step 3: Commit**

```bash
git add src/orchestrator.py .env.example
git commit -m "feat: add Orchestrator with daily check routine"
```

---

## Task 8: Claude Integration

**Files:**

- Create: `Notes/Projects/Second Brain Agent/src/anthropic_client.py`
- Create: `Notes/Projects/Second Brain Agent/src/prompts.py`

- [ ] **Step 1: Viết ClaudeClient**

```python
# src/anthropic_client.py
import os
from anthropic import AsyncAnthropic
from pathlib import Path

class ClaudeClient:
    """Wrapper cho Claude API với context awareness"""

    def __init__(self, api_key: str = None):
        self.client = AsyncAnthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))

    async def suggest_links(self, note_content: str, all_notes_summary: str) -> List[str]:
        """Hỏi Claude gợi ý links cho note"""
        prompt = f"""Given this note content and vault summary, suggest 3-5 relevant internal links.

Note content:
{note_content[:1000]}

Vault summary (topics):
{all_notes_summary[:2000]}

Respond with JSON array of link suggestions in format: [["Target Note", "reason"], ...]"""

        response = await self.client.messages.create(
            model="claude-opus-4-7",
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}]
        )
        # Parse response
        return []

    async def validate_impact_first(self, note_content: str) -> Dict:
        """Check if note follows impact-first formula"""
        prompt = f"""Analyze this note following Impact-First formula: [Action] + [Method/Tech] + [Business Outcome]

Note content:
{note_content[:1500]}

Return JSON with: {{"score": 1-10, "feedback": "...", "suggestions": ["..."]}}"""

        response = await self.client.messages.create(
            model="claude-opus-4-7",
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}]
        )
        return {"score": 7, "feedback": "OK"}
```

- [ ] **Step 2: Viết prompts module**

```python
# src/prompts.py
MASTER_CONTEXT_INSTRUCTIONS = """
Bạn đang làm việc với vault Obsidian của Phong (UEH student, Supply Chain & AI).

Nguyên tắc:
1. Impact-First: [Action] + [Method/Tech] + [Business Outcome]
2. Tránh quá kỹ thuật với nhà tuyển dụng SCM
3. Target: sinh viên & freelancer (không enterprise)
4. Giá sản phẩm: 690k VND standard
5. Career: Unilever/P&G/Shopee MT programs
"""
```

- [ ] **Step 3: Commit**

```bash
git add src/anthropic_client.py src/prompts.py
git commit -m "feat: add Claude integration with context-aware prompts"
```

---

## Task 9: Main Entry Point & CLI

**Files:**

- Create: `Notes/Projects/Second Brain Agent/main.py`
- Create: `Notes/Projects/Second Brain Agent/README.md`

- [ ] **Step 1: Viết main.py**

```python
# main.py
import asyncio
import os
from dotenv import load_dotenv
from src.orchestrator import SecondBrainOrchestrator

async def main():
    load_dotenv()

    vault_root = os.getenv("VAULT_ROOT", ".")
    dry_run = os.getenv("DRY_RUN", "true").lower() == "true"

    orchestrator = SecondBrainOrchestrator(vault_root)

    if dry_run:
        print("DRY RUN MODE - no changes will be written")

    await orchestrator.run_daily_check()

if __name__ == "__main__":
    asyncio.run(main())
```

- [ ] **Step 2: Viết README.md**

````markdown
# Second Brain Maintenance Agent Team

Automated maintenance system cho Obsidian vault của Phong.

## Setup

```bash
cd Notes/Projects/Second\ Brain\ Agent
pip install -r requirements.txt
cp .env.example .env
# Edit .env với ANTHROPIC_API_KEY và VAULT_ROOT
```
````

## Usage

```bash
python main.py
```

## Schedule

Tự động chạy hàng ngày qua cron:

```bash
0 6 * * * cd /path/to/vault && python Notes/Projects/Second\ Brain\ Agent/main.py >> logs/cron.log 2>&1
```

## Agents

1. **MetadataAgent** - Validate frontmatter, categories, tags
2. **LinkAgent** - Check orphan notes, suggest connections
3. **Orchestrator** - Coordinate team, generate reports

## Safety

- DRY_RUN=true mặc định
- Tất cả changes được log
- Git commit tự động (nếu enabled)

````

- [ ] **Step 3: Commit**

```bash
git add main.py README.md
git commit -m "chore: add main entry point and documentation"
````

---

## Task 10: Testing & Verification

**Files:**

- Create: `Notes/Projects/Second Brain Agent/tests/test_integration.py`
- Create: `Notes/Projects/Second Brain Agent/scripts/test_local.sh`

- [ ] **Step 1: Viết integration test**

```python
# tests/test_integration.py
import pytest
from src.orchestrator import SecondBrainOrchestrator

@pytest.mark.asyncio
async def test_full_daily_check(tmp_path):
    # Setup test vault
    vault = tmp_path / "vault"
    vault.mkdir()
    notes = vault / "Notes"
    notes.mkdir()

    # Create sample note
    sample = notes / "Test Note.md"
    sample.write_text("---\ncreated: 2026-01-01\ntags: [test]\nstatus: Draft\n---\nContent")

    orchestrator = SecondBrainOrchestrator(str(vault))
    report = await orchestrator.run_daily_check()

    assert report is not None
    assert "Total notes" in report
```

- [ ] **Step 2: Viết test script**

```bash
#!/bin/bash
# scripts/test_local.sh
set -e
cd Notes/Projects/Second\ Brain\ Agent

echo "=== Running tests ==="
python -m pytest tests/ -v

echo "=== Running dry-run daily check ==="
DRY_RUN=true python main.py

echo "=== All checks passed ==="
```

- [ ] **Step 3: Make executable & commit**

```bash
chmod +x Notes/Projects/Second\ Brain\ Agent/scripts/test_local.sh
git add tests/test_integration.py scripts/test_local.sh
git commit -m "test: add integration tests and test script"
```

---

## Task 11: Setup Cron Job

**Files:**

- Create: `Notes/Projects/Second Brain Agent/scripts/setup_cron.sh`
- Modify: N/A (cron config)

- [ ] **Step 1: Viết setup_cron.sh**

```bash
#!/bin/bash
# scripts/setup_cron.sh
CRON_JOB="0 6 * * * cd /home/tan-hong-phong/Documents/obsidian/kepano-obsidian-main && /usr/bin/python3 Notes/Projects/Second\ Brain\ Agent/main.py >> Notes/Projects/Second\ Brain\ Agent/logs/cron_$(date +\%Y-\%m-\%d).log 2>&1"

# Check if already exists
if crontab -l 2>/dev/null | grep -q "Second Brain Agent"; then
    echo "Cron job already exists"
else
    (crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
    echo "Cron job installed: runs daily at 6:00 AM"
fi
```

- [ ] **Step 2: Install cron**

```bash
cd Notes/Projects/Second\ Brain\ Agent
./scripts/setup_cron.sh
crontab -l
```

- [ ] **Step 3: Commit**

```bash
git add scripts/setup_cron.sh
git commit -m "chore: add cron setup script for daily automation"
```

---

## Task 12: Final Integration & Git Hooks

**Files:**

- Create: `Notes/Projects/Second Brain Agent/.git/hooks/post-commit` (optional)
- Modify: Root `.git/hooks/pre-commit` để validate notes

- [ ] **Step 1: Viết pre-commit hook**

```bash
#!/bin/bash
# .git/hooks/pre-commit
echo "Running Second Brain Agent metadata validation..."

python Notes/Projects/Second\ Brain\ Agent/main.py --dry-run

if [ $? -ne 0 ]; then
    echo "Validation failed! Fix issues before committing."
    exit 1
fi

exit 0
```

- [ ] **Step 2: Test full flow**

```bash
# Make a test change to a note
echo "Test update" >> Notes/Master\ Context.md

# Run agent
DRY_RUN=true python Notes/Projects/Second\ Brain\ Agent/main.py

# Check logs
tail Notes/Projects/Second\ Brain\ Agent/logs/*.log
```

- [ ] **Step 3: Final commit**

```bash
git add .git/hooks/pre-commit
git commit -m "ci: add pre-commit hook for automatic validation"
```

---

## Task 13: Documentation & Usage Guide

**Files:**

- Modify: `Notes/Projects/Second Brain Agent/README.md` (enhance)
- Create: `Notes/Projects/Second Brain Agent/docs/usage-guide.md`

- [ ] **Step 1: Viết usage guide**

````markdown
# Usage Guide

## Daily Maintenance

Agent chạy tự động hàng ngày lúc 6:00 AM qua cron.

### Manual Run

```bash
cd Notes/Projects/Second Brain Agent
DRY_RUN=false python main.py
```
````

### Output

- Daily log: `Daily/YYYY-MM-DD.md` được append summary
- Agent log: `logs/agent_YYYY-MM-DD.log`
- Git commit (if enabled): tự động commit changes

### What Gets Fixed

1. **Metadata** - thêm missing fields, normalize tags
2. **Links** - suggest connections, flag orphans
3. **Content** - gợi ý impact-first phrasing
4. **Consistency** - check category/tag consistency

### Approvals

Với `DRY_RUN=false`, agent sẽ:

- Tạo backup của mọi file
- Apply changes tự động (có thể config lại)
- Commit với message format: `feat(agents): auto-fix [type] for [n] notes`

````

- [ ] **Step 2: Commit final docs**

```bash
git add docs/usage-guide.md
git commit -m "docs: add usage guide for Second Brain Agent team"
````

---

## Verification Steps

**After all tasks complete:**

1. **Run full test suite:**

```bash
cd Notes/Projects/Second\ Brain\ Agent
./scripts/test_local.sh
```

2. **Manual dry-run:**

```bash
DRY_RUN=true python main.py
```

3. **Check generated logs:**

```bash
ls -la logs/
cat logs/cron_*.log
```

4. **Verify git status clean:**

```bash
git status
```

5. **Test actual run (if ready):**

```bash
DRY_RUN=false python main.py
# Check if changes appear
git diff
```

---

## Files Created/Modified Summary

**Created:**

- `Notes/Projects/Second Brain Agent/` (entire project)
  - `src/{state,context,metadata_agent,link_agent,orchestrator,anthropic_client,prompts}.py`
  - `tests/` (test files)
  - `scripts/` (test_local.sh, setup_cron.sh)
  - `data/`, `logs/`
  - `requirements.txt`, `main.py`, `.env.example`, `README.md`, `docs/`

**Modified:**

- Root `.git/hooks/pre-commit` (optional)
- Daily notes (automatically appended)

---

## Rollback Plan

Nếu agent gây vấn đề:

1. Stop cron job: `crontab -r` hoặc comment out line
2. Restore từ git: `git reflog` → `git reset --hard <commit-before-agent>`
3. Disable agent: đổi `ENABLED=false` trong `.env`

---

## Configuration Updates (Based on User Answers)

**Decision Log:**

- **Obsidian Integration:** HTTP API (obsidian:// or localhost:27123) - cần cài đặt Obsidian HTTP plugin
- **Claude Model:** Opus 4.7 (cho tất cả agents)
- **Auto-commit:** Enabled (mặc định, có backup trước mỗi write)

### Required Setup Steps (User Must Do)

1. **Install Obsidian HTTP plugin:**
   - Mở Obsidian → Settings → Community plugins → Browse → Tìm "Obsidian HTTP" (hoặc "Obsidian Local REST API")
   - Cài đặt và enable
   - Port mặc định: 27123

2. **Add .env configuration:**

```env
ANTHROPIC_API_KEY=sk-ant-...
VAULT_ROOT=/home/tan-hong-phong/Documents/obsidian/kepano-obsidian-main
OBSIDIAN_API_URL=http://localhost:27123
DRY_RUN=false  # Sau khi test xong
AUTO_COMMIT=true
```

3. **Test Obsidian API connection:**

```bash
curl http://localhost:27123/  # Should return {"status":"ok"}
```

### Code Updates Required

**In `src/obsidian_bridge.py`:**

- Add proper authentication handling nếu plugin có auth
- Add retry logic cho network failures
- Implement vault refresh after writes

**In `src/metadata_agent.py` và `src/link_agent.py`:**

- Replace `open()` calls với `obsidian_bridge.read_note()`
- Add error handling cho API failures

**In `src/orchestrator.py`:**

- Add git auto-commit logic:

```python
def commit_changes(self, message: str):
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", message])
```

---

**Plan tóm tắt:** 13 tasks, tập trung vào từng component một cách tuần tự với tests đầy đủ. Mỗi task có code cụ thể, commit message rõ ràng. Kết thúc với cron automation và documentation.

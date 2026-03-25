# BLUEPRINTS 1-10

## UAP MVP v0.1 — Step-by-Step Construction

**Instructions:** Follow blueprints IN ORDER. Each builds on the previous.  
**Method:** Copy-paste all code blocks directly into Cursor.

---

# BLUEPRINT 1: PROJECT SCAFFOLDING

## Goal
Create the complete folder structure and configuration files.

## Spec Requirements
- All folders from MVP_MAP.md must exist
- `.clinerules` must ban dangerous patterns
- `.gitignore` must exclude standard Python artifacts
- Git repository must be initialized

## Todo List

### Step 1.1: Create Root Folder
Open Cursor. Create a new folder called `uap-mvp`.

### Step 1.2: Create All Subfolders
In Cursor terminal, paste this ENTIRE block:

```bash
# Create all directories
mkdir -p config
mkdir -p memory
mkdir -p plan
mkdir -p src/gatekeeper
mkdir -p src/agent
mkdir -p src/tools
mkdir -p src/gates
mkdir -p tests
mkdir -p scripts
mkdir -p workspace/output

# Create __init__.py files for Python packages
touch src/__init__.py
touch src/gatekeeper/__init__.py
touch src/agent/__init__.py
touch src/tools/__init__.py
touch src/gates/__init__.py
touch tests/__init__.py

# Verify structure
find . -type d | head -20
```

### Step 1.3: Create .clinerules
Create file `.clinerules` in root folder. Paste this content:

```yaml
# .clinerules - Rules for AI assistants (Cursor, Cline, etc.)
# UAP MVP v0.1

# =============================================================================
# ABSOLUTE BANS (Agent MUST NOT do these)
# =============================================================================

banned_commands:
  - sed          # No text-based code manipulation
  - awk          # No text-based code manipulation
  - perl -pe     # No text-based code manipulation
  - "s/"         # No regex substitution on code

banned_patterns:
  - "import re"  # Only allowed in src/tools/banned_patterns.py
  - "re.sub"     # Never use regex on code files
  - ".replace("  # Use AST tools instead

# =============================================================================
# MANDATORY RULES (Agent MUST do these)
# =============================================================================

before_any_code_change:
  - Read memory/memory.json
  - Read plan/spec.md
  - Read plan/todo.md
  - Update plan/todo.md with current step

after_any_code_change:
  - Run: python -m pytest tests/ -v
  - Run: python -m pylint src/ --fail-under=7
  - Update memory/memory.json with results

for_code_modifications:
  - Use src/tools/ast_refactor.py
  - Never use string replacement
  - Never use regex on .py files

# =============================================================================
# FILE RULES
# =============================================================================

memory_json:
  location: memory/memory.json
  read: always at turn start
  write: always at turn end
  schema: memory/memory_schema.json

spec_md:
  location: plan/spec.md
  read: at turn start
  write: never (human only)

todo_md:
  location: plan/todo.md
  read: at turn start
  write: after each step completed

# =============================================================================
# QUALITY GATES
# =============================================================================

before_commit:
  - All tests must pass
  - Pylint score >= 7.0
  - No banned patterns in diff
  - todo.md must be updated

max_retries: 3
on_third_failure: escalate to human
```

### Step 1.4: Create .gitignore
Create file `.gitignore` in root folder. Paste:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
ENV/
env/
.venv/

# IDE
.idea/
.vscode/
*.swp
*.swo
.cursor/

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/
.nox/

# Local
*.log
*.local
.env
.env.local

# UAP specific
workspace/output/*
!workspace/output/.gitkeep
```

### Step 1.5: Create README.md
Create file `README.md` in root folder. Paste:

```markdown
# UAP MVP v0.1

Universal Agentic Protocol - Minimum Viable Product

## Quick Start

1. Install dependencies: `pip install -r requirements.txt`
2. Write task in `plan/spec.md`
3. Run: `python scripts/run_hello_world.py`

## Core Principles

- **MEM1**: Agent reads only from files, not chat history
- **AST-Only**: No regex/sed on code files
- **Cheap Gate**: All code must pass pytest + pylint

## Structure

See `plan/spec.md` for current task.
See `plan/todo.md` for progress.
See `memory/memory.json` for agent state.
```

### Step 1.6: Create config/agent_config.yaml
Create file `config/agent_config.yaml`. Paste:

```yaml
# Agent Configuration - UAP MVP v0.1

agent:
  name: "uap-agent-001"
  version: "0.1.0"
  
# Memory settings (MEM1)
memory:
  path: "memory/memory.json"
  schema_path: "memory/memory_schema.json"
  reset_on_commit: true

# Plan settings
plan:
  spec_path: "plan/spec.md"
  todo_path: "plan/todo.md"

# Quality gates
gates:
  pytest:
    enabled: true
    min_coverage: 0
    fail_fast: true
  pylint:
    enabled: true
    min_score: 7.0

# Limits
limits:
  max_retries: 3
  max_file_lines: 500
  max_tokens_per_turn: 10000

# Banned operations
banned:
  commands: ["sed", "awk", "perl"]
  patterns: ["re.sub", ".replace("]
```

### Step 1.7: Create requirements.txt
Create file `requirements.txt` in root folder. Paste:

```
pytest>=7.0.0
pylint>=2.15.0
pre-commit>=3.0.0
pyyaml>=6.0
jsonschema>=4.0.0
```

### Step 1.8: Initialize Git
In Cursor terminal, paste:

```bash
git init
git add .
git commit -m "BP1: Project scaffolding complete"
```

## Verification

Run these commands. ALL must succeed:

```bash
# Check folders exist
ls -la config memory plan src tests scripts workspace

# Check files exist
ls -la .clinerules .gitignore README.md requirements.txt

# Check git initialized
git status

# Install dependencies
pip install -r requirements.txt
```

**Expected Output:** No errors. All directories and files present.

---

# BLUEPRINT 2: MEMORY SYSTEM

## Goal
Implement the MEM1 constant-memory architecture.

## Spec Requirements
- `memory.json` stores agent state
- Schema validates memory structure
- Memory manager handles read/write
- Agent NEVER uses chat history

## Todo List

### Step 2.1: Create memory/memory_schema.json
Create file `memory/memory_schema.json`. Paste:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "UAP Agent Memory Schema",
  "type": "object",
  "required": ["agent_id", "session_id", "turn_count", "last_action", "status"],
  "properties": {
    "agent_id": {
      "type": "string",
      "description": "Unique identifier for this agent"
    },
    "session_id": {
      "type": "string",
      "description": "Current session identifier"
    },
    "turn_count": {
      "type": "integer",
      "minimum": 0,
      "description": "Number of turns completed"
    },
    "last_action": {
      "type": "string",
      "description": "Description of last action taken"
    },
    "status": {
      "type": "string",
      "enum": ["idle", "working", "blocked", "complete", "error"],
      "description": "Current agent status"
    },
    "files_modified": {
      "type": "array",
      "items": {"type": "string"},
      "description": "List of files changed in last turn"
    },
    "tests_passed": {
      "type": "integer",
      "minimum": 0,
      "description": "Number of tests passing"
    },
    "tests_failed": {
      "type": "integer",
      "minimum": 0,
      "description": "Number of tests failing"
    },
    "blockers": {
      "type": "array",
      "items": {"type": "string"},
      "description": "Current blockers preventing progress"
    },
    "error_log": {
      "type": "array",
      "items": {"type": "string"},
      "description": "Recent errors encountered"
    }
  }
}
```

### Step 2.2: Create memory/memory.json
Create file `memory/memory.json`. Paste:

```json
{
  "agent_id": "uap-agent-001",
  "session_id": "session-init",
  "turn_count": 0,
  "last_action": "initialized",
  "status": "idle",
  "files_modified": [],
  "tests_passed": 0,
  "tests_failed": 0,
  "blockers": [],
  "error_log": []
}
```

### Step 2.3: Create src/agent/memory_manager.py
Create file `src/agent/memory_manager.py`. Paste:

```python
"""
MEM1 Memory Manager - UAP MVP v0.1

The agent's ONLY persistent state. No chat history allowed.
"""

import json
import os
from datetime import datetime
from typing import Any, Dict, List, Optional
from pathlib import Path

# Use jsonschema if available, graceful fallback if not
try:
    import jsonschema
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False


class MemoryManager:
    """
    Implements MEM1 (Constant Memory) architecture.
    
    Core principle: Agent reads ONLY from files, never from chat history.
    """
    
    def __init__(
        self,
        memory_path: str = "memory/memory.json",
        schema_path: str = "memory/memory_schema.json"
    ):
        self.memory_path = Path(memory_path)
        self.schema_path = Path(schema_path)
        self._memory: Dict[str, Any] = {}
        self._schema: Optional[Dict[str, Any]] = None
        
        # Load schema if available
        if self.schema_path.exists() and HAS_JSONSCHEMA:
            with open(self.schema_path, 'r') as f:
                self._schema = json.load(f)
    
    def load(self) -> Dict[str, Any]:
        """
        Load memory from disk. This is the ONLY way agent gets state.
        """
        if not self.memory_path.exists():
            self._memory = self._create_default_memory()
            self.save()
        else:
            with open(self.memory_path, 'r') as f:
                self._memory = json.load(f)
        
        return self._memory.copy()
    
    def save(self) -> None:
        """
        Save memory to disk. Validates against schema first.
        """
        if self._schema and HAS_JSONSCHEMA:
            jsonschema.validate(self._memory, self._schema)
        
        # Ensure directory exists
        self.memory_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(self.memory_path, 'w') as f:
            json.dump(self._memory, f, indent=2)
    
    def update(self, **kwargs) -> None:
        """
        Update specific memory fields.
        """
        for key, value in kwargs.items():
            if key in self._memory or key in self._get_allowed_keys():
                self._memory[key] = value
        
        # Auto-increment turn count
        self._memory["turn_count"] = self._memory.get("turn_count", 0) + 1
        
        self.save()
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a memory value.
        """
        return self._memory.get(key, default)
    
    def add_to_list(self, key: str, value: str) -> None:
        """
        Append to a list field (e.g., files_modified, error_log).
        """
        if key not in self._memory:
            self._memory[key] = []
        if isinstance(self._memory[key], list):
            self._memory[key].append(value)
            self.save()
    
    def clear_list(self, key: str) -> None:
        """
        Clear a list field.
        """
        if key in self._memory and isinstance(self._memory[key], list):
            self._memory[key] = []
            self.save()
    
    def reset_session(self) -> None:
        """
        Reset for new session (Hard Reset).
        Preserves agent_id, resets everything else.
        """
        agent_id = self._memory.get("agent_id", "uap-agent-001")
        self._memory = self._create_default_memory()
        self._memory["agent_id"] = agent_id
        self._memory["session_id"] = f"session-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        self.save()
    
    def _create_default_memory(self) -> Dict[str, Any]:
        """
        Create default memory structure.
        """
        return {
            "agent_id": "uap-agent-001",
            "session_id": f"session-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
            "turn_count": 0,
            "last_action": "initialized",
            "status": "idle",
            "files_modified": [],
            "tests_passed": 0,
            "tests_failed": 0,
            "blockers": [],
            "error_log": []
        }
    
    def _get_allowed_keys(self) -> List[str]:
        """
        Get list of allowed memory keys from schema.
        """
        if self._schema:
            return list(self._schema.get("properties", {}).keys())
        return list(self._create_default_memory().keys())
    
    def __str__(self) -> str:
        return json.dumps(self._memory, indent=2)


# Convenience function for quick access
def get_memory() -> MemoryManager:
    """Get a memory manager instance."""
    return MemoryManager()
```

### Step 2.4: Create tests/test_memory.py
Create file `tests/test_memory.py`. Paste:

```python
"""Tests for MEM1 Memory Manager."""

import json
import os
import tempfile
import pytest
from pathlib import Path

from src.agent.memory_manager import MemoryManager


@pytest.fixture
def temp_memory_dir():
    """Create temporary directory for test memory files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir


@pytest.fixture
def memory_manager(temp_memory_dir):
    """Create a memory manager with temp paths."""
    memory_path = Path(temp_memory_dir) / "memory.json"
    schema_path = Path("memory/memory_schema.json")
    return MemoryManager(str(memory_path), str(schema_path))


class TestMemoryManager:
    """Test suite for MemoryManager."""
    
    def test_load_creates_default_if_missing(self, memory_manager):
        """Memory should create default state if file doesn't exist."""
        memory = memory_manager.load()
        
        assert memory["status"] == "idle"
        assert memory["turn_count"] == 0
        assert memory["files_modified"] == []
    
    def test_save_and_load_roundtrip(self, memory_manager):
        """Memory should persist across save/load."""
        memory_manager.load()
        memory_manager.update(status="working", last_action="testing")
        
        # Create new manager pointing to same file
        new_manager = MemoryManager(
            memory_manager.memory_path,
            memory_manager.schema_path
        )
        loaded = new_manager.load()
        
        assert loaded["status"] == "working"
        assert loaded["last_action"] == "testing"
    
    def test_update_increments_turn_count(self, memory_manager):
        """Each update should increment turn count."""
        memory_manager.load()
        initial_count = memory_manager.get("turn_count")
        
        memory_manager.update(status="working")
        
        assert memory_manager.get("turn_count") == initial_count + 1
    
    def test_add_to_list(self, memory_manager):
        """Should append to list fields."""
        memory_manager.load()
        memory_manager.add_to_list("files_modified", "test.py")
        memory_manager.add_to_list("files_modified", "main.py")
        
        assert memory_manager.get("files_modified") == ["test.py", "main.py"]
    
    def test_reset_session(self, memory_manager):
        """Reset should clear state but preserve agent_id."""
        memory_manager.load()
        original_agent_id = memory_manager.get("agent_id")
        memory_manager.update(status="working", turn_count=50)
        
        memory_manager.reset_session()
        
        assert memory_manager.get("agent_id") == original_agent_id
        assert memory_manager.get("turn_count") == 0
        assert memory_manager.get("status") == "idle"


class TestMEM1Principle:
    """Tests ensuring MEM1 principle is followed."""
    
    def test_no_chat_history_dependency(self, memory_manager):
        """Memory should work without any chat context."""
        # Load memory in isolation (no chat history available)
        memory = memory_manager.load()
        
        # Should have all required fields
        assert "agent_id" in memory
        assert "status" in memory
        assert "turn_count" in memory
    
    def test_state_survives_reload(self, memory_manager):
        """State should survive complete reload (simulating new context)."""
        memory_manager.load()
        memory_manager.update(
            status="working",
            last_action="processing task",
            tests_passed=5
        )
        
        # Simulate context death and rebirth
        del memory_manager
        
        # New manager (fresh context) should see same state
        fresh_manager = MemoryManager(
            str(Path(memory_manager.memory_path)),
            str(Path(memory_manager.schema_path))
        )
        fresh_memory = fresh_manager.load()
        
        assert fresh_memory["status"] == "working"
        assert fresh_memory["tests_passed"] == 5
```

### Step 2.5: Run Tests
In Cursor terminal, paste:

```bash
python -m pytest tests/test_memory.py -v
```

## Verification

```bash
# All tests should pass
python -m pytest tests/test_memory.py -v

# Check memory.json exists and is valid JSON
python -c "import json; print(json.load(open('memory/memory.json')))"

# Commit
git add .
git commit -m "BP2: Memory system (MEM1) complete"
```

**Expected Output:** All tests pass. Memory loads/saves correctly.

---

# BLUEPRINT 3: LIVING PLAN

## Goal
Create the spec.md and todo.md templates that drive the agent.

## Spec Requirements
- `spec.md` defines what to build (human writes, agent reads)
- `todo.md` tracks progress (agent updates)
- Clear format that's easy to parse

## Todo List

### Step 3.1: Create plan/spec.md Template
Create file `plan/spec.md`. Paste:

```markdown
# SPEC: [Task ID]

## Status: DRAFT | APPROVED | IN_PROGRESS | COMPLETE

## Objective
[One sentence describing what needs to be built]

## Requirements
- [ ] Requirement 1
- [ ] Requirement 2
- [ ] Requirement 3

## Constraints
- Max file size: 500 lines
- Max complexity: 20 (cyclomatic)
- Test coverage: >= 80%
- No regex on code files

## Inputs
[What the agent receives]

## Expected Output
[What the agent must produce]

## Success Criteria
- [ ] All requirements implemented
- [ ] All tests pass
- [ ] Pylint score >= 7.0
- [ ] No banned patterns used

## Notes
[Any additional context]
```

### Step 3.2: Create plan/todo.md Template
Create file `plan/todo.md`. Paste:

```markdown
# TODO: [Task ID]

## Current Status: NOT_STARTED | IN_PROGRESS | BLOCKED | COMPLETE

## Progress

### Phase 1: Setup
- [ ] Read spec.md
- [ ] Read memory.json
- [ ] Plan implementation

### Phase 2: Implementation
- [ ] Step 1: [description]
- [ ] Step 2: [description]
- [ ] Step 3: [description]

### Phase 3: Verification
- [ ] Run tests
- [ ] Check coverage
- [ ] Run pylint
- [ ] Update memory.json

## Current Focus
[What the agent is working on RIGHT NOW]

## Blockers
[List any blockers, or "None"]

## Completed Steps
[List completed items with timestamps]

## Notes
[Observations during implementation]
```

### Step 3.3: Create tests/conftest.py
Create file `tests/conftest.py`. Paste:

```python
"""Pytest configuration and fixtures."""

import pytest
from pathlib import Path


@pytest.fixture
def project_root():
    """Get project root directory."""
    return Path(__file__).parent.parent


@pytest.fixture
def spec_path(project_root):
    """Get spec.md path."""
    return project_root / "plan" / "spec.md"


@pytest.fixture
def todo_path(project_root):
    """Get todo.md path."""
    return project_root / "plan" / "todo.md"


@pytest.fixture
def memory_path(project_root):
    """Get memory.json path."""
    return project_root / "memory" / "memory.json"
```

### Step 3.4: Commit
In Cursor terminal, paste:

```bash
git add .
git commit -m "BP3: Living Plan templates complete"
```

## Verification

```bash
# Check files exist
cat plan/spec.md
cat plan/todo.md

# Files should contain template structure
grep "SPEC:" plan/spec.md
grep "TODO:" plan/todo.md
```

**Expected Output:** Both files exist with proper templates.

---

# BLUEPRINT 4: GATEKEEPER LITE

## Goal
Validate that spec.md is not empty before agent starts.

## Spec Requirements
- Check spec.md exists
- Check spec.md has content (not just template)
- Check required sections present
- Block agent if spec invalid

## Todo List

### Step 4.1: Create src/gatekeeper/validator.py
Create file `src/gatekeeper/validator.py`. Paste:

```python
"""
Gatekeeper Lite - Spec Validation
UAP MVP v0.1

Validates spec.md before agent is allowed to start.
"""

import re
from pathlib import Path
from typing import Tuple, List
from dataclasses import dataclass


@dataclass
class ValidationResult:
    """Result of spec validation."""
    is_valid: bool
    errors: List[str]
    warnings: List[str]


class GatekeeperLite:
    """
    Validates spec.md before agent execution.
    
    Rules:
    1. spec.md must exist
    2. spec.md must not be empty
    3. spec.md must have Objective section with content
    4. spec.md must have at least one Requirement
    """
    
    REQUIRED_SECTIONS = ["Objective", "Requirements"]
    
    def __init__(self, spec_path: str = "plan/spec.md"):
        self.spec_path = Path(spec_path)
    
    def validate(self) -> ValidationResult:
        """
        Validate the spec file.
        
        Returns:
            ValidationResult with is_valid, errors, warnings
        """
        errors: List[str] = []
        warnings: List[str] = []
        
        # Check 1: File exists
        if not self.spec_path.exists():
            errors.append(f"spec.md not found at {self.spec_path}")
            return ValidationResult(False, errors, warnings)
        
        # Read content
        content = self.spec_path.read_text()
        
        # Check 2: Not empty
        if len(content.strip()) < 50:
            errors.append("spec.md is too short (< 50 chars). Please fill in the template.")
            return ValidationResult(False, errors, warnings)
        
        # Check 3: Has placeholder text
        if "[Task ID]" in content or "[One sentence" in content:
            errors.append("spec.md still contains placeholder text. Please fill in actual values.")
            return ValidationResult(False, errors, warnings)
        
        # Check 4: Required sections present
        for section in self.REQUIRED_SECTIONS:
            if f"## {section}" not in content:
                errors.append(f"Missing required section: ## {section}")
        
        if errors:
            return ValidationResult(False, errors, warnings)
        
        # Check 5: Objective has content
        objective_match = re.search(
            r'## Objective\s*\n(.*?)(?=\n##|\Z)',
            content,
            re.DOTALL
        )
        if objective_match:
            objective_content = objective_match.group(1).strip()
            if len(objective_content) < 10:
                errors.append("Objective section is too short. Please describe the task.")
        else:
            errors.append("Could not parse Objective section.")
        
        # Check 6: Has at least one requirement
        if "- [ ]" not in content and "- [x]" not in content:
            warnings.append("No checkbox requirements found. Consider adding specific requirements.")
        
        # Check 7: Status is set
        if "Status: DRAFT" in content:
            warnings.append("Spec status is DRAFT. Change to APPROVED when ready.")
        
        return ValidationResult(len(errors) == 0, errors, warnings)
    
    def gate(self) -> bool:
        """
        Gate function - returns True if agent can proceed, False otherwise.
        Prints errors/warnings to console.
        """
        result = self.validate()
        
        if result.errors:
            print("❌ GATEKEEPER: Spec validation FAILED")
            for error in result.errors:
                print(f"   ERROR: {error}")
            return False
        
        if result.warnings:
            print("⚠️  GATEKEEPER: Spec validation passed with warnings")
            for warning in result.warnings:
                print(f"   WARNING: {warning}")
        else:
            print("✅ GATEKEEPER: Spec validation PASSED")
        
        return True


def validate_spec(spec_path: str = "plan/spec.md") -> bool:
    """Convenience function to validate spec."""
    gatekeeper = GatekeeperLite(spec_path)
    return gatekeeper.gate()
```

### Step 4.2: Create tests/test_gatekeeper.py
Create file `tests/test_gatekeeper.py`. Paste:

```python
"""Tests for Gatekeeper Lite."""

import tempfile
import pytest
from pathlib import Path

from src.gatekeeper.validator import GatekeeperLite, ValidationResult


@pytest.fixture
def temp_spec_dir():
    """Create temporary directory for test spec files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


class TestGatekeeperLite:
    """Test suite for GatekeeperLite."""
    
    def test_missing_file_fails(self, temp_spec_dir):
        """Should fail if spec.md doesn't exist."""
        gatekeeper = GatekeeperLite(str(temp_spec_dir / "nonexistent.md"))
        result = gatekeeper.validate()
        
        assert result.is_valid is False
        assert "not found" in result.errors[0]
    
    def test_empty_file_fails(self, temp_spec_dir):
        """Should fail if spec.md is empty."""
        spec_path = temp_spec_dir / "spec.md"
        spec_path.write_text("")
        
        gatekeeper = GatekeeperLite(str(spec_path))
        result = gatekeeper.validate()
        
        assert result.is_valid is False
        assert "too short" in result.errors[0]
    
    def test_template_placeholder_fails(self, temp_spec_dir):
        """Should fail if spec still has placeholder text."""
        spec_path = temp_spec_dir / "spec.md"
        spec_path.write_text("""
# SPEC: [Task ID]

## Objective
[One sentence describing what needs to be built]

## Requirements
- [ ] Requirement 1
""")
        
        gatekeeper = GatekeeperLite(str(spec_path))
        result = gatekeeper.validate()
        
        assert result.is_valid is False
        assert "placeholder" in result.errors[0]
    
    def test_valid_spec_passes(self, temp_spec_dir):
        """Should pass with a properly filled spec."""
        spec_path = temp_spec_dir / "spec.md"
        spec_path.write_text("""
# SPEC: test-001

## Status: APPROVED

## Objective
Create a Python function that adds two numbers and returns the result.

## Requirements
- [ ] Function named 'add'
- [ ] Takes two parameters
- [ ] Returns sum

## Constraints
- Max file size: 500 lines

## Success Criteria
- [ ] All tests pass
""")
        
        gatekeeper = GatekeeperLite(str(spec_path))
        result = gatekeeper.validate()
        
        assert result.is_valid is True
        assert len(result.errors) == 0
    
    def test_missing_objective_fails(self, temp_spec_dir):
        """Should fail if Objective section is missing."""
        spec_path = temp_spec_dir / "spec.md"
        spec_path.write_text("""
# SPEC: test-001

## Requirements
- [ ] Something to do

## Other Section
Content here
""")
        
        gatekeeper = GatekeeperLite(str(spec_path))
        result = gatekeeper.validate()
        
        assert result.is_valid is False
        assert any("Objective" in e for e in result.errors)
```

### Step 4.3: Run Tests
```bash
python -m pytest tests/test_gatekeeper.py -v
```

### Step 4.4: Commit
```bash
git add .
git commit -m "BP4: Gatekeeper Lite complete"
```

## Verification

```bash
# Tests pass
python -m pytest tests/test_gatekeeper.py -v

# Test with actual spec (should fail - still template)
python -c "from src.gatekeeper.validator import validate_spec; validate_spec()"
```

**Expected Output:** Tests pass. Actual spec validation fails (expected - still template).

---

# BLUEPRINT 5: AST TOOLING

## Goal
Set up AST-based code modification tools.

## Spec Requirements
- Parse Python files using AST
- Rename variables without regex
- Add/remove imports without regex
- Modify function signatures without regex

## Todo List

### Step 5.1: Create src/tools/ast_refactor.py
Create file `src/tools/ast_refactor.py`. Paste:

```python
"""
AST-Based Code Refactoring Tools
UAP MVP v0.1

All code modifications MUST use these tools.
NEVER use regex, sed, awk, or string.replace() on code.
"""

import ast
from pathlib import Path
from typing import Optional, List, Set


class ASTRefactor:
    """
    AST-based code modification tools.
    
    These tools parse code into an Abstract Syntax Tree, modify the tree,
    and write it back. This ensures syntactically correct modifications.
    """
    
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self._source: Optional[str] = None
        self._tree: Optional[ast.AST] = None
    
    def load(self) -> 'ASTRefactor':
        """Load and parse the source file."""
        self._source = self.file_path.read_text()
        self._tree = ast.parse(self._source)
        return self
    
    def save(self) -> None:
        """Write the modified AST back to file."""
        if self._tree is None:
            raise ValueError("No AST loaded. Call load() first.")
        
        # Use ast.unparse (Python 3.9+) to convert AST back to source
        new_source = ast.unparse(self._tree)
        self.file_path.write_text(new_source)
    
    def get_function_names(self) -> List[str]:
        """Get all function names in the file."""
        if self._tree is None:
            self.load()
        
        names = []
        for node in ast.walk(self._tree):
            if isinstance(node, ast.FunctionDef):
                names.append(node.name)
        return names
    
    def get_class_names(self) -> List[str]:
        """Get all class names in the file."""
        if self._tree is None:
            self.load()
        
        names = []
        for node in ast.walk(self._tree):
            if isinstance(node, ast.ClassDef):
                names.append(node.name)
        return names
    
    def get_imports(self) -> Set[str]:
        """Get all imported module names."""
        if self._tree is None:
            self.load()
        
        imports = set()
        for node in ast.walk(self._tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module)
        return imports
    
    def rename_function(self, old_name: str, new_name: str) -> bool:
        """
        Rename a function throughout the file.
        Returns True if function was found and renamed.
        """
        if self._tree is None:
            self.load()
        
        found = False
        
        class FunctionRenamer(ast.NodeTransformer):
            def visit_FunctionDef(self, node):
                nonlocal found
                if node.name == old_name:
                    node.name = new_name
                    found = True
                return self.generic_visit(node)
            
            def visit_Call(self, node):
                if isinstance(node.func, ast.Name) and node.func.id == old_name:
                    node.func.id = new_name
                return self.generic_visit(node)
        
        self._tree = FunctionRenamer().visit(self._tree)
        ast.fix_missing_locations(self._tree)
        return found
    
    def rename_variable(self, old_name: str, new_name: str) -> int:
        """
        Rename a variable throughout the file.
        Returns count of replacements made.
        """
        if self._tree is None:
            self.load()
        
        count = 0
        
        class VariableRenamer(ast.NodeTransformer):
            def visit_Name(self, node):
                nonlocal count
                if node.id == old_name:
                    node.id = new_name
                    count += 1
                return node
        
        self._tree = VariableRenamer().visit(self._tree)
        ast.fix_missing_locations(self._tree)
        return count
    
    def add_import(self, module: str, names: Optional[List[str]] = None) -> None:
        """
        Add an import statement at the top of the file.
        
        Args:
            module: Module name (e.g., 'os', 'pathlib')
            names: Optional list of names to import (for 'from X import Y')
        """
        if self._tree is None:
            self.load()
        
        if names:
            # from module import names
            import_node = ast.ImportFrom(
                module=module,
                names=[ast.alias(name=n, asname=None) for n in names],
                level=0
            )
        else:
            # import module
            import_node = ast.Import(
                names=[ast.alias(name=module, asname=None)]
            )
        
        # Insert at beginning of file (after docstring if present)
        insert_idx = 0
        if (self._tree.body and 
            isinstance(self._tree.body[0], ast.Expr) and
            isinstance(self._tree.body[0].value, ast.Constant)):
            insert_idx = 1
        
        self._tree.body.insert(insert_idx, import_node)
        ast.fix_missing_locations(self._tree)


def rename_in_file(file_path: str, old_name: str, new_name: str) -> bool:
    """
    Convenience function to rename a function in a file.
    
    Usage:
        rename_in_file("src/main.py", "old_func", "new_func")
    """
    refactor = ASTRefactor(file_path)
    refactor.load()
    result = refactor.rename_function(old_name, new_name)
    if result:
        refactor.save()
    return result


def analyze_file(file_path: str) -> dict:
    """
    Analyze a Python file and return its structure.
    
    Usage:
        info = analyze_file("src/main.py")
        print(info["functions"])  # ['main', 'helper']
    """
    refactor = ASTRefactor(file_path)
    refactor.load()
    return {
        "functions": refactor.get_function_names(),
        "classes": refactor.get_class_names(),
        "imports": list(refactor.get_imports())
    }
```

### Step 5.2: Create tests/test_ast_tools.py
Create file `tests/test_ast_tools.py`. Paste:

```python
"""Tests for AST refactoring tools."""

import tempfile
import pytest
from pathlib import Path

from src.tools.ast_refactor import ASTRefactor, rename_in_file, analyze_file


@pytest.fixture
def temp_python_file():
    """Create a temporary Python file for testing."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write('''
def hello():
    """Say hello."""
    message = "Hello"
    return message

def greet(name):
    """Greet someone."""
    return hello() + ", " + name
''')
        f.flush()
        yield Path(f.name)


class TestASTRefactor:
    """Test suite for ASTRefactor."""
    
    def test_get_function_names(self, temp_python_file):
        """Should list all functions in file."""
        refactor = ASTRefactor(str(temp_python_file))
        refactor.load()
        
        names = refactor.get_function_names()
        
        assert "hello" in names
        assert "greet" in names
    
    def test_rename_function(self, temp_python_file):
        """Should rename function and its calls."""
        refactor = ASTRefactor(str(temp_python_file))
        refactor.load()
        
        result = refactor.rename_function("hello", "say_hello")
        refactor.save()
        
        assert result is True
        
        # Verify by re-parsing
        new_refactor = ASTRefactor(str(temp_python_file))
        new_refactor.load()
        names = new_refactor.get_function_names()
        
        assert "say_hello" in names
        assert "hello" not in names
    
    def test_rename_variable(self, temp_python_file):
        """Should rename variable throughout file."""
        refactor = ASTRefactor(str(temp_python_file))
        refactor.load()
        
        count = refactor.rename_variable("message", "msg")
        refactor.save()
        
        assert count >= 2  # Defined and returned
        
        # Verify by checking content
        content = temp_python_file.read_text()
        assert "msg" in content
    
    def test_add_import(self, temp_python_file):
        """Should add import statement."""
        refactor = ASTRefactor(str(temp_python_file))
        refactor.load()
        
        refactor.add_import("os")
        refactor.save()
        
        # Verify
        refactor2 = ASTRefactor(str(temp_python_file))
        refactor2.load()
        imports = refactor2.get_imports()
        
        assert "os" in imports


class TestConvenienceFunctions:
    """Test convenience functions."""
    
    def test_rename_in_file(self, temp_python_file):
        """rename_in_file should work as a one-liner."""
        result = rename_in_file(str(temp_python_file), "hello", "hi")
        
        assert result is True
        
        info = analyze_file(str(temp_python_file))
        assert "hi" in info["functions"]
    
    def test_analyze_file(self, temp_python_file):
        """analyze_file should return file structure."""
        info = analyze_file(str(temp_python_file))
        
        assert "functions" in info
        assert "classes" in info
        assert "imports" in info
        assert "hello" in info["functions"]
```

### Step 5.3: Run Tests
```bash
python -m pytest tests/test_ast_tools.py -v
```

### Step 5.4: Commit
```bash
git add .
git commit -m "BP5: AST tooling complete"
```

## Verification

```bash
# Tests pass
python -m pytest tests/test_ast_tools.py -v

# Quick demo
python -c "from src.tools.ast_refactor import analyze_file; print(analyze_file('src/tools/ast_refactor.py'))"
```

**Expected Output:** Tests pass. Analyze shows functions/classes in file.

---

# BLUEPRINT 6: REGEX BAN

## Goal
Create a pre-commit hook that blocks regex/sed/awk on Python files.

## Spec Requirements
- Detect banned patterns in git diff
- Block commit if violations found
- Clear error messages

## Todo List

### Step 6.1: Create src/tools/banned_patterns.py
Create file `src/tools/banned_patterns.py`. Paste:

```python
"""
Banned Pattern Detection
UAP MVP v0.1

Detects forbidden patterns (sed, awk, regex on code) in diffs.
"""

import re
import subprocess
import sys
from typing import List, Tuple


# Patterns that are NEVER allowed on .py files
BANNED_PATTERNS = [
    (r'\bsed\s+', "sed command detected"),
    (r'\bawk\s+', "awk command detected"),
    (r'\bperl\s+-[a-z]*p', "perl in-place edit detected"),
    (r're\.sub\s*\(', "re.sub() detected - use AST tools"),
    (r're\.subn\s*\(', "re.subn() detected - use AST tools"),
    (r'\.replace\s*\(["\'][^"\']+["\']', "string.replace() on code detected - use AST tools"),
]

# Files where regex IS allowed (for pattern detection itself)
ALLOWED_FILES = [
    "src/tools/banned_patterns.py",
    "src/gatekeeper/validator.py",  # Uses regex on markdown, not code
]


def check_diff_for_banned_patterns() -> List[Tuple[str, str, str]]:
    """
    Check staged git diff for banned patterns.
    
    Returns:
        List of (filename, line, violation_message) tuples
    """
    violations = []
    
    try:
        # Get staged diff
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only"],
            capture_output=True,
            text=True,
            check=True
        )
        changed_files = result.stdout.strip().split('\n')
    except subprocess.CalledProcessError:
        return []  # Not a git repo or no changes
    
    for filepath in changed_files:
        if not filepath.endswith('.py'):
            continue
        
        if any(filepath.endswith(allowed) for allowed in ALLOWED_FILES):
            continue
        
        try:
            # Get diff for this file
            result = subprocess.run(
                ["git", "diff", "--cached", filepath],
                capture_output=True,
                text=True,
                check=True
            )
            diff_content = result.stdout
        except subprocess.CalledProcessError:
            continue
        
        # Check each added line
        for line in diff_content.split('\n'):
            if not line.startswith('+'):
                continue
            if line.startswith('+++'):
                continue
            
            for pattern, message in BANNED_PATTERNS:
                if re.search(pattern, line):
                    violations.append((filepath, line[1:].strip(), message))
    
    return violations


def check_file_for_banned_patterns(filepath: str) -> List[Tuple[int, str, str]]:
    """
    Check a single file for banned patterns.
    
    Returns:
        List of (line_number, line_content, violation_message) tuples
    """
    violations = []
    
    if any(filepath.endswith(allowed) for allowed in ALLOWED_FILES):
        return []
    
    try:
        with open(filepath, 'r') as f:
            for line_num, line in enumerate(f, 1):
                for pattern, message in BANNED_PATTERNS:
                    if re.search(pattern, line):
                        violations.append((line_num, line.strip(), message))
    except FileNotFoundError:
        pass
    
    return violations


def main() -> int:
    """
    Pre-commit hook entry point.
    Returns 0 if OK, 1 if violations found.
    """
    violations = check_diff_for_banned_patterns()
    
    if violations:
        print("❌ REGEX BAN: Commit blocked due to banned patterns!")
        print("")
        for filepath, line, message in violations:
            print(f"  File: {filepath}")
            print(f"  Line: {line[:60]}...")
            print(f"  Violation: {message}")
            print("")
        print("Use AST tools instead: src/tools/ast_refactor.py")
        return 1
    
    print("✅ REGEX BAN: No banned patterns detected")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

### Step 6.2: Create .pre-commit-config.yaml
Create file `.pre-commit-config.yaml` in root. Paste:

```yaml
# Pre-commit hooks for UAP MVP v0.1
# Install: pip install pre-commit && pre-commit install

repos:
  # Local hooks
  - repo: local
    hooks:
      - id: regex-ban
        name: Check for banned patterns (sed/awk/regex)
        entry: python src/tools/banned_patterns.py
        language: system
        types: [python]
        pass_filenames: false
      
      - id: pytest
        name: Run pytest
        entry: python -m pytest tests/ -v --tb=short
        language: system
        types: [python]
        pass_filenames: false
        stages: [commit]
      
      - id: pylint
        name: Run pylint
        entry: python -m pylint src/ --fail-under=7
        language: system
        types: [python]
        pass_filenames: false
        stages: [commit]
```

### Step 6.3: Install Pre-commit Hooks
In Cursor terminal, paste:

```bash
pip install pre-commit
pre-commit install
```

### Step 6.4: Test the Hook
Create a test file that violates the rules:

```bash
# This should be BLOCKED
echo 'import re
result = re.sub("old", "new", text)' > workspace/output/bad_code.py

git add workspace/output/bad_code.py
git commit -m "Test commit"  # Should fail!

# Clean up
rm workspace/output/bad_code.py
git reset HEAD workspace/output/bad_code.py
```

### Step 6.5: Commit (Clean Files Only)
```bash
git add .clinerules src/tools/banned_patterns.py .pre-commit-config.yaml
git commit -m "BP6: Regex ban complete" --no-verify  # Skip hooks for this meta-commit
```

## Verification

```bash
# Pre-commit is installed
pre-commit --version

# Hooks are configured
cat .pre-commit-config.yaml

# Test detection
python src/tools/banned_patterns.py
```

**Expected Output:** Pre-commit installed. Hook config present.

---

# BLUEPRINT 7: CHEAP GATE

## Goal
Create pytest + pylint runner for quality gate.

## Spec Requirements
- Run pytest on tests/ directory
- Run pylint on src/ directory
- Return pass/fail status
- Integrate with pre-commit

## Todo List

### Step 7.1: Create src/gates/cheap_gate.py
Create file `src/gates/cheap_gate.py`. Paste:

```python
"""
Cheap Gate - Quality Gate Runner
UAP MVP v0.1

Runs pytest and pylint before code is accepted.
"""

import subprocess
import sys
from dataclasses import dataclass
from typing import Optional


@dataclass
class GateResult:
    """Result of running quality gates."""
    pytest_passed: bool
    pytest_output: str
    pylint_passed: bool
    pylint_score: float
    pylint_output: str
    
    @property
    def passed(self) -> bool:
        return self.pytest_passed and self.pylint_passed


class CheapGate:
    """
    Runs pytest and pylint quality gates.
    """
    
    def __init__(
        self,
        test_path: str = "tests/",
        src_path: str = "src/",
        pylint_min_score: float = 7.0
    ):
        self.test_path = test_path
        self.src_path = src_path
        self.pylint_min_score = pylint_min_score
    
    def run_pytest(self) -> tuple[bool, str]:
        """
        Run pytest on test directory.
        
        Returns:
            (passed, output)
        """
        try:
            result = subprocess.run(
                ["python", "-m", "pytest", self.test_path, "-v", "--tb=short"],
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )
            passed = result.returncode == 0
            output = result.stdout + result.stderr
            return passed, output
        except subprocess.TimeoutExpired:
            return False, "pytest timed out after 5 minutes"
        except Exception as e:
            return False, f"pytest error: {e}"
    
    def run_pylint(self) -> tuple[bool, float, str]:
        """
        Run pylint on source directory.
        
        Returns:
            (passed, score, output)
        """
        try:
            result = subprocess.run(
                ["python", "-m", "pylint", self.src_path, "--output-format=text"],
                capture_output=True,
                text=True,
                timeout=120  # 2 minute timeout
            )
            output = result.stdout + result.stderr
            
            # Extract score from output
            score = 0.0
            for line in output.split('\n'):
                if "Your code has been rated at" in line:
                    # Format: "Your code has been rated at X.XX/10"
                    try:
                        score_str = line.split("at ")[1].split("/")[0]
                        score = float(score_str)
                    except (IndexError, ValueError):
                        pass
            
            passed = score >= self.pylint_min_score
            return passed, score, output
        except subprocess.TimeoutExpired:
            return False, 0.0, "pylint timed out after 2 minutes"
        except Exception as e:
            return False, 0.0, f"pylint error: {e}"
    
    def run_all(self) -> GateResult:
        """
        Run all quality gates.
        
        Returns:
            GateResult with all results
        """
        pytest_passed, pytest_output = self.run_pytest()
        pylint_passed, pylint_score, pylint_output = self.run_pylint()
        
        return GateResult(
            pytest_passed=pytest_passed,
            pytest_output=pytest_output,
            pylint_passed=pylint_passed,
            pylint_score=pylint_score,
            pylint_output=pylint_output
        )
    
    def gate(self) -> bool:
        """
        Run gates and print summary.
        Returns True if all gates pass.
        """
        print("=" * 60)
        print("CHEAP GATE: Running quality checks...")
        print("=" * 60)
        
        result = self.run_all()
        
        # Pytest results
        if result.pytest_passed:
            print(f"✅ pytest: PASSED")
        else:
            print(f"❌ pytest: FAILED")
            print(result.pytest_output[-500:])  # Last 500 chars
        
        # Pylint results
        if result.pylint_passed:
            print(f"✅ pylint: PASSED ({result.pylint_score:.2f}/10)")
        else:
            print(f"❌ pylint: FAILED ({result.pylint_score:.2f}/10, need {self.pylint_min_score})")
        
        print("=" * 60)
        
        if result.passed:
            print("✅ CHEAP GATE: ALL CHECKS PASSED")
        else:
            print("❌ CHEAP GATE: CHECKS FAILED")
        
        return result.passed


def run_cheap_gate() -> bool:
    """Convenience function to run cheap gate."""
    gate = CheapGate()
    return gate.gate()


if __name__ == "__main__":
    success = run_cheap_gate()
    sys.exit(0 if success else 1)
```

### Step 7.2: Test the Gate
```bash
python src/gates/cheap_gate.py
```

### Step 7.3: Commit
```bash
git add .
git commit -m "BP7: Cheap Gate complete"
```

## Verification

```bash
# Run the gate
python src/gates/cheap_gate.py

# Should see pytest and pylint results
```

**Expected Output:** Both pytest and pylint run. May show warnings but should pass.

---

# BLUEPRINT 8: AGENT LOOP

## Goal
Create the main agent execution loop.

## Spec Requirements
- Read from files only (MEM1)
- Update todo.md after each step
- Update memory.json after each turn
- Integrate with gatekeeper

## Todo List

### Step 8.1: Create src/agent/loop.py
Create file `src/agent/loop.py`. Paste:

```python
"""
Agent Loop - Main Execution Engine
UAP MVP v0.1

Implements MEM1: Agent reads ONLY from files, never from chat history.
"""

import sys
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any

from src.agent.memory_manager import MemoryManager
from src.gatekeeper.validator import GatekeeperLite
from src.gates.cheap_gate import CheapGate


class AgentLoop:
    """
    Main agent execution loop.
    
    MEM1 Principle: At the start of every turn, the agent reads:
    1. memory/memory.json (its state)
    2. plan/spec.md (what to build)
    3. plan/todo.md (current progress)
    
    The agent has NO access to chat history.
    """
    
    def __init__(
        self,
        memory_path: str = "memory/memory.json",
        spec_path: str = "plan/spec.md",
        todo_path: str = "plan/todo.md"
    ):
        self.memory = MemoryManager(memory_path)
        self.gatekeeper = GatekeeperLite(spec_path)
        self.cheap_gate = CheapGate()
        
        self.spec_path = Path(spec_path)
        self.todo_path = Path(todo_path)
    
    def load_context(self) -> Dict[str, Any]:
        """
        Load all context from files.
        This is the ONLY way the agent gets information.
        """
        context = {
            "memory": self.memory.load(),
            "spec": self._read_file(self.spec_path),
            "todo": self._read_file(self.todo_path),
            "timestamp": datetime.now().isoformat()
        }
        return context
    
    def _read_file(self, path: Path) -> str:
        """Read file content or return empty string."""
        if path.exists():
            return path.read_text()
        return ""
    
    def _write_file(self, path: Path, content: str) -> None:
        """Write content to file."""
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
    
    def update_todo(self, step_completed: str) -> None:
        """
        Update todo.md with completed step.
        """
        todo_content = self._read_file(self.todo_path)
        
        # Add timestamp to completed steps section
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        completion_line = f"- [x] {step_completed} (completed {timestamp})\n"
        
        # Find "Completed Steps" section and append
        if "## Completed Steps" in todo_content:
            todo_content = todo_content.replace(
                "## Completed Steps\n",
                f"## Completed Steps\n{completion_line}"
            )
        else:
            todo_content += f"\n## Completed Steps\n{completion_line}"
        
        self._write_file(self.todo_path, todo_content)
    
    def run_turn(self) -> bool:
        """
        Execute one turn of the agent loop.
        
        Returns:
            True if turn completed successfully
        """
        print("\n" + "=" * 60)
        print("AGENT LOOP: Starting turn")
        print("=" * 60)
        
        # Step 1: Load context (MEM1)
        print("\n📖 Loading context from files...")
        context = self.load_context()
        print(f"   Memory: turn_count={context['memory'].get('turn_count', 0)}")
        print(f"   Spec length: {len(context['spec'])} chars")
        print(f"   Todo length: {len(context['todo'])} chars")
        
        # Step 2: Gatekeeper check
        print("\n🚪 Running Gatekeeper...")
        if not self.gatekeeper.gate():
            self.memory.update(
                status="blocked",
                last_action="gatekeeper_rejected",
                blockers=["Invalid spec.md"]
            )
            return False
        
        # Step 3: Mark as working
        self.memory.update(status="working", last_action="turn_started")
        
        # Step 4: [PLACEHOLDER - Agent would execute task here]
        print("\n⚙️  Agent execution would happen here...")
        print("   (MVP: Manual code writing, agent verifies)")
        
        # Step 5: Run cheap gate
        print("\n🧪 Running Cheap Gate...")
        gate_passed = self.cheap_gate.gate()
        
        # Step 6: Update memory with results
        if gate_passed:
            self.memory.update(
                status="complete" if gate_passed else "error",
                last_action="turn_completed"
            )
            print("\n✅ TURN COMPLETED SUCCESSFULLY")
        else:
            self.memory.update(
                status="error",
                last_action="gate_failed"
            )
            print("\n❌ TURN FAILED - Gate checks did not pass")
        
        return gate_passed
    
    def run(self, max_turns: int = 1) -> bool:
        """
        Run multiple turns (for automation).
        
        Args:
            max_turns: Maximum turns to execute
            
        Returns:
            True if all turns completed successfully
        """
        for turn in range(max_turns):
            print(f"\n{'#' * 60}")
            print(f"# TURN {turn + 1} of {max_turns}")
            print(f"{'#' * 60}")
            
            success = self.run_turn()
            
            if not success:
                print(f"\n⛔ Stopping after turn {turn + 1} due to failure")
                return False
        
        return True


def run_agent(max_turns: int = 1) -> bool:
    """Convenience function to run agent."""
    agent = AgentLoop()
    return agent.run(max_turns)


if __name__ == "__main__":
    success = run_agent()
    sys.exit(0 if success else 1)
```

### Step 8.2: Create tests/test_agent.py
Create file `tests/test_agent.py`. Paste:

```python
"""Tests for Agent Loop."""

import tempfile
import pytest
from pathlib import Path

from src.agent.loop import AgentLoop


@pytest.fixture
def temp_agent_dir():
    """Create temporary directory with agent files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        
        # Create required directories
        (tmpdir / "memory").mkdir()
        (tmpdir / "plan").mkdir()
        
        # Create memory.json
        (tmpdir / "memory" / "memory.json").write_text('''{
            "agent_id": "test-agent",
            "session_id": "test-session",
            "turn_count": 0,
            "last_action": "initialized",
            "status": "idle",
            "files_modified": [],
            "tests_passed": 0,
            "tests_failed": 0,
            "blockers": [],
            "error_log": []
        }''')
        
        # Create spec.md (valid)
        (tmpdir / "plan" / "spec.md").write_text('''
# SPEC: test-001

## Status: APPROVED

## Objective
Create a simple test function.

## Requirements
- [ ] Function exists
- [ ] Function returns True

## Success Criteria
- [ ] Tests pass
''')
        
        # Create todo.md
        (tmpdir / "plan" / "todo.md").write_text('''
# TODO: test-001

## Current Status: NOT_STARTED

## Progress
- [ ] Implement function

## Completed Steps
''')
        
        yield tmpdir


class TestAgentLoop:
    """Test suite for AgentLoop."""
    
    def test_load_context_reads_files(self, temp_agent_dir):
        """Agent should load context from files only."""
        agent = AgentLoop(
            memory_path=str(temp_agent_dir / "memory" / "memory.json"),
            spec_path=str(temp_agent_dir / "plan" / "spec.md"),
            todo_path=str(temp_agent_dir / "plan" / "todo.md")
        )
        
        context = agent.load_context()
        
        assert "memory" in context
        assert "spec" in context
        assert "todo" in context
        assert context["memory"]["agent_id"] == "test-agent"
        assert "Objective" in context["spec"]
    
    def test_update_todo_adds_completion(self, temp_agent_dir):
        """update_todo should add timestamped completion."""
        agent = AgentLoop(
            memory_path=str(temp_agent_dir / "memory" / "memory.json"),
            spec_path=str(temp_agent_dir / "plan" / "spec.md"),
            todo_path=str(temp_agent_dir / "plan" / "todo.md")
        )
        
        agent.update_todo("Test step completed")
        
        todo_content = (temp_agent_dir / "plan" / "todo.md").read_text()
        assert "Test step completed" in todo_content
        assert "completed" in todo_content


class TestMEM1Compliance:
    """Tests ensuring MEM1 principle is followed."""
    
    def test_no_external_state(self, temp_agent_dir):
        """Agent should not use any state outside files."""
        agent = AgentLoop(
            memory_path=str(temp_agent_dir / "memory" / "memory.json"),
            spec_path=str(temp_agent_dir / "plan" / "spec.md"),
            todo_path=str(temp_agent_dir / "plan" / "todo.md")
        )
        
        # First load
        context1 = agent.load_context()
        
        # Modify files
        (temp_agent_dir / "memory" / "memory.json").write_text('''{
            "agent_id": "test-agent",
            "session_id": "modified-session",
            "turn_count": 99,
            "last_action": "modified",
            "status": "working",
            "files_modified": ["test.py"],
            "tests_passed": 5,
            "tests_failed": 0,
            "blockers": [],
            "error_log": []
        }''')
        
        # Second load should reflect file changes
        context2 = agent.load_context()
        
        assert context2["memory"]["turn_count"] == 99
        assert context2["memory"]["session_id"] == "modified-session"
```

### Step 8.3: Run Tests
```bash
python -m pytest tests/test_agent.py -v
```

### Step 8.4: Commit
```bash
git add .
git commit -m "BP8: Agent Loop complete"
```

## Verification

```bash
# Tests pass
python -m pytest tests/test_agent.py -v

# Run agent (will fail gatekeeper - spec still template)
python src/agent/loop.py
```

**Expected Output:** Tests pass. Agent runs but gatekeeper blocks (expected).

---

# BLUEPRINT 9: HARD RESET

## Goal
Create context wipe script that simulates container death.

## Spec Requirements
- Clear all runtime state
- Preserve only file-based state
- Reset memory session
- Simulate fresh start

## Todo List

### Step 9.1: Create scripts/reset_context.py
Create file `scripts/reset_context.py`. Paste:

```python
"""
Hard Reset - Context Wipe Simulation
UAP MVP v0.1

Simulates what happens when the agent's container dies and respawns.
After git commit, we "kill" the agent and it starts fresh.

What survives:
- memory/memory.json (but session is reset)
- plan/spec.md
- plan/todo.md
- workspace/* (generated files)

What dies:
- All chat history (simulated)
- All in-memory state (simulated)
- Current context window (simulated)
"""

import sys
import argparse
from datetime import datetime
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.agent.memory_manager import MemoryManager


def hard_reset(preserve_progress: bool = True) -> None:
    """
    Perform a hard reset of agent context.
    
    Args:
        preserve_progress: If True, keep completed work in memory.
                          If False, full reset to initial state.
    """
    print("=" * 60)
    print("HARD RESET: Simulating context wipe")
    print("=" * 60)
    
    memory = MemoryManager()
    old_memory = memory.load()
    
    print(f"\n📊 Before reset:")
    print(f"   Session: {old_memory.get('session_id')}")
    print(f"   Turn count: {old_memory.get('turn_count')}")
    print(f"   Status: {old_memory.get('status')}")
    
    # Reset memory
    if preserve_progress:
        # Keep some state, reset session
        tests_passed = old_memory.get('tests_passed', 0)
        memory.reset_session()
        memory.update(tests_passed=tests_passed)
        print("\n🔄 Partial reset: Session cleared, progress preserved")
    else:
        # Full reset
        memory.reset_session()
        print("\n🔄 Full reset: All state cleared")
    
    new_memory = memory.load()
    
    print(f"\n📊 After reset:")
    print(f"   Session: {new_memory.get('session_id')}")
    print(f"   Turn count: {new_memory.get('turn_count')}")
    print(f"   Status: {new_memory.get('status')}")
    
    # Print what survives
    print("\n" + "=" * 60)
    print("SURVIVING FILES (Agent will read these on restart):")
    print("=" * 60)
    
    surviving_files = [
        "memory/memory.json",
        "plan/spec.md",
        "plan/todo.md",
    ]
    
    for filepath in surviving_files:
        path = Path(filepath)
        if path.exists():
            size = path.stat().st_size
            print(f"   ✓ {filepath} ({size} bytes)")
        else:
            print(f"   ✗ {filepath} (missing)")
    
    # Check workspace
    workspace = Path("workspace/output")
    if workspace.exists():
        files = list(workspace.glob("*.py"))
        if files:
            print(f"   ✓ workspace/output/ ({len(files)} Python files)")
    
    print("\n" + "=" * 60)
    print("DESTROYED (Agent cannot access):")
    print("=" * 60)
    print("   ✗ Chat history")
    print("   ✗ Previous context window")
    print("   ✗ In-memory variables")
    print("   ✗ Runtime state")
    
    print("\n✅ HARD RESET COMPLETE")
    print("   Agent will start fresh on next run")
    print("   Only file-based state survives (MEM1 principle)")


def main():
    parser = argparse.ArgumentParser(description="UAP Hard Reset")
    parser.add_argument(
        "--full",
        action="store_true",
        help="Full reset (clears all progress)"
    )
    args = parser.parse_args()
    
    hard_reset(preserve_progress=not args.full)


if __name__ == "__main__":
    main()
```

### Step 9.2: Create workspace/.gitkeep
```bash
touch workspace/output/.gitkeep
```

### Step 9.3: Test Hard Reset
```bash
# Run the reset
python scripts/reset_context.py

# Check memory was reset
cat memory/memory.json
```

### Step 9.4: Commit
```bash
git add .
git commit -m "BP9: Hard Reset complete"
```

## Verification

```bash
# Run reset
python scripts/reset_context.py

# Verify new session ID
python -c "import json; print(json.load(open('memory/memory.json'))['session_id'])"
```

**Expected Output:** Reset completes. New session ID generated.

---

# BLUEPRINT 10: HELLO WORLD RUN

## Goal
Run ONE complete task through the entire system.

## Spec Requirements
- Write a real spec
- Agent processes it
- Code is generated
- Tests pass
- No regex used

## Todo List

### Step 10.1: Write Real Spec
Edit `plan/spec.md` to contain:

```markdown
# SPEC: hello-001

## Status: APPROVED

## Objective
Create a Python function that adds two numbers and returns the result.

## Requirements
- [ ] Function named 'add' in workspace/output/calculator.py
- [ ] Takes two parameters: a and b
- [ ] Returns the sum of a and b
- [ ] Includes docstring
- [ ] Type hints for parameters and return value

## Constraints
- Max file size: 500 lines
- Max complexity: 20
- Test coverage: >= 80%
- No regex on code files

## Inputs
- Two numbers (int or float)

## Expected Output
- Sum of the two numbers

## Success Criteria
- [ ] Function exists and is callable
- [ ] add(2, 3) returns 5
- [ ] add(-1, 1) returns 0
- [ ] add(0.5, 0.5) returns 1.0
- [ ] All tests pass
- [ ] Pylint score >= 7.0
```

### Step 10.2: Write Real Todo
Edit `plan/todo.md` to contain:

```markdown
# TODO: hello-001

## Current Status: IN_PROGRESS

## Progress

### Phase 1: Setup
- [x] Read spec.md
- [x] Read memory.json
- [x] Plan implementation

### Phase 2: Implementation
- [ ] Create workspace/output/calculator.py
- [ ] Implement add() function
- [ ] Add docstring and type hints

### Phase 3: Verification
- [ ] Create test file
- [ ] Run tests
- [ ] Run pylint
- [ ] Update memory.json

## Current Focus
Create the add() function

## Blockers
None

## Completed Steps

## Notes
First real task through the MVP system.
```

### Step 10.3: Create the Code (Manual - Simulating Agent)
Create file `workspace/output/calculator.py`. Paste:

```python
"""
Calculator Module
UAP MVP v0.1 - Hello World Task

Generated by agent following spec hello-001.
"""


def add(a: float, b: float) -> float:
    """
    Add two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
        
    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
    """
    return a + b
```

### Step 10.4: Create Test File
Create file `tests/test_calculator.py`. Paste:

```python
"""Tests for calculator module - Hello World task."""

import pytest
import sys
from pathlib import Path

# Add workspace to path
sys.path.insert(0, str(Path(__file__).parent.parent / "workspace" / "output"))

from calculator import add


class TestAdd:
    """Test suite for add function."""
    
    def test_add_positive_numbers(self):
        """add(2, 3) should return 5."""
        assert add(2, 3) == 5
    
    def test_add_negative_and_positive(self):
        """add(-1, 1) should return 0."""
        assert add(-1, 1) == 0
    
    def test_add_floats(self):
        """add(0.5, 0.5) should return 1.0."""
        assert add(0.5, 0.5) == 1.0
    
    def test_add_zeros(self):
        """add(0, 0) should return 0."""
        assert add(0, 0) == 0
    
    def test_add_large_numbers(self):
        """Should handle large numbers."""
        assert add(1000000, 2000000) == 3000000
```

### Step 10.5: Create Run Script
Create file `scripts/run_hello_world.py`. Paste:

```python
"""
Hello World Demo - Complete UAP MVP Run
UAP MVP v0.1

Demonstrates the entire MVP pipeline:
1. Load context from files (MEM1)
2. Validate spec (Gatekeeper)
3. Run quality gates (Cheap Gate)
4. Update memory
5. Hard reset
"""

import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.agent.loop import AgentLoop
from src.agent.memory_manager import MemoryManager
from scripts.reset_context import hard_reset


def run_hello_world():
    """Run the complete Hello World demo."""
    print("\n" + "#" * 70)
    print("#" + " " * 68 + "#")
    print("#" + "           UAP MVP v0.1 - HELLO WORLD DEMO".center(68) + "#")
    print("#" + " " * 68 + "#")
    print("#" * 70)
    
    # Step 1: Show initial state
    print("\n" + "=" * 60)
    print("STEP 1: Initial State")
    print("=" * 60)
    
    memory = MemoryManager()
    state = memory.load()
    print(f"Agent ID: {state['agent_id']}")
    print(f"Session: {state['session_id']}")
    print(f"Turn count: {state['turn_count']}")
    
    # Step 2: Run agent loop
    print("\n" + "=" * 60)
    print("STEP 2: Running Agent Loop")
    print("=" * 60)
    
    agent = AgentLoop()
    success = agent.run_turn()
    
    # Step 3: Show results
    print("\n" + "=" * 60)
    print("STEP 3: Results")
    print("=" * 60)
    
    state = memory.load()
    print(f"Status: {state['status']}")
    print(f"Last action: {state['last_action']}")
    print(f"Turn count: {state['turn_count']}")
    
    if success:
        print("\n✅ HELLO WORLD COMPLETE!")
        print("   The entire MVP pipeline executed successfully.")
        print("\n   What happened:")
        print("   1. Agent loaded context from files (MEM1)")
        print("   2. Gatekeeper validated spec.md")
        print("   3. Cheap Gate ran pytest + pylint")
        print("   4. Memory was updated")
    else:
        print("\n❌ HELLO WORLD FAILED")
        print("   Check the errors above.")
    
    # Step 4: Demonstrate hard reset
    print("\n" + "=" * 60)
    print("STEP 4: Hard Reset (Optional)")
    print("=" * 60)
    print("Run 'python scripts/reset_context.py' to simulate context death")
    
    return success


if __name__ == "__main__":
    success = run_hello_world()
    sys.exit(0 if success else 1)
```

### Step 10.6: Run the Complete Demo
```bash
# Run Hello World
python scripts/run_hello_world.py
```

### Step 10.7: Verify Everything Works
```bash
# All tests pass
python -m pytest tests/ -v

# Pylint passes
python -m pylint src/ --fail-under=7

# Cheap gate passes
python src/gates/cheap_gate.py

# Check no regex was used
git log --oneline -5
grep -r "re.sub" workspace/output/ || echo "No regex found (good!)"
```

### Step 10.8: Final Commit
```bash
git add .
git commit -m "BP10: Hello World complete - MVP v0.1 finished!"
```

## Verification

```bash
# Run complete demo
python scripts/run_hello_world.py

# Expected output:
# ✅ HELLO WORLD COMPLETE!
```

**Expected Output:** 
- Gatekeeper passes
- Tests pass
- Pylint passes
- Memory updated
- "HELLO WORLD COMPLETE!" message

---

# 🎉 CONGRATULATIONS!

You have completed UAP MVP v0.1.

## What You Built

1. **MEM1 Memory System** - Agent reads only from files
2. **Living Plan** - spec.md + todo.md drive execution
3. **Gatekeeper** - Validates specs before work begins
4. **AST Tooling** - Code modification without regex
5. **Regex Ban** - Pre-commit hook blocks bad patterns
6. **Cheap Gate** - pytest + pylint quality checks
7. **Agent Loop** - Main execution engine
8. **Hard Reset** - Context wipe simulation

## Next Steps

1. **Try More Tasks** - Write different specs and run them
2. **Add Complexity** - Tasks requiring multiple files
3. **Increase Coverage** - Get to 80%+ test coverage
4. **Graduate to v1.0** - Add Tournament system (Appendix F)

---

*UAP MVP v0.1 Blueprints | December 2025*

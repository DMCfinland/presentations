# Claude Code Skill Architecture — Reference Pattern
<!-- last_updated: session-28 -->

**Sources:**
- Official docs: https://code.claude.com/docs/en/skills.md
- Official docs: https://code.claude.com/docs/en/sub-agents.md
- Real-world example: [claude-seo](https://github.com/AgriciDaniel/claude-seo) (MIT, 2026-02-07)
**Saved:** 2026-02-11

---

## Why This Matters

Claude Code skills are the building blocks for reusable AI workflows. Understanding this architecture lets us build custom skills for any domain — not just SEO. The claude-seo repo is the cleanest open-source example we've found.

---

## File Structure

```
~/.claude/
├── skills/
│   ├── seo/                          # Main skill (orchestrator)
│   │   ├── SKILL.md                  # Entry point — YAML frontmatter + instructions
│   │   ├── references/               # Domain knowledge loaded on-demand
│   │   │   ├── cwv-thresholds.md
│   │   │   ├── schema-types.md
│   │   │   ├── eeat-framework.md
│   │   │   └── quality-gates.md
│   │   ├── schema/                   # Data templates (JSON)
│   │   │   └── templates.json
│   │   ├── scripts/                  # Python helper tools
│   │   │   ├── fetch_page.py
│   │   │   ├── parse_html.py
│   │   │   ├── capture_screenshot.py
│   │   │   └── analyze_visual.py
│   │   ├── hooks/                    # Pre-commit and post-edit validators
│   │   │   ├── pre-commit-seo-check.sh
│   │   │   └── validate-schema.py
│   │   └── pdf/                      # Reference documents
│   │       └── google-seo-reference.md
│   │
│   ├── seo-audit/                    # Sub-skill 1
│   │   └── SKILL.md
│   ├── seo-page/                     # Sub-skill 2
│   │   └── SKILL.md
│   ├── seo-technical/                # Sub-skill 3
│   │   └── SKILL.md
│   ├── seo-plan/                     # Sub-skill with assets
│   │   ├── SKILL.md
│   │   └── assets/                   # Industry-specific templates
│   │       ├── saas.md
│   │       ├── ecommerce.md
│   │       ├── local-service.md
│   │       ├── publisher.md
│   │       ├── agency.md
│   │       └── generic.md
│   └── [other sub-skills...]/
│
├── agents/                           # Subagents for parallel work
│   ├── seo-technical.md
│   ├── seo-content.md
│   ├── seo-schema.md
│   ├── seo-sitemap.md
│   ├── seo-performance.md
│   └── seo-visual.md
│
└── settings.json                     # Hook configuration (optional)
```

---

## Key Architectural Patterns

### 1. SKILL.md Frontmatter (Entry Point)

Every skill needs a `SKILL.md` with YAML frontmatter:

```yaml
---
name: seo
description: >
  Comprehensive SEO analysis for any website or business type...
  Triggers on: "SEO", "audit", "schema", "Core Web Vitals"...
allowed-tools:
  - Read
  - Grep
  - Glob
  - Bash
  - WebFetch
---
```

**All frontmatter fields (official docs):**

| Field | Required | Description |
|-------|----------|-------------|
| `name` | No | Slash command name. If omitted, uses directory name. Lowercase, hyphens, max 64 chars |
| `description` | Recommended | When Claude should use this skill + trigger keywords. Used for auto-invocation |
| `argument-hint` | No | Autocomplete hint (e.g., `[url]`, `[issue-number]`) |
| `allowed-tools` | No | Tools Claude can use without permission when skill is active |
| `model` | No | Force specific model (`sonnet`, `opus`, `haiku`) |
| `context` | No | Set to `fork` to run in isolated subagent context |
| `agent` | No | Subagent type when `context: fork` (e.g., `Explore`, `Plan`) |
| `disable-model-invocation` | No | `true` = Claude can't auto-load, only manual `/name` works |
| `user-invocable` | No | `false` = hidden from `/` menu, only Claude can invoke |
| `hooks` | No | Hooks scoped to this skill's lifecycle |

**String substitutions in skill content:**
- `$ARGUMENTS` — all args passed when invoking
- `$0`, `$1`, `$N` — specific argument by index
- `${CLAUDE_SESSION_ID}` — current session ID

**Dynamic context injection:**
- `` !`command` `` — runs shell command, injects output into skill content before sending to Claude
- Example: `` !`gh pr diff` `` injects the PR diff inline

### 2. Orchestrator + Sub-Skills Pattern

The main skill is a **router/orchestrator** that:
1. Parses the user's command (`/seo audit`, `/seo page`, etc.)
2. Detects context (business type, page type)
3. Delegates to the right sub-skill or spawns subagents for parallel work

Sub-skills are **self-contained** — each has its own `SKILL.md` with focused instructions.

### 3. Subagents for Parallel Execution

Agents in `~/.claude/agents/` run as separate Claude instances:

```yaml
---
name: seo-technical
description: Technical SEO specialist...
tools: Read, Bash, Write, Glob, Grep
---

You are a Technical SEO specialist. When given a URL:
1. Fetch the page(s)...
2. Check robots.txt...
[detailed instructions]
```

The orchestrator spawns 6 agents in parallel during a full audit, then merges results.

### 4. On-Demand Reference Loading

References stored in `references/` are NOT loaded at startup. The skill instructions say:

> "Load these on-demand as needed — do NOT load all at startup"

This keeps context lean. Claude only reads `quality-gates.md` when evaluating content quality, not for every command.

### 5. Helper Scripts

Python scripts in `scripts/` extend Claude's capabilities:
- `fetch_page.py` — HTTP fetching with proper headers
- `parse_html.py` — HTML → structured SEO data extraction
- `capture_screenshot.py` — Visual capture via Playwright
- `analyze_visual.py` — Above-fold, mobile, font analysis

Claude calls these via Bash tool when needed.

### 6. Hooks (Optional Quality Gates)

Hooks run automatically on file operations:
- **Pre-commit hook**: Blocks commits with SEO problems (placeholder text, deprecated schema)
- **Post-edit hook**: Validates schema markup after file edits

Configured in `~/.claude/settings.json`:
```json
{
  "hooks": {
    "PreToolUse": [{"matcher": "Bash", "hooks": [...]}],
    "PostToolUse": [{"matcher": "Edit|Write", "hooks": [...]}]
  }
}
```

---

## Design Principles to Replicate

| Principle | How claude-seo Does It |
|-----------|----------------------|
| **Single responsibility** | Each sub-skill does ONE thing well |
| **Lazy loading** | Reference files loaded only when needed |
| **Parallel execution** | 6 subagents run simultaneously during audits |
| **Graceful degradation** | Playwright optional — tool works without it |
| **Quality gates** | Hard stops prevent bad outputs (50+ location pages) |
| **Industry detection** | Adapts behavior based on context signals |
| **Structured output** | Consistent report format with scores and priorities |
| **Clean uninstall** | Uninstall script removes exactly what was installed |

---

## Template for Building a New Skill

To create a skill for domain X:

1. **Main orchestrator:** `~/.claude/skills/x/SKILL.md`
   - YAML frontmatter with name, description, triggers, tools
   - Command routing table
   - Orchestration logic

2. **Sub-skills:** `~/.claude/skills/x-[command]/SKILL.md`
   - One per command variant
   - Self-contained instructions

3. **Subagents:** `~/.claude/agents/x-[specialist].md`
   - For parallel work during complex commands
   - YAML frontmatter with name, description, tools

4. **References:** `~/.claude/skills/x/references/*.md`
   - Domain knowledge, thresholds, frameworks
   - Loaded on-demand, not at startup

5. **Scripts:** `~/.claude/skills/x/scripts/*.py`
   - Helper tools for data fetching/processing
   - Called via Bash when needed

6. **Install/uninstall:** `install.sh` + `uninstall.sh`
   - Clone to temp, copy to `~/.claude/`, install deps, clean up

---

## Potential Skills for 1658 Holdings

Using this architecture, we could build:

| Skill | Use Case |
|-------|----------|
| `/dmc` | Finland DMC workflows (client comms, proposals, pricing) |
| `/mining` | Mining session orchestration and processing |
| `/knowledge` | Knowledge base queries across YouTube research |
| `/company` | Company onboarding and status across portfolio |
| `/cost` | Cost calculator for API queries and batch jobs |

---

## Official Skill Discovery & Loading

### Where Skills Are Found (priority order)

| Priority | Location | Scope |
|----------|----------|-------|
| Highest | Enterprise settings (managed) | All org users |
| 2nd | `~/.claude/skills/` | Personal, all projects |
| 3rd | `.claude/skills/` | Current project only |
| Lowest | `<plugin>/skills/` | Where plugin is enabled |

### Loading Behavior

- Only skill **descriptions** are loaded into context at startup (not full content)
- Full skill content loads **only when invoked**
- Description character budget: 2% of context window (~16,000 chars)
- Check `/context` for warnings about excluded skills

### Context Loading Matrix

| Configuration | User Can Invoke | Claude Can Auto-Invoke |
|--------------|----------------|----------------------|
| Default | Yes (`/name`) | Yes (from description match) |
| `disable-model-invocation: true` | Yes | No |
| `user-invocable: false` | No | Yes |

---

## Community Skill Collections

| Collection | Size | Notes |
|-----------|------|-------|
| [claude-skills](https://github.com/alirezarezvani/claude-skills) | 53 skills | Marketing, C-suite advisory, PM, engineering, finance |
| [claude-code-plugins-plus-skills](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) | 270+ plugins, 1,537 skills | CCPI package manager, massive catalog |
| [claude-seo](https://github.com/AgriciDaniel/claude-seo) | 1 skill (13 sub-skills) | Best architecture example we've found |

### CCPI Package Manager

Community CLI tool for discovering and installing skill packs:
```bash
pnpm add -g @intentsolutionsio/ccpi
ccpi search marketing
ccpi install plugin-name
ccpi list --installed
```

---

## Plugin Distribution Format

For packaging multiple skills as a distributable unit:

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   ├── skill-one/
│   │   └── SKILL.md
│   └── skill-two/
│       └── SKILL.md
├── agents/
│   └── specialist.md
├── hooks/
└── .mcp.json
```

Plugin skills get namespaced: `/plugin-name:skill-name`

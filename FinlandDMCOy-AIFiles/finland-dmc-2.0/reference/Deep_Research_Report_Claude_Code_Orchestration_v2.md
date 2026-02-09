# Deep Research Report v2: Claude Code Session Orchestration for Multi-Company Holdings

**Date:** 2026-02-09
**Source:** claude.ai Deep Research (Opus), corrected with follow-up research
**Status:** Accepted — action items executed

## Key Decisions Made

1. **Two-Zone file strategy:** Workshop (local+Git) vs. Company Knowledge (OneDrive→SharePoint)
2. **Local Git + OneDrive sync = sufficient.** No GitHub needed.
3. **CLAUDE.md hierarchy:** User → Holdings → Company → Project (all confirmed working)
4. **Custom subagents created:** mining-organizer, company-setup, file-builder
5. **Agent Teams:** Available but not needed yet — start with subagents
6. **OneDrive sync on Mac with .md/.txt files:** Stable for single-user setup

## Architecture Summary

```
Zone A (Workshop — local + Git):
  1658HoldingsOy-AIFiles/
  ├── CLAUDE.md (holdings-level)
  ├── _shared/
  └── FinlandDMCOy-AIFiles/
      ├── CLAUDE.md (company-level)
      └── finland-dmc-2.0/ (project with CLAUDE.md, ROADMAP.md, etc.)

Zone B (Company Knowledge — OneDrive → SharePoint → M365):
  OneDrive/FinlandDMCOy/AI-Knowledge/
  ├── golden-prompts/
  ├── company-knowledge/
  ├── examples/
  ├── pricing/
  └── client-data/
```

## Full research report available in the claude.ai conversation history.

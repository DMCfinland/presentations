# External Intel: everything-claude-code Research
**Source:** Claude Code (GitHub API + WebSearch + community analysis)
**Date:** 2026-04-01 | Session 139
**Topic:** affaan-m/everything-claude-code (129K stars)
**Full synthesis:** ~/1658HoldingsOy-AIFiles/research/everything-claude-code-harness/synthesis-2026-04-01.md

## Key Findings

1. **129K stars in 73 days** — viral X thread drove growth. 7:1 star-to-fork ratio = real adoption exists but thin (near-zero Reddit/HN presence).
2. **1 person = 77% of commits** (affaan-m: 607/~790). 89 open issues, 9 closed. Maintenance debt growing.
3. **"Instincts" = adaptive rules with confidence scoring** — more than just CLAUDE.md rules, but shipped instincts are static YAML. The dynamic learning system exists but requires manual operation. NOT vector DB.
4. **Security component is the real value** — hook-based enforcement of dangerous command blocking, secrets detection, MCP health checks. This is a genuine gap in our system.
5. **Memory = file-based JSONL + YAML** — less structured than our typed memory system. No external services. No GDPR amplification.
6. **Zero published benchmarks** — no evidence of measured performance improvement anywhere.
7. **1,820 files across 7 IDE platforms** — would conflict with our CLAUDE.md token budget and existing 130+ session harness.

## Decision: SKIP full install + Cherry-Pick 18 items (3 tiers)

**Tier A (this week, ~2hrs):** Cost tracker hook, suggest-compact hook, block-no-verify hook, critical file protection hook, governance capture hook, desktop notification hook, "What Did NOT Work" template
**Tier B (this month, ~2.5hrs):** Pre-compact saver, MCP health check, bash audit log, ADR skill, context budget audit, confidence scoring, product lens skill
**Tier C (evaluate later):** Automated session persist, pattern harvest trigger, blueprint skill, skill stocktake

Full catalog: `research/everything-claude-code-harness/cherry-pick-catalog-2026-04-01.md`

## Grok Spar Status
Grok brief prepared but not yet sent to Grok. Brief in: `research/everything-claude-code-harness/grok-brief-2026-04-01.md`

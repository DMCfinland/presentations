---
name: Stack Registry over Dual-Folder for AI Tool Governance
description: A single living Stack Registry (status-tagged markdown/JSON) beats ARKISTO+TUOTANTO dual-folder for governing a multi-tool AI stack. Solves the behavioral problem, not just the filing problem.
type: feedback
---

When an AI stack grows to 5+ tools over 100+ sessions, governance drift occurs: CEO defaults to familiar tools ("man with a hammer") even when a better tool exists.

**Wrong solution:** ARKISTO + TUOTANTO folders. Solves documentation symptom, not behavior. CEO bypasses folder discipline under deadline pressure. Archive goes stale within 2 weeks.

**Right solution:** Stack Registry — single living file with:
- Tool name + current version
- Status: active / experimental / archived
- Job: exactly one job this tool does (nothing else)
- Context trigger: when to reach for this tool
- Performance note: why this tool won vs. alternatives
- Version history: old approaches preserved, searchable

**"Man with a hammer" fix:** Embed routing logic in the daily CoS bot. Bot says "tämä on Gemini-kysymys" or "tämä vaatii Claude Code -session" at the point of use. User doesn't need to remember the registry — the router does it.

**Governance cadence:** Triggered, not calendar-based:
1. New tool enters consideration
2. PWJ failure >10% on deliverables
3. Major business shift
4. 6-week forced review (backstop only)
Between sessions: tool-combination changes banned. Micro-tweaks logged in registry.

**Why:** Behavior change happens at point of use, not in a filing system. Registry + routing is the only model that scales with actual CEO behavior (Grok Round 5, Lucas — session 115).

**File location:** `_shared/stack-registry.md` (Zone A, Git-tracked) + curated export to CoS Project File for routing awareness.

**Source:** Patrick (original ARKISTO/TUOTANTO idea) + Grok Round 5 Lucas (counter-proposal, session 115, 2026-03-25)

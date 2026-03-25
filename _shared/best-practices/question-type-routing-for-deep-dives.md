# Question-Type Routing for Deep Dive Sections
<!-- source: knowledge-management-research-2026.md Section 3 | session: 70 -->
<!-- created: 2026-03-12 | confidence: 0.7 | tier: B -->

**What:** Convert Deep Dive file pointers in warm packs from vague file references to decision-tree routing. Format: "If asking '[specific question]' → load [file]."

**Why:** Keyword-based file pointers fail when you don't already know what you need. Decision-tree routing activates on intent, not on knowing the filename. The barrier to loading KB files is "I must already know I need it" — routing on question type removes that barrier.

**When to apply:** Any time you add or update a Deep Dive line in any warm pack. Also: run on all existing Deep Dive sections during next Opus review.

**How:**
- Before: `"How do I orchestrate agents?" → topics/agent-architecture.md`
- After: `"If asking 'how should I orchestrate multiple searches?' → agent-architecture.md (249 insights). If asking 'how do I hand off between agent waves?' → agent-orchestration-patterns.md"`
- Each Deep Dive pointer should have 1-2 concrete question examples, not just a topic description.

**Source session:** Session 70 (extracted from knowledge-management-research-2026.md — validated by production evidence: Low KB consultation rate was partly a retrieval barrier problem, not a relevance problem)

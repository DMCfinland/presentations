---
name: realism-safeguards-implementation
description: Any implementation plan needs a mandatory "REALISM & SAFEGUARDS" section — 3 specific ways the plan gets read once and ignored, each with a mitigation. Without this, polished plans with satisfied criteria never get executed.
type: project
---

# Pattern: REALISM & SAFEGUARDS — Mandatory Implementation Section

**The rule:** Every implementation document must include a REALISM & SAFEGUARDS section before the quick-start checklist. Structure:
1. Patrick's realistic weekly AI time budget (estimated from CURRENT-STATUS.md or reasoned)
2. 3 specific failure modes: "3 ways THIS plan could be read once and ignored"
3. One mitigation per failure mode

**Why it exists:** Grok Heavy (Harper + Benjamin + Lucas, S101) found that 80-95% of AI initiative implementation plans are executed once then abandoned. Standard PWJ criteria verify PRESENCE not EXECUTABILITY. A document can satisfy all 9 mechanical criteria — gap table, matrix, imperatives, citations — and still produce zero behavior change if the execution friction isn't addressed. The REALISM section forces the Worker to model Patrick's actual Monday morning before finalizing.

**The Monday test:** Before finalizing, Worker simulates: "Patrick opens this at 8am Monday. Would he execute the Tier 1 imperatives before 9am?" If not — why not? Every Tier 1 action that fails this test needs either a lower-friction version or an explicit guardrail.

**Structure:**
```markdown
### REALISM & SAFEGUARDS
Patrick's realistic weekly AI time budget: [from CURRENT-STATUS.md or ~X hours/week estimate]

3 specific ways THIS plan could be read once and ignored:
1. [Specific failure mode for this plan] → Mitigation: [concrete guardrail]
2. [Specific failure mode for this plan] → Mitigation: [concrete guardrail]
3. [Specific failure mode for this plan] → Mitigation: [concrete guardrail]
```

**Failure modes must be plan-specific**, not generic ("user gets busy"). Acceptable examples:
- "Chief of Staff bot used once, gets generic response, abandoned — Mitigation: 2-week daily check-in calendar block"
- "Plan stays in _drafts/ folder, never re-opened — Mitigation: Quick-start checklist printed/pinned"
- "Tier 2 practices require setup that never gets scheduled — Mitigation: Specific calendar block within 2 weeks of reading"

**Where it goes:** After ANTI-PATTERNS, before QUICK-START CHECKLIST. The safeguards section is the bridge between knowing what to do and actually doing it.

**Applies to:** Any implementation roadmap, adoption plan, or "how to use X" guide — not just AI practices. Wherever the gap between "reading the document" and "executing the document" is non-trivial.

source: session-101 | Grok Heavy S101 | Harper enterprise adoption failure rates + Lucas execution risk scoring

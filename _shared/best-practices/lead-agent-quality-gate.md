# Lead Agent Quality Gate Architecture
<!-- source: Grok 4.20 Research Debate session 71 | session: 71 -->
<!-- created: 2026-03-12 | confidence: 0.85 | tier: B -->
<!-- validated: Salesforce Agentforce (8K+ customers), UiPath/Bank of America (245% ROI), Cursor 2026 -->

**What:** Planner-Worker-Judge loop where a Lead Agent orchestrates subagents, actively red-teams their output against ACCEPTANCE CRITERIA, rejects if not met (max 3 rounds), then autonomously decides the next task — without returning to Patrick until a genuine decision boundary or done-criteria is met.

**Why:** Nate AI principle (2026): producing work is not the bottleneck — saying yes/no and quality control is. Patrick's attention is the scarce resource. AI slop is cheap to produce and expensive to review. The gate intercepts slop before Patrick sees it.

**When to apply:** Any multi-step task where subagents are delegated work. Especially Tier 1/2 sessions where autonomy is the goal.

**Architecture:**
```
Patrick (front-loaded spec via structured intake)
    ↓ goal + done criteria + tier classification + constraints
Lead Agent plans → spawns subagents with ACCEPTANCE CRITERIA block
    ↓
Subagent executes
    ↓
Lead Agent red-teams:
  - Did output meet ACCEPTANCE CRITERIA? (specific, not open-ended)
  - Value-drift check: does output match original done-criteria? (guards against goal drift)
  - Confidence threshold: if confidence <85% → escalate, don't iterate
    ↓ REJECT if criteria not met (max 3 rounds — each round = FRESH agent, not continued conversation)
Lead Agent ACCEPTS → decides: what's next?
    ↓ continues autonomously
Escalate to Patrick ONLY when:
  - Genuine decision boundary (spend >€X, irreversible action, external stakeholder)
  - Quality gate failed after 3 rounds + reason log
  - Ambiguity that changes entire task direction
  - Done-criteria fully met → deliver
```

**Critical property — Judge restart = fresh context, not continuation (Cursor, Jan 2026):**
"The Judge's ability to restart cleanly — bringing in a new agent with fresh context — turned out to be one of the system's most important properties."

Why this matters more than it looks:
- A rejected subagent accumulates context of its own failed attempts → biases next try toward the same wrong approach (context rot in the rejection loop)
- Fresh context = no anchoring to previous failures → genuinely explores different paths
- Token efficiency: fresh agent = smaller context window = cheaper per round
- **Implementation rule:** MAX_ROUNDS: 3 means 3 NEW agent instances, not 3 continued turns in the same conversation. Continuing the same agent defeats the purpose.

**DD1 compromise — Structured rejection summary (for interdependent/long-horizon tasks):**
Pure fresh wipe is correct for Tier 1/2. But in Tier 3 strategy sessions and tasks >60 min, full amnesia discards irreplaceable domain knowledge (discovered constraints, schema versions, negotiation context). Mitigation:
- After each rejected round, Lead Agent writes a **rejection summary file** before spawning the next fresh agent. Contents: (1) what approach was attempted, (2) exact failure reason against acceptance criteria, (3) domain model snapshot (key discovered facts, constraints, schema state)
- Fresh agent is given the rejection summary file at spawn — gets failure history without context rot of the full conversation
- Rule: summary ≤ 500 words. If you can't summarize in 500 words, tighten the acceptance criteria.
- **This is NOT the same as continuing the same agent.** Summary file = structured external memory. Fresh agent = no anchoring bias. Both properties preserved.

**Critical failure mode — same-model red-teaming:**
Lead Agent using the same model family as subagents will generate hallucination consensus (consistent-but-wrong). Mitigation:
- Red-team round MUST use structured ACCEPTANCE CRITERIA checklist — not "review this for quality"
- Each criterion must be independently verifiable (not "is this good" — "does it contain X, Y, Z?")
- Criteria defined in Patrick's intake, not by the Lead Agent itself

**DD5 exception — Refinement gate (Tier 3 discovery-driven tasks):**
For Tier 3 sessions where done-criteria evolve with findings (municipal negotiations, strategic pivots, CRM discovery): Lead Agent may propose **sub-criteria elaborations** with logged rationale. Judge validates before proceeding. CEO escalation required for scope changes.
- ALLOWED: sub-criteria elaboration = "discovery revealed we need to add EU AI Act compliance section" → Lead proposes, Judge validates, continues
- ESCALATE: scope change = "we should also cover the whole go-to-market strategy" → stop, ask Patrick
- Distinction: elaboration adds specificity within original scope. Scope change changes the goal itself.
- Log every elaboration: `[elaboration-log]: original criteria + proposed addition + rationale`. Visible at session end.

**Structured intake (front-load Patrick's attention):**
Before any work starts, ask:
1. Goal in one sentence — what are we achieving?
2. Done criteria — what does finished look like? (specific, verifiable)
3. Tier classification — 1 (routine), 2 (verifiable), 3 (strategic judgment)?
4. Constraints — what must NOT happen?
5. Output format — exactly what deliverable?
6. Escalation trigger — what warrants stopping to ask Patrick?

**Acceptance criteria block (in every subagent spawn prompt):**
```
ACCEPTANCE CRITERIA (Lead Agent will verify these before accepting):
1. [specific verifiable condition]
2. [specific verifiable condition]
3. [specific verifiable condition]
MAX_ROUNDS: 3
CONFIDENCE_THRESHOLD: if confidence <85%, escalate to Patrick with reason
VALUE_DRIFT_CHECK: compare to original done-criteria "[paste criteria here]"
```

**Production evidence (2025-2026):**
- Salesforce Agentforce: 8,000+ customers, 2-3 round quality gate, $900M AI revenue contribution in 6 months
- Bank of America Erica (ReAct + acceptance criteria): 3B+ interactions, 245% ROI
- ServiceNow: 54% deflection on common tickets with planner-judge architecture
- Cursor Jan 2026: structured intake + 3-round gate + fresh Judge restarts → longer autonomous runs without quality drop (specific multiplier UNVERIFIED — Grok Run 8 2026-03-12: hierarchy + fresh restarts confirmed, 2-3× figure not found verbatim in blog)

**What this is NOT:**
- Not a replacement for good upfront intake — gates cannot compensate for vague goals
- Not a license to run Tier 3 strategic decisions autonomously — escalation is required there
- Not "review this" — must use structured criteria or same-model consensus defeats the gate

---
name: anchor-bias-cognitive-snapshots
description: Mental Model Anchors in Cognitive Snapshots can pre-bias Workers the same way as pre-filled Grok spar outputs — discovered when "Chief of Staff bot = highest value" was locked as anchor before the matrix was built.
type: feedback
---

# Pattern: Anchor Bias in Cognitive Snapshots

**The rule:** Mental Model Anchors that state conclusions rather than hypotheses bias the Worker before analysis begins. "Chief of Staff bot is the highest-value practice" embedded as an anchor = validation theater — the Worker confirms rather than analyzes.

**Fix:** Label strong directional assumptions in Cognitive Snapshots as testable hypotheses, not facts:
- WRONG: `<anchor>Mikko's Chief of Staff bot is the highest-value immediately-adoptable practice.</anchor>`
- RIGHT: `<anchor>TESTABLE HYPOTHESIS: Chief of Staff bot MAY be highest-value. Score all 8 on the matrix first. If matrix disagrees, report which scored higher. Counter-arguments expected.</anchor>`

**Why:** Discovered via Grok Heavy Lucas attack (S101). Lucas identified that pre-loading a conclusion into the Mental Model Anchor is structurally identical to the Grok spar anti-pattern (NEVER embed expected outcomes — it reduces independence). The Cognitive Snapshot is meant to preserve reasoning, not constrain it. Anchors that say "X is fact" lock the Worker into the same cognitive trap as pre-filled spar outputs.

**When to apply:**
- When writing any Mental Model Anchor about which option is "best" or "highest-value"
- When an anchor names a specific tool/practice as THE answer before analysis has been done
- When a bridge prompt pre-selects which items get full specs before a scoring matrix is built

**Safe anchor patterns:**
- ✅ "Research phase is DONE. Do NOT re-research." (factual constraint)
- ✅ "Stack is fixed: Claude Code + n8n + Supabase." (architectural fact)
- ✅ "OPA gates = Wave 3A regardless of matrix score." (hard constraint)
- ❌ "X is the highest-value practice." (conclusion masquerading as constraint)

**How to apply:** At bridge prompt review time, scan all `<anchor>` entries. Any anchor that names a winner or recommends a specific approach → downgrade to "TESTABLE HYPOTHESIS, [matrix/analysis] decides."

source: session-101 | Grok Heavy Lucas attack | validated immediately

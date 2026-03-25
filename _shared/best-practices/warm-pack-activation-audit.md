---
name: warm-pack-activation-audit
description: Warm pack system has a content-loading gap — ID loads automatically via hook, but warm-packs.md content requires explicit Claude action. Audit protocol for Opus reviews.
type: feedback
source: patrick
session: 88
---

# Warm Pack Activation Audit

## The Problem

The warm pack system has **two distinct steps** — only the first happens automatically:

| Step | What happens | Automatic? |
|------|-------------|------------|
| 1. ID reference loads | SessionStart hook reads CURRENT-STATUS.md → shows `warm_pack: crm-build` | ✅ Yes |
| 2. Content loads | Claude reads `_shared/warm-packs.md` and opens the matching section | ❌ No — Claude must do this proactively |

**Result:** Sessions may have warm pack ID noted but warm pack content (triggers, rules, additional key files) never consulted. The system gives the *illusion* of activation without the substance.

**Why:** The CLAUDE.md session protocol says "Load warm pack section from warm-packs.md (grep the warm_pack: ID from context pack)" — but this instruction competes with the immediate pressure to answer the user's first message. It gets skipped.

---

## When Warm Pack Content IS Redundant

If the Context Pack in CURRENT-STATUS.md already lists the same key files as the warm pack, content loading adds little value. The warm pack is genuinely useful when:
- It contains triggers/rules not in CLAUDE.md
- It points to additional files not in the Context Pack
- The session starts from a generic prompt (not a task-specific custom prompt)

When a custom session prompt lists files explicitly (like the session 89 prompt), the warm pack content may be 80% redundant.

---

## How to Apply

**In custom session prompts:** Explicitly include warm pack loading as a numbered step:
```
2. Lue CURRENT-STATUS.md
   → noteeraa session numero
   → etsi warm_pack ID → lue _shared/warm-packs.md kyseinen osio kokonaan
```

**In standard sessions (no custom prompt):** After reading CURRENT-STATUS.md, Claude must proactively grep warm-packs.md before starting work. Add to CLAUDE.md session protocol if audit shows <40% activation.

**Why it matters:** Warm packs are the compacted knowledge of a project — triggers, known pitfalls, key files. Skipping them = cold-starting on a warm project.

---

## Opus Review Audit Protocol (PWJ-style)

Run at every Opus review (next: session 110). Goal: verify warm packs are working.

### PWJ Intake

**Goal:** Determine if warm pack content (not just ID) is being activated in sessions where it would add value.

**Done criteria (all three required):**
1. Activation rate calculated: % of non-mining sessions where session log shows evidence of warm pack content consulted (keyword: warm pack name, specific file from warm pack, or warm pack trigger fired)
2. Verdict: WORKING (≥40%) / PARTIAL (20-39%) / BROKEN (<20%)
3. If PARTIAL or BROKEN: one concrete fix proposed and implemented before Opus review closes

**Tier:** Tier 2 (expert-checkable with criteria)

**Constraints:**
1. Only count non-mining sessions (mining sessions don't need warm packs)
2. "Evidence of consultation" = session log mentions a file that is in the warm pack but NOT in the Context Pack explicitly — OR warm pack trigger language appears in session work
3. Do not count sessions where custom prompt listed all files explicitly (those are false negatives)

**Output format:**
```
Warm Pack Audit — Session [N]
Sessions analyzed: [X non-mining sessions since last review]
Excluded (custom prompt / mining): [Y]
Activations confirmed: [Z]
Activation rate: Z/(X-Y) = [%]
Verdict: WORKING / PARTIAL / BROKEN
Finding: [one sentence]
Fix (if needed): [concrete change to CLAUDE.md or hook]
```

**Escalation trigger:** If BROKEN two reviews in a row → retire warm pack system, fold content directly into CLAUDE.md Tier A rules or Context Pack.

---

## Warning Signs

1. Session log says "loaded warm pack" but no warm-pack-specific file appears in the work
2. Same key file missed repeatedly despite being in warm pack
3. Patrick corrects Claude on something that was in the warm pack

---

**Why:** Catching activation failure at Opus review costs 0 build impact. Discovering it mid-project means weeks of suboptimal context loading.

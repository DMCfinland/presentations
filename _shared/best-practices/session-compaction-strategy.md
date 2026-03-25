# Session Compaction Strategy
<!-- created: session-39 | source: web research + cost math validation -->

## What /compact Does

Summarizes the entire conversation history into a compact block (~2-5K tokens), then continues.
- Resets the running token counter back to ~summary size
- Does NOT wipe context (unlike /clear) — preserves key facts, decisions, file paths
- Compact itself costs ~$0.05 (generating ~3K output tokens at $15/MTok). Negligible.
- Auto-compact triggers at **75% of context window** (50K tokens of headroom preserved for reasoning)

---

## Cost Math: Why This Matters

Each turn adds its own text + ALL previous turns to the input. Cost grows as O(N²):

| Turns | Cost per turn | Session total (5K/turn added) |
|-------|-------------|-------------------------------|
| 1 | 5K | 5K |
| 5 | 25K | 75K |
| 10 | 50K | 275K |
| 15 | 75K | 600K |
| 20 | 100K | 1,050K |

**Key finding:** At turn 10 you've spent only ~25% of a 20-turn session total.
The LAST 10 turns of a 20-turn session cost 75% of the total.

### Compact at Turn 10: ~47% Total Savings

| Scenario | Turns 1-10 | Turns 11-20 | Total |
|----------|-----------|------------|-------|
| No compact | 275K | 775K | 1,050K |
| Compact at T10 (resets to ~5K) | 275K | ~280K | ~560K |
| **Saving** | — | **-65%** | **~47%** |

---

## Token Threshold Router (updated session-89)

```
< 120K   → Continue. /compact optional at phase break.
120-140K → YELLOW ZONE. Flag: "Approaching 140K — consider Session Bridge soon."
> 140K   → TRIGGER Session-Bridge Protocol (see _shared/best-practices/session-bridge-protocol.md)
> 180K   → FORCE bridge. 200K pricing cliff 20K away.

Architecture Pivot signal (≥12 human interventions OR paradigm shift in last 20K tokens):
> 100K   → ESCALATE: "Pivot detected — recommend Session Bridge NOW, not at 140K."
```

**At 140K+: do NOT /compact. Execute Session-Bridge Protocol.**
See: `_shared/best-practices/session-bridge-protocol.md`

## When to /compact (under 120K only)

**Do compact:**
- At natural phase breaks (finished a mining block, switching from research to build)
- After reading 3+ large files (each adds to the base tax permanently)
- Around turn 10-12 in file-heavy sessions
- Before starting a new parallel workstream in the same session

**Do NOT compact:**
- Mid-task while Claude is actively reasoning across recent context
- After the final message before session end (pointless)
- When switching to a completely different project (use /clear or new window instead)
- When token count is above 120K → use Session-Bridge instead

**Rule of thumb:** `/compact` under 120K at phase breaks. Above 120K: Session-Bridge.

---

## Performance Impact: Low for Our Workflow

Compacting loses granular wording from earlier turns. **For 1658 Holdings this is near-zero impact because:**
- All analysis outputs go to `.md` files immediately (BOARD-MEETINGS-ANALYSIS.md, BUDGET-ANALYSIS.md, etc.)
- The compact summary references those files; the files have the detail
- Session protocol already writes CURRENT-STATUS.md at the END, not during

**Where performance loss would matter:**
- Multi-step coding work where earlier code snippets are still in active use → compact only after committing/saving
- Complex deductive reasoning chains where earlier steps are not yet written down

---

## Compact vs New Window vs /clear

| Tool | Use when | Cost reset | Context preserved |
|------|----------|-----------|-------------------|
| `/compact` | Continuing same project, long session | Partial (resets to summary) | Key facts + file paths |
| New window | Different project/topic | Full | Nothing (start fresh) |
| `/clear` | Starting completely over | Full | Nothing |

**Best hybrid for 1658 Holdings:**
- New window per project (DMC session ≠ Järvisydän session)
- `/compact` within long single-project sessions at natural breaks

---

## Integration with Session Protocol

Add to Session Protocol (Tier A candidate after 3 uses):

> **Context health:** In file-heavy sessions, use `/compact` after ~turn 10-12 or after completing a phase (research → build, mining → synthesis). All key outputs should already be written to `.md` files before compacting.

source: session-39 (web-verified)
when-to-apply: any session with 10+ turns or 3+ large file reads

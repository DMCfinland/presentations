---
name: ambition-erosion-prevention
description: How to prevent North Star vision from narrowing during technical implementation — wave scoping can silently kill the strategic goal
type: feedback
source: patrick
session: 88
---

# Ambition Erosion Prevention

## The Problem
Technical implementation narrows scope. Wave agents follow their spawn prompt exactly — if the spawn prompt says "build email ingestion → deals table," that's what gets built. The North Star ("Second Brain") exists only in strategy docs, not in acceptance criteria.

**Real example (Session 88):** Wave 2A was scoped for "email ingestion → deals table." It succeeded perfectly. But the system was labeled "Second Brain CRM" — creating false confidence that the vision was being implemented. 30-50% of emails went to dead letter queue because the pipeline was designed for client inquiries only. Discovered only during live testing, not design phase.

**Why:** North Star and wave scope are written by different people at different times. Agents optimize for their scope, not the vision.

---

## The Fix: North Star Check in Every Spawn Prompt

Every Agent Teams spawn prompt must include this check as an explicit acceptance criterion:

```
NORTH STAR CHECK (required before marking complete):
Does this deliverable serve the North Star: [STATE NORTH STAR]?
Or does it only serve the wave scope?
If wave scope conflicts with North Star, escalate before completing.
```

---

## Warning Signs of Ambition Erosion

1. **Naming mismatch** — system is called "Second Brain" but only touches one data type
2. **Dead letter queue filling up** — pipeline rejecting "non-conforming" data that should be processed
3. **"We'll add that in a later wave"** — said too often = scope permanently narrowing
4. **Dedicated tables per category** — schema enforces narrow thinking before vision is implemented
5. **Single confidence threshold** — binary pass/fail = no room for uncertainty = ambition erosion in code form

---

## How to Apply

- Before spawning any agent: read the North Star, then read the wave scope. Are they compatible?
- Judge phase: "Does this output move toward the North Star or away from it?"
- Schema design: design for the vision, not just the current wave. Unified tables > dedicated tables.
- Acceptance criteria: always include one criterion that references the North Star explicitly.

**Why:** Catching scope drift at design time costs 0. Catching it at testing time (Session 88) costs a full-day pivot session.

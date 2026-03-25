---
name: pwj-grok-tandem-loop
description: Run PWJ audit first (quality floor + mechanical fixes), then Grok Heavy sparring (strategic ceiling + political blind spots). Neither tool alone is sufficient for high-stakes documents with both technical and political dimensions.
type: feedback
---

## Pattern: PWJ → Grok Heavy Tandem Loop

**Rule:** For high-stakes documents with both technical quality requirements AND political/strategic considerations, run PWJ first, then immediately run Grok Heavy sparring on the same material.

**Why:** PWJ finds mechanical errors (unverified placeholders, missing verifications, weak language). Grok finds strategic flaws that PWJ misses (political risks, jurisdiction issues, ROI assumptions, meeting priority inversions). In S99: PWJ found 4 fixable issues → GREEN. Grok found 3 strategic flaws PWJ never surfaced: Aku Kärki COI risk, Lieksa contract unverifiable publicly, Metsähallitus jurisdiction gap. Neither tool alone was sufficient.

**How to apply:**
1. Run `/pwj` → get GREEN (mechanical quality confirmed)
2. Immediately run Grok Heavy using grok-spar template — include the same documents as context
3. Feed Grok findings back into documents + meeting briefs
4. If Grok changes meeting priorities dramatically → that's signal, not noise. Apply it.

**Characteristic output of Grok that PWJ misses:**
- Political risks involving stakeholders (COI, equity objections)
- Verifiability of third-party claims (are precedents actually public?)
- Meeting agenda priority inversions ("you have the order wrong")
- Jurisdiction/legal boundaries not visible from document text alone

**When NOT to use:**
- Routine document formatting → PWJ alone
- Pure strategic brainstorming without existing document → Grok first, PWJ after

**Source:** S99 (2026-03-19) — Kulusiirto paketti audit

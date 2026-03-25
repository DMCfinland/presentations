# DELIVERY STRATEGY — DMC-SECONDBRAIN-CRM
**Version:** 1.0 | **Date:** 2026-03-11

---

## Adoption Sequence

**Rule:** Never present this as "an AI system." Present it as "your system."
**Never:** "The AI decided" | **Always:** "The system found this for you — want to keep it?"

---

## Day 1 — Vibe Demo

**Goal:** Build confidence that something better than Pipedrive already exists.
**Audience:** Patrick (self-review)

Actions:
1. Open VIBE-DEMO.html in browser
2. Red team it yourself: Does it feel like Pipedrive? Is anything confusing?
3. Fix anything that feels "techy" or "AI-y" before Sebastian sees it
4. Save a screenshot for your own reference

Success: Patrick says "yes, I'd use this."

---

## Week 2 — Sebastian + Liisa Intro

**Goal:** Stop Pipedrive pressure. Show something real. Get verbal commitment to pilot.
**Format:** 30-minute casual meeting, Patrick's laptop

**Script (for Sebastian):**
"Sebastian, I want to show you something we've been building. It's a system that automatically shows us our client pipeline — what's happening, who's working on what. It pulls this from the emails and proposals we already have. No extra work from you. Take a look."
[Open VIBE-DEMO.html]
"What do you think? Does this show you what you need to see?"

**Script (for Liisa):**
"Liisa, one thing this does is show you the full picture of what's coming in — before you even have to look for it. See this card? This would have appeared automatically when AHI Travel sent their latest inquiry. What data would you want to see on a card like this?"

**What to capture:**
- What they liked (replicate in build)
- What confused them (fix before Reeta sees it)
- What they asked for (add to backlog)
- Verbal: "Would you use this?" → YES required to proceed with live build

**What NOT to say:**
- Anything about "AI" or "machine learning" or "automation"
- Anything about "replacing" TravelTree or current workflows
- Any promises about timeline ("it'll be done in 2 weeks")

---

## Per-Person Adoption Pitches

### Sebastian Heiskanen (Easiest — start here)
**Pain:** Deals lost because no central view. Has to check emails manually.
**Pitch:** "You'll never have to dig through email to find deal status again. It just appears."
**Demo moment:** Show a deal card that appeared from an email with zero manual entry.
**Win condition:** He checks the Kanban first instead of email.

### Liisa Vihermaa (Data-focused)
**Pain:** Incomplete picture of what's in the pipeline.
**Pitch:** "You'll see things you didn't know we had — deals that fell through the cracks."
**Demo moment:** Show the "AI-enriched today" count. "These are new opportunities the system found."
**Win condition:** She asks "where did this data come from?" and is pleased by the answer.

### Laura Ilvonen (Completeness-focused)
**Pain:** Group ops scattered across email + TravelTree + notes.
**Pitch:** "All your group trips in one place, connected to TravelTree."
**Demo moment:** Click "Open in TravelTree" from a deal card.
**Win condition:** She uses the TT link from the CRM instead of navigating directly.

### Reeta Vihavainen (Highest bar — last)
**Pain:** First AI tool at work. Worried about control and accuracy.
**Pitch:** "Everything needs your approval before anything happens. The system is read-only by default — you're always in control."
**Demo moment:** Show the "Needs your review" queue. "The system found this, but nothing moves forward until you say so."
**Win condition:** She reviews 3 cards solo without asking for help.

### Janna Kankkunen (Head of Sales — Pipedrive comparison)
**Pain:** "Why isn't this Pipedrive?"
**Pitch:** "We built something that does what Pipedrive does, plus auto-fills from your emails. Pipedrive requires you to enter data. This one enters it for you."
**Demo moment:** Show side-by-side: Pipedrive empty card vs DMC card pre-filled from email.
**Win condition:** "OK, I see why you built this instead of buying Pipedrive."

---

## Week 4 — Internal Pilot

**Goal:** First real workflow completed without Patrick's help.
**Audience:** Sebastian + Liisa (pilot users)
**Format:** 20-minute solo session, Patrick observes but does not help

Tasks for pilot:
1. Log in
2. Find an existing deal and check its status
3. Move a deal to the next stage
4. Find the "needs review" queue
5. Mark one AI-enriched card as verified

Success: Both complete all 5 tasks in <20 minutes. If stuck on any task → UX fix before Reeta.

---

## Week 5 — DPIA Gate

**STOP. Do not proceed with live email mining until:**
1. DPIA document written + signed
2. Finnish DPA notification submitted (if required by Art. 36)
3. Supabase DPA signed
4. Retention periods documented
5. Deletion pipeline tested
6. Patrick reviews with counsel or GDPR consultant

**Consequence of skipping:** Finnish DPA (Tietosuojavaltuutettu) enforcement action + potential fine.
**Practical note:** DPIA is not a blocker for the demo or UI build — only blocks live email mining.

---

## Week 8 — MVP Launch

**Success criteria (all required):**
- [ ] Sebastian + Liisa using system daily (check auth.sessions — >3 logins/week each)
- [ ] Reeta has completed first workflow solo
- [ ] 0 client-facing actions without approval in first month
- [ ] Pipedrive conversation ended
- [ ] AHI Travel deal visible and accurate in pipeline

**Fallback (Month 3):** If adoption fails for any staff member:
1. Interview them: what's missing?
2. Build that specific feature first before anything else
3. If systemic failure: consider Moonstride as fallback CRM (named in CRM Decision Synthesis)
4. Do NOT announce Moonstride as fallback to staff — creates false urgency

---

## Communication Rules (all channels)

**What to say:**
- "Your pipeline" not "the CRM"
- "The system found this from your emails" not "AI extracted this"
- "Nothing goes to clients without your approval" — say this explicitly, early, often
- "This works alongside TravelTree" not "instead of"

**What to never say:**
- Any of the forbidden words from INTAKE.md
- "Beta" / "prototype" / "demo" (call it "your system")
- Anything implying the system acts autonomously
- Promises about what will be added later (under-promise, over-deliver)

---

## If Staff Pushes Back

| Objection | Response |
|-----------|----------|
| "What if it sends something wrong to a client?" | "It can't. Nothing goes to clients without your say-so. The system suggests; you decide." |
| "I don't trust what the AI finds" | "Good instinct. Everything it finds has a 'Needs review' label. You verify before it counts." |
| "This is too complicated" | [Fix the UI. Don't explain. If they say this, something in the UX is broken.] |
| "I prefer Pipedrive" | "Walk me through your Pipedrive workflow. Let's see if we can match it — or beat it." |
| "What happens to our client data?" | "It stays in our own system in Finland. We signed a data agreement. Your data, your system." |

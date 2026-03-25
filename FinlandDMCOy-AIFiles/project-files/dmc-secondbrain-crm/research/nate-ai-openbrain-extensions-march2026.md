# Nate AI — Open Brain Extensions Research
**Date:** 2026-03-13 | **Source:** natesnewsletter.substack.com (March 13, 2026)
**Article:** "You built an AI memory system. Now your agent needs hands. Here are 6 extensions that compound."
**YouTube:** https://www.youtube.com/watch?v=japT66frdhM&t=473s (transcript not accessible — companion video)
**Relevance:** HIGH — visual layer design directly applies to BP08 Staff Dashboard v2.0

---

## Source Article — Full Key Concepts

### The Core Problem Nate Solves
> "The hard part is knowing what to put in it."

Infrastructure works. Content strategy doesn't. The fix: build extensions where BOTH human and agent see and act on the same data. Shared surface, two doors.

---

## The Two-Door Principle (PRIMARY CONCEPT)

> "A shared surface with two doors. Your agent enters through one. You enter through the other. Both sides read the same data, both sides write to it, and each one does what it's best at."

**Why this matters for BP08:**
Current design has this implicitly (n8n writes, staff reads Kanban). Nate makes it explicit and shows why it's the correct architecture. The failure mode is building only the agent door (data goes in, no human surface) or only the human door (Pipedrive — humans enter data manually, no agent).

**Four modes required per surface:**
1. Agent reads
2. Agent writes
3. Human reads
4. Human writes

Our Kanban board satisfies all four: n8n writes (agent door), staff reads + manually updates (human door).

---

## Four Design Principles

### 1. Time-Bridging
> "Your agent bridges time. Its memory doesn't decay. Anywhere the value comes from linking events spread across months or years, that's your agent's territory."

Example: Dishwasher warranty expiring + technician comment 18 months ago = agent surfaces connection autonomously.

**DMC application:** Client inquired about Lapland in March 2024 → came back in March 2026. Agent bridges 2-year gap: "AHI Travel last booked this route in 2024 — here's what we quoted, what changed in pricing, who guided the trip." Staff gets institutional memory on first contact.

### 2. Cross-Category Reasoning
> "The power isn't in any single table. It's in the connections between tables that no human would cross-reference manually."

Example: Both parents' schedules + all kids' activities → conflict detection no human would catch manually.

**DMC application:** Deal stage + staff workload + supplier availability + seasonal window = "Liisa has 7 active deals in proposal phase right now — Regent is the highest risk to reassign before April." Cross-referencing deal table + staff load + seasonal deadlines.

### 3. Proactive Surfacing
> "The most valuable answers are to questions you didn't ask. A database waits for queries. An agent notices things proactively."

Example: Meal planner volunteers fish gap + Thursday logistics without being asked.

**DMC application:** Our stale deal alerts do this. Extension: seasonal pricing window closures ("Lapland aurora season rate valid until March 31 — 3 deals still in inquiry stage"), supplier capacity alerts, flight season notifications.

### 4. The Judgment Line (MOST IMPORTANT)
> "Agent surfaces, human decides, agent executes. The agent handles memory and pattern recognition. You handle judgment. The division is clean and it's what makes the system trustworthy. Blur the line and you'll stop using it."

Example: Agent spots James needs follow-up, gives full context → human decides IF and HOW → agent executes.

**DMC application:** This is already our approve/dismiss flow for AI activity suggestions. Nate validates this as the correct design. Staff must stay the decision-maker or adoption collapses.

---

## The Pull/Push Paradigm

> "Conversational clients handle the pull — you ask a broad question and the agent reasons across your data in the moment. Autonomous agents handle the push — they scan your data on a schedule and surface what's urgent before you think to ask. Same database, different interfaces."

**Mapping to BP08:**
| Mode | In BP08 | Trigger |
|------|---------|---------|
| PUSH | Morning briefing (08:30 Teams) | Cron — autonomous, scheduled |
| PUSH | Stale deal alerts | Cron — n8n W3 |
| PUSH | Proposal opened notification | Event — n8n W4 webhook |
| PULL | Kanban board (staff opens it) | Human action |
| PULL | Deal detail drawer | Human action |
| PULL | Morning dashboard (staff reviews) | Human action |

Both modes hit the same Supabase tables. Architecture is correct.

---

## The Visual Layer Argument

> "Planning is visual — it requires scanning and comparing and making quick decisions while you're both looking at the same picture."
> "A chat window is a keyhole. You can ask one question and get one answer. You can't see the landscape."

Nate explicitly argues a chat interface alone is insufficient for pipeline/scheduling tasks because:
- You need to **scan** (see all deals simultaneously)
- You need to **compare** (stage distribution, workload)
- You need to **spot patterns** spatially (Thursday conflict visible on calendar, not in text)

**Validates BP08 Kanban decision.** Teams notifications = conversational interface for time-sensitive pushes. Kanban = visual interface for spatial/scanning tasks. Both required.

---

## The Amnesia Problem

> "Every one of these agents has the same problem: they can't remember you. New sessions start from zero, tool switches wipe the slate."

OpenClaw: 250K GitHub stars in 2 months (fastest open-source project in history). Devin: $1M → $73M ARR in 9 months. Sierra: $10B valuation. All have the same amnesia problem.

**What this means for DMC:** Our pgvector embeddings of 107 client profiles + email threads = organizational memory layer. Every time a staff member opens a deal, the agent has full history. This is a competitive moat.

---

## The Emotional Corrective (NEW ANGLE)

> "Your brain — which is wired to construct narratives from recent experience — starts telling you a story. The story says you're not good enough. The story is wrong, but it feels true."

> "You've advanced past five of seven first-round interviews, a 71% conversion rate. The rejections are telling you something about fit, not ability."

**DMC application:** When a deal goes cold or a proposal gets rejected, the data corrects the distortion. Morning dashboard could show: "You've won 7 of last 10 proposals in this stage — this one is still early." Prevents spiral, maintains confidence.

---

## Six Extension Use Cases (Pattern Library)

| Use Case | Nate's Domain | DMC Translation |
|----------|--------------|-----------------|
| Household knowledge | Home maintenance facts | Supplier knowledge base (rates, contacts, history) |
| Home maintenance (time-bridging) | Warranty + service history | Client history + pricing evolution |
| Kid logistics (cross-category) | Schedules + tasks + deadlines | Staff workload + deal deadlines + supplier windows |
| Meal planning (proactive) | Pantry + schedule + nutrition | Seasonal availability + pricing windows |
| Professional relationships (judgment line) | Network maintenance | Client relationship health + follow-up timing |
| Job hunt (all principles) | Pipeline + pattern recognition | Deal pipeline + win rate + pattern analysis |

---

## The Open Brain Technical Architecture (OB1)

From promptkit.natebjones.com companion guide:

**Core stack:**
- Supabase (thoughts table: content + vector 1536-dim + JSONB metadata)
- OpenRouter (text-embedding-3-small + gpt-4o-mini)
- Slack (capture interface)
- MCP server (semantic search + recent listing + stats + capture)

**Matches DMC stack exactly:**
- Supabase ✓ (our relational + pgvector)
- text-embedding-3-small ✓ (our D33 decision)
- MCP ✓ (our planned agent access layer)
- n8n instead of Slack (we use email as capture, not Slack)

**Security model:** RLS + 64-char access key validated per request — matches our Wave 1A schema.

**`match_thoughts()` function:** Semantic similarity search, threshold 0.7, configurable limits — same pattern as our planned pgvector queries.

---

## Delta Analysis — New vs Already Captured

### Already in nate-ai-secondbrain-research.md (don't re-document)
- AI loop concept
- Frictionless capture
- Four-layer architecture (Capture → Organization → Processing → Automation)
- Morning digest as primary surface
- Vector + relational hybrid
- Zero manual entry as adoption strategy
- Open brain / no vendor lock-in
- n8n over Zapier

### NET NEW in this article
1. **Two-door principle** (named, explicit, architectural framework)
2. **Four design principles** (time-bridging, cross-category, proactive surfacing, judgment line)
3. **Pull/push paradigm** (named distinction between scheduled push and on-demand pull)
4. **Visual layer argument** (explicit case for WHY Kanban/dashboard, not just chat)
5. **The emotional corrective** (data corrects stress-induced narrative distortion)
6. **Six extension pattern library** (concrete use cases → DMC translations)
7. **Amnesia problem** framing (memory layer as competitive moat)
8. **OB1 GitHub structure** (community contributions, automated PR review with 11 rules)
9. **OpenClaw / Moltbook** context (agent proliferation → amnesia problem widespread)
10. **Cost data**: 20 thoughts/day = $0.10-0.30/month (validates our pgvector cost model)

---

## BP08 Evolution Opportunities (Pre-Grok Analysis)

### Confirmed Design Choices (Nate validates)
- Kanban board → correct for spatial/scanning work ✓
- Morning briefing (push) → correct ✓
- Approve/dismiss for AI suggestions → judgment line maintained ✓
- Realtime Supabase updates → correct (team visual layer) ✓
- pgvector embeddings → correct architecture ✓

### Potential Improvements for Grok to Evaluate

**1. Time-bridging panel on deal cards**
"Similar historical deals" — when viewing a deal, surface top 3 semantically similar historical deals with outcomes. Gives sales staff institutional memory on first contact. Requires pgvector semantic search + deal outcome data.

**2. Cross-category reasoning view**
Staff workload + deal deadlines + seasonal windows in one view. Currently: stale deal alerts per deal. Future: "Liisa has 7 deals in proposal phase — 3 expire before April 30 — she is at capacity." Requires staff load calculation.

**3. Emotional corrective metric**
"Pipeline health" line on morning dashboard: "Your win rate this quarter: 6/9 (67%) — above team average (58%)." Prevents stress-induced narrative distortion. Requires win/loss tracking + historical rate calculation.

**4. Proactive seasonal alerts**
System surfaces pricing window closures proactively without staff asking: "Aurora season rates valid until March 31 — 3 deals in inquiry stage haven't received proposal yet." Requires rate card integration + deal stage filtering.

**5. Two-door principle for supplier data**
Agent writes supplier knowledge (new rates, availability, capacity from emails) → human reads supplier panel on deal card. Currently suppliers are static. Extension: n8n classifies supplier emails → updates rate_cards table → deal cards reflect current availability.

---

## YouTube Note

Video `japT66frdhM` at timestamp 473s (≈7:53) not accessible via WebFetch (JS-only rendering). Likely the companion video to this Substack article or the original "Build your second brain" series.

**Action needed:** YouTube transcript skill required for future Nate AI video mining.

---

*Source: [natesnewsletter.substack.com — March 13, 2026](https://natesnewsletter.substack.com/p/you-built-an-ai-memory-system-now)*
*YouTube companion: https://www.youtube.com/watch?v=japT66frdhM&t=473s*

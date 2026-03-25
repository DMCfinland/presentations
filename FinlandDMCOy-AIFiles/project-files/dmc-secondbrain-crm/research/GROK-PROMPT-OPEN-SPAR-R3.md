# Grok Prompt — Open Spar Round 3
**Date:** 2026-03-13
**Model:** Grok 4 Heavy (4-agent council)
**Mode:** Strategy Spar — fully open, no pre-loaded conclusions
**Template base:** Template 2 + Parallel protocol
**Paste to:** grok.com → select Heavy mode → paste PASTE START...PASTE END

---

## PASTE START

OUTPUT FORMAT: Four sections — (1) What this system is fundamentally capable of that we're not using yet, (2) What would break this system at scale or over time, (3) What a smarter competitor would do differently, (4) Lucas's single strongest challenge to the entire direction. Label every finding [Harper]/[Benjamin]/[Lucas]. Surface agent disagreements explicitly — do not resolve them.

GOAL: We have built an AI second brain CRM for a small travel company. Tell us what we are missing, what is wrong with our direction, and what we should be building that we haven't thought of.

CONTEXT:

**The company:** A 5-person Finnish destination management company (B2B group travel, inbound tourism). Clients are European and global tour operators, corporate buyers, and specialist travel agents. Revenue: approximately €1.5M/year. Relationships are long-term — 5-10 year client histories are normal. Finnish B2B culture: reserved, trust-based, no hard sell.

**What we've built so far:**
- Supabase database (self-hosted, Hetzner Frankfurt) with 14 tables: clients, contacts, deals, deal_activities, deal_stage_history, suppliers, rate_cards, deal_embeddings (pgvector 1536-dim), and supporting tables
- All 107 active client profiles embedded as atomic facts using text-embedding-3-small
- n8n automation platform reading the company's Microsoft 365 shared mailbox via Graph API
- A Next.js Kanban board showing deals in 6 stages: inquiry → proposal_sent → revision → confirmed → operating → invoiced
- Morning dashboard: personalized list of 3 priority actions per staff member, generated at 07:00, delivered at 08:30 via Teams
- Stale deal alerts: yellow at 7 days, red at 14 days, delivered to deal owner
- AI activity suggestions: agent suggests next action on each deal, staff approves/edits/dismisses — never auto-executes

**The only data source:** Company email (Microsoft 365). No CRM history was imported. No manual data entry. Everything the system knows came from parsing email threads.

**What the system does NOT have yet:**
- No integration with the itinerary/booking tool (TravelTree)
- No calendar integration
- No supplier database (supplier rates live in email threads only)
- No client history before the email mining started
- No external data sources of any kind

**The design constraint we will never break:** Agent surfaces → human decides → agent executes. Staff must approve every outreach and every stage change that isn't obviously mechanical. Zero exceptions.

**The North Star — what we want this system to feel like in 3 years:**
"Every morning I open the PWA and the Second Brain has already prepared my day: three hot opportunities it spotted overnight — a client's seasonal booking window is opening in 10 days with a ready strategy and email draft; a high-value dormant account's historical pattern says now is perfect; plus two upsell chances on current groups drawn from identical past wins. I click into each card, review the three-option brief, tweak one sentence if needed, hit Approve — the agent sends the perfectly personalised message, tracks opens, and only nudges me later if required. The system remembers every client interaction, seasonal cycle, supplier rate, and successful approach from the last five years better than any of us ever could, so our tiny 5-person team operates with the memory and foresight of a 50-person operation. It surfaces what matters, suggests without ever deciding, and lets us spend every minute on the relationships that actually close deals."

COLLABORATION PROTOCOL: Parallel — all three agents produce independent analysis simultaneously via chatroom_send, with NO shared context between them until synthesis. Then Lucas runs a dedicated critique round attacking both the emerging synthesis AND the other agents' findings. Grok Captain synthesizes only after Lucas's critique. Do not smooth over disagreements between agents — show them explicitly.

TOOL ACTIVATION:
- Harper: web_search + x_semantic_search — find how the best B2B sales intelligence systems in 2025-2026 actually work. Search for: travel DMC CRM systems, B2B relationship intelligence platforms, proactive sales AI, what top relationship-driven sales teams use that small teams don't. Find real examples, not theory.
- Benjamin: use code_execution to reason about the data math — 107 clients × 5-10 year histories × ~50 emails/client/year = how many data points does this system realistically have? What does that mean for pattern detection reliability? What sample sizes make seasonal pattern claims statistically meaningful vs noise?
- Lucas: argue the strongest case that this North Star is the wrong direction entirely. What if the real problem isn't surfacing opportunities — what if it's something else? What does this system get wrong about how a 5-person travel team actually works?
- Grok Captain: after all tools return, synthesize with full agent disagreements visible. Do not soften Lucas.

CONSTRAINTS (priority order):
1. Do not validate what we've already built — assume it's correct and tell us what's MISSING
2. Do not suggest what we already said in the context — if you find yourself proposing something we've described, go deeper or find something different
3. Benjamin: verify your data math with actual computation before making claims about pattern reliability
4. Harper: cite live examples — not what a system could theoretically do, but what systems that exist today actually do
5. If any agent is uncertain: use tools before stating a conclusion

QUALITY BAR:
- Must include: at least one capability we haven't mentioned at all, one specific way this system could fail in year 2-3, one thing a well-funded competitor would do that we can't or haven't
- Must avoid: generic "use AI for X" advice, restating what we described in CONTEXT, advice that requires more than 5 staff to implement
- If agents disagree: show the disagreement explicitly and let us decide

VERBOSITY: Go deep. Every section should have enough detail to act on. Do not summarize — expand.

## PASTE END

---

## Pre-Flight Anti-Pattern Scan Results

1. Does OUTPUT FORMAT contain pre-filled verdicts, votes, or recommendations? → NO. Structure only (4 sections + labels).
2. Does CONTEXT contain our preferred conclusion framed as background? → NO. Context is factual system description. North Star is labeled as aspiration, not conclusion.
3. Could Grok echo back what's already written without doing any independent reasoning? → NO. We explicitly instruct: "Do not suggest what we already said in the context — if you find yourself proposing something we've described, go deeper or find something different."

✓ Clean. Safe to paste.

---

## After Getting Grok Response

Save full response as:
`FinlandDMCOy-AIFiles/project-files/dmc-secondbrain-crm/orchestration/GROK-OPEN-SPAR-R3-RESULT.md`

Debrief checklist (per grok-spar skill):
- [ ] Did Harper cite live URLs? (real tool use, not simulation)
- [ ] Did Benjamin show computed output? (verify the data math independently)
- [ ] What did Lucas specifically challenge? (highest-value output)
- [ ] Any agent disagreements? (don't resolve — bring back for discussion)
- [ ] Any numbers flagged by Benjamin? (verify independently before acting)

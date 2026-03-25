# Build-vs-Buy Decision Framework for Strategic Tools
**Version:** 1.0
**Source:** Session 58 CRM decision (2026-03-10) — 3 Grok rounds + 4 Claude subagents
**Validated:** Finland DMC Pipedrive vs Custom Second Brain decision

---

## When to Use This Framework

- Tool investment >EUR 5K/year OR strategic to daily operations
- Team has emotional attachment to a specific vendor ("can't we just get X?")
- Build-vs-buy is genuinely open (not already decided)
- Niche business where generic tools may not fit

**Cost:** ~$0-3 total (Grok free tier, Claude subagents ~$0.50 each)

---

## The 5-Step Process

### Step 1: Deep Research on the Incumbent/Favorite (Grok)
Ask 12-15 structured questions about the tool the team wants. Cover: strengths, weaknesses, pricing, integrations, adoption stats, industry-specific gaps, data export options.

**Why Grok:** Free, web-connected, handles broad research well. Save Claude budget for focused analysis.

### Step 2: Emotional Appeal + Adoption Risk (Grok Follow-up)
Separate round. Ask: why do teams love this tool? What's the adoption failure rate? What are the real-world complaints after 3-6 months? What does the team actually want vs what the tool actually delivers?

**Why separate:** Step 1 gets features. Step 2 gets feelings. The decision usually hinges on feelings.

### Step 3: Landscape Scan (Grok)
Ask Grok to compare 10-15 alternatives across the same criteria. Include: industry-specific tools, AI-first tools, open-source options, "anti-CRM" tools. Rate each on your team's top complaint (e.g., data entry burden).

**Output:** A pre-distilled briefing document combining all 3 Grok rounds + your own system plans. This becomes shared context for Step 4.

### Step 4: Parallel Claude Subagents (3-5 agents)
Spawn specialized analysts, each reading the same briefing document. Recommended roles:

| Agent | Angle | Key Question |
|-------|-------|-------------|
| UX & Adoption | Emotional hooks, day-1 experience | Will the team actually use it? |
| Technical Architect | Stack, TCO, build effort, integrations | Can we build it? What does it cost over 3 years? |
| Operations Specialist | Industry-specific workflows | Does it solve our actual daily work? |
| Change Management | Communication, rollout, risk mitigation | How do we sell this decision to the team? |

**Each agent writes to a separate file.** Lead synthesizes after all complete.

### Step 5: Synthesis + Decision
Read all agent outputs. Look for: unanimous vs split verdicts, blind spots, emotional vs rational arguments. Write a single decision document with: verdict, reasoning, implementation plan, fallback.

---

## Pattern 1: Tool Adoption for Small Teams (<20 people)

### The Data Entry Paradox
Staff complains about data entry but gets excited about tools that require it. The complaint is not about entry itself — it's about entry into systems that give nothing back. Pipedrive requires 3-5 manual actions per deal, but staff loves it because each action produces visible feedback (card moves, checkbox completes, notification fires).

**Implication:** If building custom, you must provide visible feedback for invisible work. Auto-captured data should generate notifications. Silent background processing feels like nothing changed.

### The Three-Step Pitch: Validate, Educate, Co-Create

**Never say "your idea was bad."** Even if the team's preferred tool is wrong for the business.

1. **VALIDATE (5 min):** "I heard you. [Tool X] is good — I researched it seriously. Your instinct that we need [category] is correct."
2. **EDUCATE (10 min):** Show the gaps. Let the team arrive at the conclusion. Data points, not verdicts. "Here's what I found" not "here's what I decided."
3. **CO-CREATE (20 min):** "Here's what I want to build — what would make YOU open this every morning?" Write their answers down visibly. They become co-designers, not recipients.

### Staged Reveal (Feelings First, Features Second)
Never do a big-bang launch. Each week delivers one "wow" moment:
- Week 1: Something visible immediately (even a manual Kanban board in an existing tool)
- Week 2-3: First automated feature goes live
- Week 4: The "magic moment" — system surfaces something nobody manually entered
- Month 2-3: Full system operational

**Critical rule:** Each stage must work perfectly before revealing the next. One buggy experience poisons the well.

### Temporary Bridge Tool
If custom build takes weeks, deploy a bridge on Day 1 using tools the team already has (Planner, Notion, Airtable). Populate it with real data. Message: "Here's your view — today. The real system replaces this and updates itself."

This kills the "nothing is happening" narrative and proves you listened.

### Month 3 Checkpoint with Named Fallback
Set an honest deadline. "If by month 3 you don't see clear value, we go with [named alternative]. No sunk cost, full data export."

**Why this works:** Removes "this will never be finished" fear. Creates accountability. The fallback being named (not vague) makes it credible.

### Per-Person Talking Points
Prepare individualized pitches based on work style:
- **Structured/formal staff:** Lead with data and thoroughness of research
- **Relationship-focused staff:** Lead with how the system understands relationships
- **Creative/casual staff:** Lead with freedom from forms and busywork
- **Detail-oriented staff:** Lead with completeness and audit trails
- **Professional staff:** Lead with the quality and professionalism of the tooling

---

## Pattern 2: Zero-Entry CRM Architecture

Applicable to any small company where staff resists data entry but needs pipeline visibility.

### Core Principle
The pipeline is a VIEW into auto-collected data — not a data entry tool. The system works even if staff never touches it.

### Architecture

| Layer | How It Works |
|-------|-------------|
| **Email mining** | Shared mailbox monitored continuously. Emails classified, matched to deals, parsed for next actions. |
| **AI classification** | Each email → deal stage detection + action extraction. New inquiry = auto-create deal. |
| **Deal auto-creation** | System creates deal cards from emails. Staff never fills a "new deal" form. |
| **Pipeline as view** | Kanban board reflects email-derived state. Cards move based on detected stage changes. |
| **Proposal tracking** | Host proposals as trackable links (not email attachments). Log views, time spent, revisits. |
| **Stale deal detection** | Time-based rules: no activity in X days = alert. Color-coded: green/yellow/red. |
| **Morning digest** | Daily per-person briefing: "3 things today" + overnight activity + alerts. AI-generated, not manual. |

### The Emotional Design
- Staff opens dashboard, sees everything without entering anything — "how did it know?"
- Proposal sent, notification when client opens it — anxiety of "proposal black hole" disappears
- AI suggests next action with context and draft — staff approves instead of decides — 80% cognitive load reduction

### Adoption Signal
The system is working when staff checks the dashboard BEFORE checking email. The dashboard becomes the starting point, not email.

---

## Pattern 3: CRM Industry Gap for Niche Businesses

### The Universal Split
No tool combines generic sales CRM (pipeline, activities, zero-entry) with industry-specific operations. The market is always split: generic CRM OR industry ops tool, never both.

### What This Means for Portfolio Companies

| Company Type | Generic CRM Covers | Industry Tool Covers | Gap (Custom Opportunity) |
|---|---|---|---|
| DMC / travel | Pipeline, proposals | Itineraries, suppliers, commissions, pax | Unified system with zero-entry |
| Resort / hospitality | Guest CRM, marketing | PMS, F&B, activity booking | Guest lifecycle across all touchpoints |
| Houseboat rentals | Booking pipeline | Fleet management, maintenance, seasonal pricing | Integrated booking + fleet ops |
| Any niche B2B | Sales pipeline | Domain-specific workflows | Always a gap |

**Decision rule:** If the industry-specific tool has a CRM layer, evaluate it (e.g., Moonstride for DMC). If its CRM layer scores <8/10 vs your needs, build custom CRM + integrate the ops tool via API. If no industry tool exists, build both.

**The custom build advantage:** For companies with <20 staff, the total cost of custom (AI-assisted build) is often LESS than 3-year SaaS licensing, while fitting perfectly.

---

## Pattern 4: Multi-Model Research Orchestration

### The Recipe
Use free/cheap models for breadth, paid models for depth. Never pay for research that free tools handle well.

| Phase | Model | Cost | Purpose |
|-------|-------|------|---------|
| Broad research (2-3 rounds) | Grok (free) | $0 | Web-connected, handles 15-question deep dives |
| Focused analysis (3-5 parallel) | Claude subagents (Sonnet) | ~$0.50 each | Specialized angles, structured output |
| Synthesis | Lead Claude session | ~$0.50 | Read all outputs, produce decision document |
| **Total** | | **$2-4** | Comprehensive decision with 6-8 research inputs |

### Execution Details

**Grok rounds (sequential, each builds on the last):**
1. Feature/capability deep dive on primary option
2. Emotional/adoption/risk analysis (separate round — different thinking mode)
3. Landscape scan of 10-15 alternatives

**Output between phases:** Write a pre-distilled briefing document (the Pipedrive Research Briefing pattern). Include: company context, staff map, current system, all Grok findings. This becomes the single input document for all Claude agents.

**Claude subagents (parallel):**
- Each reads the same briefing document
- Each writes to a separate output file
- Each has a specific angle and key question
- Context isolation is a feature — prevents groupthink
- 3-5 agents is the sweet spot. More = diminishing returns.

**Synthesis:**
- Read all agent files
- Look for: unanimous verdicts (strong signal), split verdicts (dig deeper), blind spots
- Write single decision document: verdict, evidence, plan, fallback, cost

### When to Use
- Any strategic decision where the team has a preferred option and you need to validate or override it
- Investment >EUR 5K/year or tool that 3+ people use daily
- Situations where emotional and rational factors both matter (most tool decisions)

### When NOT to Use
- Commodity tools with obvious best choice (e.g., password manager, file storage)
- Decisions under EUR 1K/year — just try the top 2 options
- Pure technical decisions with no adoption risk (e.g., which database)

---

## Quick Reference: Reusable Artifacts from DMC CRM Decision

| Artifact | Reuse For |
|----------|-----------|
| 15-question Grok prompt template | Any tool deep-dive |
| Emotional appeal follow-up prompt | Any tool where team has a favorite |
| 4-agent spawn pattern (UX, Tech, Ops, Change) | Any build-vs-buy with adoption risk |
| Pre-distilled briefing document format | Any multi-agent research task |
| Validate-Educate-Co-Create pitch | Any decision that overrides team preference |
| Month 3 checkpoint + named fallback | Any custom build with adoption uncertainty |
| Per-person talking points template | Any change affecting 3+ team members |
| Zero-entry architecture pattern | Any company where staff resists data entry |

---

## Source Files
- `FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/CRM-DECISION-SYNTHESIS.md`
- `FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/PIPEDRIVE-RESEARCH-BRIEFING.md`
- `FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/AGENT-1-UX-ADOPTION.md`
- `FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/AGENT-4-CHANGE-MANAGEMENT.md`

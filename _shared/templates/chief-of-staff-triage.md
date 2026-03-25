# Chief of Staff — M365 Multi-Company Triage Agent

Source: ECC chief-of-staff agent, adapted for 1658 Holdings (10 companies, M365)
Status: **TODO — Design document. Implementation requires MCP M365 connector in Claude Code.**

## Vision

An always-on triage agent that processes all incoming M365 communications across 10 portfolio companies, classifies them, drafts responses, and feeds intelligence into the Second Brain.

## The Problem It Solves

Patrick manages 10 companies (~50 employees). Critical signals are buried in:
- Email inboxes (multiple accounts)
- Teams messages and channels
- SharePoint notifications
- Meeting follow-ups that nobody tracked

**Today:** Patrick manually scans everything. Signals get missed. Knowledge stays in people's heads.

**With Chief of Staff:** Automated triage surfaces only what needs attention. Everything else gets classified, summarized, and routed to the Second Brain.

## 4-Tier Classification System

Every incoming message gets exactly ONE tier, applied in priority order:

### Tier 1: SKIP (auto-archive)
- Automated notifications (SharePoint sync, Teams bot alerts, system emails)
- Newsletter subscriptions, marketing emails
- Calendar confirmations without new information
- Read receipts, delivery confirmations
- **Action:** Archive. Show count only ("47 skipped").

### Tier 2: INFO ONLY (one-line summary)
- CC'd emails (Patrick not primary recipient)
- Group chat general discussion
- File shares without questions
- Team announcements (FYI, not action)
- **Action:** One-line summary per item. No response needed.

### Tier 3: MEETING INFO (calendar cross-reference)
- Messages containing meeting links (Teams, Zoom)
- Date/time proposals for meetings
- Agenda documents shared before meetings
- Meeting summary/minutes from Copilot
- **Action:** Cross-reference with calendar. Flag conflicts. Auto-fill missing agenda.

### Tier 4: ACTION REQUIRED (draft response)
- Direct questions to Patrick awaiting response
- Decision requests from company managers
- Client communications requiring owner involvement
- Financial approvals or signatures needed
- Board meeting preparation items
- **Action:** Load relationship context → draft response → present for approval.

## Company Routing

| Company | Signal Priority | Key People to Watch |
|---------|----------------|-------------------|
| Finland DMC | HIGH — client emails, pricing decisions | Liisa, Laura, Reeta, Sebastian |
| Järvisydän Oy | HIGH — board, financial, Markus updates | Markus Heiskanen |
| Lomakylä Järvisydän | MEDIUM — operations, saneeraus updates | Markus, saneeraus administrator |
| Arctic Cruises | MEDIUM — seasonal, partner negotiations | — |
| Resort Services | LOW — routine operations | — |
| Houseboat Saimaa | LOW — seasonal | — |
| Others (4 remaining) | LOW — flag only if unusual | — |

## Second Brain Integration — The Flywheel

This is the key innovation. The Chief of Staff doesn't just triage — it feeds the Second Brain:

```
Daily M365 Scan
    ↓
Classify (4 tiers)
    ↓
For each ACTION REQUIRED and INFO ONLY message:
    ↓
Extract intelligence signals:
  - Client mentions → update client-profiles.yaml
  - Pricing discussed → update revenue-intel
  - Staff capacity signals → update staff-map
  - Strategic decisions → update company knowledge files
  - New contacts → update relationship database
    ↓
De-sloppify pass (merge with existing, flag contradictions)
    ↓
Second Brain grows DAILY without dedicated mining sessions
```

### What This Means for DMC Second Brain

Today the DMC Second Brain was built through 5 mining sessions (emails, proposals, SharePoint). That was a one-time extraction. With the Chief of Staff:

- **New client inquiry from AHI Travel** → automatically profiled, added to client-profiles.yaml
- **Liisa sends a pricing email** → rate card changes captured in revenue-intel
- **Teams call about Koli** → transcript (via teams-transcription pipeline) → meeting insights extracted
- **Flash Pack re-engages** → orphaned account alert triggered (it's flagged in the gap report)

The Second Brain becomes a **living system** instead of a **snapshot**.

## Implementation Phases

### Phase 0: Prerequisites
- [ ] M365 MCP connector working in Claude Code (currently only in claude.ai Projects)
- [ ] Teams transcription enabled (see: `_shared/projects/teams-transcription-second-brain.md`)
- [ ] Define relationship context files per company
- [ ] Define Patrick's response tone per context (formal for board, casual for staff)

### Phase 1: Read-Only Triage (MVP)
- [ ] Connect to M365 email via MCP
- [ ] Implement 4-tier classification
- [ ] Generate daily briefing (morning summary of all companies)
- [ ] No auto-responses — all drafts require Patrick's approval
- [ ] Run for 2 weeks, tune classification accuracy

### Phase 2: Draft Responses
- [ ] Add response drafting for Tier 4 messages
- [ ] Load relationship context from company knowledge files
- [ ] Present drafts with [Send] [Edit] [Skip] options
- [ ] Track response patterns to improve tone matching

### Phase 3: Second Brain Feeds
- [ ] Extract intelligence signals from classified messages
- [ ] Route to correct Second Brain files (client profiles, revenue intel, staff map)
- [ ] De-sloppify pass before writing to Second Brain
- [ ] Weekly digest: "Here's what the Second Brain learned this week"

### Phase 4: Cross-Company Intelligence
- [ ] Pattern detection across companies ("3 companies reported supplier X issues")
- [ ] Cross-sell routing (Järvisydän guest asks about DMC tours → alert DMC team)
- [ ] Holdings-level dashboard of communication health
- [ ] Integration with Teams transcription pipeline for meeting intelligence

## Design Principles (from ECC)

1. **Hooks over prompts for reliability** — Use PostToolUse hooks to enforce follow-through checklists. LLMs forget instructions ~20% of the time; hooks don't.
2. **Scripts for deterministic logic** — Calendar math, timezone handling, classification rules that don't need LLM judgment → Node.js/Python scripts, not prompts.
3. **Knowledge files are memory** — Relationship context, company profiles, classification rules persist as .md/.yaml files, version-controlled in Git.
4. **Rules are system-injected** — Classification rules in `.claude/rules/` load automatically. The LLM cannot choose to ignore them.

## Related Files

- `_shared/projects/teams-transcription-second-brain.md` — Teams transcription pipeline (prerequisite)
- `FinlandDMCOy-AIFiles/finland-dmc-2.0/mining-outputs/proposals-2024/SECOND-BRAIN/` — existing DMC Second Brain
- `_shared/best-practices/company-intelligence-protocol.md` — 7-layer framework
- `_shared/templates/de-sloppify-mining.md` — cleanup pass for Second Brain feeds

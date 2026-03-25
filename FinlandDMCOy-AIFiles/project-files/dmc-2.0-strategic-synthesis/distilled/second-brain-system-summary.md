# Second Brain System — Distilled Summary for Agent 1 (Second Brain Analyzer)

**Distilled from:** 3 Opus-generated documents (3,953 lines, ~228KB)
**Distilled by:** DISTILL-A subagent
**Date:** 2026-02-22
**Purpose:** Primary input for Wave 1 Agent 1 — replaces direct reading of source files

> CRITICAL CONTEXT: PRD v3 (Feb 9, 2026) simplified Second Brain from the M365/Azure OpenAI stack designed in these documents to "Claude Teams Projects only." Every architectural decision below is flagged CONFIRMED or SUPERSEDED accordingly.

---

## Version Evolution

### File 1: `opus-m365-architecture-design.md` (2026-02-12)
- Recommends **Option A: Teams + SharePoint Lists + Power Automate + Azure OpenAI (GPT-4o, Sweden Central)**
- Full schema: 6 SharePoint Lists + Inbox Log + Prompt Versions
- 5 AI prompt templates (classification, daily digest, A4 page, meeting prep, weekly review)
- 4-phase implementation roadmap (Phase 0–2) with timeline and cost
- Dismissed Option B (Notion hybrid) and Option C (Copilot) with detailed comparisons

### File 2: `opus-build-execution-plan.md` (2026-02-12)
- Refines File 1 into a buildable execution plan
- Answers 6 owner questions: context compression, progress tracking, model assignment, Batch API, cost, build confidence
- Proposes 6-increment build with validation gates (Option D) — **replaces** original 14-step sequential plan from an addendum
- Adds microtask breakdowns (86 total), inter-increment handoff protocol, and Go/No-Go checklist
- References a 4th document: `opus-design-improvements-addendum.md` (not distilled here — see source)

### File 3: `opus-swot-and-build-optimization.md` (2026-02-12)
- CTO-style validation review
- SWOT analysis across 12 strengths, 11 weaknesses, 11 opportunities, 12 threats
- Validates Option D build plan recommended in File 2
- Identifies 5 missing deployment elements (Day 1 runbook, rollback plan, Phase 0 go/no-go criteria, staff onboarding checklist, DPIA)
- Extends scaling analysis to Year 5 and 50 staff
- Issues APPROVE WITH CONDITIONS verdict

**What was revised/dropped across files:**
- Original 14-step sequential build plan (from `opus-design-improvements-addendum.md`) was replaced by 6-increment Option D in Files 2 and 3
- Self-improvement claims from File 1 were downgraded in File 3: 3 of 4 loops require substantial human intervention
- Calendar integration was deprioritized to Phase 2 in Files 1–2; File 3 escalates it to Phase 1 priority as a gap

---

## DECIDED: Architecture Decisions Made

| Decision | Detail | Source | Status |
|---|---|---|---|
| Stack selection | Option A: Teams + SharePoint Lists + Power Automate + Azure OpenAI | File 1, Sec 1 | SUPERSEDED BY PRD v3 |
| AI provider | Azure OpenAI GPT-4o, Data Zone Standard EUR, Sweden Central | File 1, Sec 2.2 | SUPERSEDED BY PRD v3 |
| Storage layer | SharePoint Online, 6 lists + Inbox Log, dedicated site `/sites/dmc-brain` | File 1, Sec 3.1 | SUPERSEDED BY PRD v3 |
| Capture channel | Single Teams channel `#dmc-brain` (private); two-channel in addendum (bot DM for private feedback) | File 1, Sec 2.2 | SUPERSEDED BY PRD v3 |
| Confidence threshold | 0.6 — below routes to human review queue | File 1, Sec 2.2 | CONFIRMED (principle applies regardless of tool) |
| Classification categories | 4: client_interaction, team_feedback, weekly_win, growth_idea | File 1, Sec Appendix B Prompt 1 | CONFIRMED (content taxonomy valid) |
| Anonymous capture protocol | `[anon]` / `[anonyymi]` prefix strips identity; Inbox Log retains sender for debug only | File 1, Sec 4.4 | CONFIRMED (principle applies) |
| Relationship Health Score formula | Weighted: interaction frequency 30%, sentiment trend 25%, opportunity pipeline 20%, response time 15%, days since contact 10% | File 1, Sec 6.3 | CONFIRMED (scoring logic valid) |
| Retention policy | Interactions: 24-month rolling window; Clients/Contacts: indefinite | File 1, Sec 2.2 | CONFIRMED |
| Build approach | Option D: 6 increments with validation gates | Files 2 and 3, Sec 7.3–7.4 | SUPERSEDED BY PRD v3 (no longer building M365 stack) |
| Model assignment | Sonnet for Increments 1, 3, 5; Opus for Increments 2, 6; Split for Increment 4 | File 2, Sec 3 | SUPERSEDED BY PRD v3 |
| Prompt storage | Prompt Versions SharePoint List (8 columns, Status: Active/Inactive/Testing) | File 2, Sec 7 + File 1 Appendix | SUPERSEDED BY PRD v3 |
| GDPR compliance approach | Azure Sweden Central DPA; no EU data residency for Anthropic as of Feb 2026 | File 1, Sec 8.3 | PARTIALLY SUPERSEDED — Claude Teams has its own data handling; verify GDPR posture |
| Phase 0 scope | Patrick only, 10 clients, 4 weeks | File 1, Sec 7 | CONFIRMED (pilot-first principle) |
| Single-behavior design | Staff do ONE thing: type in capture channel, press enter | File 1, Final Notes + File 3, Sec 9 | CONFIRMED |

---

## OPEN: Unresolved Questions (at time of writing)

| Question | Source |
|---|---|
| Will single Power Automate Premium license trigger on other users' messages? (Assumption #7 — highest risk) | File 2, Sec 6.2 |
| Is Azure OpenAI access pre-approved for the tenant, or does it require a separate application (1–5 day delay)? | File 2, Sec 6.3, Dependency #6 |
| Can Power Automate read from Prompt Versions SharePoint List at runtime? | File 2, Sec 6.2, Assumption #1 |
| Can Azure Key Vault secrets be accessed from Power Automate Premium connector? | File 2, Sec 6.2, Assumption #2 |
| Can Teams thread reply detection work in Power Automate for the Fix Handler? | File 2, Sec 6.2, Assumption #3 |
| Do Adaptive Card action buttons (Mark Done, Fix, Snooze) trigger Power Automate flows? | File 2, Sec 6.2, Assumption #4 |
| Does GPT-4o handle Finnish/English mixed input with >85% accuracy? | File 2, Sec 6.2, Assumption #5 |
| Is weekly review Sunday 17:00 culturally acceptable in Finnish work culture, or should it be Monday 06:45? | File 3, Sec 2.2, W11 |
| Should calendar integration be Phase 1 (not Phase 2)? — File 3 says yes, Files 1–2 say Phase 2 | File 3, Sec 9 |
| DPIA requirement: is this system classified as high-risk under the EU AI Act (full enforcement Feb 2026)? | File 3, Sec 2.4, T6 |

---

## Key Design Choices (with citations)

| Design Choice | Source |
|---|---|
| Four-stage loop: Capture → Classify → Store → Surface | File 1, Sec 2.1 |
| HTTP action to Azure OpenAI (not Copilot, not M365 Copilot Studio) | File 1, Sec 2.2 |
| `temperature: 0.1` and `response_format: json_object` for classification | File 1, Appendix A, Flow 1 |
| 5 Power Automate flows: Classify & Route, Fix Handler, Daily Digest, Meeting Prep, Weekly Review | File 1, Secs 4–5 + Appendix A |
| Adaptive Cards format for all Teams deliveries (not plain text) | File 1, Sec 5.1 |
| Daily digest: <150 words, 06:45 EET Mon–Fri, personalized per staff member | File 1, Sec 5.1 |
| Weekly review: <250 words, Sunday 17:00 EET | File 1, Sec 5.2 |
| Meeting prep: triggered by "prep: [client]" or "valmistele: [client]", delivered within 30 seconds | File 1, Sec 5.4 |
| A4 Client Insight Pages: auto-generated weekly for Top 10, on-demand for others | File 1, Sec 6.1 |
| Pattern extraction threshold: 2+ mentions required (single mentions are noise) | File 1, Sec 6.3 |
| Conservative routing default: when uncertain, classify as `client_interaction` | File 1, Sec 8.2 |
| No forms, no tags, no decisions at capture time | File 1, Final Notes |
| CEO models behavior 4 weeks before staff onboarding | File 1, Sec 8.1 + File 3, Sec 9 |
| Measure capture rates quietly — never share individual metrics with team | File 1, Sec 8.1 |
| Restart-friendly culture: just start again, no backlog to process | File 1, Sec 8.1 |
| Build Option D selected: 6 increments with validation gates (not 14-step sequential) | File 2, Sec 1; File 3, Sec 7.3 |
| Opus for classification + integration; Sonnet for mechanical flows | File 2, Sec 3 |
| Batch API for testing only (50-sample accuracy), not for building | File 2, Sec 4 |
| Power BI dashboard for Patrick only, Phase 1 (free with M365 Business Premium) | File 1, Sec 5.3; File 3, Sec 6.4 |
| Power Apps Canvas App recommended for Phase 2 admin UI (not custom web app) | File 3, Sec 6.2 |
| Escape hatch: migrate to Notion in 2–3 days via CSV export if SharePoint UX blocks value | File 1, Sec 2.4; File 3, Sec 3.5 |

---

## Data Architecture

### Entities and Classification

| Entity | List | Key Fields | Notes |
|---|---|---|---|
| Companies | Clients | ClientName, RevenueTier (Top 10/Active/Occasional/Dormant/New), RelationshipHealthScore (1–10), HealthTrend, AccountOwner, AnnualRevenueEUR | Master record |
| People | Contacts | FullName, Company (lookup), Role, RelationshipStrength, DecisionMaker, PersonalNotes, PreferredLanguage | 1:N to Clients |
| Touchpoints | Interactions | InteractionDate, Contact (lookup), Company (lookup), Type, Summary, RawCapture, Sentiment, OpportunitiesIdentified, NextActions, ConfidenceScore | Heart of system; 24-month retention |
| Strategic plans | Growth Roadmaps | Client (lookup), CurrentState, TargetState, CurrentRevenueTier, TargetRevenueTier, KeyInitiatives, ConfidenceLevel, Status | 1 active per client |
| Staff sentiment | Team Feedback | FeedbackDate, StaffMember (optional — blank = anon), Category, Theme, Sentiment, Status | Anonymous capture supported |
| Wins | Weekly Wins | WinDate, StaffMember, Achievement, Impact, Client (lookup) | Celebration + morale |
| Audit | Inbox Log | CaptureTimestamp, RawInput, AIClassification, ConfidenceScore, RoutedTo, AIOutput, WasCorrected | Every capture logged |
| Prompt versions | Prompt Versions | PromptName, Version, PromptText, Status (Active/Inactive/Testing), AccuracyScore | Tracks prompt history |

### Storage Rules
- Retention: Interactions 24-month rolling window; Clients/Contacts indefinite
- Indexing required on Interactions: InteractionDate, Company, Contact (list view threshold hit ~Year 2 at 5,000 items)
- SharePoint site URL pattern: `https://[tenant].sharepoint.com/sites/dmc-brain`
- All data exportable via SharePoint REST API (JSON/CSV)

### Classification Output Schema
```json
{
  "category": "client_interaction | team_feedback | weekly_win | growth_idea",
  "client": "string or null",
  "contact": "string or null",
  "interaction_type": "Call | Email | Meeting | Event | Site Visit | Other | null",
  "summary": "1-2 sentence string",
  "sentiment": "Very Positive | Positive | Neutral | Negative | Concerned",
  "opportunities": ["array"],
  "next_actions": ["array"],
  "next_action_date": "YYYY-MM-DD or null",
  "topics": ["array, max 5"],
  "is_anonymous": false,
  "team_category": "Feeling | Idea | Challenge | Process | Kudos | null",
  "confidence": 0.0
}
```

---

## Integration Design

### Designed integrations (File 1 architecture — SUPERSEDED by PRD v3)

| Integration | Direction | Mechanism | Status |
|---|---|---|---|
| Teams → Power Automate | Inbound trigger | "When new channel message posted" connector | SUPERSEDED |
| Power Automate → Azure OpenAI (GPT-4o) | Outbound | HTTP POST, api-version 2024-10-21, Sweden Central | SUPERSEDED |
| Power Automate → SharePoint Lists | Read/Write | Native SharePoint connector | SUPERSEDED |
| Power Automate → Teams DM | Outbound | Adaptive Card delivery | SUPERSEDED |
| Shared mailbox → Power Automate | Inbound trigger (Phase 1) | Outlook shared mailbox trigger on info@finlanddmc.fi | SUPERSEDED |
| Microsoft Graph API → Outlook (outgoing emails) | Phase 1 addition | Graph API permissions, additional setup required | SUPERSEDED |
| Power BI → SharePoint Lists | Read | Direct connector, free for 1 viewer with M365 Business Premium | SUPERSEDED |
| Azure Key Vault → Power Automate | Secrets retrieval | Key Vault "Get secret" action | SUPERSEDED |

### Email capture logic (File 1, Sec 4.3)
- Incoming emails only in Phase 0–1
- Checks: sender in Contacts list → classify; sender domain in Clients list → classify + flag new contact; otherwise skip
- Rate limit: 10 emails/minute to avoid API throttling
- Historical backfill: 6 months, Top 10 clients only, ~500–1,000 emails

### Contact/Client lookup resolution (File 1, Appendix C)
- Fuzzy match by contains; 1 result = use it; 0 results = flag new; 2+ = shortest edit distance
- New contacts auto-created with FullName only, flagged for enrichment

---

## SWOT Conclusions

### Strengths (top 3)
- **Single-behavior design** (S1): Staff type in one channel, press enter — everything else automated. Validates Nate B Jones framework. Maximizes adoption probability.
- **M365-native architecture** (S2): No new tools, no new logins; staff already use Teams daily; storage layer invisible to end users.
- **GDPR-compliant by design** (S3): Azure Sweden Central, Microsoft DPA, no model training on customer data, audit trail, 24-month retention.

### Weaknesses (top 3)
- **Patrick is single point of failure** (W1, HIGH): System Owner + Daily Monitor + Prompt Maintainer. No backup. Mitigation: step-by-step maintenance runbooks; EUR 200/year IT consultant retainer.
- **No calendar integration** (W2, HIGH): Staff must remember "prep: [name]" before meetings — a second behavior, violating single-behavior principle. File 3 escalates to Phase 1 priority.
- **SharePoint Lists UX is poor** (W3, MEDIUM): Functional but not beautiful. Acceptable only because staff rarely touch storage layer.

### Opportunities (top 3)
- **Cross-company rollout** (O1, MUST-HAVE): Same architecture for all 10 portfolio companies; 4–6 hours per company; EUR 240/month total for enterprise-grade CRM intelligence across 50 staff.
- **Competitive differentiation via institutional memory** (O2, MUST-HAVE): Accumulated interaction history compounds; new hires onboard on a client in 2 minutes; knowledge does not walk out with departing staff.
- **Seasonal intelligence engine** (O3, SHOULD-HAVE): After 12 months, identify booking patterns and trigger proactive outreach ("Arctic Travel started Q4 planning last September — they haven't called yet").

### Threats (top 3)
- **Staff adoption failure** (T1, HIGH): Existential risk. If Patrick stops capturing, staff stop within 2 weeks. No technology fix. Single mitigation: Patrick commits 15 min/day for 28 days.
- **Microsoft M365 pricing increases** (T2, MEDIUM): Power Automate Premium pricing could rise. Mitigation: single-license approach; Azure Logic Apps documented fallback.
- **Azure OpenAI model quality degradation** (T3, MEDIUM): Classification accuracy drop from 90% to 75% erodes trust. Mitigation: prompt versioning enables rollback; prompts are model-agnostic.

---

## PRD v3 Supersession Check

PRD v3 (Feb 9, 2026): Second Brain simplified to **"Claude Teams Projects only"** — no custom M365/Power Automate/Azure OpenAI stack.

| Decision from source files | PRD v3 Status | Notes |
|---|---|---|
| Option A stack: Teams + SharePoint Lists + Power Automate + Azure OpenAI | **SUPERSEDED** | PRD v3 uses Claude Teams Projects as the entire stack |
| Azure OpenAI GPT-4o, Sweden Central, Data Zone Standard EUR | **SUPERSEDED** | Claude Teams Projects uses Anthropic's infrastructure |
| 6 SharePoint Lists as storage layer | **SUPERSEDED** | Claude Teams Projects replaces this |
| Power Automate Premium license (EUR 15/month) for HTTP connector | **SUPERSEDED** | No longer needed |
| HTTP action to Azure OpenAI endpoint | **SUPERSEDED** | Claude handles classification natively in Teams Projects |
| Prompt Versions SharePoint List for version control | **SUPERSEDED** | Prompt management handled within Claude Teams Projects |
| Azure Key Vault for API key storage | **SUPERSEDED** | No external API key required |
| Power BI dashboard (SharePoint Lists data source) | **SUPERSEDED** | No SharePoint Lists to connect to |
| 6-increment build plan (Increments 1–6) | **SUPERSEDED** | No M365 stack to build |
| Model assignment matrix (Sonnet/Opus per increment) | **SUPERSEDED** | Build plan replaced |
| Batch API for prompt testing (50-sample batches) | **SUPERSEDED** | Testing done within Claude Projects |
| Contact/client lookup resolution via Power Automate fuzzy match | **SUPERSEDED** | Claude handles context retrieval natively |
| Email monitoring flow (info@finlanddmc.fi via shared mailbox trigger) | **SUPERSEDED** | No Power Automate flows |
| Adaptive Cards delivery format | **SUPERSEDED** | Claude Teams Projects uses its own interface |
| GDPR: "Anthropic has no EU data residency as of Feb 2026" | **NEEDS RECHECK** | Claude Teams data handling terms must be verified for GDPR compliance |
| Confidence threshold 0.6 → human review queue | **CONFIRMED** | Principle valid; implementation moves inside Claude Projects |
| 4-category classification taxonomy (client_interaction, team_feedback, weekly_win, growth_idea) | **CONFIRMED** | Content schema is tool-agnostic |
| Single-behavior capture design (one channel, type, press enter) | **CONFIRMED** | Core philosophy unchanged |
| Relationship Health Score formula (5 weighted factors) | **CONFIRMED** | Scoring logic valid regardless of tool |
| Pattern extraction threshold: 2+ mentions | **CONFIRMED** | Prompt instruction, tool-agnostic |
| Anonymous capture protocol ([anon] prefix) | **CONFIRMED** | Needs implementation inside Claude Teams Projects |
| 24-month interaction retention policy | **CONFIRMED** | Data governance policy, tool-agnostic |
| Phase 0 pilot-first approach (Patrick only, 4 weeks) | **CONFIRMED** |
| CEO models behavior before staff onboarding | **CONFIRMED** |
| Daily digest format: <150 words, structured sections, bilingual Finnish/English | **CONFIRMED** | Content spec moves into Claude Projects prompt |
| Meeting prep format: <200 words, 5-section structure | **CONFIRMED** | Content spec moves into Claude Projects prompt |
| Weekly review format: <250 words, 6-section structure | **CONFIRMED** | Content spec moves into Claude Projects prompt |
| Client A4 Insight Page template (7 sections) | **CONFIRMED** | Template valid, generation moves to Claude |
| Day 1 runbook requirement | **CONFIRMED** | Still needed, different tool |
| Rollback plan requirement | **CONFIRMED** | Still needed |
| Phase 0 go/no-go criteria (6-question framework) | **CONFIRMED** | Criteria are tool-agnostic |
| DPIA requirement (GDPR Article 35) | **CONFIRMED** | Required regardless of stack |

### Summary: What PRD v3 keeps vs. replaces

- **Replaces:** Entire technology stack (Azure OpenAI, SharePoint Lists, Power Automate, Power BI, Key Vault, all flows, all connectors)
- **Keeps:** All content logic — taxonomy, prompts, scoring formulas, templates, data entities, deployment philosophy, GDPR obligations, and operational protocols

---

*Distilled: 2026-02-22 | Source files: opus-m365-architecture-design.md, opus-build-execution-plan.md, opus-swot-and-build-optimization.md | All three dated 2026-02-12*

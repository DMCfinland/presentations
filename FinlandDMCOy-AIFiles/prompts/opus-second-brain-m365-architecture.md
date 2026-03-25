# Opus Research Prompt: Second Brain for Finland DMC (M365 Architecture)

## Context

Finland DMC Oy operates in M365 environment (Teams, SharePoint, Outlook, Excel). We're designing a "second brain" system inspired by Nate B Jones's Slack + Notion + Zapier architecture, but adapted for:

1. **Customer relationship compounding** (1,000 client contacts, Top 10 = 50% revenue)
2. **Internal teamwork/leadership tool** (staff feedback, weekly progress newsletter)
3. **M365 native stack** (Teams instead of Slack, SharePoint/Lists instead of Notion?)

## Research Questions

### 1. M365 Stack Architecture

**Compare three options:**

**Option A: Teams + SharePoint Lists + Power Automate**
- Teams channel for capture (#dmc-brain)
- SharePoint Lists for databases (Clients, Contacts, Interactions, Plans)
- Power Automate for classification + routing + digests
- Azure OpenAI or Anthropic API for intelligence

**Option B: Teams + Notion Hybrid**
- Teams for capture + surfacing (low friction)
- Notion for structured storage (better UX than SharePoint Lists?)
- Power Automate + Zapier bridge
- Anthropic API for classification

**Option C: Full Microsoft Stack (Copilot-native)**
- Teams + Copilot for capture
- Dataverse for storage
- Power Automate Premium for AI workflows
- M365 Copilot API for intelligence (if available)

**Evaluate each on:**
- Friction to capture (must be <10 seconds)
- Classification accuracy (can we get structured JSON output?)
- Digest generation quality (daily <150 words, weekly <250 words)
- Cost (per user per month)
- Maintainability (when things break, how fast to fix?)
- Data sovereignty (GDPR compliance for client data)

### 2. Database Schema Design

**Customer-Facing Databases:**
- **Clients** (Companies we serve)
  - Fields: Name, Industry, Size, Revenue Tier (Top 10 / Active / Dormant), Account Owner, Last Contact, Next Action, Relationship Health Score
- **Contacts** (People at client companies)
  - Fields: Name, Company, Role, Relationship Strength, Personal Notes, Communication Preferences, Last Interaction
- **Interactions** (All touchpoints captured)
  - Fields: Date, Contact, Type (Call/Email/Meeting/Event), Summary, Sentiment, Opportunities Identified, Next Actions
- **Growth Roadmaps** (Per-client strategic plans)
  - Fields: Client, Current State, Target State, Key Initiatives, Timeline, Confidence Level, Blockers

**Internal Teamwork Databases:**
- **Team Feedback** (Staff sentiment and ideas)
  - Fields: Date, Staff Member (Anonymous Option?), Category (Feeling/Idea/Challenge), Summary, Status
- **Weekly Wins** (Progress tracking)
  - Fields: Date, Staff Member, Achievement, Impact, Category

### 3. Capture Workflow Design

**Customer Captures:**
- After client call: "Met with Mika from Arctic Travel. Discussed expanding winter programming. They're interested in Northern Lights packages. Follow up with proposal by Friday."
- AI extracts: Contact (Mika), Company (Arctic Travel), Opportunity (Northern Lights packages), Next Action (Send proposal by Friday), Sentiment (Positive)

**Team Captures:**
- Staff posts: "Feeling overwhelmed with quote turnaround times. Would be great to have templates for common itineraries."
- AI classifies: Type (Challenge), Theme (Process Improvement), Suggestion (Template Library), Sentiment (Stressed but constructive)

### 4. Proactive Surfacing Design

**Daily Digest (7am, Teams DM to each staff):**
- Top 3 client follow-ups for today
- 1 at-risk relationship requiring attention
- 1 growth opportunity from interactions this week
- <150 words total

**Weekly Review (Sunday evening, Teams DM):**
- Client patterns this week (what we're hearing across customers)
- Top 3 suggested actions for next week
- Team sentiment summary (anonymous aggregate)
- Wins from the team
- <250 words total

**Leadership Dashboard (Weekly, separate from staff digests):**
- Revenue pipeline by client tier
- Relationship health scores trending
- Team sentiment analysis
- Top blockers mentioned by staff

### 5. Customer Insight A4 Pages

**Auto-Generated Document per Client (Refreshed Weekly):**

**Structure:**
```
# [Client Name] - Strategic Relationship Overview

## Company Profile
- Industry, Size, Decision Makers, Communication Preferences

## Relationship History (Last 12 Months)
- Interaction timeline with key moments
- Revenue delivered, Projects completed

## Patterns & Insights
- What matters to them (extracted from interactions)
- Buying signals and triggers
- Seasonal patterns
- Preferences and pain points

## Growth Roadmap
- Current State: [Revenue tier, engagement level]
- Target State: [Realistic next tier, timeline]
- Key Initiatives: [3-5 specific actions to grow relationship]
- Confidence Level: [AI-assessed likelihood of success]
- Next Actions: [Concrete steps, owners, dates]

## Recent Interactions (Last 30 Days)
- Bullet list of key touchpoints with context
```

**AI Prompt Design:**
- How to extract relationship health scores from interactions?
- How to identify growth opportunities from patterns?
- How to generate realistic roadmaps (not aspirational BS)?

### 6. Email + Excel Mining Strategy

**Email Mining:**
- DMC has years of Outlook history with Top 10 clients
- Extract: Date, Sender, Recipient, Subject, Summary, Sentiment, Opportunities
- Classify into Interactions database
- One-time backfill + ongoing capture (Power Automate rule on new emails?)

**Excel Mining:**
- Client database with ~1,000 contacts
- Fields likely include: Company, Contact Name, Email, Phone, Past Bookings, Notes
- Import into Clients + Contacts databases
- Match with email history where possible

**Questions:**
- Can Power Automate + AI classify email history in bulk? (API rate limits?)
- How to preserve context without overwhelming storage?
- Should we filter by importance (Top 10 only for backfill, then expand)?

### 7. Knowledge Integration (YouTube KB Routing Pattern)

**From our YouTube research:**
- routing-index.yaml pattern (196 videos, 87KB, 99% token reduction)
- Cross-references: topic-map, concept-map, pattern-map, related insights

**Application to DMC:**
- Each client has a "knowledge fingerprint" (topics they care about)
- When staff captures interaction, AI tags with topics
- System routes relevant past insights when preparing for meetings
- Example: "Arctic Travel mentioned sustainability → System surfaces our sustainability case studies + past client successes in that area"

**Questions:**
- Should we build topic ontology upfront or let it emerge from captures?
- How to connect client topics to our knowledge base (YouTube KB + internal docs)?
- Can we auto-generate "prep briefs" before client meetings using routing?

---

## Deliverables Requested

### 1. Architecture Recommendation
- Which option (A/B/C) best balances friction, power, cost, maintainability?
- Clear justification with tradeoffs explained
- Migration path if we change later (portability)

### 2. Detailed Technical Specification
- Exact tools and configurations
- Database schemas with all fields specified
- Power Automate workflow diagrams (or Zapier if hybrid)
- AI prompt templates for classification and summarization
- Cost estimate per user per month

### 3. Implementation Roadmap
- Phase 0: Pilot (10 clients, 3 staff, 30 days)
- Phase 1: Data migration (email + Excel mining)
- Phase 2: Company-wide rollout (all 1,000 contacts, all staff)
- Timeline estimates for each phase

### 4. Customer A4 Insight Page Template
- Complete template with sections specified
- AI prompt for generation
- Example using fictional client

### 5. Risk Assessment
- What are failure modes? (adoption, classification accuracy, cost overruns)
- GDPR compliance for client data in AI workflows
- Data sovereignty concerns (Azure vs. Anthropic API)
- Maintenance burden (who fixes when Power Automate breaks?)

---

## Success Criteria

**Habit Maintenance (Primary Metric):**
- >80% of staff capture ≥1 interaction per working day
- >60% of staff read daily digest

**Customer Value Compounding:**
- Relationship health scores for Top 10 clients trend upward
- Growth roadmaps result in actionable pipeline expansion
- Zero lost follow-ups (measurable via "missed opportunity" captures)

**Internal Teamwork:**
- Staff sentiment visible to leadership
- Weekly wins celebrated and visible
- Process improvements identified and acted on

**System Health:**
- Classification accuracy >85% (measured via corrections)
- Time to capture <10 seconds
- Digest read rate >60%
- System uptime >95% (Power Automate reliability)

---

## Reference Materials

**YouTube KB Insights (Second Brain Systems):**
1. "Why 2026 Is the Year to Build a Second Brain" (Nate B Jones)
   - Core architecture: Capture → Classify → File → Surface
   - 8 engineering principles for non-engineers
   - Habit maintenance as infrastructure
   - Trust through transparency, not perfection

2. "The Honest Case for AI Note-Taking—From a Skeptic" (Nate B Jones)
   - Accept 15-20% hallucination rate vs. 100% organizational burden
   - Paradigm shift: organize → judgment over semantic retrieval
   - Consistency of input habit = primary success metric

**Finland DMC Specifics:**
- 1,000 client contacts total
- 100-200 somewhat active clients
- Top 10 clients = 50% of revenue
- Business key: fostering working relationships (trust is critical)
- Goal: grow new clients into Top 10 through relationship compounding

**M365 Environment:**
- Current tools: Teams, SharePoint, Outlook, Excel
- Staff comfort level: Familiar with Teams, less so with Power Automate
- IT constraints: [Patrick to specify if any]

---

## Tone and Approach

- Be opinionated: Recommend ONE architecture with clear reasoning
- Be realistic: Don't over-promise on AI accuracy or effort required
- Be specific: Provide exact prompts, schemas, workflows (ready to implement)
- Be practical: Consider maintainability and staff adoption, not just technical elegance
- Be strategic: Connect to business outcomes (revenue growth, relationship health)

**This is a research phase.** You're designing the blueprint, not building it yet. Once we have a clear architecture, we'll hand off to an orchestrated Opus team for implementation.

---

## Output Format

**Document Structure:**
1. Executive Summary (1 page: recommendation + key tradeoffs)
2. Architecture Deep Dive (5-10 pages: technical spec, schemas, workflows)
3. Implementation Roadmap (2-3 pages: phased approach, timelines, costs)
4. Customer A4 Template + Example (2 pages)
5. Risk Assessment + Mitigation (2 pages)

**Appendices:**
- Power Automate workflow diagrams (visual)
- AI prompt templates (copy-paste ready)
- Database schemas (detailed field specs)
- Cost calculator spreadsheet

**Total: 15-20 pages of strategic technical design, ready for orchestrated build.**

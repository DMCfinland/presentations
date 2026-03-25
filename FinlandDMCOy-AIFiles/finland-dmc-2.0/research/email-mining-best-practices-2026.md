# Email Mining Research Report: Mass Corporate Mailbox Intelligence Extraction

**Context:** 5-person DMC (Finland DMC Oy), shared sales mailbox, goal: extract client intelligence, tone patterns, proposal templates, pricing data, relationship signals. Finnish company, EU jurisdiction.

**Research date:** February 20, 2026

---

## Topic 1: Mass Email Mining Techniques

### Core Approaches

Three viable patterns exist for mining large corporate mailboxes at scale:

**Pattern A — Extract-then-process (recommended for our case)**
Pull emails in bulk via API, store as structured JSON/text, then feed to LLM in batches. Separates the data acquisition problem from the intelligence extraction problem. Easier to retry, cheaper to iterate.

**Pattern B — Real-time pipeline**
Trigger LLM extraction on each new incoming email. Tools: n8n, Power Automate, Zapier. Better for ongoing enrichment than retroactive corpus mining. Not relevant for the "mine the history" use case but useful after the initial extraction.

**Pattern C — RAG-on-email-corpus**
Export all emails to a vector database, then run semantic queries ("show me all pricing discussions with Nordic clients") on demand. Best for interactive exploration after bulk extraction.

**Recommended architecture:** Pattern A for initial historical mining, Pattern B for ongoing enrichment, Pattern C for the AI drafting assistant.

### Key Intelligence Frameworks

LlamaIndex's email extraction pipeline is the most production-tested approach for LLM-based extraction. Uses Pydantic schemas to define extraction targets — you define a class like `SalesEmailData` with fields, and the LLM populates it. Output is structured JSON per email, which aggregates cleanly into a database.

Most valuable extraction targets for a DMC sales mailbox:
- Client name, company, country/market
- Event type (incentive trip, conference, corporate retreat, wedding)
- Group size range mentioned
- Budget signals (explicit numbers, "flexible," "premium," "budget-conscious")
- Destination mentioned
- Stage of conversation (inquiry / proposal sent / negotiation / booked / lost)
- Response time (theirs and ours)
- Tone indicators (formal, warm, urgent, price-sensitive)
- Proposal template pattern (which structure was used)
- Outcome (won/lost/unknown)

Sources:
- LlamaIndex Email Data Extraction: https://docs.llamaindex.ai/en/stable/examples/usecases/email_data_extraction/
- Robocorp LLM email extraction: https://github.com/robocorp/example-llm-emails
- Intradyn: What is Email Mining: https://www.intradyn.com/email-mining/

---

## Topic 2: LLM-Based Email Mining — Best Practices

### The Validated Stack (2024-2025)

**Model selection:**
- Classification/routing: Haiku — 60x cheaper than Opus, sufficient for categorical work
- Structured extraction: Sonnet — near-Opus quality at 5x lower cost
- Synthesis: Opus — strategic analysis only, not per-email

**Chunking strategy for email threads:**
Long threads (5+ messages) can exceed context or produce lazy responses. Best practice: extract each message separately in the thread, then run a thread-level synthesis pass.

**Positive instructions outperform negative:**
"Extract ONLY the following fields in JSON. If a field is not present, output null. No explanations."

**Single-shot extraction:**
Design prompt to get everything in one pass. Multi-turn dialogue on 5,000 emails is impractical.

**Batch API for historical mining:**
Anthropic Batch API gives 50% discount on all tokens. 24-hour turnaround acceptable for one-time operation.

**Prompt caching for shared context:**
System prompt cached after first request at 90% off. Stack Batch API (50% off) + prompt caching (90% off cached tokens) for maximum savings.

Sources:
- n8n email categorization with LLM: https://kirill-markin.com/articles/how-to-automate-email-categorization-with-n8n-and-llm/
- LLM email classification on Databricks: https://pub.towardsai.net/llm-powered-email-classification-on-databricks-2089cdae4806

---

## Topic 3: M365/Outlook Email Mining — Specific Approaches

### Three-Tier Access Architecture

**Tier 1 — Graph API (REST) — RECOMMENDED**
Supports reading, filtering, searching messages. Default page size: 10 messages. Supports `$top` (max 1,000 per request) with `@odata.nextLink` pagination. Supports `$filter`, `$search`, `$select`.

Rate limits: 10,000 requests per 10 minutes per user per app, max 4 concurrent. For 10,000 emails with `$top=100` = 100 API calls, well within limits. `python-o365` handles pagination automatically.

```
GET /v1.0/users/{shared-mailbox-id}/mailFolders/Inbox/messages
?$top=100
&$select=subject,from,toRecipients,body,receivedDateTime,conversationId
&$filter=receivedDateTime ge 2022-01-01T00:00:00Z
```

**Tier 2 — Mailbox Import/Export APIs (Preview)**
For compliance/bulk export. TNEF format. Too complex for our case.

**Tier 3 — Microsoft Graph Data Connect**
Organization-wide data warehouse scale. Azure Data Factory pipeline. Overkill for 5-person DMC.

**Power Automate approach:**
AI Builder has entity extraction. Writes to SharePoint. ~$15/user/month. Good for ongoing routing, limited for deep historical mining.

Sources:
- Microsoft Graph Mail API: https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview
- python-o365: https://github.com/O365/python-o365
- Microsoft Graph Data Connect: https://learn.microsoft.com/en-us/graph/data-connect-concept-overview

---

## Topic 4: Privacy and Compliance — Finnish/EU Jurisdiction

### Two Separate Legal Regimes Apply

**Regime 1: Processing client email data (GDPR)**
Legal basis: **legitimate interest** (Article 6(1)(f)).

Three-part legitimate interest test:
1. **Purpose test:** Improving sales, understanding client needs = legitimate business purpose. YES.
2. **Necessity test:** No less intrusive way to analyze historical patterns at scale. YES.
3. **Balancing test:** Clients emailing a business mailbox have reasonable expectation of business use — but not external sharing.

Requirements:
- Document Legitimate Interest Assessment (written)
- Add AI analysis to Privacy Policy
- Data minimization: extract only what's necessary
- Secure storage
- Respect "do not contact" signals
- Define retention period

**Regime 2: Processing employee email data (Finnish Working Life Act 759/2004)**
- Employers can only process employee data **directly necessary** for employment
- **Shared mailbox (sales@) = company resource** — employer has full legitimate access
- **Personal inbox (firstname@) = strict restrictions** — do NOT mine without legal review

### Recommended compliance actions:
1. Document Legitimate Interest Assessment
2. Update Privacy Policy to mention AI analysis
3. Scope to shared sales mailbox ONLY
4. Exclude clearly personal communications
5. Secure storage with same access controls as raw emails
6. Set retention period
7. Consider mention in client terms of service

Sources:
- Finnish Data Protection Ombudsman: https://tietosuoja.fi/en/is-the-employer-allowed-to-read-an-employee-s-e-mail
- Act on Protection of Privacy in Working Life: https://tem.fi/en/protection-of-privacy-at-work
- Tyosuojelu.fi guidance: https://tyosuojelu.fi/en/employment-relationship/rights-and-responsibilities-at-work/privacy-protection/e-mail

---

## Topic 5: Email Intelligence Extraction Frameworks

### DMC-Specific Extraction Schema

**Per-Email Fields:**
```
EmailRecord:
  message_id: str
  date: datetime
  direction: "inbound" | "outbound"
  thread_id: str
  client_name: str | null
  client_company: str | null
  client_country: str | null
  client_email: str
  our_contact: str
  event_type: str | null
  destination: str | null
  group_size_min: int | null
  group_size_max: int | null
  travel_dates: str | null
  budget_mentioned: float | null
  budget_currency: str | null
  budget_signal: "explicit" | "range" | "vague" | "premium_signal" | "budget_sensitive" | null
  conversation_stage: "inquiry" | "info_requested" | "proposal_sent" | "negotiation" | "booked" | "cancelled" | "lost" | "follow_up" | "unclear"
  tone_ours: "formal" | "warm" | "urgent" | "consultative" | "transactional" | null
  tone_theirs: "formal" | "warm" | "urgent" | "demanding" | "friendly" | "vague" | null
  pain_points_mentioned: list[str]
  usp_highlighted: list[str]
  outcome: "won" | "lost" | "unknown"
  lost_reason: str | null
```

**Thread-Level Aggregation:**
```
ThreadRecord:
  thread_id: str
  client: str
  event_type: str
  total_emails: int
  days_to_response_avg: float
  our_response_time_avg: float
  outcome: str
  deal_value: float | null
  key_objections: list[str]
  winning_arguments: list[str]
  proposal_template_pattern: str
```

### Relationship Strength Signals
- Email frequency
- Response latency
- Thread length
- Tone progression (formality decrease = trust building)
- Initiative direction (who initiates more)
- Recency (relationship decay signal)
- Event count (bookings per client)

Sources:
- Introhive: https://www.introhive.com/relationship-intelligence/
- 4Degrees CRM: https://www.4degrees.ai/blog/unlocking-the-power-of-relationship-intelligence-crm-for-deal-driven-teams

---

## Topic 6: Scale Strategies — From 20 to 10,000+ Emails

### Architecture

**Step 1: Export** — python-o365 or Graph API script. 10,000 emails = 100 API calls < 5 minutes.

**Step 2: Pre-filter (Haiku)** — Classify: sales_inquiry | proposal_request | booking_confirmation | client_feedback | internal | spam. Cost: ~$0.50 for 10,000 emails. Reduces corpus to 3,000-5,000.

**Step 3: Per-email extraction (Sonnet Batch API)** — Full schema extraction.
- Input: 5,000 × 500 tokens × $1.50/M = $3.75
- Output: 5,000 × 200 tokens × $7.50/M = $7.50
- **Total: ~$11-15 for full corpus**

**Step 4: Thread synthesis (Sonnet)** — Group by conversationId, ~800 threads. Minimal cost.

**Step 5: Pattern synthesis (Opus, once)** — Strategic analysis of aggregated data.

**Step 6: Ongoing enrichment** — Power Automate or n8n trigger on new emails. Near-zero per-email cost.

---

## Topic 7: Tools Landscape

### Revenue Intelligence Platforms
| Tool | Email Mining | Small DMC fit? |
|---|---|---|
| Gong.io | Yes (call-first) | No — enterprise pricing |
| Introhive | Strong Outlook mining | No — 100+ seats |
| Affinity | Strong | Possible — used by PE/VC |
| MeetGeek | Basic | Yes for new emails |

**Key finding:** No commercial platform fits a 5-person DMC doing retroactive mining. Custom pipeline with Graph API + Claude is cheaper and more tailored.

### Email Mining Tools
| Tool | Fit |
|---|---|
| LlamaIndex | High — production-grade extraction |
| LangChain | High — flexible pipelines |
| n8n | High — no-code, self-hostable |
| python-o365 | High — clean Graph API library |
| Power Automate + AI Builder | Medium — accessible but limited |

---

## Topic 8: AI Email Drafting from Mined Data

### RAG vs. Fine-Tuning vs. Custom Instructions

**Fine-tuning:** Authentic tone but expensive, ties to model version, needs 1,000+ examples. Overkill for 5-person DMC.

**RAG:** Store extractions in vector DB, retrieve similar past proposals as context. Always up to date, works with any model.

**Custom Instructions:** Compress findings into a 2,000-3,000 token system prompt. 80% of benefit for a small team.

**Recommended path for Finland DMC:**
1. Mine and extract (Phase 4 above)
2. Synthesize top patterns with Opus
3. Build Custom Instructions (system prompt)
4. Add simple RAG: retrieve 3 most similar past proposals as context
5. Start with Claude Projects before building full infrastructure

### Open Source References
- RFX email RAG agent: https://github.com/tolgadur/rfx-email-agent
- LangGraph email automation: https://github.com/kaymen99/langgraph-email-automation
- n8n RAG email workflow: https://n8n.io/workflows/2852

---

## Practical Recommendations for Finland DMC

### Implementation Sequence

1. **Legal groundwork** — LIA document, update Privacy Policy, shared mailbox only
2. **Export** — python-o365 Graph API script (1-2 hours setup)
3. **Classification** — Haiku batch, ~$0.50
4. **Extraction** — Sonnet Batch API, ~$11-15
5. **Synthesis** — Opus one-shot, ~$2-5
6. **Drafting assistant** — Claude Projects with Custom Instructions + RAG

### Total Cost: $15-30 for full historical corpus mining

### Key Risks
1. Do NOT mine personal employee inboxes (Finnish law)
2. Group emails by conversationId to avoid fragmented context
3. Run `$count` before committing to full extraction
4. For pricing data, extract exact quotes not interpretations
5. Set up ongoing pipeline after initial mining for compounding value

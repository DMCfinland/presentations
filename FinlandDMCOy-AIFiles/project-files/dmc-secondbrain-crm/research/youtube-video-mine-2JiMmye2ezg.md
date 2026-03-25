# YouTube Video Mine — You Don't Need SaaS. The $0.10 System That Replaced My AI Workflow (45 Min No-Code Build)

**URL:** https://www.youtube.com/watch?v=2JiMmye2ezg
**Channel:** AI News & Strategy Daily | Nate B Jones (@NateBJones)
**Date mined:** 2026-03-11

---

## Video Summary

Nate B Jones presents the "Open Brain" — a personal, database-backed, MCP-connected knowledge system built on Supabase (Postgres + pgvector) that costs $0.10–$0.30/month and can be set up in 45 minutes with no coding. The core problem: every AI tool (Claude, ChatGPT, Cursor) starts from zero on every new chat, creating compounding switching costs. Open Brain solves this by providing a single shared memory layer any AI can query via MCP. The system has two parts: a Capture side (Slack message → Edge Function → Supabase, auto-embedded and classified within 5 seconds) and a Retrieval side (hosted MCP server reachable from any AI client via URL). Nate argues this is what true AI adoption looks like — restructuring workflows around AI as a primary collaborator with persistent memory it can actually access.

---

## Key Concepts (most actionable first)

### 1. The "AI Starts From Zero" Problem — and Why It Matters for DMC
Every new chat context means re-explaining client history, deal status, supplier relationships, and trip context. Open Brain's solution — shared memory via MCP — maps directly onto the DMC-SECONDBRAIN-CRM problem. Our email pipeline already auto-mines and stores data in Supabase. The missing piece is an MCP layer that lets Claude (or any agent) query that accumulated context on demand.

**DMC application:** Add an MCP server (Supabase Edge Function) exposing `semantic_search` over the existing Supabase tables. When a staff member asks Claude about a client or deal, Claude retrieves from the live database rather than from a pasted summary.

### 2. Architecture Pattern: Capture → Embed → Store → MCP Retrieval
The Open Brain pipeline is structurally identical to our n8n email pipeline, just with a different capture source:

```
Capture source (Slack / Email)
  → Edge Function (LLM extracts metadata + generates embedding in parallel)
  → Supabase row (content + vector + structured fields)
  → MCP server (semantic_search tool exposes it to any AI client)
```

Our n8n Triple-LLM already does extraction and classification. We are one step away: add pgvector embedding on write + an MCP server edge function on read.

### 3. Structured Capture Templates That Drive Clean Metadata Extraction
Open Brain ships with four capture prompt templates specifically designed to give the extraction LLM clear signals for better tagging and retrieval:

- **Decision Capture:** "Decision — [context]" — triggers `task_type: decision`, owner extraction, searchable rationale
- **Person Note:** "[Name] — [what happened / what you learned]" — triggers `type: person_note`, people extraction, semantic context
- **Insight Capture:** "Insight: [realization]. Triggered by: [what caused it]" — triggers `type: idea`, preserves original context for later retrieval
- **Meeting Debrief:** Structured format that surfaces action items and relationship context

**DMC application:** Our n8n email classifier already infers these types. But for manual staff captures (call notes, supplier meetings, fam trip observations), these four templates give staff a dead-simple input format that produces clean, searchable records — no form to fill, just a Slack message with a prefix trigger.

### 4. Memory Migration Prompt — Frontloading the Brain
The system includes a "Memory Migration" prompt that extracts everything an AI already knows about you from existing chat histories (Claude Projects, ChatGPT conversations). This populates the brain immediately rather than waiting for gradual capture.

**DMC application:** Run a memory migration pass over existing M365 email mining outputs. All the client relationships, supplier contacts, and deal patterns already extracted in DMC 2.0 mining can be bulk-inserted as structured embeddings — the brain starts with knowledge, not from zero.

### 5. Vendor Lock-in as an Architectural Risk
Nate frames platform memory silos (Claude memory, ChatGPT memory, Copilot memory) as creating compounding switching costs. Each platform knows a different slice of your context. Open Brain's response: own your data in Postgres, expose it via the open MCP protocol, and every AI client connects to the same truth.

**DMC application:** This is exactly the architecture we chose (Supabase as single source of truth, Next.js Kanban as the interface). The principle validates our choice and adds a specific extension: expose the Supabase CRM data via MCP so Claude and any future AI tools can query it directly without a human intermediary.

### 6. MCP as the Universal AI Integration Layer
The MCP server is deployed as a Supabase Edge Function — no local process, no credentials on client machines, reachable from anywhere via URL. Any MCP-compatible client (Claude Desktop, Cursor, future tools) connects with just a URL.

**DMC application:** Our existing Supabase project can host the MCP server at zero additional infrastructure cost. Staff connecting Claude Desktop get immediate access to client history, deal status, and supplier data through natural language — "what do we know about [client]?" becomes a live database query.

### 7. The "Knowledge Compounds" Principle
Every capture adds to the vector knowledge graph, making subsequent searches more relevant. This is structurally opposite to traditional CRM data entry, which requires effort now for unclear future benefit. Open Brain's auto-capture (Slack → embedded → stored) makes the value visible immediately.

**DMC application:** This validates the zero-data-entry principle behind our CRM architecture. Auto-mining email → Supabase means the knowledge graph grows without staff effort. Surfacing this visibly (the "auto-mined email digest" in the adoption strategy) closes the feedback loop.

### 8. Weekly Review Ritual as a Closing Loop
The system includes a Friday weekly review prompt that surfaces themes, forgotten action items, and connections missed during the week. This is not automatic — it's a deliberate ritual that uses the accumulated captures to generate insights.

**DMC application:** A weekly n8n workflow that queries the deals table for stale items, upcoming follow-ups, and high-value patterns, then sends a structured digest to staff. This mirrors the "stale alerts" workflow already in our 12-workflow architecture — extend it to include pattern detection across the week's activity.

---

## Architecture / Technical Insights

### Open Brain Stack (Nate's reference implementation)
- **Storage:** Supabase PostgreSQL + pgvector extension (vector similarity search)
- **Embedding:** Generated in Supabase Edge Function at write time, in parallel with metadata extraction
- **Classification:** LLM-powered metadata extraction inside the same Edge Function (people, topics, action items, type)
- **MCP Server:** Second Supabase Edge Function, hosted on same project, no local dependencies
- **Capture Interface:** Slack channel → Supabase webhook → Edge Function (5-second pipeline)
- **Cost:** $0.10–$0.30/month for infrastructure (embedding API cost is the variable)

### benclawbot/open-brain (open-source implementation, MIT license)
A community reference implementation with a broader ingest surface:
- **Ingest sources:** Telegram exports, WhatsApp chat history, Gmail archives, Claude Code sessions, manual API/CLI
- **MCP Tools:** `memory_search`, `memory_store`, `memory_stats`, `memory_trends`, `memory_report`
- **Analytics:** Weekly markdown reports, topic emergence tracking (>50% growth triggers alerts), co-occurrence analysis
- **Notifications:** Telegram alerts for emerging trends; email digests
- **Interfaces:** MCP server (port 8080), FastAPI REST (port 8000), Streamlit dashboard (port 8501), CLI
- **Docker-deployable** with pgvector/pgvector:0.5.1 image
- **Embedder providers:** OpenRouter (free tier), OpenAI, Ollama (local), any OpenAI-compatible endpoint

### pgvector Schema Pattern
```
memories table:
  id
  content (text)
  embedding (vector)
  source (telegram | email | slack | manual)
  tags (array — GIN indexed)
  entities (people, orgs, dates — auto-extracted)
  task_type / thought_type (decision | insight | person_note | action)
  created_at
```

### MCP Tools Interface Pattern
```
capture_thought(content, type?) → generates embedding + extracts metadata in parallel → stores row
semantic_search(query, filters?) → generates query embedding → vector similarity match → ranked results
memory_trends() → topic emergence analysis across time window
memory_report() → weekly summary generation
```

---

## Applicable to Our Build

### High priority additions

**1. Add pgvector to existing Supabase schema**
Enable the pgvector extension. Add an `embedding vector(1536)` column to `contacts`, `deals`, and `deal_activities` tables. Populate on write via n8n (add embedding generation step after the Triple-LLM extraction). Cost: ~$0.0001 per embedding at text-embedding-3-small rates — negligible at our volume.

**2. MCP Server Edge Function (30-minute build)**
Write a Supabase Edge Function that exposes two tools:
- `search_brain(query)` — semantic search over deals + contacts + activities
- `get_deal_context(deal_id)` — structured retrieval for a specific deal

Deploy as a hosted MCP endpoint. Any Claude Desktop instance (Patrick's or staff's) connects with one URL. No local server required.

**3. Staff Slack Capture Channel**
Add a `#crm-notes` Slack channel. n8n webhook listens, auto-classifies input using the four capture template patterns (Decision / Person / Insight / Meeting). Stores to Supabase with embedding. This extends the auto-mining to cover information staff have in their heads — supplier calls, fam trip observations, client conversations not over email.

**4. Memory Migration Pass**
Run a one-time bulk insert: take all M365 email mining outputs (DMC 2.0 research, client entities, supplier data) and generate embeddings for them. This pre-populates the brain so the system starts with 2+ years of context, not zero.

**5. Weekly Pattern Digest (extend stale alerts workflow)**
Extend existing n8n stale-alerts workflow to include a Friday pattern report: top active deals, clients with no recent contact, emerging topics across the week's email activity. Send to staff as a structured digest (applies the "weekly review ritual" concept).

### Lower priority / FinnConcierge relevance

**6. Traveler-facing Open Brain for FinnConcierge**
When FinnConcierge is built: each traveler session can capture preferences, past experiences, and stated interests into a per-traveler brain. Vector search over traveler history means FinnConcierge can say "last time you were in Lapland you mentioned preferring snowshoeing over snowmobiling" — without any user-facing form.

---

## Quotes Worth Keeping

"Every time you open a new chat window, your AI starts from zero. That's not a prompting problem — it's an architectural problem."

"True AI adoption isn't about using more AI tools. It's about restructuring your workflows around AI as a primary collaborator — and that requires a persistent memory system the AI can actually access."

"Your second brain is closed. Your AI can't use it." (Nate's framing for the gap between Notion/Obsidian-style PKM and what AI agents actually need)

"It's not like Obsidian, a note-taking app. It's a memory layer for your AI — you put thoughts in, and your AI pulls the right ones out when they're relevant. You don't organize them, file them, or maintain them. Vector search handles retrieval by meaning."

"The knowledge graph compounds. Every capture makes subsequent searches more relevant."

---

## Note on Access

YouTube page returned only JavaScript config (Finnish locale, not logged in). Video metadata retrieved via YouTube oEmbed API. Full video content accessed through:
- Nate's Substack article (natesnewsletter.substack.com) — primary source for video content
- Secondary search synthesis across Nate's prompt kit site, LinkedIn posts, and Recapio transcript summary
- benclawbot/open-brain GitHub (MIT, community implementation) — technical schema and MCP tool details
- Multiple web searches for specific technical details

The Recapio transcript page and promptkit.natebjones.com pages returned permission denied on WebFetch. All content above is sourced from accessible public pages and search result snippets. Confidence level: HIGH for concepts and architecture; MEDIUM for exact prompt template wording (paraphrased from search snippets, not raw transcript).

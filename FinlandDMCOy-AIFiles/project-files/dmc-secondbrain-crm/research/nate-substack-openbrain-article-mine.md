# MINE: Nate B Jones — "Open Brain" Substack Article
**Source:** Substack premium article, published 2026-03-02
**Mined:** 2026-03-11
**Relevance:** HIGH — direct architecture validation for DMC-SECONDBRAIN-CRM pgvector + MCP decision

---

## Core Thesis

> "The specification problem is a memory problem. And memory architecture determines agent capabilities more than model selection does."

Every new chat window resets context to zero. Platform memory silos = 5 sticky notes on 5 separate desks. The fix: one Postgres/pgvector database + one MCP server → any AI reads the same brain.

---

## Architecture (exact spec)

**Capture path:**
1. Type thought in Slack channel
2. Hits Supabase Edge Function
3. Edge Function: generates vector embedding + extracts metadata (people, topics, type, action items) IN PARALLEL
4. Stores raw text + embedding + metadata in Postgres + pgvector table
5. Replies in-thread with confirmation (round trip <10 seconds)

**Retrieval path:**
MCP server with 3 tools:
- `semantic_search` — find thoughts by meaning (not keywords)
- `list_recent` — browse captures from last N days
- `stats` — view patterns and capture frequency

**Compatible clients (all via MCP):**
Claude Desktop, Claude Code, ChatGPT, Cursor, VS Code Copilot — same brain, all of them.

**Cost:** $0.10–$0.30/month on Supabase + Slack free tiers.

---

## Key Insights for DMC CRM

### 1. pgvector is the core differentiator
"When you ask 'what was I thinking about career changes?', it finds your note about Sarah considering consulting, even though you never used the word 'career' in the original thought."

**DMC equivalent:** "Find all Alpine groups 50+ pax who mentioned budget constraints" — finds deals even when the exact words weren't used. Standard SQL can't do this. pgvector can.

### 2. Memory Migration = Day 1 value
"Run the Memory Migration right after setup. It extracts everything your AI already knows about you... Every other AI you connect starts with that foundation instead of zero."

**DMC equivalent:** Bulk-embed the 107 client profiles from DMC 2.0 mining outputs on Day 1. Staff gets semantic search over historical deal intelligence immediately — before a single new email is processed.

### 3. Compounding advantage is real and quantifiable
Each thought captured → makes next search smarter → makes next AI interaction better → wider gap vs. non-users every week. This is the core ROI argument for the CRM second brain to Patrick's staff.

### 4. MCP is bidirectional
"Any MCP-compatible client becomes both a capture point and a search tool." Slack, Claude Code, any future AI tool → all write to the same brain. Future-proof architecture.

### 5. Metadata extraction doesn't need to be perfect
"The LLM makes its best guess with limited context, and sometimes it'll misclassify a thought or miss a name. Doesn't matter much. The embeddings handle the heavy lifting."

**Implication for CRM:** Don't over-engineer the Triple-LLM metadata extraction quality. The vector embedding catches what the classifier misses. Confidence threshold of 0.7 (D: Wave 2A) is fine — semantic search recovers the rest.

### 6. Platform memory silos = lock-in through accumulated context
"You've spent months building up history with one tool, and now you want to try the latest Gemini or the new Grok? You lose everything."

**DMC implication:** Staff using the CRM accumulates 12-18 months of deal intelligence. If the CRM is ever rebuilt, that intelligence lives in Supabase/pgvector — not locked in Pipedrive or any SaaS. This is the "own your data" argument in concrete form.

---

## Four Capture Templates (from the article)

Relevant as staff Slack channel templates (#crm-capture):

1. **Decision:** `decision: [what we decided] because [why]`
2. **Person:** `person: [name] — [what they said/context]`
3. **Insight:** `insight: [observation] — [why it matters]`
4. **Meeting:** `meeting: [who, what topic] — [key outcomes]`

Each designed for clean metadata extraction. After 1 week, staff develop their own patterns.

---

## Weekly Review Pattern

Weekly synthesis prompt: clusters by topic, scans unresolved action items, detects patterns across days, surfaces forgotten threads. Becomes more valuable every week.

**DMC CRM equivalent:** n8n weekly workflow → summarize "deals with no activity in 7+ days" + "email mining patterns this week" → push to Teams channel. Automated Weekly Review.

---

## What This Changes for DMC Build

| Decision | Before Article | After Article |
|----------|---------------|---------------|
| pgvector scope | Uncertain — Wave 1A or backlog? | Wave 1A. 30-min add now vs. migration on 500+ rows later. |
| Capture channel | Nice-to-have | Core feature — habit formation = compounding value |
| Memory migration | Future concern | Day 1 task — run bulk-embed of 107 profiles immediately after setup |
| Staff adoption pitch | "Zero data entry" | "Zero data entry + AI that gets smarter about your clients every week" |

---

## Reference Implementation
- GitHub: `benclawbot/open-brain` (MIT license)
- Stack: Supabase Edge Functions + pgvector + MCP server
- Same stack as DMC CRM — no new infrastructure required

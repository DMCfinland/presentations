# Mining Output — Cluster D: Execution & Build
Source files: Coding execution strategy (10.12), Tässä projektimme nykytila / Project Status (11.12), Agentic Coding Design Goal (18.12), ViikonlopunDokumenttiTaskit (weekend tasks)
Mined: 2026-02-21

---

## DECISIONS

1. [source: 10.12 Coding execution strategy] The team decided to use Claude / Anthropic as the main AI brain for the build, specifically citing best long-context reasoning (200K tokens), native Projects feature with built-in Git and persistent files, and Claude 3.5 Sonnet / Opus 4 ranking #1 or #2 on every agentic coding benchmark in December 2025.

2. [source: 10.12 Coding execution strategy] Decided to use the "Anthropic-style harness" as the core build pattern: external memory in a Git repo, tiny persistent artifacts (architecture.md + features.yaml + progress.json), one-time big-picture planning exploded into 400–600 atomic rows, Sub-Boss + Coder + Tester loop per row, and an orchestrator that never lets context explode.

3. [source: 10.12 Coding execution strategy] Decided that the founder (Patrick) will never touch code or terminal directly — all interaction goes through Claude chat or Slack, and all code execution is delegated to agents.

4. [source: 11.12 Tässä projektimme nykytila] Decided to complete a "Vertical Slice Mock MVP" first — a thin but functional slice through the entire system (backend to frontend) — before scaling to full blueprint generation. This was completed with Cursor.

5. [source: 11.12 Tässä projektimme nykytila] Decided to use Blueprint Driven Development as the core methodology: no code is written without a .md Blueprint that defines logic, data contracts, and interfaces. The architect creates the Blueprint; Code Agent (Cursor) reads it and implements automatically.

6. [source: 11.12 Tässä projektimme nykytila] Decided NOT to run the 1000-task phase manually through Cursor's chat window ("Chat-driven development"). The recommendation was to use Cursor to build an automation harness script (Python) that handles mass coding via API calls.

7. [source: 11.12 Tässä projektimme nykytila] Decided to use a Custom Python CLI Harness run in Cursor's terminal (or cloud) rather than GUI chat, because task state is stored to disk (JSON/SQLite), not in chat history — enabling parallel agents and preventing context overflow.

8. [source: 18.12 AgenticCodingDESIGN GOAL] Decided to relieve Sonnet from the "PM / Middle Management" role — described as "adding latency and diluting the technical signal" — and establish a Direct Uplink from Gemini (Senior Auditor) to Opus (Lead Researcher).

9. [source: 18.12 AgenticCodingDESIGN GOAL] Decided to shift scope from drafting a specific guide to conducting a Comparative Analysis for a "Bible of Agentic Coding" — benchmarking the "Darwinian/Tournament" model against other SOTA architectures before committing resources.

10. [source: 10.12 Coding execution strategy] Agreed that Gemini or GPT-4o can be brought in as reviewers, and human devs can be added later — the repo is normal GitHub, everything is standard, keeping the architecture future-proof.

---

## REQUIREMENTS

1. [source: 10.12 Coding execution strategy] The system must be buildable by a solo founder without becoming a full-time coder or managing a human dev team — "vision is huge, coding bandwidth is low."

2. [source: 10.12 Coding execution strategy] The AI coding system must be capable of building a 500+ feature enterprise SaaS autonomously, with expected total cost under $600 and expected calendar time of 7–21 days for a full enterprise MVP.

3. [source: 11.12 Tässä projektimme nykytila] The system (FinnConcierge) must operate with Zero Friction: login via "Magic Link" sent directly from the booking confirmation — no app store installations, no passwords.

4. [source: 11.12 Tässä projektimme nykytila] The system must be built as an agent network ("Agentic Mesh"), not a chatbot — specifically: a Psychologist, Chef, Librarian, and Accountant agent that communicate with each other to serve the customer.

5. [source: 11.12 Tässä projektimme nykytila] The Master Agent must maintain context (ContextBackpack), orchestrate all traffic, delegate to sub-agents (Tools), and decide when a human handover is needed.

6. [source: 11.12 Tässä projektimme nykytila] The Mood Evaluator must analyze every user message in the background and update a 7-dimensional MoodMatrix profile (e.g., Energy, Luxury, Safety) — it must not reply to the user, only inform the Master Agent.

7. [source: 11.12 Tässä projektimme nykytila] The Orchestrator (Python script, not an LLM) must manage task state (TODO, IN_PROGRESS, DONE, FAILED), prevent context overflow by sending Sub-boss only the files relevant to the current task, and run up to 10 agents in parallel threads.

8. [source: 11.12 Tässä projektimme nykytila] The Shadow Ledger must log all transactions and calculate commissions (Shadow Accounting) even when the actual payment occurs through a third party.

9. [source: 11.12 Tässä projektimme nykytila] The Traveler PWA (Next.js 15) must be a "Chameleon" — dynamically adapting to the brand via Tenant Config — designed to serve multiple resort clients (e.g., Järvisydän, KonTiki).

10. [source: 18.12 AgenticCodingDESIGN GOAL] The adversarial gate requirement: no code may enter the codebase without passing an adversarial challenge — a "Red Team" agent must attack the code before it is committed.

11. [source: 18.12 AgenticCodingDESIGN GOAL] The system must automate the error loop: when an agent fails, it reads stderr, queries a "Senior Dev" Agent (NOT a human), and retries. A "3-Strike" rule must define the exact threshold for when to finally alert the human.

12. [source: 11.12 Tässä projektimme nykytila] The Initializer's context window must not become overloaded — it must leverage multiple Sub-boss coding teams running in parallel.

---

## TECH CHOICES

1. [source: 10.12 Coding execution strategy] Claude / Anthropic — chosen as the main AI brain. Rationale: best long-context reasoning (200K tokens), native Projects feature (built-in Git + persistent files, no terminal required), #1 or #2 on agentic coding benchmarks December 2025, cheaper than GPT-4o for long sessions.

2. [source: 10.12 Coding execution strategy] Claude 3.5 Sonnet / Opus 4 — the specific models chosen for the build phase ("still #1 or #2 on every agentic coding benchmark in Dec 2025").

3. [source: 10.12 Coding execution strategy] Gemini and GPT-4o — considered as optional reviewer models (not primary builders), specifically to be brought in as external quality reviewers if desired.

4. [source: 11.12 Tässä projektimme nykytila] Azure Serverless (Python) — chosen as the backend stack for FinnConcierge.

5. [source: 11.12 Tässä projektimme nykytila] Next.js 15 PWA — chosen as the frontend stack for the Traveler interface (Traveler PWA, BP_11).

6. [source: 11.12 Tässä projektimme nykytila] Azure OpenAI — chosen as the LLM integration layer (functions exist as evaluate_with_llm but are still in TODO state — not yet connected).

7. [source: 11.12 Tässä projektimme nykytila] Azure SQL + Cosmos DB — chosen as the production databases. Currently the code uses in-memory/mock databases; connecting to Azure SQL and Cosmos DB is the next step.

8. [source: 11.12 Tässä projektimme nykytila] Azure Event Grid — chosen as the event/messaging layer for the event-driven agentic orchestration.

9. [source: 11.12 Tässä projektimme nykytila] Cursor — used as the Code Agent for reading Blueprints and implementing them automatically. Used to build the Vertical Slice Mock MVP; also intended to build the harness scripts (initializer.py, orchestrator.py).

10. [source: 11.12 Tässä projektimme nykytila] Custom Python CLI Harness — chosen over Cursor GUI chat for the 1000-task coding phase. Components: initializer.py (reads MASTER_MAP.md, generates TASKS.json with 500 microtasks via Claude 3.5 Sonnet API), orchestrator.py (reads JSON tasks, runs loop, calls agent instances via API, writes files to disk).

11. [source: 11.12 Tässä projektimme nykytila] TASKS.json with DAG (Directed Acyclic Graph) structure — chosen as the task state format. Structure: {"id": "TASK-001", "dependency": null, "description": "...", "verification_criteria": "..."} — enables parallel execution of independent tasks.

12. [source: 18.12 AgenticCodingDESIGN GOAL] Anthropic Agent Harness + Cline/Cursor + Docker — identified as the target "Hands-Off Tooling" stack for the build harness.

---

## RISKS

1. [source: 10.12 Coding execution strategy] Regular agents forget everything after a few hours and produce "spaghetti" because they have no long-term memory or structure. This was identified as the core problem with normal agents and the primary risk to avoid.

2. [source: 11.12 Tässä projektimme nykytila] Cursor's chat window alone cannot reliably manage 1000-task state — "the context window fills up and it starts to hallucinate or forget old tasks." Explicitly identified as a reason NOT to use chat-driven development for mass coding.

3. [source: 18.12 AgenticCodingDESIGN GOAL] "Context Rot" — agents get "dumber" as chat history grows. Identified as the primary technical problem requiring a SOTA state management solution (Amnesia patterns vs. Summary nodes vs. RAG).

4. [source: 18.12 AgenticCodingDESIGN GOAL] The "Darwinian/Tournament" model costs 3x inference compared to simpler hierarchical models. Whether this cost justifies the quality gain is explicitly unresolved — it is the central research question of the "Bible of Agentic Coding" project.

5. [source: 11.12 Tässä projektimme nykytila] LLM integration functions (evaluate_with_llm) exist but are all still in TODO state — the architectural structure is ready but the actual OpenAI calls are not yet made. Risk: the system has not been tested under real LLM calls (latency and cost unknown).

6. [source: 11.12 Tässä projektimme nykytila] The Auditor Agent prompt explicitly flags the risk that some parts of the initial 6 blueprints may have been "ignored or hacked to make the test pass" — blueprint validity is unconfirmed at the point of scale-up.

7. [source: 11.12 Tässä projektimme nykytila] Latency and cost friction specifically flagged as a concern when switching from mock keyword-based logic to real LLM calls — described as "the biggest friction point" to identify before scaling.

---

## OPEN QUESTIONS

1. [source: 11.12 Tässä projektimme nykytila] Go/No-Go decision pending: Did the Vertical Slice Mock MVP prove the architecture is ready to scale? Specifically: (a) Did agents pass context (Mood Matrix, User ID) correctly without losing state? (b) Was the Shadow Ledger able to capture transaction triggers from the Booking Agent correctly? (c) Which parts of the 6 blueprints were ignored or hacked to make the test pass?

2. [source: 18.12 AgenticCodingDESIGN GOAL] Does the "Darwinian/Tournament" model (1 Leader + 3 Competitor Coders + Red Team) justify its 3x inference cost vs. alternative architectures — specifically Microsoft AutoGen (Hierarchical), ChatDev (Waterfall), and MetaGPT (SOP-based)?

3. [source: 18.12 AgenticCodingDESIGN GOAL] What is the SOTA state management pattern for preventing Context Rot? "Amnesia" patterns (wiping worker memory after every task) vs. "Summary nodes" (keeping a running context.md) vs. RAG (retrieving code snippets from a vector DB) — which is superior and when?

4. [source: 18.12 AgenticCodingDESIGN GOAL] Should tests be written before the code (TDD by the same agent) or by a separate "Red Team" agent after generation? The adversarial gate design is unresolved.

5. [source: 18.12 AgenticCodingDESIGN GOAL] How do we define the exact "3-Strike" threshold — at what point does the error loop escalate from automated agent retry to human alert?

6. [source: 11.12 Tässä projektimme nykytila] Blueprints BP_06 (Booker), BP_08 (Communication), BP_09 (Watchdog), and BP_10 (Infra / Security) are awaiting specification — unresolved content and scope.

7. [source: 10.12 Coding execution strategy] How should the existing 200-page Word document be cut into smaller pieces for the Vision & Architecture Crew prompt? The document structure question was raised but not answered in the source material.

---

## NOTABLE QUOTES

1. [source: 10.12 Coding execution strategy] "Regular agents forget everything after a few hours and produce spaghetti because they have no long-term memory or structure." — Core framing of why the harness pattern was chosen.

2. [source: 11.12 Tässä projektimme nykytila] "Emme rakenna chatbotia, vaan Agenttien verkoston. Järjestelmässä on 'Psykologi', 'Kokki', 'Kirjastonhoitaja' ja 'Kirjanpitäjä', jotka keskustelevat keskenään palvellakseen asiakasta." — Translation: "We are not building a chatbot, but a network of Agents. The system has a 'Psychologist', 'Chef', 'Librarian', and 'Accountant' who communicate with each other to serve the customer." Core product philosophy statement.

3. [source: 18.12 AgenticCodingDESIGN GOAL] "Sonnet (PM) is hereby relieved of duty. The 'Middle Management' layer was adding latency and diluting the technical signal." — Strategic pivot on agent topology, removing an intermediate orchestration layer.

4. [source: 11.12 Tässä projektimme nykytila] "Tämä on kriittistä ymmärtää. Emme koodaa mitään ilman Blueprintiä." — Translation: "This is critical to understand. We do not code anything without a Blueprint." Core methodology rule, stated as absolute.

5. [source: 11.12 Tässä projektimme nykytila] "Ikuinen muisti: Taskien tila on levyllä (JSON/SQLite), ei chat-historiassa." — Translation: "Eternal memory: task state is on disk (JSON/SQLite), not in chat history." — The key architectural principle separating the harness approach from naive chat-driven coding.

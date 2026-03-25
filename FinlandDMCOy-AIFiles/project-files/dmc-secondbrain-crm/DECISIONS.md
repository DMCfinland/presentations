# DECISIONS LOG — DMC-SECONDBRAIN-CRM
**Format:** `[date] DECISION: [what] BECAUSE: [why] REJECTED: [alternatives]`
**Note:** D1-D12 are in orchestration/SHARED-CONTEXT.md. This file extends from D13.
**Migration:** Copy this file to `~/Desktop/FinnConcierge/DECISIONS.md` during Wave 0 setup.

---

## Locked Decisions (D1-D12)
See `orchestration/SHARED-CONTEXT.md` — Locked Decisions table.

---

## Extended Decisions (D13+)

[2026-03-11] **D13: Auth separation**
DECISION: Staff = Supabase JWT with role claims. Travelers (B2C) = no-login or easy login based on customer preference. No shared auth between systems.
BECAUSE: Different trust levels, different user types. Travelers should not need accounts for basic concierge use.
FUTURE: Tour guide session (guide + client view) is a known future use case — design auth schema to accommodate without requiring refactor.
REJECTED: Single Supabase Auth project for both staff and travelers (coupling risk).

[2026-03-11] **D14: CRM does NOT reuse FinnConcierge AI agents**
DECISION: CRM email pipeline (Triple-LLM) is independent of FinnConcierge AI agents (mood_evaluator, chef_agent, librarian_agent, booker_agent).
BECAUSE: Different purposes (B2B CRM extraction vs B2C traveler concierge). Coupling would create fragility.
FUTURE: Synergy via shared staff dashboard — both systems surface into one view, not shared pipeline.
REJECTED: Reusing mood_evaluator for email sentiment analysis (over-engineering).

[2026-03-11] **D15: Synergy = shared staff dashboard (future), not shared pipeline (now)**
DECISION: CRM and FinnConcierge remain architecturally separate systems. Synergy point is the staff dashboard — eventually both systems' data surfaces into one interface for staff.
BECAUSE: Premature integration = higher coupling, more failure modes, slower build.
FUTURE: Staff dashboard shows CRM pipeline + FinnConcierge B2C session summary in one view.
REJECTED: Shared n8n pipeline for both B2B and B2C data flows.

[2026-03-11] **D16: TravelTree for B2B CRM now; FinnConcierge gets own itinerary system later**
DECISION: B2B CRM uses TravelTree T1+T2 API integration (already planned, free endpoints). FinnConcierge B2C will either get its own itinerary UI or a separate TT integration — decided when FinnConcierge build starts.
BECAUSE: Don't over-engineer for B2C before B2B is working. TT is proven and trusted by DMC staff.
FUTURE: Goal = itinerary views in TravelTree and FinnConcierge traveler app look visually similar (consistent UX).
REJECTED: Shared itinerary component across both systems now (premature).

[2026-03-11] **D17: FinnConcierge B2C deferred until CRM is working**
DECISION: FinnConcierge (B2C traveler AI concierge) build is deferred until DMC-SECONDBRAIN-CRM is live and the long-running agent build process is proven.
BECAUSE: Two parallel system builds = split focus, doubled complexity, risk to both.
SEQUENCE: CRM first → email drafter golden prompts → FinnConcierge B2C.
REJECTED: Parallel CRM + FinnConcierge build (resource/focus conflict).

[2026-03-11] **D18: Email drafter golden prompts run parallel after CRM Wave 1 starts**
DECISION: Comprehensive M365 email mine (Azure connector) → email drafter golden prompts is a separate parallel workstream. Starts after Wave 1 is underway, not blocking CRM build.
BECAUSE: CRM and email drafter share the same M365 data source but are independent deliverables. Email drafter has faster ROI (staff uses it immediately).
SEQUENCE: Wave 1 starts → M365 mine → email drafter prompts → feed insights back to CRM email pipeline design.
REJECTED: Waiting for full CRM build before starting email drafter (wastes time, staff needs it sooner).

---

## Integration Interface Decisions (D19–D26)
**Source:** Grok 4.20 4-role planning debate (ARCHITECT + DESIGNER + BOSS + RED TEAM), 2026-03-11
**Status:** Locked — apply before Wave 1A (schema migration) begins.

[2026-03-11] **D19: Standard columns on all new CRM tables**
DECISION: Every new CRM table gets: `tenant_id`, `created_by_ai_pipeline` (boolean), `mined_at` (timestamptz, nullable), `retention_policy_days` (int, default 730).
BECAUSE: GDPR retention automation requires mined_at. Multi-tenant requires tenant_id. AI pipeline audit requires created_by_ai_pipeline.
REJECTED: Adding GDPR columns later (requires ALTER TABLE on live data).

[2026-03-11] **D20: Bridge columns on deals table**
DECISION: `deals` includes: `finnconcierge_session_id` (uuid, nullable), `external_itinerary_ref` (text, nullable), `tt_booking_ref` (text, nullable).
BECAUSE: Nullable bridge columns cost nothing now but avoid ALTER TABLE on 500+ rows when FinnConcierge connects.
REJECTED: Junction table `deal_sessions` (over-engineering for 5-person team at this stage).

[2026-03-11] **D21: sessions_archive bridge column**
DECISION: `sessions_archive` gets `deal_id` (uuid, nullable, FK → deals.id ON DELETE SET NULL).
BECAUSE: Single bridge between B2C sessions and B2B deals. Required for future unified staff dashboard query.
REJECTED: Keeping sessions_archive completely isolated (blocks staff dashboard permanently).

[2026-03-11] **D22: All TravelTree columns prefixed tt_**
DECISION: Any TravelTree-specific column uses `tt_` prefix (e.g., `tt_booking_ref`, `tt_itinerary_id`).
BECAUSE: Prevents column name clashes when FinnConcierge adds its own itinerary columns later.
REJECTED: Generic names (creates confusion when two itinerary systems coexist).

[2026-03-11] **D23: Shared /packages/ui — 4 mandatory components**
DECISION: Both systems use shared monorepo `/packages/ui`: BaseCard, StageBadge, ValuePill, ActivityTimeline.
BECAUSE: Visual consistency between CRM and FinnConcierge required for unified staff dashboard.
REJECTED: Separate component libraries per app (doubles work, diverging visual language).

[2026-03-11] **D24: n8n health banner on every staff page**
DECISION: Staff dashboard shows "n8n last run: Xh ago" on every page. Red if >4h.
BECAUSE: Automation observability = staff trust. Staff need visible proof email mining is working (R1 F7).
REJECTED: Admin-only workflow health view (non-admins also need to trust the system).

[2026-03-11, updated 2026-03-12] **D25: Traveler auth = magic link only**
DECISION: FinnConcierge traveler auth = Supabase email OTP (60-min expiry) + resend button on login page + httpOnly session cookie. Google social as optional second path. No passwords. NOTE: Staff auth is separate (Supabase JWT with role claims — D13). This decision covers B2C travelers only (deferred per D17).
BECAUSE: Zero friction for mobile, appropriate for occasional travel use, no password management overhead.
REJECTED: Password auth (too much friction for B2C travel). 15-min expiry (too short for mobile travelers — Janna condition, Grok debate 2026-03-12).

[2026-03-11] **D26: Wave 3A cost ceiling = $8 (one-time exception)**
DECISION: Wave 3A (Kanban Frontend) has a $8 ceiling. All other waves: $5 hard cap.
BECAUSE: Wave 3A installs @dnd-kit + TanStack + builds drag-drop Kanban + Realtime — will legitimately exceed $5.
REJECTED: Unlimited ceiling (GetOnStack precedent: undetected loop → $47K over 4 weeks).

---

## Second Brain + Capture Decisions (D27–D30)
**Source:** Nate B Jones YouTube + Substack Open Brain research, 2026-03-11
**Status:** Locked — apply before Wave 1A begins.

[2026-03-11] **D27: Booking reference format = FDM-[6-char alphanumeric]**
DECISION: Traveler-facing booking reference = `FDM-` prefix + 6 uppercase alphanumeric characters (e.g., FDM-K7X2P1). Server-side generated (crypto.randomBytes). Maps internally to deal_id UUID — UUID never exposed externally.
BECAUSE: Unguessable (IDOR-safe), human-readable for phone/email support, short enough to dictate verbally.
REJECTED: Exposing deal_id UUID directly (guessable sequential IDs, UUID too long for verbal dictation).

[2026-03-11] **D28: Capture channel = Microsoft Teams (not Slack)**
DECISION: Staff knowledge capture uses a dedicated Teams channel (`#crm-capture`) — already in M365 stack, no new tool required. Post format: `decision:` / `person:` / `insight:` / `meeting:` prefixes. Teams webhook → n8n → Supabase Edge Function → embedding + metadata → deal_embeddings table.
BECAUSE: Teams is already open on every staff screen. Zero new tool adoption required. Slack would add another subscription and context switch.
FALLBACK: Slack free tier if Teams webhook proves unreliable (n8n has native Teams + Slack nodes — swap is 5 minutes).
REJECTED: Slack as primary (adds tool, extra cost, adoption friction for M365 team).

[2026-03-11] **D29: pgvector in Wave 1A scope (not backlog)**
DECISION: Wave 1A schema migration includes `deal_embeddings` table: `id uuid`, `deal_id uuid FK → deals.id`, `embedding vector(1536)`, `model_used text`, `created_at timestamptz`. Supabase Edge Function generates embedding on every deal write (parallel to metadata extraction).
BECAUSE: ALTER TABLE on 500+ live rows + data backfill migration is expensive. 30-minute schema addition now vs. painful migration later. Semantic search ("find Alpine groups who mentioned budget constraints") is core second brain value — not a nice-to-have.
REFERENCE: benclawbot/open-brain MIT — same Supabase + pgvector stack.
REJECTED: pgvector as backlog item (creates migration debt on live data).

[2026-03-11] **D30: Memory migration = two-phase**
DECISION: Phase 1 (Day 1 after Wave 1A): bulk-embed existing 107 DMC client profiles from mining outputs (`finland-dmc-2.0/mining-outputs/`). Staff gets semantic search over historical deal intelligence before a single new email is processed. Phase 2 (onboarding): structured Q&A session with each staff member → capture their institutional knowledge as embeddings (key clients, preferences, relationships).
BECAUSE: "Every other AI you connect starts with that foundation instead of zero" (Nate B Jones). Day 1 value requires Day 1 context — don't make staff wait weeks for the system to become useful.
SEQUENCE: Wave 1A schema → bulk-embed script → staff Q&A sessions → live email mining (post-DPIA).
REJECTED: Starting with empty embeddings (system feels useless on Day 1, adoption fails).

[2026-03-11] **D31: Webhook endpoint security**
DECISION: All ingest endpoints (Teams webhook handler, n8n triggers, MCP server) use header-only auth (`x-brain-key` or `Authorization: Bearer` — never URL query param). Per-service credentials: separate key for Teams webhook, separate key for n8n, separate key for MCP server (not a shared key). Rate limiting applied at Supabase Edge Function level or n8n throttle on all ingest endpoints.
BECAUSE: URL query param auth gets logged in browser history, server logs, proxy logs — anyone with the URL has full read/write access. Single shared key = rotate everything on one compromise. No rate limit on leaked key = unlimited extraction.
SOURCE: Robert MacNaughton security audit + Pokemon Is Awful (Substack comments, 2026-03-11). C1 from nate-substack-comments-addendum.md.
REJECTED: Single shared key across services (one breach = full system exposure). Auth via URL query param (logged everywhere).

[2026-03-11] **D32: deal_embeddings soft-delete**
DECISION: `deal_embeddings` table includes `active boolean default true` column. Deletion = `UPDATE deal_embeddings SET active = false` (soft-delete only — never DROP rows). Hard-delete only via `erase_contact_pii()` GDPR erasure function. All queries filter `WHERE active = true` by default.
BECAUSE: Audit trail required — GDPR erasure log must prove deletion occurred, which requires the row to exist as evidence until formal erasure. Soft-delete preserves audit trail while making row invisible to AI pipeline.
SOURCE: Chris Maughan + Mark Madsen community pattern (Substack comments, 2026-03-11). C5 from nate-substack-comments-addendum.md.
REJECTED: Hard-delete on staff request (breaks GDPR deletion log). No delete mechanism (retention compliance impossible).

[2026-03-11] **D33: Atomic facts chunking for bulk-embed (D30 Phase 1)**
DECISION: D30 Phase 1 bulk-embed breaks 107 client profiles into atomic facts before embedding — NOT full profile blobs. Each atomic fact = one standalone sentence (e.g., "AHI Travel: senior Nordic traveler segment, 75% of DMC revenue"). Target: 10-20 facts per profile = 1,070–2,140 embedding rows on Day 1. Each fact = one row in deal_embeddings.
BECAUSE: Semantic queries ("find clients who asked about budget Lapland options") return specific matching facts, not entire profiles. Full-blob embeddings average out meaning — atomic facts preserve specific retrievable signals.
SOURCE: Nate B Jones atomic facts recommendation (Substack article + comments, 2026-03-11). C4 from nate-substack-comments-addendum.md.
REJECTED: Embedding full 107-profile blobs (semantic search returns irrelevant profile sections, degrades accuracy).

---

## Email Drafter Feedback Loop (D36–D38)
**Source:** Patrick Heiskanen design session, 2026-03-12
**Status:** Locked — add to Wave 1A addendum migration before Wave 2A starts.

[2026-03-12] **D36: Email drafter data model — sessions + iterations + prompt_versions**
DECISION: Capture full email drafting loop in 3 tables:
- `prompt_versions` — all golden prompt versions (version_tag, email_type, prompt_text, is_active, ab_weight). Multiple versions per email_type = A/B competition. Weighted random assignment at session creation.
- `email_draft_sessions` — one row per email drafted: deal_id FK, client_id FK, email_type, context_snapshot (jsonb), prompt_version_id FK, z_sent_text, z_sent_at, z_human_edited, R fields (auto-captured), session_type (human_iteration|ai_sparrer|human_oneshot), sparrer_ready flag.
- `email_draft_iterations` — N rows per session: iteration_number, x_draft, x_model, y_feedback, y_feedback_source (human|ai_sparrer), y_feedback_type (tone|length|content|rewrite|accepted).
BECAUSE: Need to capture full (X1,Y1,X2,Y2...Z,R) loop to build AI sparrer. prompt_version_id FK makes R signal correlation by prompt version measurable — enables prompt competition. Multiple iteration rounds supported from day 1 (human or AI sparrer both use same structure). Human can always override at any stage.
FUTURE: When enough sparrer_ready sessions collected, AI sparrer replaces human Y rounds. session_type field tracks the transition. Phase 3: jury evaluations inform automatic golden prompt improvement.
REJECTED: Single-row model (can't handle N iteration rounds). Free-text prompt_version label (can't correlate R signal to specific prompt text).

[2026-03-12] **D37: R auto-capture via email pipeline (no manual entry)**
DECISION: R fields on email_draft_sessions are populated automatically by n8n, not manually by staff:
- On outbound email sent: record session_id in outbound email metadata.
- On inbound reply matching session: set r_client_responded=true, r_response_at, run Claude Haiku sentiment classification → r_response_sentiment (positive|neutral|negative).
- Check deal stage delta at reply time → r_deal_progressed.
- After 7 days no reply: set r_client_responded=false, r_response_sentiment='no_response', r_captured_at=now().
- Teams #crm-capture post (D28 channel) → r_notes field (manual addendum, optional).
BECAUSE: Manual R capture = never happens. Automatic = always happens. 7-day window matches realistic B2B reply cadence. R signal is only valuable if it's complete — gaps break the sparrer training data.
REJECTED: Manual staff rating (adoption failure). Shorter window (misses slow B2B replies). Sentiment from staff judgement (subjective, inconsistent).

[2026-03-12] **D38: Prompt competition + red team jury**
DECISION: Multiple prompt_versions with is_active=true for same email_type compete via weighted random A/B assignment. Periodic jury run (Claude Sonnet as judge, weekly or when N≥20 new sessions per version):
- Input: last N sessions per active version + their R scores.
- Jury scores each version: avg_r_score (response rate × sentiment), avg_iterations_needed (lower = better), quality_score (0–1 AI assessment of draft quality).
- Output stored in `prompt_evaluations` table: strengths, weaknesses, suggested_improvements, ranking_vs_competitors, recommended_action (promote|keep|demote|retire).
- Promotion = raise ab_weight. Retire = set is_active=false, deactivated_at=now(). New challenger versions created from suggested_improvements.
- Self-improving loop: jury suggestions → Patrick reviews → new prompt_version created → enters competition.
BECAUSE: R signal tells you which prompt actually converts clients, not which one looks good. AI jury can evaluate quality at scale without Patrick reviewing every draft. Competition pressure ensures prompts keep improving. Same mechanism works for both human-iteration and ai_sparrer phases.
FUTURE: Phase 3 — jury creates challenger prompt versions automatically (Patrick approves before activating). Fully automated prompt evolution with human approval gate.
REJECTED: Single canonical prompt (no improvement signal). Manual prompt review only (doesn't scale). Jury without R signal (measures writing quality, not business outcome).

---

## Staff Adoption Pitch (locked language — use verbatim)

**Core punchline (source: patrick, 2026-03-11):**
> "Zero data entry — and the system gets smarter about your clients every week because it remembers everything."

**Per-person variants:**
- Sebastian: "You'll never dig through email for deal status again. It just appears — and gets better every week."
- Liisa: "You'll see things you didn't know we had. The system remembers every client interaction so you don't have to."
- Janna: "Pipedrive requires you to enter data. This one enters it for you — and gets smarter the longer you use it."
- Reeta: "Everything needs your approval. The system finds; you decide. And it learns from every decision you make."
- Laura: "All your group trips connected to TravelTree — and it remembers every group preference you've ever handled."

---

## Opportunity Engine + Long-Term Architecture (D43–D50)
**Source:** Grok 4 Heavy 4-agent council, Round 2, 2026-03-13
**Status:** Locked — apply D43 + D44 before Wave 3C spawns. D45-D50 guide Wave 3C build.

[2026-03-13] **D43: raw_content column on deal_embeddings (re-embedding resilience)**
DECISION: Add `raw_content text` column to `deal_embeddings` table alongside the `embedding vector(1536)` column. Backfill script runs once after column is added. Every future embedding insert must write both the vector AND the source text that generated it.
BECAUSE: text-embedding-3-small is an OpenAI model. In 3 years a superior or cheaper model will exist. Without raw_content, re-embedding requires re-fetching all source data from n8n or email archives — expensive and fragile. With raw_content, re-embedding is a single script: `SELECT raw_content FROM deal_embeddings → generate new vector → UPDATE`.
CHANGE: ALTER TABLE deal_embeddings ADD COLUMN raw_content text; + backfill from deal content sources.
REJECTED: Relying on source data availability for future re-embedding (email archives may be deleted, n8n logs purged).

[2026-03-13] **D44: Model routing abstraction layer**
DECISION: All AI model calls in n8n workflows and Supabase Edge Functions route through a single abstraction layer: one Supabase Edge Function `/model-router` that accepts `{task_type, input, max_tokens}` and returns output. task_type determines model: `classification` → Sonnet, `extraction` → Haiku, `strategy_brief` → Sonnet, `embedding` → text-embedding-3-small via OpenRouter.
BECAUSE: If a model is deprecated, price changes significantly, or a better option emerges, today's approach requires editing every n8n workflow and Edge Function. Abstraction layer = change model in one place. Also enables cost monitoring per task_type.
IMPLEMENTATION: ~2-day task. Do before Wave 3C. Not blocking Wave 2A.
REJECTED: Hardcoding model names per workflow (maintenance burden multiplies with every new workflow).

[2026-03-13] **D45: Client seasonal pattern miner — highest-impact missing capability**
DECISION: Build a client seasonal pattern miner that extracts per-client booking cadence from historical closed deals in deal_embeddings + deal_stage_history. Output: per-client record `{client_id, typical_season, typical_destination, avg_interval_months, last_booking_date, next_expected_window}`. Runs weekly cron. Powers anniversary and re-engagement signals directly.
BECAUSE: Finnish travel DMC business is entirely seasonal. Lapland winter, summer archipelago, spring shoulder — every client has a rhythm. This intelligence exists in our 5-year deal history but no human can track 107 clients' individual cycles. Seasonal pattern miner converts history into predictive timing intelligence. Compounds every year as more data accumulates. Zero new data entry required.
SOURCE: Grok council winner (Agent 3, DMC Operations), confirmed by full council, 2026-03-13.
REJECTED: Manual tracking of booking anniversaries (doesn't scale to 107 clients, requires data entry).

[2026-03-13] **D46: Opportunity signal priority order**
DECISION: Opportunity Engine surfaces signals in this priority order: (1) Anniversary — client booking window opens based on seasonal pattern, (2) Re-engagement — dormant high-value account 12+ months dark, (3) Upsell — confirmed deal matches add-on opportunity, (4) Referral — post-trip positive sentiment detected, (5) Lapsed proposal — combine with pricing window check. Market signals: EXCLUDED permanently.
BECAUSE: Anniversary signals are the most predictive (time-bridged, high confidence). Re-engagement has highest absolute revenue potential (Flash Pack = €558K). Upsell requires zero new relationship work. Market signals introduce GDPR friction + unreliable feeds + cost — unjustifiable for 5-person team.
REJECTED: Market signals (competitor routes, flight capacity) — external data, GDPR friction, unreliable feeds.

[2026-03-13] **D47: Strategy brief = limited version, agent-surfaces-human-decides**
DECISION: Opportunity Engine generates a 4-section strategy brief per signal: (1) context summary from deal_embeddings, (2) 3 strategy options (A/B + Dismiss), (3) recommended option with 1-sentence rationale, (4) action buttons [Send A] [Send B] [Dismiss] [Edit]. Agent never auto-sends. Every outreach requires explicit staff approval. Brief uses only verified deal_embeddings data — no inference or embellishment.
BECAUSE: Finnish B2B culture is reserved — tone mismatch in an auto-generated email could damage a €200K relationship. One bad outreach = client lost. Judgment line must hold: agent surfaces options, human chooses and approves.
RISK: Hallucinated context in brief → mitigated by data-only sourcing from deal_embeddings (no LLM inference on relationship tone).
REJECTED: Auto-send on high-confidence signals (judgment line violation, cultural risk). Full AI-written custom emails without structured options (hallucination risk in B2B context).

[2026-03-13] **D48: Market signals permanently excluded from Opportunity Engine**
DECISION: Opportunity Engine will never ingest external market data (flight routes, competitor pricing, travel trends). All signals derive from internal Supabase data only: deals, deal_activities, deal_embeddings, rate_cards, clients.
BECAUSE: External data = GDPR compliance complexity (data processor agreements), unreliable feed quality, maintenance cost for a 5-person team. Internal data is richer (we know client history, pricing, preferences) and fully GDPR-safe. An internal-only system can also be reasoned about and audited without external dependencies.
FUTURE: If Patrick explicitly requests market intelligence, revisit as a separate module with its own DPIA — not part of the Opportunity Engine core.
REJECTED: External route/competitor feeds (GDPR, unreliable, unjustifiable cost).

[2026-03-13] **D49: Daily Opportunity Briefing on morning dashboard**
DECISION: Morning dashboard (BP08 section 1.3) gets a dedicated "Opportunity Briefing" section between "YOUR DAY" and "OVERNIGHT" panels. Shows up to 3 opportunity cards per staff member, ranked by D46 priority order. Each card: signal type, client name, signal summary, [Review] button. One-click opens full strategy brief (D47 format). Zero cards shown if no signals — never show empty state as failure.
BECAUSE: Push delivery (morning briefing) is the highest-adoption pattern for a 5-person team. Opportunities missed because staff had to think to look for them = revenue loss. Morning briefing = agent surfaces proactively, human reviews at natural workflow moment (start of day).
IMPLEMENTATION: n8n cron runs Opportunity Engine at 07:00 → writes to opportunities table → morning dashboard query includes opportunities by staff owner at 08:30.
REJECTED: Opportunity signals in a separate tab (requires staff to navigate, reduces adoption). Real-time push notification per signal (notification fatigue in a 5-person team).

[2026-03-13] **D50: North Star confirmed as design target**
DECISION: The following paragraph is the design target for all future BP08 and Opportunity Engine decisions. Every new feature is tested against it: "Does this move us closer to this experience?"
> "Every morning I open the PWA and the Second Brain has already prepared my day: three hot opportunities it spotted overnight — AHI Travel's Lapland anniversary window opens in 10 days with a ready strategy and email draft; Flash Pack is 8 months dormant but their 18-month pattern says now is perfect; plus two upsell chances on current groups drawn from identical past wins. I click into each card, review the three-option brief (recommended one highlighted with risk/reward), tweak one sentence if needed, hit Approve — the agent sends the perfectly personalised message, tracks opens, and only nudges me later if required. The system remembers every client interaction, seasonal cycle, supplier rate, and successful approach from the last five years better than any of us ever could, so our tiny 5-person team operates with the memory and foresight of a 50-person operation. It surfaces what matters, suggests without ever deciding, and lets us spend every minute on the relationships that actually close deals."
SOURCE: Grok 4 Heavy 4-agent council, 2026-03-13. Validated against all 7 Nate AI Open Brain principles.

---

## Statistical Guardrails + Strategic Phasing (D51–D52)

**Status:** Locked 2026-03-13 — must apply before Wave 3C spawns.

[2026-03-13] **D51: Statistical guardrail on individual pattern claims (Benjamin kill shot)**
DECISION: Wave 3C must NOT surface individual client seasonal predictions as confident signals. Replace with cohort-level predictions. Surfacing rules: (a) cohort signal (N≥10 in same tier+destination group) = surface with no caveat; (b) individual signal (N≥5) = surface with explicit "Low confidence — limited history" label; (c) individual signal (N<5) = do NOT surface as a standalone signal (can contribute to cohort only).
BECAUSE: Benjamin (Grok R3) verified 3–7 booking observations per client over 7.5 years. With 3–7 data points, individual seasonal predictions are ~57% accurate — near coin-flip. Surfacing "Flash Pack's 18-month pattern says now is perfect" when based on 4 bookings damages staff trust when it's wrong. System credibility is the single most fragile asset in a 5-person team.
IMPLEMENTATION: (1) Add cohort_n integer column to client_patterns table — count of clients in same tier+destination cohort. (2) Add confidence_tier enum: 'cohort_strong' (cohort N≥10), 'individual_ok' (individual N≥5), 'suppressed' (N<5). (3) Opportunity signal engine only fires for confidence_tier IN ('cohort_strong', 'individual_ok'). (4) Strategy brief for 'individual_ok' signals must include: "Signal confidence: limited (N=[N] bookings — treat as directional, not predictive)."
REJECTED: Using 4+ booking threshold (still too low — 57% accuracy); suppressing all individual signals (throws away valid N≥5 data).
SOURCE: Grok Open Spar Round 3, Benjamin, 2026-03-13.

[2026-03-13] **D52: Strategic phasing — Phase 1 = Second Brain CRM, Phase 2 = ERP/admin reduction**
DECISION: System built in two phases. Phase 1 (now through ~2027): Pipedrive-style proactive Second Brain CRM — opportunity surfacing, seasonal intelligence, relationship memory, Wave 3C opportunity engine. Phase 2 (~2027–2028, after TravelTree mining session): ERP capabilities — confirmed → invoiced admin reduction, TravelTree integration (D16), supplier workflow automation. Phase 2 cannot start before a dedicated TravelTree mining session establishes what data exists in TT and what APIs are available.
BECAUSE: Lucas (Grok R3) correctly identified confirmed→invoiced as the long-term admin bottleneck — one failed execution damages a 10-year relationship faster than a missed re-engagement email. However, TravelTree integration requires mining before building. Wave 3C (pre-sale opportunity engine) proceeds NOW. D16 (TravelTree) deferred to Phase 2.
WAVE SEQUENCE IMPACT: Wave 3C unblocked. D16 remains in plan but moves to Phase 2. Wave sequence for Phase 1 unchanged.
REJECTED: Starting D16 now (no source data from TravelTree yet — would build blind). Abandoning Wave 3C to prioritize operations (Lucas was only half-right — clients #40–107 do need memory assistance).
SOURCE: Patrick decision, 2026-03-13. Lucas challenge (Grok R3) was the prompt.

---

## n8n Infrastructure Requirements (D53–D59)
**Source:** Cross-validated by Grok Heavy 4-agent council AND Gemini 2.5 Pro (independently, 2026-03-24)
**Status:** Locked — apply before Wave 2A (email pipeline) starts. All 7 findings were unanimous across both external models.
**Context:** Original session 89 architecture (6 custom TypeScript services on Railway) was replaced by n8n self-hosted on Hetzner. This review identified what the pivot solved, what it didn't, and what new risks it introduced.

[2026-03-24] **D53: n8n must use PostgreSQL, not SQLite**
DECISION: n8n's internal database must be PostgreSQL (separate instance from Supabase app DB). Set `N8N_DATABASE_TYPE=postgres` in docker-compose.
BECAUSE: Default SQLite hits `database is locked` errors under concurrent LLM-heavy workloads (Triple-LLM D7 pipeline). Both Grok and Gemini identified this independently as production-breaking.
REJECTED: SQLite (default — fails under concurrent writes). Using Supabase app DB for n8n internals (couples infrastructure).

[2026-03-24] **D54: N8N_ENCRYPTION_KEY must be set and backed up externally**
DECISION: Generate encryption key (`openssl rand -hex 32`), set as `N8N_ENCRYPTION_KEY` env var, back up outside VPS before first launch. This key encrypts all OAuth2 credentials in n8n's database.
BECAUSE: Losing this key during Hetzner rebuild/migration makes all Microsoft Graph credentials permanently unrecoverable. Both models flagged independently.
REJECTED: Relying on n8n default key generation (not portable, not recoverable).

[2026-03-24] **D55: Queue mode + Redis + worker containers required**
DECISION: n8n must run in queue mode with Redis and separate worker containers (docker-compose). Without this, Triple-LLM pipeline (~45s/email) causes event loop thrashing and webhook timeouts.
BECAUSE: Microsoft Graph requires webhook response within 10 seconds. 5 concurrent LLM-heavy workflows spike CPU to 100% on 2vCPU VPS. Both models confirmed independently.
REJECTED: Default single-process mode (fails under any email burst).

[2026-03-24] **D56: n8n OAuth2 for Graph API is NOT fully reliable — Credential Watchdog required**
DECISION: Build a dedicated n8n workflow that proactively calls Graph API every 45 minutes and alerts via Teams if the credential fails. Do not rely on n8n's native OAuth2 refresh for production email pipeline.
BECAUSE: Both models found documented failure modes: silent refresh failures, refresh token rotation not persisted, credential loss after restarts. Gemini proposed Credential Watchdog pattern; Grok confirmed OAuth2 is not "solved natively."
REJECTED: Trusting n8n's native OAuth2 handling without monitoring (documented failures in 2025-2026).

[2026-03-24] **D57: Supabase is the state bus — n8n is a stateless worker**
DECISION: All pipeline state (deltaLink, subscriptionId, S4→S5 handoff status, audit records) must be stored in Supabase, not in n8n's internal state. n8n workflows read from and write to Supabase at every step.
BECAUSE: n8n workflows are logically isolated and stateless. Multi-workflow state sharing (sync workflow ↔ webhook workflow ↔ classification workflow) requires external persistent store. Both models converged on this independently.
IMPLEMENTATION: `sync_state` Supabase table with columns: `key` (text PK), `value` (jsonb), `updated_at` (timestamptz). Stores deltaLink, active subscriptionId, last successful sync timestamp.
REJECTED: n8n internal state or Data Tables (insufficient for cross-workflow coordination at this complexity).

[2026-03-24] **D58: Execution data pruning mandatory**
DECISION: Set `EXECUTIONS_DATA_SAVE_ON_SUCCESS=none` and configure `EXECUTIONS_DATA_PRUNE=true` with appropriate retention. n8n stores full execution payloads (including LLM outputs) by default.
BECAUSE: Without pruning, n8n's Postgres grows to GBs within weeks at 107-client volume with Triple-LLM + S5 validation retries. Both models flagged independently.
REJECTED: Default execution storage (disk fills, performance degrades).

[2026-03-24] **D59: Graph API calls require ImmutableId header + webhook validationToken handler**
DECISION: (a) All Graph API calls must include `Prefer: IdType="ImmutableId"` header — use HTTP Request node, not the pre-built Microsoft Graph node. (b) Webhook subscription creation requires a dedicated Code node to echo the `validationToken` synchronously. (c) Delta query sweep every 15-30 minutes (n8n Schedule node) with deltaLink stored in Supabase (D57).
BECAUSE: (a) Staff moving email to subfolder changes standard ID → PATCH returns 404. Unanimous across all 3 original reviewers (session 89). (b) Graph API silently rejects subscriptions without proper validation echo. Grok flagged. (c) Graph webhooks are "best effort" — 1-5% of emails missed without delta fallback. Unanimous session 89.
REJECTED: Using n8n's pre-built Microsoft Graph node (doesn't support ImmutableId or ETag management).

---

## Transcript Pipeline Architecture (D60)
**Source:** Session 112 — 5-agent research synthesis + Patrick decisions
**Status:** Locked — build plan in `~/1658HoldingsOy-AIFiles/_drafts/TRANSCRIPT-PIPELINE-BUILD-PLAN.md`

[2026-03-25] **D60: Transcript Pipeline — locked architecture decisions**
DECISION: Transcript pipeline builds on existing Second Brain stack with these additions:
(a) 7 new tables (additive, zero ALTER TABLE on CRM tables). Full schema in TRANSCRIPT-PIPELINE-BUILD-PLAN.md Section 2.
(b) n8n only for MVP (Workflows A-E) — no custom TypeScript/Python before Markus pilot is validated.
(c) Raw data retention: 90 days default (Patrick decision — GDPR minimum is floor, not ceiling). meeting_analysis: 365 days.
(d) Markus-first pilot (Järvisydän Oy, opt-in) before staff rollout. Avoids Panopticon effect (Gemini design validation).
(e) Green/Yellow/Red classification mandatory before any commitment data reaches Patrick.
(f) D44 model routing: tech debt — direct Claude API calls acceptable for MVP. Blocking only at Wave 3C.
(g) transcript_pipeline_state (separate Supabase table) for pipeline state — no key collision with email pipeline sync_state (D57 pattern).
(h) Whisper hybrid on same Hetzner host via faster-whisper (CTranslate2 CPU backend). Requires ≥10GB RAM — verify before enabling.
(i) YT-menettely (Finnish Co-operation Act) required before staff rollout. NOT required before Markus opt-in pilot (verify with lawyer).
BECAUSE: MVP focus, additive architecture, Markus use case proven before scaling. Panopticon risk: starting "CEO watches staff" view kills project.
REJECTED: Power Automate (not in stack). Separate Supabase database (same DB, new tables). Markus data to Patrick without G/Y/R filter. D44 model routing now (blocks MVP unnecessarily).
UPDATE S115: D60(b) superseded by D62 (n8n Cloud EU replaces self-hosted). D60 DB assumption (same instance) refined by D61 (dedicated schema + RLS + Pooler).

---

## Transcript Pipeline Architecture — S115 Grok Validation (D61–D62)
**Source:** Session 115 — Grok Heavy 2-round validation (Round 1: reject A/B, Round 2: find Option C)
**Status:** Locked — pending Patrick verification items noted below

[2026-03-25] **D61: Database — dedicated schema + RLS + Dedicated Pooler (same Supabase project)**
DECISION: Transcript pipeline uses a dedicated `transcripts` schema within the existing Supabase project. Not a separate Supabase project. Isolation via:
- Schema-level separation (transcripts schema, not public schema)
- RLS policies scoped to transcripts schema only
- Column privileges: Data API disabled for transcripts schema (direct DB access only, no PostgREST exposure)
- Upgrade to Pro-plan Dedicated Pooler (PgBouncer co-located) — independent connection limits for CRM and transcript workloads
BECAUSE: Same-project-with-schema avoids cross-DB sync complexity (Lucas: "cross-project ETL hell") while providing GDPR-adequate logical isolation. Harper + Benjamin CONDITIONAL GO. Dedicated Pooler eliminates connection pool contention identified in Round 1.
REJECTED: Same instance public schema (GDPR contamination + connection pool collision). Separate Supabase project (cross-project ETL complexity for solo dev).
CONDITION: Frendy or external consultant must perform initial RLS + schema + role setup (est. 4–6h). Do not self-build without Postgres expertise.
OPEN: Lucas NO GO — RLS maintenance burden at month 6 if Claude API adds new fields. Mitigation: document all policies in schema migration files from day 1.

[2026-03-25] **D63: YT-laki koskee pilottia — muut työntekijät ratkaisevat**
DECISION: YT-lain yhteistoimintamenettely on pakollinen ennen Markus-pilottia jos Markuksen kokouksissa on muita Järvisydänin työntekijöitä. Markuksen asema rekisterinpitäjänä ei suojaa pilottia kun toisten työntekijöiden puhe tallentuu transkriptiin.
BECAUSE: YT-laki koskee työnantajan toteuttamaa henkilöstön seurantaa. Jos transkripti sisältää muidenkin kuin Markuksen puheen, kyse on henkilöstön seurantatyökalusta — ei henkilökohtaisesta muistiinpanovälineestä.
EXCEPTION: Jos pilotti rajataan tiukasti vain kokouksiin joissa ei ole muita Järvisydänin työntekijöitä (esim. Markus + Patrick kahdenkeskiset), YT-menettely ei välttämättä koske. Tämä on kuitenkin käytännössä erittäin kapea rajaus.
NEXT STEP: Selvitä Grok spar 3 (tai lakimies) — onko 1:1-poikkeus realistinen vai tehdäänkö YT-menettely ennen kaikkea.
SOURCE: Patrick S115 — "varmaan koskee jos muut työntekijät myös tallennettavassa teamsissa"

[2026-03-25] **D62: Automation engine — n8n Cloud EU (Frankfurt)**
DECISION: Replace n8n self-hosted on Hetzner with n8n Cloud EU (Frankfurt-hosted, managed). Starter plan covers 5–15 meetings/week (2,500 executions/month).
BECAUSE: CVE-2026-21858 (CVSS 10.0, "Ni8mare" — unauthenticated RCE via webhook content-type confusion) confirmed real by Grok Harper agent. 14,000–26,000 exposed self-hosted instances as of 2026-03. Self-hosted with public webhook endpoint = unacceptable risk. n8n Cloud = managed patching + EU data residency + GDPR DPA + keeps visual editor + native Graph API nodes.
REJECTED: n8n self-hosted (CVE-2026-21858 RCE risk). Trigger.dev (queue incidents 2025, cold starts, TS debugging burden for solo dev, no visual editor).
CONDITION: Patrick must verify before build:
  1. n8n.io/pricing — confirm Starter execution limits and current price
  2. n8n Cloud GDPR DPA availability (Frankfurt EU region)
  3. Test: 50 webhook calls in test mode to confirm Graph API reliability
TCO: ~€24/month (Starter) + ~€1,920/year labor estimate (Benjamin). Total ~€2,500/year.
OPEN: Lucas NO GO (vendor lock-in + pricing change risk). Accepted — risk is lower than CVE RCE risk on same server as CRM data.

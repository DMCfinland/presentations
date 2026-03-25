# Mikko Alasaarela — Knowledge File
**Built:** 2026-03-19 | **Sources:** 3× Grok Heavy rounds + web research (S97–S98)
**Status:** Mature — do not re-research. Update only when Agion publishes new material or Patrick requests.

---

## ★ BEST PRACTICES — APPLY TO 1658 HOLDINGS AI SYSTEM

*These are practices extracted from Mikko's work and thinking that are directly applicable to Patrick's daily AI usage and the 1658 Holdings system. Not aspirational — actionable today.*

### 1. Chief of Staff Bot — Always On Second Screen
**What Mikko does:** Never opens Word or Google Docs for thinking. Opens the Chief of Staff bot and dumps raw thought. The bot asks Socratic questions, forces structure, produces drafts.
**Apply now:** Dedicate a persistent Claude conversation (or Claude Code session) as the Chief of Staff channel. When a new problem or idea appears — open it there first, not a blank document. Dump raw. Let the dialogue do the structuring.
**Impact:** Replaces the solo "stare at blank page" loop with structured dialogue from the first second.

### 2. Agent Farm Manager Mindset
**What Mikko does:** Thinks of himself not as the doer but as the manager of an agent team. Every task starts with: "which agent handles this?" not "how do I do this?"
**Apply now:** Before starting any task in Claude Code, ask: "Is this a task I should delegate to a subagent, or does it require my direct judgment?" If delegatable → spawn. Reserve Patrick-time for: strategy, evaluation, escalation, and new problem framing.
**Impact:** Stops the "CEO doing clerk work" failure mode. Matches the Tier 1/2/3 work framework already in the system.

### 3. Mission-as-Code — KPIs in Every Prompt
**What Mikko does:** Every agent task is tied to a business KPI or goal explicitly. Agents always know the current mission, not just the immediate task.
**Apply now:** Add the business context to every significant agent spawn prompt. Not "write this email" but "write this email to advance the DMC proposal win rate — current rate 40%, target 60%, this prospect is €25k/year." Claude Code has this pattern — extend it to every externally-spawned subagent.
**Impact:** Prevents agents optimizing for the literal task at the expense of the actual goal.

### 4. Urgency + Experimentation Loop (No Perfect Conditions)
**What Mikko does:** Holiday hackathons. Heavy inference spend on personal experimentation. "Don't wait. Learn fast." Treats rapid iteration as the primary skill, not waiting for the right setup.
**Apply now:** When uncertain about a workflow — build it this session, even messily. Don't wait for Wave 3A or the right conditions. The cost of a 30-minute experiment is lower than weeks of planning. Budget for "Mikko-style" exploration sessions explicitly.
**Impact:** Closes the gap between "theoretically good system" and "battle-tested daily driver."

### 5. Compound on Existing Strengths — Not Random Tasks
**What Mikko does:** Applies AI multiplier to areas where he is already elite (systems thinking, agent governance design, Finnish public sector relationships). Doesn't use AI to become mediocre at new things.
**Apply now:** For Patrick: apply AI multiplier to CEO-level strategic judgment, portfolio oversight, M365 mining, and client relationship management. Do NOT try to use AI to replace deep expertise you don't have yet. Go deep where you're already strong.
**Impact:** Compound leverage (Section F) only works if the pre-AI baseline is already elite.

### 6. Replace Review with Policy — Build Trust Score into Workflows
**What Mikko does:** 95% auto-approval via Governance-as-Code. Not "I review everything" but "the policy handles it; I only see exceptions."
**Apply now (now):** For n8n workflows already running — identify which ones Patrick still manually reviews that have 100% approval rate over 20+ runs. Auto-approve those. Build a simple mental trust_score per workflow: N runs without error = reduce gates. Formally implement with Supabase column on Wave 3A.
**Impact:** Converts time spent on routine review into time available for genuine judgment work.

### 7. Sovereignty-First Data Architecture
**What Mikko does:** EU data, customer-specific models, immutable audit. Not "use the cheapest API" but "use the one where you own the outputs and the data doesn't train the provider."
**Apply now:** Already partly implemented (Anthropic Teams + DPA). Continue: for any new AI service integrated into the 1658 stack — check data residency and training policy before integrating. Default: anthropic.com/teams (DPA in place), Supabase (EU region), n8n (self-hostable).
**Impact:** GDPR compliance + enterprise credibility when selling AI-powered services to Finnish B2B clients.

### 8. The Productivity Filter — One Metric to Rule Them
**What Mikko does:** "Productivity is the only metric that matters." Every tool, every workflow, every vendor decision is filtered through: does this increase output per unit of human effort?
**Apply now:** Before adding any new tool or workflow: "Does this increase output per unit of Patrick-time?" If yes, do it. If it just adds capability without increasing leverage — defer or skip. This is already implicit in the system's quality-over-quantity principle. Make it explicit in vendor evaluations and session planning.
**Impact:** Stops tool accumulation / complexity creep that reduces rather than increases leverage.

---

## A. IDENTITY

**Who he is:** Finnish AI entrepreneur and systems-level leverage thinker. Founded Gamelion (2006), Linko, Inbot, Equel Social, Atlan (Chairman), and currently Agion (2024–present). Also held Nokia Bell Labs EIR role (2023–25). Speaks frequently on Finnish productivity, public sector AI, and agent governance.

**Core invariant (unchanged since ~2013):**
> "AI as universal thinking accelerator that multiplies output 3–10× (or 1000× in personal demos) while preserving sovereignty, trust, and human oversight."

This framing has been consistent across every venture and every public appearance — before AI hype, during it, and after it.

**Thinking style:**
- Systems-level: always asking "what changes the leverage function?" not "what's the feature?"
- Sovereign-first: EU vs US AI, private customer-specific models, immutable audit trails
- Productivity obsessive: treats output per unit of human effort as the only metric worth measuring
- Nation-scale ambition: frames every tool in terms of what it means for Finland's GDP

**Recurring obsessions:**
1. Algorithmic influence on worldview (LinkedIn articles on neutralizing personalization filter bubbles)
2. Sovereignty/privacy in enterprise AI (closed, customer-specific models)
3. Human role → agent-farm manager / trainer (not doer)
4. Urgency: "don't wait" framing repeated across all venues

---

## B. VENTURE MAP

| Company | Years | Status | Notes |
|---------|-------|--------|-------|
| Gamelion | pre-2013 | **EXIT #1 (confirmed)** | Mobile software tools, Red Dot award, LED pico-projector patents. Sold to BLStream (200% growth trajectory). Only fully confirmed exit. |
| Linko Inc. | 2013–14 | Unconfirmed exit | Mobile AI CRM, $2.6M seed. Mikko departed early. "Possible loose exit" — not confirmed. |
| Inbot | 2013/14–2019 | **SHUTDOWN (not an exit)** | AI sales chatbot → InToken crypto. Explicit board shutdown Oct 2019 due to Estonian crypto regulations. Mikko's own Medium post confirms this was NOT an exit. |
| Equel Social | ~2021–24 | **DE-LISTED (not an exit)** | Community app countering algorithmic social media. De-listed from app stores. No exit documentation. |
| Atlan | ongoing | Limited data | Chairman role. No public venture details available. |
| Nokia Bell Labs EIR | ~2023–25 | Not a company | Entrepreneur-in-Residence = productization of Bell Labs AI research. Marketed as "Bell Labs background" — accurate but implies research depth that wasn't the role. Fed directly into Agion governance work. |
| Agion | 2024–present | **Active** | Agent governance OS for enterprise/public sector. €1M/6mo revenue, Valtiokonttori named customer, Wolt+Oura investors. |

**Through-line:** Every venture applies the same invariant (contextual intelligence multiplies leverage). Capital-attraction strong; PMF/regulatory failure recurs (Inbot, Equel).

**"3 exits" claim:** Resume inflation risk. Only Gamelion is a confirmed exit. Never repeat "3 exits" as fact.

---

## C. AJATTELUN KIIHDYTIN

**What it is NOT:** A documented framework. Zero verbatim hits for "ajattelun kiihdytin" as a methodology across all indexed sources. It is the title of the May 2024 Norders podcast episode and a descriptive label for his personal practice.

**What it actually IS** (from Norders podcast auto-captions — only primary source found):

**Verbatim Finnish (Norders, May 2024):**
> "Aina kun mulla on joku idea tai joku ongelma, mä en enää avaa Wordia tai Google Docsia, vaan mä avaan sen mun Chief of Staff -botin ja mä alan keskustelemaan sen kanssa... Se on vähän niinku kuminen ankka, mut se on maailman älykkäin kuminen ankka."

**Translation:** "Whenever I have an idea or a problem, I no longer open Word or Google Docs — I open my Chief of Staff bot and I start talking with it... It's a bit like a rubber duck, but the world's smartest rubber duck."

**The 5-step practice:**
1. Open "Chief of Staff" bot (always on second screen, always on)
2. Dump raw thought or problem into chat — NOT Word, NOT Google Docs
3. Bot asks Socratic questions → forces structure
4. Structured thoughts become drafts/plans
5. Separate agents handle pre-meeting research, communications, scheduling

**Key implication:** He has replaced solo thinking with human-AI dialogue as the primary cognitive act. The "thinking accelerator" is this replacement — not a product, not a framework, just a practice. Anyone can implement it today with Claude, ChatGPT, or any capable model.

---

## D. AGION / AANG

### The 5 Pillars (public narrative)
1. **Mission-as-Code:** KPIs → executable agent missions
2. **Governance-as-Code:** 95% auto-approval, <10ms decision latency, programmatic rules
3. **Dynamic Trust:** real-time scoring, earned autonomy per agent
4. **Radical Transparency:** 100% immutable audit trail
5. **Human-AI Partnership:** humans visionary, agents execute

**Enterprise claims:** 10k+ agents, O(1) scaling, Valtiokonttori named client, €1M/6mo revenue.

### HLR — Human Leverage Ratio
**What it is (Benjamin's model):**
```
HLR = [automation_depth × (1 − error_rate) × trust_threshold × num_agents]
      / [1 + (gates_per_100_tasks / 100 × 0.05)]
```

| Scenario | Auto Depth | Error Rate | Trust | Agents | Gates/100 | HLR |
|----------|-----------|------------|-------|--------|-----------|-----|
| Mainstream | 0.30 | 0.05 | 0.70 | 10 | 20 | 1.98× |
| Mid | 0.50 | 0.03 | 0.80 | 50 | 10 | 19.3× |
| High | 0.80 | 0.02 | 0.90 | 200 | 5 | 140.8× |
| Frontier | 0.95 | 0.01 | 0.95 | 1000 | 2 | 892.6× |

The flip from ~3× to 100×+ occurs when: automation_depth > 0.9 AND gates < 5 AND agents > 500.

**What HLR actually is:** Marketing language with no public benchmarks. No before/after data from Valtiokonttori or any customer. "200× personal leverage" claim never surfaced in any indexed source.

### Reality vs. Public Narrative
| Claim | Reality |
|-------|---------|
| "Sovereign enterprise OS" | Zero open-source. Closed-source black box. |
| "1 named customer" | Valtiokonttori — no public case study, no verified numbers |
| "Transparency pillar" | Immutable audit = marketing; product is opaque |
| "Agent farm for public sector" | €1M/6mo = real revenue but from 1 customer |
| "3 exits" | 1 confirmed exit (Gamelion). Inbot = shutdown. |

**Solo operator ceiling (Lucas):** Full AANG requires DevOps workload — policy maintenance, real-time engine, trust calibration. Solo ceiling ~6-10×, not 200×. OPA/Rego gates alone are solo-feasible up to ~50× (N=100, gates=5, auto=0.9).

---

## E. FINNISH YOUTUBE / PODCAST EXTRACTS

> **Note on sourcing:** Most of Mikko's Finnish appearances are on Spotify/Apple Podcasts, not YouTube. The Grok research team accessed Norders auto-captions for Finnish quotes. Direct YouTube URLs found: Solteq only.

### Key Verbatim Finnish Quotes

**Norders (May 2024) — "Miten rakentaa ajattelun kiihdytin tekoälyllä?" (1h11m)**
Primary source for personal methodology. See Section C for full verbatim quote.
> "Se on vähän niinku kuminen ankka, mut se on maailman älykkäin kuminen ankka."

**Norders / Finnish podcast (date unclear)**
[Harper verbatim]:
> "jos jokainen suomalainen olisi agenttitiimin johtaja, niin me olisimme automaattisesti maailman ykkönen tuottavuudessa"
> (If every Finn becomes an agent-team leader, we are automatically the world's #1 in productivity.)

**Finnish public-sector framing (multiple shows):**
> "Me voidaan automatisoida puolet julkisen sektorin työstä"
> (We can automate half of public sector work.)

> "Tää on se ainoa keino, miten me voidaan ratkaista Suomen tuottavuusongelma"
> (This is the ONLY way we can solve Finland's productivity problem.)

**"hopealuoti" (silver bullet) framing** — repeated across Finnish appearances; notably absent from English keynotes.

**Triple GDP claim:** "Make all public workers triple-productive" — appears in Finnish public sector talks.

### Finnish-Specific Reveals (not in English content)
- National urgency tone: framing AI as existential for Finland's competitiveness, not just an efficiency tool
- "hopealuoti" = presents himself as the solution to a national problem
- Public sector rhetoric far more direct in Finnish; English keynotes are polished/safer
- The productivity-as-patriotism framing is distinctly Finnish in its register

### Solteq Podcast (YouTube: https://youtu.be/Wc504njPu6E) — English
> "One Canadian friend of mine shipped 10 million lines of code last year by himself using an agent farm. And then 2.5 million additional lines in a single month — equivalent to the output of an entire mid-sized development agency."

> "Anyone listening to this podcast — don't wait. Learn fast."

> "Only 1% of organizations are currently leveraging agents for 2-3x productivity improvements."

### Episode List (confirmed appearances)
| # | Show | Episode | Date | Duration |
|---|------|---------|------|---------|
| 1 | Norders | "Miten rakentaa ajattelun kiihdytin tekoälyllä?" | May 2024 | 1h11m |
| 2 | Puheenaihe #435 | "Miten tekoäly muuttaa työtä?" | May 2024 | 1h17m |
| 3 | #neuvottelija | "Tekoälyagentit neuvottelijoina" | May 2024 | 59m |
| 4 | Solteq | "Tekoälyagentit mullistavat liiketoiminnan" | May 2024 | 35m |
| 5 | Teknologiateollisuus | "Tekoäly ja tuottavuusloikka" (w/ Jussi Herlin/KONE) | May 2024 | 49m |
| 6 | Puhutaan tekoälystä | "Vieraana Mikko Alasaarela" | May 2024 | 40m |
| 7 | Suomen Yrittäjät | "Yrittäjän podcast: Tekoälyagentit tulevat" | Jun 2024 | 31m |
| 8 | Alma Talent | "Tekoäly mullistaa asiantuntijatyön" | May 2024 | 10m |
| 9 | #neuvottelija ep.346 | "Julkinen sektori agenttifarmiksi" | Mar 2026 | — |
| 10 | Norders | "Ajattelu tekoälyn aikakaudella" | Oct 2024 | — |

---

## F. COMPOUND LEVERAGE

### The Model
Pre-AI elite operators (5–10× baseline) get an ADDITIONAL 5–10× multiplier from AI. This is COMPOUND leverage — not selection bias.

**Patrick's correction (S97):** Lucas's original "selection bias" argument was incomplete. The correct model: elite pre-AI operators do NOT regress to median when AI arrives. They stack the AI multiplier ON TOP of their existing advantage.

| Pre-AI Baseline | AI 1.3× | AI 3× | AI 5× | AI 10× |
|----------------|---------|-------|-------|--------|
| 1× (median) | 1.3× | 3× | 5× | 10× |
| 2× | 2.6× | 6× | 10× | 20× |
| 5× (elite) | 6.5× | 15× | 25× | 50× |
| 10× (top 1%) | 13× | 30× | 50× | 100× |

200×/250× requires extreme tails (10× pre × 20–25× AI) — outside observed distributions.

### Why the Math Is Insufficient (Patrick's second correction)
Multiplying two qualitative estimates produces false precision. A "10× developer" and "10× AI multiplier" are both qualitative labels, not measured quantities. Multiplying them to get "100×" gives a precise-looking number for a non-mathematical claim.

**The honest question is structural:** Does this person's output compound across time, teams, and domains non-linearly? For Mikko: likely yes — Chief of Staff bot + agent swarms + public sector deals + personal experimentation all point to non-linear compounding. But the specific number (100×, 200×) is not knowable.

### Empirical Reality Check (Mollick/BCG 2025)
Power users of AI tools achieve ~1.3–1.7× effective overall productivity. No sustained 5–10× AI multiplier for individuals has been documented. Mollick tops 36% in narrow tasks.

**Verdict:** 5–25× total leverage is plausible for elite operators with disciplined agent practice. 200× is aspirational marketing. The structural insight (elite operators compound rather than average) is real; the arithmetic is theater.

---

## G. WHAT TO STEAL

Three concrete architectural moves validated across Grok rounds 1–2. Applicable to 1658 Holdings / CRM build.

### Move 1 — OPA/Rego Policy Gates
**What:** Deploy Open Policy Agent (8.9k stars, CNCF project) rules as git-tracked Rego policies. Call via n8n HTTP node (<10ms decision latency).
**Why:** Brings "Governance-as-Code" concept into solo-feasible range. Maintains approval gates without human review overhead.
**When to build:** Wave 3A of CRM build.
**Repository:** github.com/open-policy-agent/opa

### Move 2 — Supabase Trust Score Column
**What:** Add `trust_score FLOAT` column to agent or workflow table in Supabase. Post-task trigger increments score based on success/failure. Higher trust_score = fewer gates required.
**Why:** Solo implementation of Agion's "Dynamic Trust" pillar. Earned autonomy for recurring workflows.
**When to build:** Wave 3A alongside OPA gates.

### Move 3 — Mission-as-Code KPI Injector
**What:** Python or Supabase edge function that prepends portfolio KPIs to every agent spawn prompt. "The mission is to increase DMC proposal win rate from X% to Y% by Z date" becomes automatic context.
**Why:** Agion's "Mission-as-Code" — agents that always know the current business objective, not just the immediate task.
**When to build:** After OPA + trust score foundation is in place.

**Expected lift (Benjamin's estimate):** 15–30× at N=50–100 agents vs. zero-governance baseline.
**Lucas's ceiling (conservative):** 6–10× for solo operator — still significant.

---

## H. VERDICT

### Builder Evidence
- 15+ years of consistent mental model, applied across multiple ventures
- Patents (LED pico-projector), Red Dot award, Gamelion exit
- Nokia Bell Labs EIR → real productization work feeding Agion
- Personal daily agent practice (holiday hackathons, Chief of Staff bot)
- Nation-scale framing that predates the 2024 AI hype wave
- Real revenue (€1M/6mo) from named public sector customer
- Wolt + Oura investors = smart capital, not just hype believers

### Narrator Evidence
- "3 exits" = only 1 confirmed. Inbot = shutdown. Resume inflation risk.
- Agion = zero open-source, despite sovereignty and transparency rhetoric
- "Ajattelun kiihdytin" undocumented — real practice but no replicable framework
- Finnish small-ecosystem investor network (Helsinki bubble, not independent validation)
- "hopealuoti" / civilizational rhetoric → high base rate of underdelivery among Finnish serial founders with shutdowns in history
- HLR = vanity metric without public before/after data

### Calibrated Assessment
**High-signal THINKER worth mining for mental models. Not an automatic hero or investment thesis.**

The core extraction, regardless of Agion's outcome:
> *Replace solitary thinking with human-AI dialogue as the primary cognitive act.*

This is actionable today, costs nothing, and is validated by the Chief of Staff bot practice. Whether Agion delivers its sovereign enterprise OS or not, this mental model transfer is the real value.

**For Patrick specifically:**
- Study his public sector leverage framing (applicable to Järvisydän + DMC positioning)
- Steal the 3 architectural moves (OPA gates, trust score, KPI injector) on Wave 3A timeline
- Do NOT assume the "3 exits" narrative or the 200× leverage claims are literal facts
- If Agion publishes open-source: revisit immediately. Currently: study the concept, verify the implementation separately.

---

## OPEN QUESTIONS (unresolved — for Patrick's decision)

1. **Contact strategy:** Reach out to Mikko? (Finland DMC B2B partnership angle, or just to learn.) Deferred until Patrick reviews this file.

2. **GitHub repo mining:** OPA + vorionsys/vorion → mine Rego patterns applicable to n8n/Supabase. Lower priority. Add if Wave 3A build starts.

3. **Zone B copy:** Should this file go to OneDrive (Zone B) for M365 search? Strategic research asset.

---

*Sources: GROK-ROUND-1-HLR.md, GROK-ROUND-2-COMPOUND.md, GROK-ROUND-3-SYNTHESIS.md (all in this folder) + web research session 98 (Solteq YouTube URL, episode metadata, Norders Spotify dates)*

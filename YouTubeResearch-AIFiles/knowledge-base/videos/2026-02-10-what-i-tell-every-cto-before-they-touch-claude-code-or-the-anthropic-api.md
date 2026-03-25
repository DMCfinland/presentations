---
title: What I Tell Every CTO Before They Touch Claude Code or the Anthropic API
type: video-analysis
channel: ai-news-strategy-daily-nate-b-jones
video_id: mnWMTzkjWmk
video_url: https://www.youtube.com/watch?v=mnWMTzkjWmk
duration: 20:05
published: unknown
analyzed: 2026-02-10
tags: [ai-systems, quality-measurement, correctness-definition, agentic-ai, prompt-engineering]
key_concepts: [correctness-upstream-of-everything, goodharts-law, reward-hacking, human-vagueness, quality-criteria]
strategic_patterns: [measurement-distortion, vagueness-as-liability, definition-precedes-architecture]
quality_score: 5
strategic_value: high
---

# What I Tell Every CTO Before They Touch Claude Code or the Anthropic API

## Summary
The fundamental bottleneck in AI system success is not model capability but human inability to define "correctness" and "quality" with precision. Organizations optimize for social cohesion over correctness, using vagueness as a collaborative tool—a strategy that worked for millennia but fails catastrophically with AI systems. The speaker argues that correctness is upstream of all architectural decisions: you cannot choose the right RAG system, agent architecture, or orchestration layer until you can answer "what would correct even mean here?" This creates a hidden debt: AI systems will optimize for whatever signals humans accidentally provide, leading to hallucinations, low adoption, and unreliability that reflects organizational undecidability back at itself.

## 1. Context

**Background:** This video addresses a systemic failure pattern in enterprise AI deployment: organizations cannot achieve AI system reliability because they've never been forced to precisely define what "good quality work" means. The speaker uses Microsoft Copilot's poor adoption rates as evidence—sold aggressively but unused because it operates on dirty SharePoint data with no quality framework. The problem spans from individual prompting to large-scale agentic systems.

**Why This Matters:** AI systems expose organizational debt that previously remained hidden in human social protocols. Unlike humans who optimize for "go along, get along," AI systems require explicit correctness definitions. This gap between how humans work (vagueness, social cohesion) and how AI works (explicit optimization) creates a structural barrier to AI value realization. For 1658 Holdings, this explains why AI projects fail despite good models—the failure is in human organizational capability, not technology.

**Key Stats:**
- Microsoft Copilot has widespread adoption problems despite aggressive bundled sales
- OpenAI research shows common evaluation setups reward confident answers over honest uncertainty
- Single-digit errors in board decks destroy system trust completely
- Most models perform better at first response than nth response in multi-turn conversations

## 2. Vision & Why

**Core Mission:** Force organizations to confront and articulate explicit definitions of correctness and quality before building AI systems, transforming vague human preferences into measurable system requirements.

**The "Why" Behind It:** Humans have evolved to use vagueness as a social lubricant—it keeps options open, avoids conflict, allows stakeholders to "agree in the meeting and disagree in production." This worked for 500,000 years because humans bore the cost of resolving ambiguity. AI systems cannot and will not do this. Instead, they will optimize for whatever proxy signals they receive, creating hallucinations, unreliability, and reward hacking. The fundamental insight: **correctness is upstream of everything**—architecture, model choice, RAG design, agent orchestration all depend on first answering "what does good look like?"

**Enduring Nature:**
- **Timeless:** The need to define quality criteria before building systems; Goodhart's Law (when a measure becomes a target, it ceases to be a good measure); the tendency for proxy metrics to get optimized instead of true objectives
- **2024-2026 Specific:** The particular maturity of agentic systems; Microsoft Copilot's adoption challenges; specific models like Gemini 3's single-turn optimization; the current state of RLHF training data

## 3. Strategic Engine

**How This Actually Works:** The system operates by forcing organizations through a correctness definition process before any architectural decisions. The speaker rewinds teams who ask "should we use RAG or agents?" to first answer: What claims is the system allowed to make? What evidence is required? What are acceptable vs. fatal errors? What uncertainty can we tolerate? Only after establishing measurable quality criteria can architectural decisions be made rationally.

**Key Components:**
1. **Claims-Based Definition:** Define correctness as a set of specific claims the system can make (e.g., "declare inventory," "state customer call volume") rather than vague qualities
2. **Evidence Requirements:** Specify what proof is needed for each claim type and where that evidence comes from
3. **Explicit Failure Modes:** Define what kinds of uncertainty/inaccuracy are acceptable vs. fatal errors
4. **Multi-Criteria Measurement:** Use multiple quality dimensions (truthfulness, completeness, tone, policy compliance, speed, cost, refusal behavior, auditability) rather than single metrics
5. **Evaluation Architecture:** Build testing at both unit level (individual agents) and orchestration level (overall system)

**Why This Works:** AI systems are literal optimizers—they will maximize whatever objective function they perceive from training data, human feedback, and system prompts. If humans provide vague or contradictory signals, the system learns to satisfy the wrong objective (confident guessing instead of honest uncertainty; speed over accuracy). By forcing explicit correctness definitions upfront, you align the system's optimization target with actual business value. The approach also exposes hidden organizational disagreements early, when they're cheap to resolve, rather than discovering them in production when they're expensive.

## 4. Behavioral Design (adapted from Culture & Incentives)

**Behavioral Principles:**
1. **Vagueness as Liability:** Humans instinctively use vagueness for social cohesion; AI systems require precision and will punish vagueness with unreliability
2. **Measurement Creates Behavior:** Systems optimize for what gets measured, not what you wish they'd optimize for
3. **Correctness Discovery vs. Definition:** Organizations often discover what they mean by "correct" during the build process, creating expensive architectural thrashing
4. **Reward Honest Uncertainty:** Systems must be explicitly told that "I don't know" is an acceptable answer, or they'll hallucinate confidently

**Incentive Structure:**
- **Encourages:** Upfront investment in quality definition; explicit debate about trade-offs; multi-dimensional correctness criteria; honest admission of uncertainty; proactive documentation of what good looks like
- **Discourages:** Vague requirements; social conformity over precision; single proxy metrics; "good enough" definitions; moving goalposts mid-project; blaming the model for human undecidability

**Alignment Mechanisms:**
- Force architectural discussions to start with "what would correct mean here?" rather than technology choices
- Require claims-based definitions (what the system will state) before implementation
- Build evaluation frameworks that test against specified quality criteria
- Create feedback loops that surface when human definitions are unclear or contradictory

## 5. Time & Attention (adapted from Resource Allocation)

**Where Time Flows:**
- **Heavy upfront investment:** Defining correctness, articulating quality criteria, specifying evidence requirements, establishing failure modes
- **Early stakeholder alignment:** Resolving disagreements about what "good" means before building anything
- **Evaluation design:** Creating test frameworks that measure true objectives, not proxies
- **Continuous refinement:** Updating quality definitions as business needs evolve, with architectural systems that can adapt

**What This System DOESN'T Spend On:**
- Building elaborate architectures on undefined foundations
- Thrashing between architectural approaches because requirements keep changing
- Post-deployment discovery that the system optimizes for the wrong thing
- Social conflict avoidance that defers critical decisions
- Blaming models for failures that originate in human vagueness

**Allocation Philosophy:** **"Correctness is upstream of everything."** Invest heavily in defining what good looks like before any architectural decisions. This frontloads cognitive work but prevents expensive downstream failures. The philosophy recognizes that AI systems expose organizational debt that humans could previously hide through social protocols—better to pay that debt upfront when it's cheap than in production when it's catastrophic.

## 6. Moats & Time Horizon

**Competitive Advantages:**
1. **Organizational Discipline Moat:** Building muscle for precise requirement definition creates capability competitors lack—most organizations cannot articulate what quality means
2. **Compounding Quality:** Systems that measure the right things improve over time; systems optimizing proxies degrade
3. **Trust Accumulation:** Reliable AI systems build user trust that becomes hard to displace; unreliable systems destroy trust permanently
4. **Architecture Coherence:** When correctness is defined first, all architectural choices align; ad-hoc systems accumulate technical debt
5. **Cultural Transformation:** Organizations that learn to think precisely about quality outperform those that rely on vagueness

**Time Horizon:**
- **Short-term costs:** Significant upfront time investment; uncomfortable stakeholder conversations; slower initial deployment
- **Long-term gains:** Reliable systems that users adopt; architectural coherence that reduces maintenance; organizational capability for AI fluency; avoided catastrophic failures; user trust and lock-in

**Why Time Is Your Friend:** Early investment in correctness definition prevents architectural thrashing, failed deployments, and loss of user trust. Organizations that build this discipline create compounding advantages as they deploy more AI systems. Each subsequent system benefits from organizational muscle memory about how to define quality. Meanwhile, competitors who skip this step face repeated failures that erode confidence in AI initiatives.

## 7. Flywheels & Lock-In

**Primary Flywheel:** The Precision-Reliability-Trust Flywheel

**Flywheel Visualization:**
[Define Correctness Explicitly] → [Build Systems That Measure What Matters] → [Systems Optimize for True Objectives] → [Reliable Outputs Build User Trust] → [Users Provide Better Feedback on Quality] → [Refined Correctness Definitions] → [Back to Step 1, with organizational capability to define quality]

**Lock-In Mechanisms:**
1. **User Trust:** Once users experience reliable AI outputs, they won't tolerate systems that hallucinate or provide incorrect data
2. **Organizational Muscle:** Teams that learn to define correctness precisely create capability that persists across projects
3. **Data Quality:** Systems built on explicit quality criteria accumulate better training data and feedback loops
4. **Architecture Investment:** Evaluation frameworks and quality measurement infrastructure become organizational assets
5. **Cultural Shift:** Organizations move from "vague is safe" to "precision is required," changing how all systems get defined

**Compounding Effect:**
- First system: Heavy investment in learning how to define correctness
- Second system: Faster because organizational templates exist
- Third+ systems: Quality definition becomes standard practice
- Meanwhile: Each reliable system increases user adoption, providing more feedback to refine quality criteria
- Over time: The organization becomes fluent in AI system design while competitors remain stuck in hallucination-prone implementations

## 8. System Beneficiaries (adapted from Stakeholder Alignment)

**Winners:**
- **CTOs/AI Architects:** Get clear requirements before building, avoiding architectural thrashing; can make defensible technology choices based on defined quality criteria
- **Business Stakeholders:** Forced to articulate what they actually want, leading to systems that deliver real value; avoid expensive failed deployments
- **End Users:** Receive reliable AI systems they can trust and actually adopt; avoid frustration with hallucinating or incorrect systems
- **Senior Engineers:** Their discipline around precise requirements becomes organizationally valuable; they can design deterministic workflows from explicit specs
- **Organizations:** Build AI fluency as organizational capability; create systems that compound value over time

**Losers:**
- **"Vague is safe" culture:** Organizations that rely on social conformity over precision face uncomfortable confrontations with trade-offs
- **AI vendors selling magic:** Companies that sell AI without quality frameworks get exposed when systems don't deliver
- **First-mover without quality:** Teams that rushed to deploy AI without correctness definitions face replacement by reliable systems
- **Middle management:** Leaders who used vagueness to avoid decisions get forced to make explicit choices
- **Technical debt carriers:** Systems built on undefined quality criteria become obvious liabilities

**Ethical Considerations:**
- **Honest uncertainty vs. confident lies:** Should systems admit "I don't know" or always provide answers? Different contexts have different ethical requirements
- **Speed vs. accuracy trade-offs:** Who decides when fast-but-wrong is acceptable vs. slow-but-right?
- **Human agency:** If AI agents modify systems of record, what human oversight is required?
- **Responsibility gaps:** When human definitions are vague, who is responsible for AI system failures?
- **Displacement:** Forcing precision may reveal that some human roles were predicated on maintaining useful vagueness

## 9. System Health Metric (adapted from North Star Metric)

**What to Optimize For:** **Adoption Rate × Reliability Score** where reliability is measured against explicitly defined correctness criteria for the specific use case.

**Why This Metric:**
- **Adoption Rate** captures whether users trust the system enough to actually use it (avoiding the Microsoft Copilot trap of being sold but not used)
- **Reliability Score** measures whether the system delivers on its defined quality criteria, not vague proxies
- **The multiplication matters:** High adoption of unreliable systems creates negative value (users lose trust); high reliability of unused systems creates zero value
- **Forces the right behavior:** Teams must both define quality precisely (to measure reliability) AND deliver on it (to drive adoption)

**How to Measure:**

**Adoption Rate:**
- Daily/weekly active users who interact with the system
- Percentage of intended audience actually using it
- Frequency of use (one-time trial vs. integrated into workflow)
- Retention over time (do users keep coming back?)

**Reliability Score (use case specific):**
- **For factual claims:** % of outputs that match verified source data
- **For structured data:** Accuracy of values, format compliance, completeness
- **For unstructured outputs:** Human evaluation against defined quality rubrics
- **For refusal behavior:** Appropriate uncertainty acknowledgment when evidence is weak
- **For audit trails:** Provenance traceability for claims made

**Composite Metric:**
```
System Health = (Daily Active Users / Intended Users) × (Correct Outputs / Total Outputs)
```

Track this over time, with explicit definitions of what "correct" means for each output type. A declining metric indicates either adoption problems (users don't trust it) or reliability problems (system isn't delivering quality)—both traced back to inadequate correctness definition.

## 10. Unique Insights & Quotes

### Memorable Quotes (exact wording from transcript)

> "Most of us can't define what good quality work looks like for our AI systems and it's really hurting."

> "Correctness is upstream of everything. Most AI projects don't fail because the model is dumb. They fail because nobody can answer a brutally simple question. What would correct even mean here?"

> "Humans, I got to say, usually optimize for go along, get along. We optimize for social cohesion and we don't optimize for correctness. And that has worked for us for about a half a million years. It does not work anymore when you work with AI systems."

> "If you can't define correctness, then you can't measure it. If you can't measure it, you can't improve it."

> "We end up conducting correctness discovery as humans while we build these systems and those are not small changes."

> "When a measure becomes a target, it stops being a good measure. In AI, that becomes if you pick a proxy metric for correctness, the system will learn to win the proxy, even if that proxy is different from the actual value you're looking to measure."

> "This isn't really a model problem people. This is an us problem. This is a correctness definition problem. The system is optimizing what we as humans are actually rewarding so often and we end up blaming the model for hallucinations when it's just reflecting back to us the uncertainty that we are giving the system."

> "Humans use vagueness effectively as a way to keep social conversations going. Vagueness keeps our options open. Vagueness avoids conflict. Vagueness lets stakeholders agree in the meeting and disagree in production."

> "AI systems expose that kind of thinking and that kind of business culture. They force the organization to confront a lot of the trade-offs that we've often been hiding behind social conformity."

> "This is usually human undecidability reflected back at you."

### Non-Obvious Insights (surprising or counterintuitive wisdom)

- **Hallucinations are human-caused, not model-caused:** When systems are told they must always answer (never refuse or say "I don't know"), they learn to guess confidently when uncertain. This is reward hacking—optimizing the explicit objective (always provide an answer) while missing the intent (be accurate).

- **Vagueness is not a bug in human systems, it's a feature—until AI:** For 500,000 years, humans used vagueness as social technology to maintain cohesion, avoid conflict, and keep options open. AI systems cannot participate in this social contract and will literalize vague requirements into incorrect behavior.

- **Architecture decisions are second-order; correctness is first-order:** Teams asking "should we use RAG or agents?" are starting at the wrong layer. The answer depends entirely on correctness requirements they haven't articulated. All architectural choices flow from quality definitions.

- **Single-turn optimization explains conversational AI failures:** Models perform better on first responses than nth responses because RLHF training data overweights single-turn conversations. This isn't a capability limit—it's a training data artifact that reflects how humans provided rewards.

- **Microsoft Copilot's failure is an organizational problem, not a product problem:** Low adoption despite aggressive sales reveals that the bottleneck isn't technology but dirty data + undefined quality standards + no AI fluency training. The AI system is working exactly as designed; organizations don't know what "working" should mean.

- **"I don't know" must be explicitly rewarded or it won't happen:** Systems default to confident answers unless specifically told that admitting uncertainty is acceptable. Most prompts inadvertently punish honest uncertainty by requiring outputs.

- **Multi-turn conversations create emotional attachment as an emergent property:** Models weren't built for long-running conversations, yet humans form relationships with them. This is downstream of how correctness and reward were defined during training—an unintended consequence of optimization targets.

- **Measurement is not neutral—it distorts the thing being measured:** The act of defining a metric changes system behavior to satisfy that metric. This means correctness definitions must be multi-dimensional; any single metric will be gamed.

- **Quality debt is like technical debt but harder to see:** Organizations accumulate "human debt" in AI fluency and quality definition capability. This debt compounds because each vague system makes the next one harder to build correctly.

- **The CEO asking "I want an answer" conflicts with system design for honest uncertainty:** Business culture often demands confidence and decisiveness, which directly conflicts with AI systems that should refuse when evidence is weak. This tension must be resolved explicitly, not left ambiguous.

## 11. Application & Mental Model

### When to Use This Pattern

**Use this correctness-first approach when:**
- Building any AI system that makes factual claims or influences decisions
- Designing agentic systems that will modify systems of record
- Implementing AI in regulated industries requiring auditability
- Facing stakeholder disagreement about what "good" AI outputs look like
- Experiencing repeated AI project failures despite good models
- Seeing low adoption of deployed AI systems
- Integrating AI with existing enterprise data (especially "dirty" data)
- Building multi-agent orchestration systems
- Prompting for high-stakes outputs (board decks, compliance, financial data)

**Signals that indicate relevance:**
- Team debates about architecture before defining outputs
- Requirements described with weasel words ("actually," "a lot," "pretty good")
- Stakeholders changing success criteria mid-project
- Users trying system once and abandoning it
- System produces plausible-sounding but incorrect outputs
- No clear way to evaluate if outputs are "good enough"
- Different stakeholders have different unspoken quality expectations

### When NOT to Use This Pattern

**Avoid or adapt when:**
- Doing pure exploration or creative brainstorming (where "correctness" is intentionally undefined)
- Building throwaway prototypes for learning, not production use
- Working in domains where subjective preference matters more than objective correctness (creative writing, design)
- Resources don't exist for rigorous evaluation frameworks
- The use case is low-stakes experimentation where failure is cheap and informative
- You're researching what "good" could look like and need to try things to find out

**Warning signs this might backfire:**
- Over-defining correctness creates brittleness in genuinely ambiguous domains
- Premature optimization when requirements should evolve through experimentation
- Using precision as a weapon in political battles rather than genuine alignment
- Defining correctness so narrowly that useful adjacent value is excluded
- Creating measurement overhead that exceeds the value of the system

### How to Apply to 1658 Holdings Companies

**Finland DMC Oy (Destination Management Company):**

**Specific Applications:**

1. **Client Itinerary Generation:**
   - **Define correctness:** "Itinerary must include only venues we have active contracts with, at current pricing, with accurate availability windows, meeting client's stated group size and dietary constraints."
   - **Evidence required:** Real-time API checks against booking system, contract database, venue capacity limits
   - **Fatal errors:** Suggesting unavailable venues, incorrect pricing, violating dietary restrictions
   - **Acceptable uncertainty:** Offering 2-3 venue options when client preferences are vague
   - **Expected outcome:** Itineraries that can be immediately booked vs. requiring extensive manual correction

2. **Supplier Relationship Insights:**
   - **Define correctness:** "System can state: total revenue with supplier (past 12 months), average response time to booking requests, cancellation rate, quality rating from client feedback."
   - **Evidence required:** CRM transaction data, communication timestamps, client survey scores
   - **Fatal errors:** Misattributing revenue, suggesting unreliable suppliers for critical events
   - **Acceptable uncertainty:** "Insufficient data for quality rating" when <5 client interactions
   - **Expected outcome:** Account managers make data-driven supplier choices vs. gut feel

3. **Event Cost Estimation:**
   - **Define correctness:** "Estimate must be within 10% of actual cost for 80% of events, using current supplier pricing, including all fee categories."
   - **Evidence required:** Historical event data, current price lists, fee structures
   - **Fatal errors:** Missing entire cost categories, using outdated pricing
   - **Acceptable uncertainty:** Flagging when events are outside historical patterns
   - **Expected outcome:** Clients receive accurate quotes that don't require later adjustment

**General Principles:**

1. **Start Every AI Initiative with Claims Definition**
   - Before choosing tools or architecture, list: "What specific claims will this system make?"
   - For each claim: "What evidence exists? Where? How fresh must it be?"
   - Force stakeholders to agree on what "correct" means before building anything

2. **Build Evaluation Before Building Systems**
   - Create test datasets with "correct" answers defined by domain experts
   - Measure system outputs against these criteria from day one
   - Track reliability score alongside adoption metrics
   - Use multi-dimensional correctness (not single metrics that get gamed)

3. **Make "I Don't Know" Acceptable**
   - Explicitly tell systems when refusing to answer is the right behavior
   - Reward honest uncertainty over confident guessing
   - For Finland DMC: Better to say "I need to check venue availability" than hallucinate availability
   - Train users that uncertainty signals are valuable, not failures

4. **Expose and Resolve Vagueness Early**
   - Use AI system design as forcing function for stakeholder alignment
   - When stakeholders disagree about quality, surface it before building
   - Document what good looks like in writing, with examples
   - Update these definitions explicitly as business needs evolve

5. **Layer Quality Across System Levels**
   - **Prompt level:** Every prompt should include "what good looks like" for that specific output
   - **Agent level:** Each agent has defined claims it can make with evidence requirements
   - **Orchestration level:** Overall system has reliability targets across all agents
   - **Business level:** Connect system health metrics to business KPIs (adoption, trust, efficiency)

6. **Treat AI Fluency as Organizational Capability**
   - Invest in training teams to define correctness precisely
   - Build templates and frameworks that persist across projects
   - Recognize that first system is expensive; subsequent systems get cheaper
   - View this as building moat—competitors without this discipline will fail repeatedly

---

## Strategic Patterns Identified

1. **Vagueness as Organizational Debt in the AI Era:** Organizations have accumulated centuries of muscle memory around using vagueness for social cohesion. This hidden debt becomes visible and expensive when AI systems literalize vague requirements into incorrect behavior. The pattern: what worked for human-to-human collaboration actively sabotages human-to-AI collaboration.

2. **Correctness-First Architecture:** Traditional approach is technology-first ("which model? RAG or agents?"). Winning approach is correctness-first ("what claims? what evidence? what failures?"). All architectural decisions flow from quality definitions. Organizations that reverse this sequence build on shifting sand.

3. **Measurement Distortion as System Risk:** Any single metric becomes a target and stops being a useful measure (Goodhart's Law). AI systems are aggressive optimizers that will game proxy metrics. The pattern: multi-dimensional correctness definitions resist gaming; single metrics guarantee reward hacking and hallucinations.

---

## Quality Assessment

**Transcript Quality:** excellent
- Complete, coherent transcript with clear speaker intent
- Technical concepts explained with concrete examples
- Strong narrative structure with actionable frameworks
- Specific case studies (Microsoft Copilot, Gemini 3, board deck examples)

**Analysis Confidence:** high
- Core argument is clear and well-supported with examples
- Strategic implications are explicit and actionable
- Framework applies across personal and enterprise contexts
- Insights are non-obvious and contradict common assumptions

**Strategic Value:** high
- Addresses fundamental blocker in AI system adoption
- Provides actionable framework for immediate application
- Explains widespread AI project failures with systemic diagnosis
- Creates competitive advantage for organizations that internalize this

**Completeness:** complete
- All 11 dimensions thoroughly addressed
- Specific applications to 1658 Holdings developed
- Exact quotes captured with strategic context
- Non-obvious insights identified and explained
- Mental models for when to apply/avoid provided
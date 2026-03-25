---
title: Master Perplexity Prompting -- Why It's Different from ChatGPT + Demo
type: video-analysis
channel: ai-news-strategy-daily-nate-b-jones
video_id: 05RRGiF7QC0
video_url: https://www.youtube.com/watch?v=05RRGiF7QC0
duration: 20:22
published: 2024
analyzed: 2026-02-10
tags: [perplexity, search-ai, rag-architecture, prompting-strategies, internet-search, hallucination-prevention]
key_concepts: [retrieval-augmented-generation, parametric-vs-rag, epistemological-architecture, progressive-deepening, verification-loops]
strategic_patterns: [tool-specialization, architectural-constraints-enable-strengths, two-tool-verification]
quality_score: 5
strategic_value: high
---

# Master Perplexity Prompting -- Why It's Different from ChatGPT + Demo

## Summary
Perplexity represents a fundamentally different epistemological architecture than ChatGPT: it's a RAG (Retrieval Augmented Generation) search engine that looks outward to the internet by default, while ChatGPT is a parametric answer engine that looks inward to its training data. This architectural difference demands distinct prompting strategies—shorter prompts with critical context, explicit multi-perspective demands, progressive deepening through conversation, and careful attention to date filtering and source diversity. The strategic insight is that as LLMs become more fluent, the gap between fluency and factuality widens, making Perplexity's accountability architecture (transparent sourcing) increasingly essential for internet-first use cases like competitive intelligence, financial analysis, and real-time research.

---

## 1. Context

**Background:** 
Nate B Jones demonstrates how to effectively use Perplexity AI for internet searching, contrasting it with both Google (traditional search) and ChatGPT (parametric LLM). He explains that Perplexity uses retrieval augmented generation (RAG) as its fundamental architecture, meaning it retrieves relevant documents from the internet, extracts paragraphs, and uses this information to craft answers with citations. The "research mode" employs "agentic RAG" which performs dozens of searches, reads hundreds of sources, and does multiple passes to ensure comprehensive answers.

**Why This Matters:** 
For business leaders, understanding when to use Perplexity versus ChatGPT is critical for information quality and decision-making velocity. Perplexity excels at internet-first use cases (competitive intelligence, market research, real-time news) while ChatGPT excels at reasoning and synthesis. The distinction between "looking outside" (Perplexity) and "looking inside training data" (ChatGPT) has strategic implications for how companies structure their AI workflows, particularly as the knowledge recency problem intensifies—LLM training data gets out of date too fast for rapidly evolving domains.

**Key Stats:**
- Research mode performs "dozens of searches" and reads "hundreds of sources"
- Standard perplexity prompts are "much shorter than chat GPT prompts"
- Just "two to three words of critical context can dramatically improve the value of relevant results"
- Weekly Claude Code users in Korea increased significantly (noted as discovery from search)

---

## 2. Vision & Why

**Core Mission:** 
Perplexity aims to create an AI-native search engine that provides verifiable, cited answers from the internet rather than relying solely on pre-trained knowledge. It's building an "accountability architecture" where every claim is sourced and can be verified, addressing the growing "gap between fluency and factuality" as LLMs become more convincingly confident.

**The "Why" Behind It:**
Three fundamental problems drive Perplexity's approach:
1. **Knowledge Recency Problem**: "LLM training data gets out of date too fast. AI knowledge is adding to our understanding of the world very quickly."
2. **Verification Crisis**: As LLMs get "better at sounding confident," we need systems that separate fluency from factuality
3. **Parametric Limitations**: ChatGPT "does not go out and look at the internet by default"—it can't tell you about new ChatGPT instances because it looks inside its weights first

**Enduring Nature:**
**Timeless principles:**
- The need for transparent sourcing in knowledge systems
- The distinction between reasoning (parametric) and fact-retrieval (RAG) capabilities
- Progressive deepening through conversation for discovery
- Two-tool verification loops for quality assurance

**2024-2026 specific:**
- Specific models mentioned (GPT-5 Pro, Claude, Sora 2)
- Current state of RAG vs. parametric architectures
- Particular features like "research mode" and "spaces"

---

## 3. Strategic Engine

**How This Actually Works:**

Perplexity's RAG architecture operates as follows:
1. External documents across the internet are embedded and stored
2. Every query triggers a fresh retrieval of relevant documents
3. In standard mode: retrieves documents → extracts paragraphs → synthesizes with citations
4. In research mode (agentic RAG): performs dozens of searches → reads hundreds of sources → multiple passes → comprehensive synthesis

The key differentiation: "Chat GPT's default is to go and look inside its own training data and its weights in the model for an answer for your question. It does not go out and look at the internet by default."

**Key Components:**

1. **RAG Foundation**: Real-time internet retrieval with citation transparency
2. **Research Mode**: Agentic search with multi-pass verification ("turns effort level up to 11")
3. **Focus Modes**: Academic (peer-reviewed sources), Social, Finance—constrains search domain strategically
4. **Spaces & Labs**: Standing instructions for repeated workflows (Spaces) and polished reports (Labs)
5. **Progressive Threading**: Conversational deepening where each answer opens new exploration paths

**Why This Works:**

The architecture succeeds because it solves for **verifiability** not just **plausibility**. As Nate explains: "Chat GPT will say, I believe this is true based on patterns. That is one of the roots of hallucination in LLMs. They want to be helpful. They have parametric patterns in their data and they just do that instead of searching or using tools. Perplexity says these sources claim this. I found the sources. Here are the sources. You figure it out."

---

## 4. Behavioral Design

**Behavioral Principles:**

1. **Specificity Over Length**: "On average, perplexity prompts are much shorter than chat GPT prompts" but require precise context
2. **Explicit Multi-Perspective Demands**: Don't trust convergence—force the system to find disagreement
3. **Progressive Deepening**: Start broader than you would with ChatGPT, then iteratively drill down
4. **Two-Tool Verification**: Use ChatGPT to check Perplexity's work and vice versa
5. **Source Skepticism by Default**: "Never trust single source answers"

**Incentive Structure:**

The system encourages:
- **Precision in constraints**: "Don't be vague about matters that are in the API" (date filters, source limits)
- **Triangulation over synthesis**: "Compare findings from at least three peer-reviewed studies...ensure that you note conflicts in conclusions"
- **Manual verification**: "Please make sure you go to the cited source and search for the phrase"

The system discourages:
- **Few-shot prompting**: "Perplexity will overindex on those examples and dredge up only things related to those examples"
- **Vague parameters**: "Only search recent sources" is less helpful than specific date filters
- **Single-pass acceptance**: Always verify quotes in original sources

**Alignment Mechanisms:**

1. **Output Constraints**: "Please provide evidence. For every claim you make here, please list specific section references or page numbers so I can check your work"
2. **Academic Mode Toggle**: Forces peer-reviewed sources (PubMed, Semantic Scholar) to reduce AI-generated spam
3. **Citation Transparency**: Every claim is linked to source, creating accountability trail
4. **Focus Mode Switching**: Can force "reset of the model's thinking" mid-conversation to escape ruts

---

## 5. Time & Attention

**Where Time Flows:**

In Perplexity workflows, time is allocated to:
1. **Crafting precise initial queries** with 2-3 critical context words rather than elaborate prompts
2. **Progressive deepening** through follow-up questions rather than comprehensive first prompts
3. **Source verification** and cross-checking with second LLM
4. **Setting up Spaces** with standing instructions for repeated workflows

The surprising insight: "Just adding two to three words of critical context can dramatically improve the value of relevant results" versus ChatGPT where you need structured, comprehensive initial prompts.

**What This System DOESN'T Spend On:**

- **Elaborate prompt engineering**: Shorter prompts work better
- **Few-shot examples**: These backfire by constraining search scope
- **Reasoning synthesis**: Perplexity fetches, ChatGPT reasons—don't confuse their roles
- **Static knowledge bases**: RAG updates continuously, eliminating retraining cycles

**Allocation Philosophy:**

"Treat perplexity like a conversation where you are starting with a root question to explore and every answer opens up new questions that you can thread." The philosophy is **discovery through progressive specificity** rather than **comprehensive specification upfront**.

Time allocation shifts from prompt crafting (front-loaded) to verification and threading (distributed across conversation).

---

## 6. Moats & Time Horizon

**Competitive Advantages:**

1. **Architectural Moat**: RAG architecture that "looks outside" vs. parametric models that "look inside" creates fundamental differentiation that's hard to replicate without rebuilding core infrastructure
2. **Fresh Knowledge Access**: "You can actually update a rag knowledge base like perplexity has multiple times a day" versus retraining cycles for LLMs
3. **Accountability Architecture**: Transparent sourcing creates trust that fluency alone cannot match
4. **Agentic Research Mode**: "Dozens of searches, hundreds of sources, multiple passes" creates quality differential
5. **Internet-Native Integration**: Purpose-built for web search rather than retrofitted

**Time Horizon:**

**Short-term benefits:**
- Immediate access to current information (last few weeks/days)
- Faster verification through cited sources
- Better results for competitive intelligence, news, market research

**Long-term compound effects:**
- As "the gap between fluency and factuality widens" (LLMs get more convincing but not necessarily more accurate), Perplexity's verification approach becomes more valuable
- Spaces and standing instructions create institutional knowledge
- Learning which queries work builds organizational capability
- Two-tool verification habits compound quality over time

**Why Time Is Your Friend:**

The fundamental bet: "As LLM get better at sounding confident, we need something like perplexity more because the gap between fluency and factuality widens." The more convincing LLMs become, the more essential verified, sourced information becomes. Perplexity's architecture is positioned for a world where confidence ≠ correctness.

---

## 7. Flywheels & Lock-In

**Primary Flywheel:**

Perplexity's search quality flywheel operates differently than traditional platforms:

**Flywheel Visualization:**
[User asks precise, context-rich query] → [RAG retrieves diverse, recent sources] → [User learns to verify and refine] → [Spaces capture successful patterns] → [Standing instructions reduce friction] → [User discovers non-obvious insights] → [User trusts system more] → [User asks MORE precise queries with BETTER context] → [Stronger results, stronger lock-in]

**Lock-In Mechanisms:**

1. **Learned Query Patterns**: Users develop "muscle memory" for effective Perplexity prompting (different from ChatGPT)
2. **Spaces Infrastructure**: Standing instructions and project spaces create switching costs
3. **Verification Workflows**: Two-tool verification loops become institutionalized
4. **Discovery History**: Progressive threading builds unique exploration paths that can't be replicated elsewhere
5. **Trust Accumulation**: Each verified source builds confidence in the system's accountability architecture

**Compounding Effect:**

The more you use Perplexity:
- The better you understand when to use focus modes strategically
- The more refined your "critical context words" become
- The stronger your Spaces templates become for repeated workflows
- The more you trust (but verify) the citation system
- The better you get at progressive deepening conversations

As Nate demonstrates: First query (vague) → poor results → Second query (specific, constrained) → rich, surprising discoveries (Korea Claude Code culture) → Third query (targeted follow-up) → deep insight into unexpected domain.

---

## 8. System Beneficiaries

**Winners:**

1. **Researchers & Analysts**: Get real-time information with citations for verification
2. **Competitive Intelligence Teams**: Can track market developments with transparent sourcing
3. **Content Creators**: Discover "corners of the world that you didn't expect" for unique angles
4. **Compliance-Sensitive Organizations**: Transparent sourcing reduces liability vs. hallucinated claims
5. **Financial Analysts**: Real-time market data with verifiable sources (Finance focus mode)
6. **Builders/Developers**: Stay current on rapidly evolving AI tooling and infrastructure

**Losers:**

1. **Those Who Want Reasoning Over Facts**: Perplexity "isn't necessarily focused on reasoning first"—ChatGPT wins there
2. **Low-Information-Quality Tolerance Users**: The verification overhead may not be worth it for casual queries
3. **Static Knowledge Workers**: If your domain doesn't change rapidly, parametric models may suffice
4. **SEO-Dependent Publishers**: As Perplexity synthesizes sources, original publishers may lose traffic
5. **AI Content Farms**: Perplexity "will site AI generated spam because it cannot tell the difference"—though academic mode mitigates this

**Ethical Considerations:**

1. **Attribution vs. Traffic**: Perplexity cites sources but may reduce click-through to original publishers
2. **AI Spam Vulnerability**: "Sometimes the AI generated source is correct and sometimes it's wrong. But perplexity can't tell either way."
3. **Verification Burden**: System pushes verification responsibility to users—"You figure it out"
4. **Quality Gatekeeping**: Academic mode helps, but what about domains without peer review infrastructure?
5. **Quote Accuracy**: "Perplexity describes a quote. Please make sure you go to the cited source and search for the phrase. It is often there, but it may not be there verbatim."

---

## 9. System Health Metric

**What to Optimize For:**

**Source Diversity × Verification Rate**

The core metric should be: **(Number of distinct, reputable sources cited per query) × (Percentage of claims user verifies)**

This captures both:
1. Whether the system is actually triangulating (not converging on single source)
2. Whether users are engaging with the accountability architecture (not just trusting blindly)

**Why This Metric:**

Single metrics fail to capture Perplexity's unique value:
- Pure "answer quality" doesn't capture verification advantage
- "Source count" alone doesn't ensure diversity or quality
- "User satisfaction" doesn't ensure they're verifying

The combined metric ensures:
- System is leveraging its RAG architecture effectively (diversity)
- Users are using the tool correctly (verification)
- The accountability architecture is actually functional (not decorative)

As Nate emphasizes: "Never trust single source answers" and "there is really no substitute for that double LLM check."

**How to Measure:**

**For Organizations:**
1. **Source Diversity Score**: Track unique domains cited per 100 queries
2. **Verification Rate**: Monitor click-through to cited sources (requires logging)
3. **Second-Tool Verification**: Track frequency of ChatGPT/Claude cross-checks
4. **Academic Mode Usage**: Percentage of high-stakes queries using academic focus
5. **Quote Verification**: Sample rate of users checking verbatim quotes in source

**For Individuals:**
- Keep verification log: Which claims did you check? What percentage verified?
- Track your "surprise discovery rate": How often do results reveal non-obvious insights?
- Monitor your refinement pattern: Are you learning to ask better initial queries?

**Red Flags:**
- Accepting single-source answers without skepticism
- Never using academic mode for important queries
- Not verifying direct quotes in source documents
- Treating Perplexity output as interchangeable with ChatGPT

---

## 10. Unique Insights & Quotes

### Memorable Quotes

> "Chat GPT's default is to go and look inside its own training data and its weights in the model for an answer for your question. It does not go out and look at the internet by default."

> "Just adding two to three words of critical context can dramatically improve the value of relevant results."

> "Perplexity will overindex on those examples and dredge up only things related to those examples from your fshot prompt."

> "Chat GPT will say, I believe this is true based on patterns. That is one of the roots of hallucination in LLMs. They want to be helpful. They have parametric patterns in their data and they just do that instead of searching or using tools. Perplexity says these sources claim this. I found the sources. Here are the sources. You figure it out."

> "As LLM get better at sounding confident, we need something like perplexity more because the gap between fluency and factuality widens."

> "That's how perplexity works. It's very different from Google, right? Because Google just finds you an answer. But what is less understood is that it's also very different from chat GPT."

> "On average, perplexity prompts are much shorter than chat GPT prompts."

> "Treat perplexity like a conversation where you are starting with a root question to explore and every answer opens up new questions that you can thread."

> "There is really no substitute for that double LLM check. And you can use chat GPT to check perplexity's work and you can also use perplexity to check chat GPT's work."

> "Perplexity may not be perfect but it has an accountability architecture. Rag allows you to create verifiable chains of reasoning through transparent sourcing."

### Non-Obvious Insights

- **Architectural Epistemology Matters**: The distinction isn't "better" or "worse"—it's fundamentally different epistemological architectures (parametric vs. RAG) that demand different use cases and prompting strategies. This is a strategic tool selection issue, not a quality hierarchy.

- **Few-Shot Backfires in RAG**: The same technique (few-shot prompting) that improves ChatGPT results actively degrades Perplexity results by constraining search scope. What works in parametric models fails in retrieval architectures.

- **Shorter is Stronger for Search**: Counterintuitively, "perplexity prompts are much shorter than chat GPT prompts" but achieve better results for search tasks. The system needs constraint, not elaboration.

- **Focus Mode as Strategic Reset**: You can switch focus modes mid-conversation "to force a reset of the model's thinking when you are trying to get it out of a rut"—this is unique to RAG architectures where you're redirecting search strategy, not context window.

- **Verification Creates Two Flywheels**: Using ChatGPT to verify Perplexity AND using Perplexity to verify ChatGPT creates two orthogonal quality flywheels. The tools check each other's blind spots (reasoning vs. facts).

- **Progressive Deepening vs. Comprehensive Specification**: The optimal Perplexity strategy is opposite to ChatGPT—start broader than you would with ChatGPT, then thread deeper, rather than front-loading comprehensive context.

- **The Recency Moat Widens**: "LLM training data gets out of date too fast" but "you can actually update a rag knowledge base like perplexity has multiple times a day"—this gap widens as AI knowledge accelerates, making RAG architectures increasingly strategically valuable.

- **Spaces as Institutional Memory**: Spaces with standing instructions create "internet first project space that perplexity excels at"—this is organizational capability building, not just tool usage. It's capturing search patterns as institutional knowledge.

- **The Fluency-Factuality Gap is the Core Problem**: As LLMs get "better at sounding confident," the systemic risk increases. Perplexity's accountability architecture becomes more valuable precisely because other AI gets more convincing, not despite it.

- **Quote Attribution is Fuzzy**: Even with citations, "it may not be there verbatim. It may be in a different format, and it may not have the connotation in context that perplexity is suggesting in its synthesis." Verification isn't binary—it requires interpretation.

---

## 11. Application & Mental Model

### When to Use This Pattern

**Use Perplexity (RAG architecture) when:**

1. **Knowledge Recency Matters**: Information from last days/weeks/months is critical (competitive intelligence, market research, current events)
2. **Verification is Non-Negotiable**: Stakes are high and you need transparent sourcing (financial analysis, legal research, medical information)
3. **Discovery Over Synthesis**: You're exploring "corners of the world you didn't expect" rather than synthesizing known information
4. **Internet-Native Tasks**: Competitive intelligence, equity analysis, news aggregation, builder/developer tool research
5. **Multi-Perspective Requirements**: You need triangulation from diverse sources, not coherent synthesis
6. **Real-Time Data**: Tracking rapidly evolving domains where training data goes stale quickly

**Signals this approach is relevant:**
- You find yourself saying "What's new with X?"
- You need to cite sources for claims
- The domain changes faster than model retraining cycles
- You want to verify an LLM's confident-sounding claim
- You're researching competitors or market movements

### When NOT to Use This Pattern

**Use ChatGPT/Claude (parametric architecture) when:**

1. **Reasoning Over Facts**: You need logical analysis, synthesis, or creative generation more than current facts
2. **Static Knowledge Domains**: Historical analysis, established frameworks, mathematical reasoning
3. **Coherent Synthesis Required**: You want unified perspective, not source diversity
4. **Private/Proprietary Data**: Working with internal documents or sensitive information
5. **Creative Tasks**: Writing, brainstorming, code generation from known patterns
6. **Low-Stakes Speed**: Quick answers where verification overhead isn't justified

**Signals this approach would backfire:**
- You need deep reasoning chains, not facts
- The domain is well-established and stable
- You want creative synthesis, not source triangulation
- Verification overhead exceeds value of answer
- You're working with non-public information

**Avoid Perplexity for:**
- Complex reasoning tasks (use ChatGPT with o1/o3)
- Creative writing (parametric models excel)
- Private document analysis (use ChatGPT with file upload)
- Historical analysis where sources are established
- Tasks where you want confident synthesis over source diversity

### How to Apply to 1658 Holdings Companies

**Finland DMC Oy (Destination Management):**

1. **Competitive Intelligence Workflow**
   - Create a Space called "Nordic DMC Intelligence" with standing instruction: "Structure all responses as: Current State (offerings/pricing), Competitive Positioning (our differentiation), Emerging Threats (new entrants/models), Strategic Implications (recommended responses)"
   - Weekly research mode queries: "Please find me a diverse set of well-grounded novel updates on Nordic destination management and tourism since [date], specifically focused on corporate travel and DMC services in Finland, Sweden, Norway"
   - Expected outcome: Real-time awareness of competitive moves, pricing changes, new market entrants

2. **Client Trend Monitoring**
   - Monthly query: "Compare findings from at least three industry reports on corporate travel trends in Europe, published since [date], and ensure you note conflicts in conclusions that are relevant for understanding post-pandemic business travel behavior"
   - Filter by date: Last 3 months only
   - Focus mode: Academic or Finance (for reputable travel industry analysis)
   - Expected outcome: Anticipate client needs before competitors

3. **Supplier & Partner Discovery**
   - Use progressive deepening: Start with "What are emerging trends in Nordic hospitality and venue partnerships?" → Discover surprising data point → "Can you please summarize a diverse set of perspectives around [specific trend]?"
   - Expected outcome: Discover non-obvious partnership opportunities

4. **Crisis Monitoring**
   - Standing Space: "Nordic Travel Disruptions" with instruction to prioritize government sources, major news outlets, and travel advisories
   - Daily checks during peak season: "Recent travel disruptions, cancellations, or safety issues affecting Finland, Sweden, Norway since [yesterday's date]"
   - Expected outcome: Proactive client communication before they hear from other sources

**General Principles for 1658 Holdings Portfolio:**

1. **Two-Tool Verification for Major Decisions**
   - Use Perplexity for fact-gathering and current intelligence
   - Use ChatGPT/Claude to synthesize findings and stress-test reasoning
   - Never act on single-tool output for high-stakes decisions
   - Example workflow: Perplexity finds competitive intelligence → ChatGPT analyzes strategic implications → Perplexity verifies specific claims → Final decision

2. **Spaces as Institutional Knowledge**
   - Create standing Spaces for recurring workflows (competitive intelligence, market research, supplier monitoring)
   - Document successful query patterns as institutional knowledge
   - Train team members on progressive deepening technique rather than comprehensive prompts
   - Expected outcome: Organizational capability that compounds over time

3. **Academic Mode for High-Stakes Research**
   - When researching regulatory changes, market data, or client-facing claims, default to Academic focus
   - Reduces AI-generated spam risk
   - Creates citation trail for audit purposes
   - Expected outcome: Higher quality, verifiable information for critical decisions

4. **Strategic Time Allocation**
   - Spend less time on elaborate prompts, more time on verification and threading
   - Invest in learning "critical context words" that dramatically improve results
   - Build two-tool verification habits rather than relying on single source
   - Expected outcome: Better decisions through verification, not just faster answers

5. **Know When to Switch Tools**
   - Perplexity for: "What's happening in [market/competitor space]?" "What are current [trends/practices]?" "Recent developments in [domain]?"
   - ChatGPT for: "Analyze these findings..." "What are strategic implications of..." "Generate a framework for..."
   - Don't use Perplexity for reasoning, don't use ChatGPT for real-time facts
   - Expected outcome: Right tool for right job, not default to favorite

---

## Strategic Patterns Identified

1. **Architectural Constraints Enable Strengths**: Perplexity's RAG architecture isn't "better" than ChatGPT's parametric approach—it's specialized. The constraint (must retrieve from internet) enables the strength (always current, always sourced). This is a general pattern: architectural constraints that seem limiting actually enable unique capabilities. Strategic implication: Don't chase "general purpose" AI—specialize tools for specific epistemological architectures.

2. **Two-Tool Verification Loops**: Using two orthogonal AI systems (parametric + RAG) to check each other creates quality assurance neither achieves alone. ChatGPT checks Perplexity's reasoning, Perplexity checks ChatGPT's facts. This is a specific instance of the general pattern: **systems with different failure modes provide mutual correction**. Strategic implication: Build complementary tool pairs, not redundant tool stacks.

3. **The Fluency-Factuality Gap as Moat**: As LLMs get more convincing (fluency ↑), the need for verification infrastructure increases (factuality becomes scarcer). Perplexity's accountability architecture becomes MORE valuable as competing LLMs become MORE fluent. This is **counter-positioning**: the strength of competitors (fluency) creates the gap that enables your differentiation (verifiable sourcing). Strategic implication: Look for areas where competitor's core strength creates adjacent weakness you can own.

---

## Quality Assessment

**Transcript Quality:** excellent
- Complete sentences, clear structure, minimal errors
- Technical concepts explained accessibly
- Concrete examples throughout (Korea Claude Code discovery)
- Demonstrates concepts live (poor query → good query comparison)

**Analysis Confidence:** high
- Clear architectural distinctions well-articulated
- Practical prompting strategies with rationale
- Honest about limitations (hallucination risks, verification burden)
- Demonstrates expert usage patterns in real-time

**Strategic Value:** high
- Fundamental tool selection framework (parametric vs. RAG)
- Non-obvious prompting strategies that reverse ChatGPT habits
- Clear applications to business use cases (competitive intelligence, research)
- Addresses critical future trend (fluency-factuality gap)

**Completeness:** complete
- Covers architecture, prompting strategies, verification, use cases, limitations
- Provides both conceptual framework and tactical examples
- Demonstrates concepts rather than just describing them
- Addresses "when NOT to use" as thoroughly as "when to use"
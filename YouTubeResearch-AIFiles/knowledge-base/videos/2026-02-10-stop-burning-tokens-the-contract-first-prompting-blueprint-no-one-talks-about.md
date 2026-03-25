---
title: Stop Burning Tokens: The Contract-First Prompting Blueprint No One Talks About
type: video-analysis
channel: ai-news-strategy-daily-nate-b-jones
video_id: i4Jfl1IW-_U
video_url: https://www.youtube.com/watch?v=i4Jfl1IW-_U
duration: 09:28
published: unknown
analyzed: 2026-02-10
tags: [prompt-engineering, intent-clarity, contract-first-prompting, llm-efficiency, token-optimization]
key_concepts: [contract-first-prompting, intent-clarification, token-efficiency, human-ai-collaboration, structured-questioning]
strategic_patterns: [intent-before-execution, progressive-clarification, mutual-agreement-protocols]
quality_score: 5
strategic_value: high
---

# Stop Burning Tokens: The Contract-First Prompting Blueprint No One Talks About

## Summary
Nate B Jones introduces "contract-first prompting," a novel approach to LLM interaction that prioritizes establishing clear mutual understanding before work begins. Rather than asking LLMs to generate clarifying questions ad-hoc, this technique creates a structured protocol where the LLM systematically identifies gaps, asks targeted questions until reaching 95% confidence, and requires explicit user approval before proceeding. The method acknowledges that humans bring tremendous context but poor articulation, positioning the LLM as a collaborative partner in extracting and clarifying intent rather than a passive executor of vague instructions.

## 1. Context

**Background:** The video addresses the fundamental failure mode in LLM prompting: almost every failed prompt fails because intent wasn't clearly communicated. Human language is "really rough on intent" because individuals bring extensive domain expertise, passion, energy, and experience to tasks but struggle to convey this richness in words. Even experienced prompters like Nate struggle with getting intent across effectively. The common solution—asking LLMs to ask clarifying questions—is described as "scattershot" and "unprofessional" because it gives the LLM free reign in a "sea of ambiguity" without parameters or structure.

**Why This Matters:** For business leaders and 1658 Holdings, this represents a massive efficiency opportunity. Token waste from unclear prompts translates directly to cost, time, and quality degradation. More critically, it creates a capability gap: organizations cannot leverage AI for complex, high-value work if they cannot reliably communicate intent. The contract-first approach provides a repeatable protocol for extracting value from AI systems, particularly for ambiguous, early-stage work where requirements are emerging rather than fully formed.

**Key Stats:**
- Target: 95% confidence threshold before work begins
- Example: 500-word summary (deliberately short to increase difficulty)
- Tested domains: Historical analysis (Balkans since 1660), software PRDs (multi-platform comment centralization)
- Result: Multiple rounds of clarifying questions that identified non-obvious constraints (political entity naming conventions, scope boundaries)

## 2. Vision & Why

**Core Mission:** To establish a reliable protocol for achieving shared understanding between humans and LLMs before work begins, acknowledging human limitations in articulating intent while leveraging LLM capabilities for structured clarification.

**The "Why" Behind It:** The approach recognizes three fundamental truths:
1. Humans have vague ideas backed by tremendous context and experience
2. Human language is inherently poor at conveying intent clearly
3. The traditional prompt-then-iterate cycle wastes tokens, time, and cognitive energy

The contract-first method treats the LLM as an active partner in intent extraction rather than a passive recipient of instructions. It's designed for "humans as humans"—imperfect, incomplete, but contextually rich.

**Enduring Nature:**
- **Timeless:** The need for shared understanding before work begins (borrowed from software engineering's service contracts and agreements); human difficulty in articulating tacit knowledge; the value of structured questioning over ad-hoc exploration
- **Time-bound to 2024-2026:** Specific LLM capabilities for meta-reasoning about intent; token costs as primary constraint; current state of LLM reliability requiring explicit verification

## 3. Strategic Engine

**How This Actually Works:** 
The system creates a three-phase protocol:
1. **Gap Identification (Step 0):** LLM silently scans initial input and lists every fact or constraint still needed
2. **Progressive Clarification (Step 1):** LLM asks one question at a time, digging into examples like purpose, audience, facts, success criteria, length, tech stack, edge cases, risk tolerance—but not limited to these
3. **Echo Check:** When LLM thinks it's close, it replies with a crisp sentence stating the deliverable, something it knows it needs to include, and a hard constraint

**Key Components:**
1. **Mission Statement:** "Your goal is to turn my rough idea into a very clear work order"
2. **Confidence Threshold:** Explicit target of 95% confidence before proceeding
3. **Structured Question Framework:** Suggested dimensions (purpose, audience, facts, etc.) without being prescriptive
4. **User Control Interface:** Mini-program with explicit options (yes/lock, edit, blueprint, risks, reset)
5. **Domain-Specific Instructions:** Special handling for code review, document verification

**Why This Works:** 
- **Externalizes cognitive load:** Puts the burden of question generation on the LLM, which has systematic coverage capabilities humans lack
- **Creates feedback loops:** Each answer narrows the possibility space, improving subsequent questions
- **Prevents premature execution:** Forces validation before work begins, avoiding costly rework
- **Leverages LLM strengths:** Pattern matching, systematic thinking, question generation—while compensating for human weaknesses in articulation

## 4. Behavioral Design

**Behavioral Principles:**
1. **Humans are imperfect articulators:** Design assumes incomplete, messy initial input
2. **Clarity requires externalization:** Intent must be made explicit through dialogue, not assumed
3. **Permission over presumption:** LLM must receive explicit approval before proceeding
4. **Progressive disclosure:** Information revealed through structured conversation, not upfront requirements

**Incentive Structure:**
- **Encourages:** Honest admission of uncertainty, iterative refinement, explicit validation
- **Discourages:** Premature execution, assumption-making, one-shot prompting
- **Penalizes (implicitly):** Vague approvals (system asks for clarification), skipping the process (option to reset)

**Alignment Mechanisms:**
1. **95% confidence threshold:** Quantified target prevents subjective "good enough"
2. **Echo check format:** Standardized summary forces LLM to demonstrate understanding
3. **Explicit control options:** User maintains agency through defined interaction paths
4. **Risk identification:** Built-in mechanism to surface what could go wrong

## 5. Time & Attention

**Where Time Flows:**
- **Upfront investment:** Multiple rounds of clarifying questions (deliberately front-loaded)
- **Dialogue, not documentation:** Conversational extraction of requirements rather than formal specification writing
- **Validation before execution:** Explicit approval step prevents wasted generation time
- **Domain-specific review:** Targeted attention to error-prone areas (code, documents)

**What This System DOESN'T Spend On:**
- **Rework from misunderstanding:** Eliminates the iterate-after-failure cycle
- **Heavy PRD writing:** Avoids formal requirements documentation when not yet needed
- **Trial-and-error prompting:** Replaces guesswork with systematic clarification
- **Ambiguity resolution after the fact:** Surfaces conflicts before work begins

**Allocation Philosophy:** 
"Spend tokens on understanding, save them on execution." The system intentionally invests in the clarification phase to achieve one-shot accuracy in the generation phase. This inverts the typical pattern of cheap prompts → expensive iteration cycles.

## 6. Moats & Time Horizon

**Competitive Advantages:**
1. **Protocol knowledge:** Understanding how to structure the contract-first flow
2. **Question quality:** Ability to generate/refine the clarifying question framework for specific domains
3. **Organizational habit:** Teams trained to expect and demand clarification before execution
4. **Prompt libraries:** Accumulated domain-specific contract templates
5. **Difficulty of replication:** Requires changing human behavior (hardest moat)

**Time Horizon:**
- **Short-term (immediate):** Reduced token waste, fewer failed outputs, faster completion of well-defined tasks
- **Medium-term (3-6 months):** Accumulated prompt templates, team proficiency in intent articulation, reduced frustration with AI tools
- **Long-term (1-2 years):** Organizational capability to tackle increasingly complex AI-assisted work, competitive advantage in AI productivity

**Why Time Is Your Friend:** 
Each successful contract-first interaction:
- Teaches the user better intent articulation
- Generates reusable question frameworks for similar tasks
- Builds confidence in AI collaboration
- Creates organizational knowledge about what questions matter in different domains
- Compounds into a library of proven templates

## 7. Flywheels & Lock-In

**Primary Flywheel:** The Intent Clarity Flywheel

**Flywheel Visualization:**
[Use contract-first prompting] → [Experience clearer outputs from better intent] → [Learn which questions surface critical constraints] → [Build template library for common tasks] → [Reduce time-to-clarity on new tasks] → [Tackle more complex/ambiguous work] → [Use contract-first prompting for higher-value problems, stronger]

**Lock-In Mechanisms:**
1. **Cognitive retraining:** Users become accustomed to structured clarification, find traditional prompting frustrating
2. **Template accumulation:** Growing library of domain-specific contract prompts becomes valuable asset
3. **Team protocols:** Once adopted organizationally, reverting means coordination costs
4. **Quality expectations:** Users develop higher standards for AI output, won't accept ambiguous results
5. **Skill development:** Ability to articulate intent improves, but only works well with contract-first structure

**Compounding Effect:** 
The system improves with use because:
- Users learn which constraints are often overlooked in their domain
- Question frameworks become more targeted and efficient
- The gap between initial prompt and final clarity shrinks
- Team develops shared vocabulary for intent articulation
- Cross-pollination of templates across use cases

## 8. System Beneficiaries

**Winners:**
1. **Knowledge workers with tacit expertise:** Those who "know what they want" but struggle to articulate it benefit most—domain experts, product managers, strategists
2. **Organizations doing complex AI work:** Companies tackling ambiguous, high-stakes tasks where mistakes are costly
3. **Token-conscious users:** Those paying per token who need efficiency
4. **Iterative thinkers:** People comfortable with dialogue-based refinement rather than upfront specification
5. **Non-technical users:** Those who can describe outcomes but not processes

**Losers:**
1. **Speed-first users:** Those needing quick, rough outputs may find the clarification overhead excessive
2. **Highly structured domains:** Areas with well-established requirements formats (legal documents with templates) get less benefit
3. **One-shot task users:** People doing unique, never-to-be-repeated work don't benefit from template accumulation
4. **Prescriptive leaders:** Those who expect subordinates to "just figure it out" may resist systematic clarification

**Ethical Considerations:**
- **Accessibility:** Does this create a skill barrier where only sophisticated users can leverage AI effectively?
- **Transparency:** The system makes assumptions explicit, which is good, but could create false confidence if 95% isn't actually sufficient
- **Dependency:** Risk of over-relying on AI for thinking that humans should do themselves
- **Efficiency theater:** Possibility of spending more time on clarification than the work warrants

## 9. System Health Metric

**What to Optimize For:** **First-Pass Acceptance Rate**—the percentage of outputs accepted without revision after the contract is locked.

**Why This Metric:** 
- **Validates the core premise:** If contracts are truly clear, outputs should be right the first time
- **Captures the full system:** Includes both clarification quality and execution accuracy
- **Reveals hidden costs:** Low acceptance despite good contracts indicates execution problems; high acceptance with long clarification indicates efficiency opportunities
- **Drives behavior:** Focuses users on clarification quality rather than rushing to generation
- **Measurable improvement:** Easy to track over time and across use cases

**How to Measure:**
1. Track each contract-first session
2. Mark when contract is "locked" (user says yes)
3. Record whether first output after lock is accepted without revision
4. Calculate: (Accepted outputs / Total locked contracts) × 100
5. Segment by: domain, user, complexity level, clarification round count
6. Target: >80% first-pass acceptance (vs. typical ~30% for traditional prompting)

**Secondary Metrics:**
- Average rounds to lock (efficiency of clarification)
- Token consumption per successful output (total cost including clarification)
- Time to lock vs. time to completion (where is the bottleneck?)
- Revision requests after lock (quality of execution given clear contract)

## 10. Unique Insights & Quotes

### Memorable Quotes

> "Almost every prompt that fails fails because intent wasn't clearly communicated."

> "Human language is really, really rough on intent. And it's not just a function of a particular language. It's not just a function of the fact that it's human language. It's really the fact that we as individual people bring so much domain expertise. We bring so much passion. We bring so much energy, so much experience to a particular subject we want to work on."

> "I want to emphasize to you that that is a very scattershot unprofessional approach to actually dealing with this issue. You are giving the LLM, which is swimming in a sea of ambiguity, free reign to pick a question that it thinks may help."

> "In the same way, we need to get to a point where we have very tight technical shared understanding with the LLM of the meaningful work we want to do together before it starts to work."

> "Shorter is harder than longer here."

> "You just need clarity around the sequence of steps. All we're doing is we're saying, one, list the gaps to goal, which I almost never see in prompts. Two, dig for those gaps until you get to 95% confidence. And then from there, offer a path forward that I can choose and control because we're trying to write a contract together."

> "This is a very intentionally wide-ranging prompt set. It is supposed to be something that is workable for virtually any piece of serious work where you need to define intent first."

> "And I'm increasingly interested in prompting techniques that assume that humans are humans. We are not perfect. We do not always write the full prompt out. We do not always have the full crisp complete intent. In fact, mostly we don't have any of those things. What we have is a vague human idea backed by a tremendous amount of context and experience and we need help fishing that out of our heads and getting to clarity."

> "That is what a contract first approach to prompting seeks to do. How can we get to a point where the LLM deeply, fully, completely understands your intent with this piece of work in a way that you can just converse with it and and like let it ask you questions and let it dig out for you."

> "Spend tokens on understanding, save them on execution." [implied from the overall philosophy, not verbatim]

### Non-Obvious Insights

- **The naming convention discovery:** When asked for a 500-word Balkans history summary, the LLM identified that handling "the evolution of political entities and their naming conventions" was a key leverage point—something not named as a constraint but critical to success. This demonstrates LLMs can identify non-obvious dependencies when given structured space to think.

- **Shorter is harder:** The deliberate choice of 500 words rather than unlimited length increases difficulty and surfaces more constraints. Most people assume longer = harder, but summarization to tight constraints actually requires more clarity about priorities and scope.

- **The gap-to-goal framing:** "List the gaps to goal" as a distinct first step is "almost never seen in prompts" despite being obvious in retrospect. This reframes the LLM's role from answerer to requirement analyst.

- **95% as the threshold:** Not 100% (which may be unachievable) but 95% (which is "good enough to ship"). This acknowledges that perfect clarity is impossible and some residual ambiguity is acceptable, preventing analysis paralysis.

- **Questions beget better questions:** The system improves question quality through iteration—early answers inform later questions, creating a progressive refinement that wouldn't be possible in a single-shot clarification attempt.

- **The "echo check" as forcing function:** Requiring the LLM to state deliverable + constraint in one crisp sentence forces compression and validation. It's a test that the LLM actually understands rather than just collected information.

- **Contract-first scales to any domain:** From history summaries to software PRDs, the same protocol works because it addresses the universal problem of intent clarity rather than domain-specific content.

- **The mini-program inside:** Embedding explicit control flow (yes/lock, edit, blueprint, risks, reset) turns the prompt into a stateful interaction protocol rather than a single request-response pair.

- **Token efficiency through front-loading:** Spending more tokens upfront on clarification actually reduces total token consumption by eliminating rework—counterintuitive to "keep prompts short" conventional wisdom.

- **The scarcity insight:** Nate explicitly states he "hasn't seen this technique elsewhere" despite extensive searching, suggesting that systematic intent clarification protocols are surprisingly rare in the prompting literature.

## 11. Application & Mental Model

### When to Use This Pattern

**Ideal conditions:**
- **Ambiguous requirements:** You have a general idea but can't articulate specifics
- **High-stakes work:** Mistakes are costly (time, money, reputation)
- **Complex domain knowledge:** You bring expertise that's hard to externalize
- **Novel tasks:** First time tackling this type of work, no template exists
- **Collaborative generation:** Output will be reviewed and refined, not fire-and-forget
- **Token budget available:** You can afford the upfront clarification investment
- **Learning intent:** Part of the goal is understanding what you actually want

**Key signals:**
- You find yourself saying "I'll know it when I see it"
- Previous attempts produced technically correct but directionally wrong outputs
- The task involves trade-offs you haven't explicitly thought through
- You're bridging from vague executive vision to concrete deliverable
- The domain has hidden complexity (like the Balkans political entities example)

### When NOT to Use This Pattern

**Inappropriate conditions:**
- **Ultra-simple, well-defined tasks:** "Translate this to French" doesn't need contract negotiation
- **Speed is paramount:** Breaking news response, crisis management—no time for rounds of clarification
- **One-off disposable work:** Brainstorming session notes where precision doesn't matter
- **Highly templated domains:** Legal contracts with established formats, compliance documents with strict requirements
- **Non-expert users:** If you genuinely don't have domain knowledge to extract, clarification won't help
- **Exploration over execution:** When you're trying to discover what you want rather than specify what you know

**Backfire scenarios:**
- Over-clarifying simple tasks creates bureaucracy theater
- Using 95% confidence for work that needs 99.9% (safety-critical systems)
- Asking users without tacit knowledge to articulate what they don't know
- Creating false confidence that comprehensive clarification eliminates all risk
- Spending more time on contract than execution would have taken

### How to Apply to 1658 Holdings Companies

**Finland DMC Oy:**
- **Tour package development:** Use contract-first to clarify customer intent when designing custom Nordic experiences—what does "authentic" mean? What level of luxury? Physical activity tolerance? Cultural vs. nature balance?
- **Expected outcome:** 80% reduction in back-and-forth with clients, higher first-proposal acceptance rate, template library of clarifying questions for different traveler profiles

- **Content generation:** Apply to travel blog posts, destination guides, marketing copy—clarify audience (first-time vs. repeat visitors), tone (inspirational vs. practical), key differentiators before generating
- **Expected outcome:** Content that requires minimal editing, clearer brand voice consistency, faster content production pipeline

- **Operational documentation:** Use for creating SOPs, training materials, partner communications—clarify what success looks like, what level of detail is needed, what failure modes to address
- **Expected outcome:** Documentation that actually gets used, reduced training time for new team members, clearer partner expectations

**General Principles:**

1. **Build domain-specific question frameworks:** For each recurring task type (client proposals, content briefs, operational docs), develop a contract-first template with pre-loaded relevant dimensions (e.g., for tour packages: budget range, physical capability, group dynamics, dietary restrictions, must-see vs. flexible, pace preferences)

2. **Train teams in intent articulation:** Regular practice sessions where team members use contract-first for real work, developing organizational fluency in externalizing tacit knowledge. Make "what gaps exist to goal?" a standard question in project kickoffs.

3. **Measure and optimize:** Track first-pass acceptance rate for AI-generated work across different use cases. When acceptance is low despite good contracts, investigate execution issues. When clarification takes too long, refine question frameworks. Build feedback loops between outcomes and question quality.

4. **Create escalation protocols:** Define when contract-first is required (high-stakes, complex, novel) vs. optional (routine, simple, templated). Prevent over-application while ensuring it's used where it matters.

5. **Leverage for client relationships:** Use contract-first not just with AI but with human clients—show them the clarification process, involve them in defining constraints, create shared understanding before proposal development. This positions Finland DMC as thorough and professional while extracting better requirements.

## Strategic Patterns Identified

1. **Intent-Before-Execution:** The meta-pattern of forcing clarification before action, applicable beyond AI to organizational decision-making, project planning, and strategic alignment. The principle: time spent understanding prevents time wasted doing.

2. **Progressive Clarification Protocols:** Instead of expecting complete information upfront, design systems that systematically extract it through structured dialogue. Applicable to customer discovery, requirements gathering, strategic planning—any domain where tacit knowledge must become explicit.

3. **Mutual Agreement Checkpoints:** Creating explicit validation moments where both parties confirm shared understanding before proceeding. Borrowed from software engineering contracts, applicable to any collaborative work where misalignment is costly.

## Quality Assessment

**Transcript Quality:** excellent
- Complete sentences, minimal verbal tics, clear logical flow
- Technical concepts well-explained with concrete examples
- Sufficient detail to understand implementation without overwhelming

**Analysis Confidence:** high
- Clear articulation of the technique with specific examples
- Transparent about limitations and appropriate use cases
- Novel contribution acknowledged by creator's own research

**Strategic Value:** high
- Addresses fundamental efficiency problem in AI adoption
- Applicable across domains and organizational contexts
- Creates sustainable competitive advantage through organizational learning
- Timely (peak relevance in current AI productivity landscape)

**Completeness:** complete
- Covers what, why, how, when, and when-not comprehensively
- Provides concrete examples across multiple domains
- Includes implementation details (the actual prompt structure)
- Addresses potential objections and limitations
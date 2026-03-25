---
title: "How to Build Claude Skills Better Than 99% of People"
type: video-analysis
channel: ben-ai
video_id: X3uum6W2xEI
video_url: https://www.youtube.com/watch?v=X3uum6W2xEI
duration: ~20:00
published: 2026-02
analyzed: 2026-02-25
tags: [claude-skills, skill-engineering, ai-agents, workflow-automation, progressive-disclosure, self-improving-skills]
key_concepts: [skill-architecture, progressive-disclosure, reference-files, skill-iteration-framework, self-learning-skills, plugins-vs-skills]
strategic_patterns: [prepare-before-prompt, process-in-skillmd-context-in-references, multiple-variations-at-hitl, save-approved-as-example]
quality_score: 4
strategic_value: high
---

# How to Build Claude Skills Better Than 99% of People

## Summary

Ben AI presents a comprehensive framework for building high-quality Claude skills — the instruction packages that turn AI agents into specialized workflow executors. The core insight: skills are "software engineering for AI agents" — requiring UX design (human-in-the-loop choices), context engineering (which reference files, when), feature iteration (rules section), and edge case handling. Most people skip the preparation step, which is where the biggest quality gains live. Skills should be self-improving: saving approved outputs as examples and updating rules on corrections.

---

## 1. Context

**Background:**
AI agents (Claude Code, Cowork, Codex, Gemini) are getting powerful, but still need specific guardrails, context, and SOPs for unique business processes. Previous solutions (Projects, Custom GPTs) are isolated and don't self-improve. Automation platforms (n8n) are deterministic but most work requires judgment. Skills sit in the middle: instructions for an AI agent on a specific process, with human-in-the-loop, self-improvement, and prompt-based creation/updates.

**Why This Matters:**
Skills are becoming the new software layer. Three layers are emerging: general (Anthropic/OpenAI built-in), marketplace (third-party, monetizable), and company/individual customizations. Building good skills = competitive advantage for individuals and businesses. Same input to a poorly built vs well-built skill produces dramatically different outputs.

---

## 2. What Skills Actually Are

**Architecture:**
- **Core:** `skill.md` — the process instruction (SOP)
- **Reference files (text):** example outputs, style guides, ICP docs, voice/personality, MCP instructions
- **Reference files (assets):** images, presentations, videos, binary files for output examples
- **Reference files (code):** Python/JS scripts for API calls, function execution

**Progressive Disclosure (why thousands of skills work):**
1. Only metadata (name + description) stored in agent memory
2. `skill.md` loaded only when skill is triggered
3. Reference files loaded only when skill instructs it
4. Result: one agent can access thousands of skills without context overflow

**Skills vs Plugins:**
- Plugins = bundled skills + commands + agents + connectors
- Enable departmental distribution (sales plugin, marketing plugin)
- Versionable and shareable across accounts
- Prediction: SaaS companies will start launching their own plugins

---

## 3. The Building Framework

### Step 1: Prepare First (most people skip — biggest impact)

Before prompting to build a skill:
- Think through the ideal step-by-step process to get a good outcome
- Prepare knowledge sources / reference files:
  - Business description
  - ICP description
  - Voice/personality guide
  - Strategy documents (YouTube strategy, newsletter strategy, etc.)
  - **Good output examples** — highest single impact on performance
- Identify which tools/MCPs the agent needs
- Tip: if you don't have reference files yet, create them WITH Claude first (planning mode → Q&A → generated document)

### Step 2: The Prompt Framework

1. **Name + trigger description** — metadata for when agent should activate
2. **Goal/objective** — short, since process section goes deeper
3. **Connectors/APIs/MCPs** — what tools needed + specific navigation instructions
4. **Step-by-step process** (most important):
   - What to do at each step
   - When to insert human-in-the-loop
   - What KIND of HITL (checkboxes, open field, single select — "becomes UX design")
   - Which reference files to use per step
   - Expected output per step
   - **Always offer multiple variations** at HITL steps (3-5 options, not single outputs)
5. **Rules section** — predict what could go wrong; continuously updated
6. **Progressive updates** — self-learning instructions:
   - Save approved outputs as good examples automatically
   - Update rules when user defines "never do X"

### Step 3: Keep Skill.md Clean

**Critical principle:** skill.md should focus ONLY on the process. All additional context, information, and examples go in reference files. This is what makes skills perform well. Polluting skill.md with context degrades performance.

---

## 4. The Iteration Framework

| Problem | Fix |
|---------|-----|
| Doesn't follow process correctly | Update skill.md |
| Needs additional information | Add reference file |
| Recurring bad behavior ("never do X") | Add rule OR update knowledge file |
| Struggles with software/MCP | Guide manually → create MCP reference doc |

**Key insight:** Skills are never finished. The more you use them, the better they get. Ben iterated on his infographic skill ~5 times to reach current quality.

---

## 5. Sharing & Distribution

- Export: ask Claude for a zip file of the skill
- Import: settings → capabilities → upload zip
- Deploy via GitHub for broader distribution
- Multiple skills → bundle into plugin (prompt Claude to build it)
- Multiple plugins → create plugin marketplace (requires Claude Code + GitHub)

---

## 6. Gold Insights

### Insight 1: Prepare-Before-Prompt (Process)
**What:** Before building any skill, prepare reference files (business desc, ICP, voice, strategy, output examples) and think through the ideal step-by-step process. Most people skip this — it's where the biggest quality gap lives.
**When to apply:** Every time you build a new skill or workflow
**Source evidence:** "Good output examples is generally the thing that impacts performance the most"

### Insight 2: Process in Skill.md, Context in References (Architecture)
**What:** Keep skill.md focused exclusively on the step-by-step process. All additional context (examples, guides, ICP, voice) belongs in separate reference files. This separation is what makes skills perform well — polluting skill.md with context degrades quality.
**When to apply:** Any skill building or maintenance
**Source evidence:** "Keep the skill MD very clean and focused on the process. Any additional information should be in the reference files. That's how your skill is going to perform a lot better."

### Insight 3: Multiple Variations at HITL (UX)
**What:** At every human-in-the-loop step, have the agent present 3-5 variations/options instead of single outputs. This dramatically improves productivity and outcome quality — you choose the best direction rather than iterating on one.
**When to apply:** Any skill with human review steps; deliverable building workflows
**Source evidence:** "Ask Claude to always give you multiple variations or options which you can choose from instead of just one-off outputs"

### Insight 4: Self-Learning Skills (Architecture)
**What:** Include progressive update instructions: (1) when user defines "never do X," update rule section automatically; (2) when user approves final outcome, save it as a good example for future reference. Skills become better with each use.
**When to apply:** Any frequently-used skill
**Source evidence:** "Instruct the skill to be automatically updated and improved when using the skill so it becomes self-learning"

### Insight 5: Progressive Disclosure Enables Scale (Architecture)
**What:** Only metadata (name + description) sits in agent memory. Skill.md loads on trigger. Reference files load on instruction. This three-level loading is how one agent handles thousands of skills without context overflow.
**When to apply:** System architecture for multi-skill agents; validates tiered knowledge systems
**Source evidence:** "Because of this progressive disclosure of context, we can give one agent access to thousands of potential skills"

### Insight 6: Four-Type Iteration Framework (Process)
**What:** Clean decision tree for skill improvement: process wrong → update skill.md; need more info → add reference file; recurring bad output → add rule; struggles with tool → guide manually then save MCP reference doc. Each fix type targets the right layer.
**When to apply:** Any skill maintenance or debugging
**Source evidence:** Demonstrated through infographic skill evolution over 5+ iterations

---

## 7. Applicability to 1658 Holdings

**Validates our existing architecture:**
- Progressive disclosure ↔ our 3-tier system (Tier A/B/C) + warm packs
- Reference files separate from skill.md ↔ warm packs + required_reads
- Prepare reference files first ↔ company CLAUDE.md + mining outputs before building

**New techniques to adopt:**
1. **Multiple variations at HITL** — apply to `/build` workflow: present 3-5 deliverable approaches before committing
2. **Save approved outputs as examples** — when Patrick approves a deliverable, explicitly save as reference example for that skill type
3. **Four-type iteration framework** — cleaner mental model than our current approach for skill maintenance

**Not applicable:**
- Marketplace/monetization angle (we build internal tools)
- Plugin bundling (our needs are simpler)

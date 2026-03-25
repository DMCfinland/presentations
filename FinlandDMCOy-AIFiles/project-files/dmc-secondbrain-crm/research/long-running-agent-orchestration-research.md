# Long-Running Agent Orchestration Research
**Date:** 2026-03-11 | **Agent:** R3 | **Sources consulted:** 12

---

## Key Findings (Top 8 Most Actionable)

### F1 — Context window is the single most critical resource
**What:** LLM performance degrades visibly as context fills. Anthropic's official best-practices page leads with this: "Most best practices are based on one constraint: Claude's context window fills up fast, and performance degrades as it fills." This is not a subtle degradation — agents start "forgetting" earlier instructions and making structural mistakes.
**Why it matters:** A 5-wave build spanning weeks will burn context fast. An agent that starts a session at 60% context usage is already impaired before writing its first line.
**Source:** Anthropic Claude Code Best Practices (code.claude.com/docs/en/best-practices)

### F2 — Initializer agent pattern is documented by Anthropic for multi-session continuity
**What:** Anthropic's engineering blog documents a two-part harness for long-running work: (1) an initializer agent that sets up the environment on first run — creating `init.sh`, `claude-progress.txt`, and an initial git commit — and (2) coding agents that make incremental progress each session, reading the progress file and git log before doing any work. "Each new session begins with no memory of what came before."
**Why it matters:** This pattern is exactly what BUILD-STATE.md is implementing. The Anthropic write-up validates the approach and adds specifics: JSON format for feature tracking (less prone to model overwrites than Markdown), and a standard session startup sequence.
**Source:** Anthropic Engineering, "Effective harnesses for long-running agents" (anthropic.com/engineering/effective-harnesses-for-long-running-agents)

### F3 — Task subagents beat agent teams for sequential-wave work (confirmed externally)
**What:** The official Claude Code docs confirm what was learned internally at session 48: "For sequential tasks, same-file edits, or work with many dependencies, a single session or subagents are more effective [than agent teams]." Agent teams add coordination overhead and use significantly more tokens. The docs recommend 3-5 teammates max when teams ARE used, with 5-6 tasks per teammate.
**Why it matters:** Our build is sequential-wave by design. Agent teams are the wrong tool for waves that depend on prior waves completing. Subagents or independent worktree sessions are correct.
**Source:** Anthropic Claude Code Agent Teams docs (code.claude.com/docs/en/agent-teams)

### F4 — Auto-compact triggers at 75% context and is customizable
**What:** Claude Code auto-compacts at 75% context fill. This is configurable: you can write instructions in CLAUDE.md telling Claude what to preserve during compaction (e.g., "When compacting, always preserve the full list of modified files and any test commands"). The Agent SDK also supports compaction as a built-in mechanism that theoretically allows an agent to continue useful work indefinitely.
**Why it matters:** Build agents must have CLAUDE.md compaction instructions. Without them, critical state (table names, decision rationale, locked decisions list) can be silently dropped during auto-compact mid-session.
**Source:** Anthropic Claude Code Best Practices; Claude Agent SDK docs (platform.claude.com/docs/en/agent-sdk/agent-loop)

### F5 — Git worktrees have native Claude Code support and a documented isolation pattern
**What:** Anthropic shipped built-in git worktree support for Claude Code CLI (previously desktop-only). Using the `--worktree` flag or the `isolation: worktree` frontmatter in a subagent definition, each agent gets its own worktree that is automatically cleaned up when finished. The core rule: "two teammates editing the same file leads to overwrites — break the work so each teammate owns a different set of files."
**Why it matters:** Our WAVE-BUILD-AGENTS.md already uses worktrees correctly. The native support confirms this is the right approach. File ownership per agent (Constitutional Principle 5) maps directly to the documented safe pattern.
**Source:** Anthropic Claude Code Common Workflows (code.claude.com/docs/en/common-workflows); Boris Cherny thread on native worktree support

### F6 — Cost explosion is a documented real-world failure mode — not theoretical
**What:** GetOnStack's documented case: a multi-agent system for market data research escalated from $127/week to $47,000 over 4 weeks due to an undetected infinite conversation loop between agents running for 11 days. Recovery required 6 weeks of infrastructure work (message queues, circuit breakers, cost controls, monitoring). This is not an edge case — it is a known failure mode of unsupervised multi-agent systems.
**Why it matters:** Our build needs per-session cost caps and a human check before each wave spawn, not just a pre-build estimate. Patrick's weekly Monday coherence sync (reading BUILD-STATE.md before spawning any agent) is the correct control.
**Source:** ZenML "What 1,200 Production Deployments Reveal About LLMOps in 2025" (zenml.io/blog)

### F7 — "Correct over and over" is a documented anti-pattern with a specific fix
**What:** Anthropic documents this explicitly: "If you've corrected Claude more than twice on the same issue in one session, the context is cluttered with failed approaches. Run /clear and start fresh with a more specific prompt that incorporates what you learned." Each correction attempt adds failed reasoning to context, which actively degrades subsequent attempts.
**Why it matters:** Build agents that encounter repeated failures should not retry endlessly. The BUILD-STATE.md "NEXT SESSION" section should capture the failure + what was learned, so the next agent starts clean with a better-specified prompt.
**Source:** Anthropic Claude Code Best Practices (code.claude.com/docs/en/best-practices)

### F8 — Constraining agents outperforms unleashing them — documented at scale
**What:** Cubic's experience with their AI code review agent: giving the agent more tools caused performance to degrade. The agent "became confused, generating excessive false positives until developers stopped trusting it." The lesson documented across 2025 case studies: "Success usually comes from constraining the model rather than unleashing it." One task, one file set, one clear deliverable.
**Why it matters:** Our Constitutional Principle 6 ("If you find yourself doing more than your assigned task, stop") is validated. Build agents should have narrow scope with the excess noted for the next agent — not attempted.
**Source:** Directual "AI Agents in 2025: Why 95% of Corporate Projects Fail" (directual.com/blog); multiple 2025 production case studies

---

## Context Management Patterns

### The 75% Rule
Auto-compact fires at 75% context fill. For a 200K context window, this is ~150K tokens. A build agent doing heavy file reads and code generation can reach this in one long session. Proactive strategy: for file-heavy phases (schema migration, full-codebase feature builds), plan for compaction mid-session by having all outputs written to files before turn 12-15.

### CLAUDE.md Compaction Instructions (must be in every worktree)
Add to each worktree's CLAUDE.md:
```
## Compaction Instructions
When compacting, ALWAYS preserve:
- LOCKED DECISIONS list from SHARED-CONTEXT.md (verbatim, all D1-D12)
- Current task assignment and deliverable list
- File paths of any files written this session
- Any BLOCKER or ERROR states noted for Patrick
- The BUILD-STATE.md update you were asked to write at session end
```

### Context isolation via subagents for investigation
When a build agent needs to understand a large codebase area, use a subagent for exploration rather than direct reads. The exploration context stays isolated; the main agent receives only the summary. This prevents "infinite exploration" from consuming 50K+ tokens before a single line of code is written.

### /clear between unrelated tasks
If Patrick gives a build agent a side task ("also check whether X is correct") mid-session, that side task should either be explicitly rejected ("write it in BUILD-STATE.md for the next agent") or handled via a subagent, not inline. Inline side tasks pollute the main build context.

### The "kitchen sink" failure pattern
Starting with one task, getting interrupted, returning to the first task — Claude's context fills with irrelevant information and earlier instructions fade. Build agents must be single-task by design. Constitutional Principle 6 enforces this, but Patrick also needs to not ask build agents for off-task work during a session.

---

## State Handoff Patterns

### Anthropic's Documented Pattern: Read → Work → Write
The validated session lifecycle from Anthropic's engineering blog:
1. **Start:** Read progress file + git log (last 10 commits minimum)
2. **Verify:** Run smoke tests before implementing new features
3. **Work:** Single focused task only
4. **Commit:** Write commit with descriptive message documenting what was built
5. **Update state file:** Write COMPLETED, CURRENT STATE, NEXT SESSION, DECISIONS LOG sections
6. **Close:** Do not attempt follow-on work — leave it for the next agent

### BUILD-STATE.md Structure Recommendation
Based on the Anthropic initializer pattern, BUILD-STATE.md should have:
- **COMPLETED** — append-only log, timestamped, one line per deliverable
- **CURRENT STATE** — overwritten each session, plain statement of where the build stands
- **NEXT SESSION** — what the next agent needs to know, including any failures + what was learned
- **BLOCKERS** — explicit HALT items for Patrick (never bury blockers in prose)
- **DECISIONS LOG** — append-only architectural choices made during this session

JSON format is recommended by Anthropic for feature tracking (less prone to model overwrites). For our build, this means the COMPLETED and DECISIONS sections should be structured enough that an agent cannot accidentally overwrite a prior entry.

### The "Briefing Flag" Pattern (from session 46 analysis)
For cross-wave communication: write critical updates to a persistent file rather than passing them in agent spawn prompts. The Wave 2A agent reading BUILD-STATE.md for schema results is exactly this pattern. It is more reliable than trying to summarize Wave 1 results into a spawn prompt, because the file is always current and complete.

### Context isolation: subagents start fresh
Documented in official Claude Code docs: "Teammates don't inherit the lead's conversation history. Whatever context they need, the lead has to provide in the spawn prompt." For our build, this means every agent spawn prompt must be self-contained. If a Wave 3 agent needs to know Wave 1 schema decisions, those decisions must be written into BUILD-STATE.md — not assumed to be "remembered."

### Session naming for resumability
Claude Code saves conversations locally. Use `/rename` to give sessions descriptive names like `crm-wave-1a-schema` or `crm-wave-2a-n8n`. This enables `claude --resume` to pick up exactly the right session if a wave needs to continue. Without names, sessions are indistinguishable.

---

## Known Failure Modes + Mitigations

| Failure Mode | How It Manifests | Mitigation |
|---|---|---|
| **Context rot** | Agent "forgets" locked decisions mid-session; overrides D3, D8, etc. | CLAUDE.md compaction instructions; Constitutional Principles pasted into every spawn prompt |
| **Hallucinated state** | Agent writes "COMPLETED: schema migration ✓" in BUILD-STATE.md without actually completing it | Self-check line in BUILD-STATE.md update ("verify you can run these test queries before marking complete"); human reviews git log at wave start |
| **Premature completion** | Agent marks a wave done with partial work due to unclear scope | Explicit deliverables checklist in spawn prompt (we have this); Quality Gates per wave (we have this) |
| **Over-scope drift** | Agent extends its task into adjacent work ("while I'm at it...") | Constitutional Principle 6; single-deliverable spawn prompts |
| **Infinite retry loop** | Agent hits error, retries same approach repeatedly, burning context and cost | After 2 failed attempts on same issue: write to BUILD-STATE.md as BLOCKER, end session, start fresh with better spec |
| **File ownership conflict** | Two wave agents modify the same file; later commit overwrites earlier | Worktree isolation per agent; Constitutional Principle 5 (file ownership); merge before next wave spawns |
| **Agent team cost explosion** | Multiple agents running with loops undetected; GetOnStack spent $47K | Per-wave cost caps; human approval gate before each wave; wave-by-wave not concurrent across waves |
| **Tool overload** | Agent given too many tools, degrades to confusion | Strict tool grants per agent (Wave 5A red team is the exception — intentionally broad) |
| **Spawn prompt vagueness** | Subagent receives vague prompt, produces vague result | Complete, self-contained spawn prompts with all file paths, locked decisions, and acceptance criteria |
| **State file corruption** | Agent accidentally overwrites prior COMPLETED entries in BUILD-STATE.md | Append-only section design; weekly git backup of BUILD-STATE.md; consider JSON structured sections |

---

## Compact Threshold Recommendation

**Recommendation: Proactively compact at or before 60% context fill for build agents.**

Evidence:
- Auto-compact fires at 75% (Anthropic documented). At 75%, the agent has already been operating in degraded state for some time.
- The 200K context window has a pricing cliff: above 200K input tokens, ALL tokens cost 2x. Build agents reading large files risk crossing this unintentionally.
- Heavy file reads (reading SHARED-CONTEXT.md + BUILD-STATE.md + spec documents at session start) can consume 15-25K tokens before the first code is written.
- A build session with active coding, test runs, and file writes can consume 5-10K tokens per turn.

**Practical approach:**
- Use a custom status line (`/statusline`) to track context % in real time during build sessions
- At turn 10-12 in a file-heavy session, assess: "Is my primary deliverable written to file?" If yes, compact. If no, write it, then compact.
- Configure CLAUDE.md compaction instructions before spawning any build agent (see Context Management section above)
- For schema migration (Wave 1A): the SQL migration file is the artifact. Write it early, then compact if needed for testing.
- For the vibe demo (Wave 1B): the HTML file is the artifact. Write it early.
- The `/compact Focus on [specific deliverable]` variant is more reliable than auto-compact for build agents — it lets you direct what survives.

**Do NOT use 100K as the threshold.** By 100K in a code-writing session, the agent has likely already experienced some degradation and may have silently dropped earlier constraints.

---

## Applicable to Our Build

Based on research findings, these are the specific changes and validations for WAVE-BUILD-AGENTS.md and the build process:

### Validated (no change needed)
- BUILD-STATE.md with COMPLETED / CURRENT STATE / NEXT SESSION / DECISIONS LOG sections — matches Anthropic's documented initializer pattern exactly
- Sequential waves with human gate before each wave — correct for this dependency structure
- Constitutional Principles in every spawn prompt — matches "give agents enough context" best practice
- Worktree isolation per agent — matches native Claude Code worktree support pattern
- File ownership per agent (Principle 5) — matches "avoid file conflicts" best practice
- Quality Gates per wave — matches "give Claude a way to verify its work" best practice

### Changes to make before Wave 1

**1. Add CLAUDE.md compaction instructions to every worktree**
Each worktree needs a CLAUDE.md (not just the project root) with explicit compaction instructions. Without this, auto-compact may drop locked decisions or deliverable specs mid-session.

**2. Add "session startup sequence" to every spawn prompt**
The Anthropic-documented session startup sequence should be explicit:
```
## SESSION START SEQUENCE (do in order)
1. Run: pwd (verify you are in the correct worktree)
2. Read: SHARED-CONTEXT.md (locked decisions — read every word)
3. Read: BUILD-STATE.md (focus CURRENT STATE and NEXT SESSION sections)
4. Read: [wave-specific spec file]
5. Run: git log --oneline -10 (understand what has been built)
6. Run: [smoke test command if applicable]
7. ONLY THEN: begin your assigned task
```

**3. Add session naming to spawn instructions**
Add to every spawn prompt: "After reading your context files, run `/rename crm-wave-[X][Y]-[description]` to name this session for later resumption."

**4. Specify compact behavior explicitly in spawn prompts**
Add to every spawn prompt: "If you approach 60% context fill and your primary deliverable is NOT yet written to its target file, write it immediately before continuing. If your primary deliverable IS written, run `/compact Focus on [deliverable name] and LOCKED DECISIONS D1-D12`."

**5. Add BLOCKER escalation path to BUILD-STATE.md template**
Current BUILD-STATE.md update instructions say "write a question to BUILD-STATE.md for human review." Add a distinct BLOCKERS section so Patrick can find blockers immediately without reading all prose.

**6. Consider JSON for COMPLETED section**
Anthropic specifically recommends JSON for feature tracking lists because it's "less prone to model overwrites than Markdown." Converting the COMPLETED section to append-only JSON entries would make it harder for agents to accidentally corrupt prior entries.

**7. Add per-wave cost cap to PRE-SPAWN CHECKLIST**
The current checklist has "Cost estimate for this wave: $______". Add a hard cap: "If estimated cost exceeds $5, stop and recalculate before proceeding." The GetOnStack case shows cost explosions happen quietly over time, not in one obvious burst.

**8. Explicit "after 2 failures, write blocker and stop" rule**
Add to Constitutional Principles (or spawn prompt):
```
7. FAILURE LIMIT: If you attempt the same subtask twice and fail both times,
   write the failure + what you tried to BUILD-STATE.md as a BLOCKER.
   End your session. Do NOT attempt a third time.
   A fresh session with a better spec will outperform a third attempt.
```

---

## Sources

- [Anthropic Engineering: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [Anthropic: Claude Code Best Practices](https://code.claude.com/docs/en/best-practices)
- [Anthropic: Orchestrate teams of Claude Code sessions (Agent Teams docs)](https://code.claude.com/docs/en/agent-teams)
- [Anthropic: Common Workflows — git worktrees](https://code.claude.com/docs/en/common-workflows)
- [Anthropic: How the agent loop works — Agent SDK](https://platform.claude.com/docs/en/agent-sdk/agent-loop)
- [Shipyard: Multi-agent orchestration for Claude Code in 2026](https://shipyard.build/blog/claude-code-multi-agent/)
- [ClaudeFast: Claude Code Agent Teams Complete Guide 2026](https://claudefa.st/blog/guide/agents/agent-teams)
- [VentureBeat: Claude Code's Tasks update — longer coordination across sessions](https://venturebeat.com/orchestration/claude-codes-tasks-update-lets-agents-work-longer-and-coordinate-across)
- [Addy Osmani: My LLM coding workflow going into 2026](https://medium.com/@addyosmani/my-llm-coding-workflow-going-into-2026-52fe1681325e)
- [ZenML: What 1,200 Production Deployments Reveal About LLMOps in 2025](https://www.zenml.io/blog/what-1200-production-deployments-reveal-about-llmops-in-2025)
- [Directual: AI Agents in 2025 — Why 95% of Corporate Projects Fail](https://www.directual.com/blog/ai-agents-in-2025-why-95-of-corporate-projects-fail)
- [Victor Dibia: Context Engineering 101 — How Agents Like Claude Code Manage Context](https://newsletter.victordibia.com/p/context-engineering-101-how-agents)
- [DEV: Claude Code new Tasks persisting between sessions and Swarms against Context Rot](https://dev.to/simone_callegari_1f56a902/claude-code-new-tasks-persisting-between-sessions-and-swarms-of-agents-against-context-rot-5dan)
- [DEV: Running Multiple Claude Code Sessions in Parallel with git worktree](https://dev.to/datadeer/part-2-running-multiple-claude-code-sessions-in-parallel-with-git-worktree-165i)
- [Medium: Mastering Git Worktrees with Claude Code for Parallel Development Workflow](https://medium.com/@dtunai/mastering-git-worktrees-with-claude-code-for-parallel-development-workflow-41dc91e645fe)

Excellent. This is a well-defined system with a clear goal: transitioning from a meticulously designed specification to a living, breathing operational habit for a CEO. The Karpathy-inspired, plain-text approach is powerful but requires discipline. This activation plan focuses on building that discipline through incremental adoption, quick wins, and clear protocols.

Here is the comprehensive activation plan for 1658 Holdings Oy's wiki system.

***

## Comprehensive Wiki Activation Plan: 1658 Holdings Oy

**To:** CEO, 1658 Holdings Oy
**From:** Audit & Implementation
**Date:** April 13, 2026
**Subject:** Phased activation plan for the Karpathy-inspired AI-Wiki system.

### Executive Summary

The wiki system's design is robust and fit-for-purpose. The current challenge is purely one of activation and habit formation. We will not attempt a "big bang" rollout. Instead, this is a four-phase, five-week plan designed to integrate the wiki into your existing 5-8 weekly Claude sessions. The focus is on immediate value, reducing cognitive load (`MEMORY.md` migration), and progressively building the system into an indispensable operational dashboard.

### Scoring Legend

Each action item is scored for **Impact** (how much it advances the system's utility) and **Effort** (CEO's time/focus required), on a scale of 1 (Low) to 5 (High).

---

### **Phase 0: Foundation & Critical Fixes (Week 1)**

**Goal:** Close the most critical operational loop and establish the basic workflow. This week is about making the system *work* as designed, providing immediate feedback and value.

| # | Action | Details | Impact | Effort |
|---|---|---|---|---|
| **0.1** | **Implement Startup Trigger** | Modify `CLAUDE.md` to include the `wiki_delta` compilation step at session startup. This is the single most important fix. | 5 | 1 |
| **0.2** | **Initial Obsidian Setup** | Install Obsidian, point it to the `~/1658HoldingsOy-AIFiles/` vault root, and install the Dataview plugin. This makes the files browsable and sets the stage for the dashboard. | 4 | 2 |
| **0.3** | **Migrate 3 Urgent Entities** | Perform the first `MEMORY.md` migration. Create entity pages for the three most time-sensitive items. This proves the value immediately. | 5 | 3 |

**Detailed Actions for Phase 0:**

**1. Q4: Session Startup Integration (Action 0.1)**

This ensures session deltas are never lost. Edit your master prompt file, `CLAUDE.md`, to change the session startup sequence.

**Current `CLAUDE.md` Startup (Implied):**
```
## SESSION STARTUP PROTOCOL
1. Read CURRENT-STATUS.md
2. Run /recon
3. Load warm pack
...
```

**New `CLAUDE.md` Startup Text:**
```
## SESSION STARTUP PROTOCOL
0. **Wiki Delta Ingest:** Check for any file named `SESSION-BRIDGE-*.md`. If found, locate the `%% wiki_delta_start %%` block. Run `/wiki ingest` on its content. On success, rename the bridge file to `processed-SESSION-BRIDGE-*.md`.
1. **Status Read:** Read CURRENT-STATUS.md
2. **Reconnaissance:** Run /recon
3. **Load Memory:** Load warm pack
...
```
*   **Failure Mode If Skipped:** Critical insights, decisions, and data points captured in the `wiki_delta` block at the end of a session will be orphaned in the bridge file. The central entity pages will become stale, defeating the purpose of the wiki. The system's "memory" will fragment across dozens of bridge files.

**2. Q2: Initial `MEMORY.md` Migration (Action 0.3)**

We will start the migration with a high-impact batch. At the start of a session, use this prompt:
> "/goal Create 3 new entity pages by migrating content from MEMORY.md. For each, generate the full page structure.
> 1.  **M365 Anthropic Subprocessor** (type: project, status: active, deadline: May 1, 2026!)
> 2.  **Järvisydän konserni** (type: company, status: saneeraus)
> 3.  **Karpathy Wiki system** (type: project, status: activation)"

After Claude generates them, manually replace the corresponding lines in `MEMORY.md` with a single pointer line, e.g., `* M365 Anthropic Subprocessor -> [[entities/projects/m365-anthropic-subprocessor.md]]`.

---

### **Phase 1: Habit Formation & Content Population (Weeks 2-3)**

**Goal:** Systematically reduce `MEMORY.md` while populating the wiki with the core entities. This phase focuses on the repetitive action of creating 1-2 pages per day, making it a routine.

| # | Action | Details | Impact | Effort |
|---|---|---|---|---|
| **1.1** | **Establish Migration Cadence** | At the start of the first session of each day, migrate 2-3 lines from `MEMORY.md` into new entity pages. | 5 | 2 |
| **1.2** | **Create Core Company Entities** | Create pages for the remaining portfolio companies (DMC Finland, FinnConcierge, JS-saneeraus entities). | 4 | 3 |
| **1.3** | **Design & Create First `concepts/`** | Define the structure for reusable knowledge and create the first `concepts/` page for `DSCR + Finnish bank financing`. | 5 | 3 |

**Detailed Actions for Phase 1:**

**1. Q2: `MEMORY.md` Migration Strategy (Action 1.1)**

*   **Strategy:** The "Two-a-Day" rule. The first task of your first daily session is to convert two `MEMORY.md` entries into entity pages. This is a small, achievable task that builds momentum. Do not aim for more; consistency is key.
*   **Process:**
    1.  Pick two related, high-context lines from `MEMORY.md`.
    2.  Use a prompt: `/goal Migrate these two topics from MEMORY.md into full entity pages: [paste lines here]`.
    3.  Review, save the files, and update `MEMORY.md` with the pointer links.
*   **Risks & Mitigations:**
    *   **Risk:** Creating shallow, low-quality stubs just to clear the backlog.
    *   **Mitigation:** Set the `confidence` score in the frontmatter to `2` (Low) for pages created this way. This flags them for review during the formal "Wiki Compilation Session."

**2. Q3: `concepts/` Entity Design (Action 1.3)**

Reusable concepts are the force multiplier of this system. They need a distinct structure focused on principles, not status.

**Template for `concepts/vieraspantti.md`:**
```yaml
name: Vieraspantti (Third-party Pledge)
type: concept
status: evergreen
last_updated: 2026-04-13
session: CLAUDE_20260413_1
confidence: 4 # High confidence in the definition
tags: [real-estate, financing, legal, finnish-law]
linked: [[DSCR + Finnish bank financing]], [[tonttirahoitus]]
sources: [kauppakaari.fi, lawyer_email_2025-11-08]
---
## Core Principle (1-2 sentences)
Vieraspantti is a Finnish legal concept where a property owner allows their property to be used as collateral for another person's or entity's debt, without being the debtor themselves.

## Mechanism & Application
- **Who:** A third-party asset owner (vieraspanttausvelallinen) pledges an asset for the primary debtor.
- **Why:** Common in corporate financing where a parent company provides security for a subsidiary, or in family arrangements.
- **Key Legal Point:** The pledgee's rights are limited to the pledged asset. They cannot pursue the third-party owner for any shortfall.

## Application in 1658 Holdings
- **Järvisydän Saneeraus:** Explored as a mechanism for securing new working capital using assets from a healthier group company. (See [[Järvisydän konserni]])
- **Tonttirahoitus:** A potential structure for future land acquisition projects to separate land ownership from development company debt.

## Risks & Caveats
- The asset is at risk of foreclosure if the primary debtor defaults.
- Complex inter-company agreements are required.
- Valuation of the pledged asset is critical.
```

---

### **Phase 2: Operationalization & Quality Control (Week 4)**

**Goal:** Transform the populated wiki from a passive repository into a proactive operational tool.

| # | Action | Details | Impact | Effort |
|---|---|---|---|---|
| **2.1** | **Build Obsidian Dashboard** | Create a `00_DASHBOARD.md` file using Dataview queries to provide a real-time operational view. | 5 | 3 |
| **2.2** | **Formalize Compilation Session** | Define the protocol for the periodic "Opus Review" (every 10 sessions) in a Best Practice (`BP`) file. | 4 | 2 |
| **2.3** | **Activate `/wiki lint`** | Begin using the lint command during the Compilation Session to ensure quality and prevent staleness. | 4 | 1 |

**Detailed Actions for Phase 2:**

**1. Q5: Obsidian Operational Dashboard (Action 2.1)**

Create a file named `00_DASHBOARD.md` in the vault root. Install the **Obsidian Tasks** and **Kanban** plugins in addition to Dataview.

**`00_DASHBOARD.md` Content:**
````markdown
# 1658 Holdings Oy - Operational Dashboard

## ⚠️ Action Items & Deadlines
```dataview
TASK
FROM #entities 
WHERE !completed
SORT status
```

## ?? Open Questions
*List all open questions across the entire wiki.*
```dataview
TABLE WITHOUT ID
link(file.link, name) as Entity,
Open_Questions as "Questions"
FROM #entities 
WHERE Open_Questions
```

## Decision Pipeline (Projects)
*Projects sorted by current status.*
```dataview
TABLE status, confidence, last_updated
FROM #entities/projects 
SORT status DESC
```

## Portfolio Health Check (Companies)
```dataview
TABLE status, confidence, linked
FROM #entities/companies 
SORT name ASC
```
````

**2. Q7: Quality Gate / Linting (Action 2.3)**

During the Wiki Compilation Session, run `/wiki lint`. The command should be configured to check for:
1.  **Staleness:** Pages where `last_updated` is > 30 days ago.
2.  **Low Confidence:** Pages with `confidence` < 3.
3.  **Incomplete State:** Pages where the `## Current State` section is empty or contains "TBD".
4.  **Orphaned Pages:** Pages with no `linked` entries (optional, some concepts may be new).

The lint command should output a list of files to be reviewed during the session, forcing a quality check.

---

### **Phase 3: Scaling & Refinement (Week 5 and Ongoing)**

**Goal:** Solidify advanced workflows and guard against system decay.

| # | Action | Details | Impact | Effort |
|---|---|---|---|---|
| **3.1** | **Define Bridge-to-Entity Protocol** | Establish the rule for when `SESSION-BRIDGE` content gets promoted to a permanent entity page. | 3 | 2 |
| **3.2** | **Review & Mitigate Anti-Patterns** | Consciously review the system against common failure modes. | 5 | 1 |
| **3.3** | **Finalize `MEMORY.md`** | Ensure `MEMORY.md` is now <30 lines and serves purely as a pointer index and temporary scratchpad. | 4 | 2 |

**Detailed Actions for Phase 3:**

**1. Q8: Bridge → Entity Migration (Action 3.1)**

*   **Trigger:** This is a **manual** process, not automatic. It occurs during the periodic Wiki Compilation Session.
*   **Rule:** Promote bridge content to an entity page (or append it to an existing one) if and only if: **"Does this information have value independent of the session in which it was created?"**
    *   **YES:** A new strategic insight, a final decision, a reusable contact, a key number that changes an entity's state. -> **Migrate.**
    *   **NO:** Intermediate reasoning, dead-end ideas, session-specific instructions for the AI. -> **Leave as-is in the `processed-` bridge file for archival.**

**2. Q6: Anti-Patterns to Avoid**

This is a checklist for the Compilation Session.

1.  **The Graveyard:** The wiki becomes write-only.
    *   **Protection:** The Obsidian Dashboard (Action 2.1) and `/wiki lint` for staleness (Action 2.3) force you to read and engage with old content.
2.  **Perfectionism Paralysis:** Hesitation to create a page because information is incomplete.
    *   **Protection:** The `confidence` score in the frontmatter is designed for this. It's okay to create a page with `confidence: 1` and a list of open questions.
3.  **The Black Hole:** Ingesting source documents (`/wiki ingest`) without synthesizing them into the `## Summary` and `## Current State`.
    *   **Protection:** The linter should check for an empty `Current State` (Action 2.3). The session-end protocol must emphasize updating this section.
4.  **The Garden of Forking Paths:** Creating duplicate entities (e.g., `dscr.md` and `debt-service-coverage-ratio.md`).
    *   **Protection:** The `NAMESPACE.md` file and the habit of running `/wiki query [topic]` before creating a new entity.
5.  **Tool Tinkering Trap:** Spending more time optimizing Obsidian plugins and views than adding and synthesizing knowledge.
    *   **Protection:** This plan specifies a minimal, high-value set of plugins. Defer any further customization for at least two months. The value is in the text, not the tool.
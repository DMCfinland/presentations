# Deep Research Prompt: Claude Code Session Orchestration for Multi-Company Holdings

## HOW TO USE
Upload `AI_Knowledge_Architecture_Report.docx` alongside this prompt into a new Opus deep research conversation on claude.ai.

---

## PROMPT START

I need deep research on orchestrating multiple Claude Code sessions across a multi-company holdings structure. I'm uploading my existing AI Knowledge Architecture Report as context — it describes my 10-company holdings structure, the Claude Teams project architecture, and the SharePoint knowledge base design.

### MY SITUATION

- **1658 Holdings Oy** = Heiskanen family portfolio holding company, 10 operating companies, ~50 employees
- **Finland DMC Oy** = first pilot company (5-person DMC, destination management)
- I have Claude Teams (launching now) + Claude Code installed on my Mac
- My architecture report covers claude.ai Projects structure — but it does NOT cover how Claude Code fits into the picture
- I'm currently working from a local Mac folder: `1658HoldingsOy-AIFiles/` with company subfolders
- I need to understand the OPTIMAL file storage and Claude Code session management strategy

### WHAT I NEED RESEARCHED

#### 1. Claude Code Session Orchestration Patterns

Research how people are using multiple Claude Code sessions in practice:

- **Multi-project orchestration:** How do you run Claude Code across multiple related projects without them stepping on each other? Can you have multiple Claude Code sessions open simultaneously for different companies?
- **CLAUDE.md architecture for multi-project setups:** How should CLAUDE.md files be structured when you have a parent holdings folder with child company folders? Can Claude Code inherit instructions from parent directories?
- **Session isolation vs. shared context:** When should Claude Code sessions be isolated (company-specific work) vs. have shared context (holdings-wide work)?
- **Task delegation patterns:** The "orchestrator" pattern where one Claude Code session delegates to others — is this real? How does it work? What are the current limitations (Feb 2026)?
- **Claude Code + claude.ai interplay:** Best practices for using Claude Code as the file organizer while claude.ai does the creative/mining work. How do teams hand off between the two?

#### 2. File Storage Strategy for Claude Code

Research the optimal file storage approach for my specific situation:

- **Local Mac vs. cloud-synced folders:** Claude Code works with local files. If my files are in SharePoint/OneDrive (which syncs locally via OneDrive for Mac), does Claude Code work with synced folders? Are there gotchas (sync conflicts, file locking, .tmp files)?
- **Git vs. no-git for non-code projects:** My project is prompt files and .md/.txt documents, not software. Is Git still valuable? Or is it overhead for a text-file project? What about Git for version tracking CLAUDE.md and ROADMAP.md across companies?
- **Folder structure for Claude Code:** Research how the folder hierarchy affects Claude Code's behavior. Does it read CLAUDE.md from parent directories? How deep does it look? What's the optimal nesting depth?
- **File size and count limits:** What happens when Claude Code needs to work with hundreds of files across 10 companies? Are there practical limits?
- **Backup and versioning without Git:** If not using Git, what's the best way to version-track prompt files and project configuration?

#### 3. Multi-Company Claude Code Architecture

Design recommendations for my specific holdings structure:

- **One Claude Code workspace vs. many:** Should I have one big workspace at `1658HoldingsOy-AIFiles/` or separate workspaces per company? What are the tradeoffs?
- **Shared resources pattern:** My architecture has "universal" files (prompt libraries, best practices, training materials) used across all companies. How should these be structured so Claude Code in any company folder can reference them?
- **CLAUDE.md inheritance chain:** Can I have a top-level CLAUDE.md at the holdings level + company-level CLAUDE.md files? How does Claude Code resolve these?
- **Memory and project settings:** How do `.claude/` settings and memory files work across multiple projects? Can Claude Code remember context from one company when working on another?
- **Scaling from 1 to 10 companies:** What changes when I go from Finland DMC (working now) to having 10 company folders active?

#### 4. Current State of Claude Code Features (Feb 2026)

Research the latest Claude Code capabilities relevant to orchestration:

- **Subagents / Task tool:** Can Claude Code spawn sub-sessions? What's the current capability?
- **MCP servers:** Can Claude Code connect to custom MCP servers that provide cross-company data?
- **Background tasks:** Can Claude Code run long processes across multiple folders?
- **Hooks and automation:** Pre/post-commit hooks, custom commands — what's possible?
- **Claude Code on Teams plan:** What's different from Pro? Any orchestration features exclusive to Teams/Enterprise?
- **Planned features:** Anything announced for 2026 that would change orchestration patterns?

#### 5. Where Should Files Live RIGHT NOW (Feb 2026)?

Given everything above, make a concrete recommendation:

- My current structure: `1658HoldingsOy-AIFiles/FinlandDMCOy-AIFiles/finland-dmc-2.0/`
- My architecture report proposes SharePoint as the knowledge base
- Claude Code needs local file access
- I need to work across companies
- I'm one person managing this right now (not 50 people yet)

**Decision I need help with:**
- Keep files on local Mac in the current folder structure?
- Move to OneDrive-synced folder so files are also in SharePoint?
- Use Git for versioning?
- Some hybrid approach?
- What's the migration path as I scale from 1 to 10 companies?

### OUTPUT FORMAT

Structure your research as:

1. **Executive Summary** — one paragraph, the key recommendation
2. **Claude Code Orchestration Patterns** — what's possible today, with examples
3. **File Storage Decision Matrix** — options compared with pros/cons for MY situation
4. **Recommended Architecture** — concrete folder structure + CLAUDE.md hierarchy
5. **Migration Roadmap** — from current (1 company, local Mac) to target (10 companies, team access)
6. **Current Limitations & Workarounds** — what doesn't work yet and how to handle it
7. **Sources & Further Reading** — links to documentation, community examples, official guides

Be specific to my situation. I'm a CEO, not a developer. I need practical recommendations I can execute this week, not theoretical architecture. But I also need the architecture to be correct for scaling.

## PROMPT END

# Finland DMC Company 2.0: AI-Powered Dashboard Architecture Analysis

**Date:** February 8, 2026  
**Company:** Finland DMC Oy (5-person team)  
**Contact:** Patrick  
**Current Stack:** Microsoft 365 (Excel, Outlook, OneDrive)  
**AI Goal:** Transform into "Company 2.0" with integrated AI workflow automation

---

## Executive Summary

Patrick is exploring how to create an integrated AI architecture where staff work through personalized dashboards that orchestrate both Claude (Anthropic) and Copilot (Microsoft) to automate operations across OneDrive, Outlook, and internal workflows. The vision is for staff to have "one place of work" where they speak to Claude, which then orchestrates Copilot to execute M365 operations.

**Key Question:** Is it technically feasible to build: Staff Dashboard → Claude → Copilot → M365 (actionable write access)?

---

## Conversation Context & Evolution

### Initial Vision
Patrick initially asked whether Claude Teams Projects are the only way to use the service, exploring if he could create a "vast data structure" with personalized dashboards for each staff member.

### First Discovery: M365 Connector Limitations
- Claude Teams HAS M365 connector (SharePoint, OneDrive, Outlook, Teams)
- **READ ONLY** - Cannot create, edit, or upload files to M365
- Claude CAN create files in its own environment → user downloads → manual upload to OneDrive

### Second Discovery: Claude in Excel Exception
- **"Claude in Excel" add-in** (FREE for paid Claude users)
- Official Microsoft AppSource add-in
- Can READ and WRITE Excel files directly
- Works with local files (no OneDrive requirement)
- Powered by Claude Opus 4.5
- **No equivalent for Word, PowerPoint, or Outlook**

### Third Discovery: Copilot's Write Capabilities
- Microsoft Copilot CAN write directly into M365 files
- Creates documents in OneDrive
- Edits Excel spreadsheets in place
- Drafts and sends Outlook emails
- Cost: €30/user/month (€150/month for 5 people)

### Current Challenge
Patrick wants to bridge Claude (superior reasoning) with Copilot (M365 write access) so staff can:
1. Interact with ONE interface (Claude)
2. Have Claude orchestrate Copilot operations
3. Achieve full read/write automation across M365
4. Build personalized "dashboards" that become their primary workspace

---

## Technical Components Discovered

### 1. Anthropic Cowork (Desktop Agent)
**Status:** Research preview, macOS only (Windows planned)  
**Availability:** Claude Max subscribers ($100-200/month)  
**Capabilities:**
- Folder-level access to local files
- Read, edit, create files autonomously
- Multi-step workflow automation
- Browser automation via Claude in Chrome
- Plugin/connector ecosystem
- Sandboxed execution environment

**Limitations:**
- No direct M365 write integration
- macOS only currently
- Cannot use within Claude Projects
- No session persistence (app must stay open)
- External connectors "not that reliable yet"

**Relevance to Vision:**
Could serve as the local automation layer, but needs bridge to M365 cloud services.

### 2. Model Context Protocol (MCP)
**What it is:** Open protocol for connecting AI agents to external data sources  
**Microsoft's Adoption:** Microsoft is implementing MCP across their ecosystem

**Key MCP Servers Identified:**

**a) CLI for Microsoft 365 MCP Server**
- GitHub: `pnp/cli-microsoft365-mcp-server`
- Allows natural language execution of M365 commands
- Can manage: Entra ID, OneDrive, Outlook, Planner, Power Apps, Power Automate, SharePoint, Teams
- Works with Claude Desktop, VS Code GitHub Copilot
- Uses globally installed CLI for Microsoft 365

**b) Power Automate MCP Server**
- GitHub: `rcb0727/powerautomate-mcp-docs`
- Create, manage, deploy Power Automate flows via natural language
- Works with Claude Desktop, Claude Code, VS Code Copilot
- Features: Flow creation, testing, debugging, validation
- Also manages: Power Apps, environments, DLP policies, Dataverse

**c) Dataverse MCP Server**
- Microsoft's official MCP implementation
- Connects Claude to Microsoft Dataverse
- Can be used in Copilot Studio agents
- Natural language interface to business data

**d) Power Platform Custom MCP Servers**
- Microsoft now allows custom MCP server creation
- Bridge between agents and internal systems
- Can combine connector actions, tools, custom APIs

### 3. Microsoft Copilot Studio
**Critical Finding:** Copilot Studio supports MCP servers!  
- Can connect to external MCP servers
- Custom connectors bridge MCP servers to Copilot Studio
- Agents can use MCP tools directly
- Requires OpenAPI specification for custom connectors

**Implication:** This creates a potential pathway:
```
Claude Desktop → MCP Server → Copilot Studio Agent → M365 Operations
```

### 4. Power Automate as Middleware
**Discovery:** Power Automate can:
- Be controlled via MCP (Power Automate MCP Server)
- Trigger M365 operations
- Connect to Copilot via Power Platform
- Bridge external systems

**Potential Architecture:**
```
Claude (reasoning) → Power Automate (orchestration) → Copilot (M365 execution)
```

---

## Three Possible Architectures

### Architecture A: Manual Bridge (Achievable Today)
```
Staff → Claude Teams (M365 connector for reading)
         ↓
    Claude generates exact Copilot prompts
         ↓
    Staff copies prompts to Copilot
         ↓
    Copilot executes M365 operations
```

**Pros:**
- No custom development
- Works immediately
- Combines Claude's intelligence with Copilot's access

**Cons:**
- Manual copy/paste step
- Not true automation
- Breaks the "single interface" vision

### Architecture B: MCP Bridge (Technical Implementation Required)
```
Staff → Claude Desktop with Cowork (macOS)
         ↓
    CLI for Microsoft 365 MCP Server
         ↓
    Power Automate MCP Server
         ↓
    M365 Operations (OneDrive, Outlook, etc.)
```

**Pros:**
- True automation possible
- Claude can execute M365 commands directly
- Single interface for staff

**Cons:**
- Requires MCP server setup/configuration
- macOS only (Cowork limitation)
- Technical expertise needed
- Community-built servers may lack enterprise support

### Architecture C: Enterprise Integration (Custom Development)
```
Staff Dashboard (Custom UI/Claude Projects frontend)
         ↓
    Claude Teams (via API)
         ↓
    Custom MCP Server (Power Platform)
         ↓
    Copilot Studio Agent
         ↓
    M365 Services (full read/write)
```

**Pros:**
- Full control over user experience
- Could build actual visual dashboards
- Enterprise-grade security/governance
- Platform-agnostic (not limited to macOS)

**Cons:**
- Significant development effort
- Requires Power Platform expertise
- Higher cost (development + infrastructure)
- Maintenance overhead

---

## Key Findings: What IS and ISN'T Possible

### ✅ POSSIBLE TODAY

1. **Claude reads M365 data** (via M365 connector)
2. **Claude creates files** (in Claude environment, download required)
3. **Claude works in Excel** (via free add-in, full read/write)
4. **Copilot writes to M365** (direct integration)
5. **MCP servers connect Claude to M365 tools** (CLI for M365, Power Automate)
6. **Copilot Studio can use MCP servers** (bridge between systems)
7. **Power Automate can orchestrate workflows** (middleware potential)

### ❌ NOT POSSIBLE TODAY (Without Custom Development)

1. **Direct Claude → Copilot communication** (no native API integration)
2. **Visual dashboards in Claude** (conversational interface only)
3. **Real-time auto-updating task lists** (requires custom UI)
4. **Cowork + M365 write** (Cowork lacks native M365 write integration)
5. **Windows Cowork** (macOS only currently)
6. **True agentic orchestration** (Claude doesn't "control" Copilot automatically)

### ⚠️ POSSIBLE WITH WORK

1. **MCP-based automation** (setup CLI for M365 + Power Automate MCP servers)
2. **Custom dashboard UI** (frontend → Claude API → MCP → M365)
3. **Power Automate middleware** (bridge Claude and Copilot operations)
4. **Task management via Excel** (Claude in Excel add-in + OneDrive structure)

---

## Practical Implementation for Finland DMC

### Option 1: Quick Start (No Development)
**Cost:** €125/month (Claude Teams only)

**Setup:**
1. OneDrive folder structure for staff workspaces
2. Claude Projects per staff member with M365 connector
3. Claude in Excel add-in for task management
4. Staff use manual bridge pattern for Word/PPT creation

**Workflow:**
```
Staff: "Create client proposal for Swedish group"
Claude: [Reads templates, generates content, outputs Copilot prompt]
Staff: [Copies to Copilot in Word]
Copilot: [Creates document in OneDrive]
```

### Option 2: MCP Automation (Technical Setup)
**Cost:** €125/month (Claude) + technical time
**Requirements:** macOS for Cowork, technical staff for MCP setup

**Setup:**
1. Install Cowork (Claude Max subscribers)
2. Configure CLI for Microsoft 365 MCP server
3. Configure Power Automate MCP server
4. Build workflow automation patterns

**Workflow:**
```
Staff: "Create and save client proposal to OneDrive/Clients/"
Claude + Cowork: [Executes M365 CLI commands via MCP]
                 [Creates file directly in OneDrive]
```

### Option 3: Hybrid Approach (Balanced)
**Cost:** €275/month (Claude Teams + Copilot for 2-3 power users)

**Setup:**
1. Claude Teams for all staff (reading, analysis, strategy)
2. Claude in Excel for task management
3. Copilot licenses for 2-3 staff who frequently create M365 documents
4. Manual bridge pattern where needed

**Workflow:**
- Patrick (power user): Uses both Claude and Copilot directly
- Other staff: Primarily use Claude, occasional Copilot for document creation

---

## Unanswered Questions Requiring Deep Research

### Primary Research Questions:

1. **Can CLI for Microsoft 365 MCP server provide full write access to OneDrive/Outlook?**
   - What are the exact capabilities?
   - What are the authentication/permission requirements?
   - Are there rate limits or restrictions?

2. **Can Power Automate MCP server trigger Copilot Studio agents?**
   - Is there a documented integration pathway?
   - Can this create the Claude → Copilot bridge automatically?

3. **What is the state of Cowork + M365 integration?**
   - Is there a roadmap for native M365 write support in Cowork?
   - Are there existing Cowork plugins for M365 operations?

4. **Can a custom MCP server bridge Claude and Copilot effectively?**
   - What would the architecture look like?
   - What are the security/governance considerations?
   - Has anyone built this already?

5. **What does the "dashboard" architecture realistically look like?**
   - Can Claude Projects be embedded in a custom UI?
   - Is there a Claude API for building custom frontends?
   - What are the UX limitations?

6. **Windows compatibility timeline?**
   - When will Cowork support Windows?
   - Are there workarounds for Windows users today?

7. **Enterprise deployment considerations:**
   - What are the security implications of MCP server usage?
   - How do you manage authentication across Claude, MCP, Copilot?
   - What governance controls are needed?

8. **Cost-benefit analysis:**
   - What is the ROI of custom development vs. manual workflows?
   - At what team size does automation become cost-effective?
   - What are the hidden costs (maintenance, training, support)?

---

## Recommended Next Steps

### Immediate (This Week)
1. Set up Claude Teams with M365 connector
2. Test Claude in Excel add-in with task management spreadsheet
3. Create sample OneDrive folder structure
4. Build one Claude Project as proof of concept

### Short-term (1-3 Months)
1. Experiment with manual bridge pattern
2. Evaluate Copilot licenses for 2-3 power users
3. Document workflow patterns that work well
4. Assess staff adoption and pain points

### Medium-term (3-6 Months)
1. If macOS users: Explore Cowork + MCP setup
2. Consider Power Automate for repetitive workflows
3. Decide: Continue with manual bridge or invest in automation?
4. Gather ROI data to justify further investment

### Long-term (6-12 Months)
1. Evaluate custom dashboard development
2. Consider enterprise Power Platform implementation
3. Wait for Cowork Windows support
4. Reassess market solutions (tech evolves quickly)

---

## Critical Success Factors

1. **Start simple** - Manual bridge pattern proves the concept
2. **Measure everything** - Track time saved, errors reduced, staff satisfaction
3. **Iterate based on usage** - Let actual workflows guide automation priorities
4. **Stay flexible** - AI tooling landscape changes rapidly
5. **Invest in training** - Staff need to understand the new workflows
6. **Maintain security** - Don't sacrifice data protection for convenience

---

## Conclusion

Patrick's vision of staff working through integrated dashboards that orchestrate Claude and Copilot IS technically possible, but requires different levels of investment:

- **Today:** Manual bridge pattern (achievable immediately, €125/month)
- **Technical Implementation:** MCP-based automation (requires setup, macOS only)
- **Full Vision:** Custom development (significant investment, 6-12 months)

The most pragmatic path forward: Start with manual bridge + Claude in Excel, prove ROI, then invest in automation as the benefits become clear. The technology is evolving rapidly - what requires custom development today may be a built-in feature in 6 months.

---

**Prepared for:** Deep research by Claude Opus 4.6  
**Purpose:** Comprehensive technical feasibility study and implementation roadmap

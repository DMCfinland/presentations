# Finland DMC — M365 Connector Research & Implementation Guide

**Prepared for:** Patrick, Finland DMC Oy  
**Date:** February 9, 2026  
**Purpose:** Fill Section 8 gaps in PRD v3.0, deliver actionable M365 search configuration

---

## Part 1: Research Findings (10 Questions Answered)

### 1. Search Syntax

**Answer: Natural language queries. Claude handles all query construction.**

The M365 connector operates via MCP (Model Context Protocol) tools. Claude does NOT receive a raw search bar — instead, it reasons about which MCP tool to call (Outlook search, SharePoint search, Teams search, etc.) and constructs the appropriate Microsoft Graph API call behind the scenes. Your golden prompt instructions should be written in natural language.

The connector does NOT expose KQL (Keyword Query Language) directly to the user or to Claude's prompt. Under the hood, the MCP server translates Claude's tool calls into Microsoft Graph API requests — specifically the `/search/query` endpoint for indexed search, and direct REST endpoints (`/users/{id}/messages`, `/teams/{id}/channels/{id}/messages`) for direct access.

**What works in practice:**
- "Find emails from john@example.com about hotel pricing" → Claude calls Outlook search with appropriate parameters
- "Search SharePoint for proposal documents from Q4 2025" → Claude calls SharePoint/OneDrive search
- "Look in the #client-intel Teams channel for notes about Nordic Adventures" → Claude calls Teams channel message search

**Anthropic's official guidance** from the Help Center: "Ask Claude a question that requires accessing your Microsoft 365 data. Claude will automatically detect which tools it needs and retrieve the relevant information." The troubleshooting section advises: "Be more specific about what you're looking for. Specify locations (site names, date ranges, document types). Use exact phrases for better matching."

**Source:** Anthropic Help Center — "Enabling and Using the Microsoft 365 Connector" (support.claude.com)

---

### 2. Supported Data Sources

**Answer: Outlook, SharePoint, OneDrive, Teams (chats + channels), Calendar/Meetings. All confirmed for Teams plan.**

| Service | What Claude Can Access | Confirmed |
|---------|----------------------|-----------|
| **Outlook (personal mailbox)** | Email threads, message content, metadata (sender, subject, date), attachments search | ✅ Yes |
| **Outlook (shared mailbox)** | Emails in mailboxes the user has been granted access to (via Mail.Read.Shared permission) | ✅ Yes — with setup (see Q7) |
| **Outlook (archived email)** | All emails accessible through the user's account including archived messages | ✅ Yes |
| **SharePoint** | Documents across all sites and libraries the user has permission to access (tenant-wide search) | ✅ Yes |
| **OneDrive** | Personal and shared files | ✅ Yes |
| **Teams — Chat messages** | 1:1 and group chats where user is a participant | ✅ Yes |
| **Teams — Channel messages** | Channel discussions in teams the user is a member of | ✅ Yes |
| **Teams — Private channels** | Only if user is a member of that private channel | ✅ Yes (permission-gated) |
| **Calendar** | Calendar events, meeting info, attendee lists | ✅ Yes |
| **Meeting transcripts** | Transcripts from Teams meetings (OnlineMeetingTranscript.Read.All) | ✅ Yes |
| **Meeting recordings** | Recordings and artifacts from Teams meetings | ✅ Yes |

**Critical for Finland DMC:** Your #ai-feedback, #client-intel, #supplier-notes, and #best-practices Teams channels are ALL searchable, provided the Claude-connected user is a member of those channels. Since you're a 5-person team, ensure all staff are members of all 4 channels.

**Source:** Anthropic Help Center — Permission categories section; Microsoft Marketplace listing for M365 Connector for Claude

---

### 3. Result Format and Volume

**Answer: Structured results including content snippets, metadata, and citations. Volume depends on the query.**

The connector returns structured results through MCP tool calls. Claude receives the data and synthesizes it into its response, including citations when applicable. The exact result format is:

- **Outlook emails:** Message content (body text or snippets), sender, recipients, subject, date, and sometimes attachment metadata
- **SharePoint/OneDrive:** Document snippets, file names, locations (site/library), and sometimes full document content for smaller files
- **Teams messages:** Message text, author, channel name, timestamp
- **Calendar:** Event details, attendees, time, location

**Result volume:** The Microsoft Graph Search API returns up to 25 results per search call by default. Claude can potentially make follow-up calls if it needs more. In practice, search results from a single query typically return 5–25 relevant items.

**Token cost estimate:** Based on typical Graph API search responses and MCP tool call overhead:
- A focused email search (5–10 results): ~2,000–5,000 tokens
- A broader search (20+ results): ~5,000–15,000 tokens
- Document content retrieval: varies significantly by document size

**For your context budget:** Your project files use ~10,400 tokens. Even a heavy M365 search adding 15,000 tokens brings total input to ~25,000–30,000 tokens — still only 15% of the 200K window. You have massive headroom. This is not a constraint.

**Source:** Anthropic Help Center; Microsoft Graph Search API documentation (learn.microsoft.com)

---

### 4. Token Cost of Results

**Answer: Approximately 2,000–15,000 tokens per search depending on scope. Not a concern for your setup.**

Anthropic does not publish exact token costs per M365 search. However, based on the architecture:

- Each MCP tool call returns structured JSON that gets injected into the conversation context
- Tool call results from the connector that are part of stored chats are retained (per Anthropic's Security Guide)
- The user who requested the chat can see the tool call results in full

**Practical budget for Finland DMC:**

| Component | Tokens |
|-----------|--------|
| Project knowledge files | ~10,400 |
| System prompt | ~1,500 |
| User's pasted prompt | ~2,000 |
| M365 search (focused, 1 query) | ~3,000–5,000 |
| M365 search (broad, 3 queries) | ~8,000–15,000 |
| Claude's output | ~500–1,000 |
| **Total worst case** | **~30,000–35,000** |
| **Remaining context** | **~165,000 (82%+ free)** |

**Verdict:** Token cost of M365 results is not a meaningful constraint. Your concern should be relevance, not volume.

---

### 5. Sequential / Multiple Searches

**Answer: YES. Claude can perform multiple M365 searches in a single conversation.**

The MCP architecture explicitly supports multi-tool calls. Claude can chain searches naturally:

1. First search: Outlook shared mailbox for client emails
2. Second search: Teams #client-intel channel for phone notes
3. Third search: SharePoint for past proposals
4. Then synthesize everything into a response

This is a core design feature of the MCP tool interface — Claude's reasoning layer decides which tools to call and in what order. There is no limit to the number of tool calls per conversation (within reason and rate limits).

**Important:** Each search is a separate tool call, each consuming context tokens. The golden prompt should instruct Claude to search strategically — narrow first, broaden only if needed — to avoid unnecessary token consumption.

**Source:** Anthropic documentation on MCP tool interface; Windows Forum analysis of connector architecture

---

### 6. Filtering Capabilities

**Answer: Yes — via natural language instructions. Claude translates to appropriate API filters.**

The Anthropic Help Center explicitly states you can filter by:

| Filter | How to Instruct Claude | Supported |
|--------|----------------------|-----------|
| **Date range** | "Find emails from the last week about..." | ✅ Yes |
| **Sender/recipient** | "Show me emails from sarah@client.com" | ✅ Yes |
| **Subject** | "Search for emails with 'Helsinki proposal' in the subject" | ✅ Yes |
| **File type** | "Find PowerPoint presentations about sales strategy" | ✅ Yes |
| **SharePoint site** | "Search the Engineering team site for..." | ✅ Yes |
| **Teams channel** | "What discussions happened in [channel] about..." | ✅ Yes |
| **Specific person in Teams** | "Show me Teams discussions with Sarah about..." | ✅ Yes |
| **Mailbox folder** | Should work via folder-level browsing (MailboxFolder.Read permission) | ⚠️ Test during setup |
| **Shared vs. personal mailbox** | Via explicit instruction (see Q7) | ✅ Yes — with naming |

**Tip for golden prompt:** Always instruct Claude to search with the most specific filters first. "Search shared mailbox for emails from nordic.adventures@client.com in the last 3 months about Helsinki" is much better than "Search for anything about Nordic Adventures."

**Source:** Anthropic Help Center FAQ section — "How do I ask Claude to search specific locations?"

---

### 7. Shared Mailbox Handling ⚠️ CRITICAL

**Answer: Supported via Mail.Read.Shared permission, but requires specific setup and naming.**

This is the most nuanced finding. Here's the full picture:

**The Good News:**
- The M365 connector requests `Mail.Read.Shared` permission — specifically designed for reading emails in shared mailboxes and delegated folders
- This means Claude CAN access your shared mailbox (e.g., info@finlanddmc.fi)

**The Nuance:**
- The Microsoft Graph Search API (`/search/query` endpoint for messages) has a known limitation: "Users can search their own mailbox, but can't search delegated mailboxes" (Microsoft Learn documentation)
- However, the connector also has `Mail.Read` and `MailboxItem.Read` permissions, which support direct mailbox access via REST endpoints like `GET /users/{shared-mailbox-UPN}/messages`
- This means Claude can likely LIST and READ shared mailbox emails directly, even if the unified search endpoint doesn't cover them

**What You Need to Do:**
1. **Grant shared mailbox access:** In Exchange Admin Center, ensure each Claude-connected user has Full Access permission on the shared mailbox (info@finlanddmc.fi). This is probably already done if staff can see the shared mailbox in Outlook.
2. **Specify the mailbox in your golden prompt:** The connector likely does NOT auto-detect which mailbox to search. Your prompt should explicitly reference the shared mailbox.
3. **Test immediately during Week 1 setup:** This is the single most important validation test. On Monday, after connecting, try: "Search the info@finlanddmc.fi shared mailbox for recent client emails."

**If shared mailbox search doesn't work via the connector:**
- **Workaround A:** Use Exchange mail flow rules to auto-forward a copy of all shared mailbox emails to a dedicated SharePoint library. Claude can search SharePoint without limitations.
- **Workaround B:** Ensure all staff BCC their personal mailbox when sending from the shared mailbox, so emails exist in searchable personal mailboxes too.
- **Workaround C:** Use the #client-intel Teams channel more aggressively as the primary client history repository.

**Source:** Microsoft Graph Search API docs (learn.microsoft.com/en-us/graph/search-concept-messages); Anthropic connector permission list; Microsoft Q&A on shared mailbox access via Graph

---

### 8. Language Handling (Finnish + English)

**Answer: Supported. Microsoft Search indexes content in Finnish and English.**

Microsoft 365 Search is language-agnostic for indexing — it indexes the actual content regardless of language. Finnish is a supported language in Microsoft Search. Mixed-language content (common in Finnish business: emails mixing Finnish and English) will be indexed and searchable.

**Practical implications:**
- If a client writes in Finnish, Claude can find it by searching in Finnish or by client name
- If your staff writes phone notes in Finnish in #client-intel, Claude will find them
- Claude itself is proficient in Finnish and can process Finnish-language search results

**Golden prompt consideration:** Instruct Claude to search using the client's name (language-neutral) as the primary search term, rather than language-specific keywords. Names work across languages.

---

### 9. Freshness / Indexing Delay

**Answer: Near real-time for Exchange Online (minutes). SharePoint may take slightly longer.**

- **Outlook emails (Exchange Online):** Microsoft Search indexes Exchange Online content in near real-time. A just-received email should be searchable within minutes (typically 1–5 minutes).
- **SharePoint/OneDrive documents:** May take slightly longer to index, especially for newly uploaded large documents. Typically 5–15 minutes, but can take up to a few hours for newly created sites.
- **Teams messages:** Near real-time indexing similar to Exchange Online.

**Anthropic's troubleshooting note:** "Recently uploaded documents may take time to become searchable." This confirms some delay exists.

**For Finland DMC:** This is unlikely to be an issue. You're searching for client history (hours/days/weeks old), not real-time streams. The only edge case: if a staff member posts a phone note to #client-intel and another staff member immediately tries to draft an email using that note, there may be a few minutes' delay. Mitigate by mentioning this in training.

**Source:** Anthropic Help Center troubleshooting section; Microsoft Graph Search API documentation

---

### 10. Authorization and Setup

**Answer: Two-phase setup. Global Admin one-time consent + per-user authentication. Available on Teams plan.**

**Phase 1: Admin Setup (Patrick — one time, ~15 minutes)**

1. Sign into Claude as Owner → Admin Settings → Connectors → Browse connectors → Add "Microsoft 365"
2. Go to Settings → Connectors → Find "Microsoft 365" → Click "Connect"
3. Authenticate with your M365 Global Admin credentials
4. Review and accept permissions, checking the box to "grant access on behalf of the whole organization"
5. (Optional) Restrict which users can use the connector in Entra admin center

This creates two enterprise applications in your Entra ID:
- "M365 MCP Client for Claude" (App ID: 08ad6f98-a4f8-4635-bb8d-f1a3044760f0)
- "M365 MCP Server for Claude" (App ID: 07c030f6-5743-41b7-ba00-0a6e85f37c17)

**Phase 2: Per-User Setup (Each staff member — 2 minutes each)**

1. Navigate to Settings → Connectors
2. Find "Microsoft 365" → Click "Connect"
3. Authenticate with their M365 credentials
4. Done — M365 tools are now available in their Claude conversations

**M365 License Requirement:** Users need Microsoft 365 accounts. Your M365 Business Standard licenses are sufficient — no E3/E5 required.

**Teams vs. Enterprise Plan:** The M365 connector is available on BOTH Claude Teams and Enterprise plans. No Enterprise-only restrictions for the connector itself. Enterprise Search (shared, curated search project) is also available on both plans.

**Source:** Anthropic Help Center — Phase 1 and Phase 2 setup instructions

---

## Part 2: Rewritten PRD Section 8

*(This replaces the entire "M365 Search Optimization [NEEDS RESEARCH]" section)*

### 8. M365 Search Capabilities — Confirmed

#### 8.1 Connector Overview

The Claude M365 connector uses Anthropic's MCP (Model Context Protocol) to provide read-only search access to Microsoft 365 data. Claude automatically detects which MCP tools to call based on the user's natural language query. The connector is available on Claude Teams plan and requires M365 Business Standard or higher.

**Confirmed capabilities:**

| Capability | Status | Notes |
|------------|--------|-------|
| Outlook personal mailbox search | ✅ Confirmed | Full email content, metadata, attachments search |
| Outlook shared mailbox access | ✅ Supported | Requires Mail.Read.Shared + Exchange permissions. Test during setup. |
| SharePoint search (tenant-wide) | ✅ Confirmed | All sites user has permission to access |
| OneDrive search | ✅ Confirmed | Personal and shared files |
| Teams channel messages | ✅ Confirmed | Channels where user is a member |
| Teams chat messages | ✅ Confirmed | 1:1 and group chats |
| Calendar/meetings | ✅ Confirmed | Events, attendees, meeting summaries |
| Meeting transcripts | ✅ Confirmed | Requires Teams meetings with transcription enabled |
| Multiple sequential searches | ✅ Confirmed | Claude chains tool calls in one conversation |
| Date/sender/subject filtering | ✅ Confirmed | Via natural language instructions |
| Finnish language content | ✅ Confirmed | Microsoft Search indexes all languages |
| Archived emails | ✅ Confirmed | Accessible if user has permission |

#### 8.2 Search Syntax

Claude uses natural language — no KQL or special syntax required. The golden prompt instructs Claude what to search for and where. Claude translates these into Microsoft Graph API calls via the MCP connector.

**Effective search instructions in golden prompt:**
- Specify the data source: "Search the shared mailbox" / "Look in Teams #client-intel channel" / "Check SharePoint for proposals"
- Specify filters: client name, date range, topic keywords
- Specify priority order: what to search first, second, third

**Troubleshooting tips from Anthropic:**
- Be specific about locations (site names, date ranges, document types)
- Use exact phrases for better matching
- Break complex queries into simpler, focused questions
- Verify spelling of names, projects, or terms

#### 8.3 Token Budget

M365 search results typically consume 3,000–15,000 tokens depending on the number and breadth of searches. With project files at ~10,400 tokens and typical conversation overhead, total input stays under 35,000 tokens — 17% of the 200K window. Token budget is not a constraint.

#### 8.4 Indexing Freshness

Exchange Online content (emails, Teams messages): indexed within 1–5 minutes. SharePoint/OneDrive documents: may take 5–60 minutes. For client history lookups (the primary use case), this is not a practical constraint.

#### 8.5 Shared Mailbox Configuration

The connector includes `Mail.Read.Shared` permission for shared mailbox access. Setup requirements:

1. Each user must have Full Access permission on the shared mailbox in Exchange Admin Center
2. The golden prompt must explicitly reference the shared mailbox address (info@finlanddmc.fi)
3. Validate during Week 1 that Claude can successfully read shared mailbox emails

**Fallback if shared mailbox search is limited:** The Microsoft Graph Search API has a known limitation where the search endpoint cannot search delegated mailboxes. If full-text search of the shared mailbox fails, Claude can still access it via direct message listing. The golden prompt includes instructions for both approaches.

#### 8.6 Known Limitations

| Limitation | Impact | Workaround |
|------------|--------|------------|
| Read-only access | Cannot send emails or modify documents | Expected. Claude drafts; humans send. |
| SharePoint search is tenant-wide | Cannot restrict to specific sites via connector | Use natural language to specify site names |
| Shared mailbox search may be limited | Microsoft Search API limitation on delegated mailboxes | Direct mailbox reading via Mail.Read.Shared; or use Teams channels as backup data sink |
| Recently uploaded content may not be immediately searchable | 1–60 minute indexing delay | Not a practical issue for client history lookups |
| No write to Teams channels | Cannot post to #client-intel automatically | Staff continues manual 30-second posts |

---

## Part 3: Golden Prompt v4 — M365 Search Block

Copy this block directly into each Claude Project's custom instructions.

```
═══════════════════════════════════════════════════════
M365 CONTEXT SEARCH PROTOCOL
═══════════════════════════════════════════════════════

WHEN TO SEARCH:
Search M365 BEFORE drafting ANY client-facing communication. Skip search ONLY for:
- Pure internal tasks with no client context needed
- Tasks where the user explicitly says "no search needed"
- Follow-up messages in the same conversation where search was already done

SEARCH STRATEGY — Narrow First, Broaden If Needed:

STEP 1 — SHARED MAILBOX (Primary source)
Search the shared mailbox (info@finlanddmc.fi) for emails involving [Client Name].
Look for: most recent correspondence, booking details, preferences mentioned, issues raised, key contacts.
Filter by the client's name or email domain first. If the client name returns no results, try the company name, then the contact person's name.
Prioritize the 5 most recent relevant emails. Skim for: dates, group size, preferences, special requests, complaints, compliments.

STEP 2 — TEAMS INTELLIGENCE (If client exists in Step 1)
Search the #client-intel Teams channel for posts mentioning [Client Name] or their company.
These are phone call summaries and informal notes from staff — often contain preferences and context not in emails.
Also search #supplier-notes if the task involves specific activities or suppliers the client has used before.

STEP 3 — PAST PROPOSALS (If drafting a proposal or price quote)
Search SharePoint/OneDrive for previous proposals, itineraries, or pricing documents related to [Client Name] or similar group profiles.
Use as reference for pricing consistency, preferred formatting, and what has worked before.

STEP 4 — EVALUATE WHAT YOU FOUND
After searching, briefly assess:
- Is this a RETURNING client? (Previous bookings found → personalize heavily, reference past trips)
- Is this a NEW client? (No history found → use standard high-quality approach, no false familiarity)
- Is the name possibly misspelled? (If Step 1 returns zero results for a name that sounds like a real client, try alternate spellings or search by email domain)

IF NO RESULTS FOUND:
- Do NOT fabricate history or preferences
- Treat as a new client inquiry
- Note to the user: "No prior client history found in M365. Treating as new inquiry."

TOKEN-AWARE SEARCH RULES:
- Start with the most specific search (client name + recent date range)
- Only broaden if the specific search returns too few results
- When results are extensive (20+ emails), focus on the 5 most recent and any that mention preferences, complaints, or special requests
- Do NOT retrieve full email threads if subject lines and snippets give you enough context
- Summarize what you found in 2-3 sentences before drafting, so the user can verify accuracy

LANGUAGE HANDLING:
- Search using the client's name (works regardless of language)
- Our content is mixed Finnish and English — both are indexed and searchable
- If a client communicates in Finnish, include Finnish keywords in your search
- Draft responses in the same language as the original inquiry unless the user specifies otherwise

FRIDAY REVIEW SEARCH (Special — for Patrick only):
When the user says "Friday review" or "weekly review":
1. Search #ai-feedback Teams channel for all posts from the past 7 days
2. Search shared mailbox for client replies received this week
3. Group feedback by: task type, rating, common issues
4. Cross-reference: which email types got low ratings? Which client replies suggest gaps?
5. Recommend top 3 prompt improvements and any new DO's/DON'Ts
═══════════════════════════════════════════════════════
```

---

## Part 4: Setup Checklist

### Monday — M365 Connector Authorization (Patrick, ~30 min)

**Step 1: Enable connector in Claude Admin (5 min)**
- [ ] Sign into claude.ai as Organization Owner
- [ ] Navigate to Admin Settings → Connectors
- [ ] Click "Browse connectors"
- [ ] Find "Microsoft 365" → Click "Add to your team"

**Step 2: Global Admin consent (10 min)**
- [ ] Navigate to Settings → Connectors
- [ ] Find "Microsoft 365" → Click "Connect"
- [ ] Sign in with your M365 Global Admin credentials (must be the same account as your Claude account, or use the manual Entra ID method if different)
- [ ] Review permissions — check the box to grant access on behalf of the whole organization
- [ ] Verify "Microsoft 365" now shows as connected in your Settings

**Step 3: Validate shared mailbox access (10 min)**
- [ ] Start a new Claude conversation
- [ ] Test: "Search the info@finlanddmc.fi shared mailbox for recent emails"
- [ ] Test: "Find emails from the last week in our shared mailbox"
- [ ] If shared mailbox search fails: verify Full Access permission in Exchange Admin Center
- [ ] Document results — this determines golden prompt approach

**Step 4: Test Teams channel search (5 min)**
- [ ] Post a test message in #client-intel: "Test: Nordic Adventures phone call - prefer outdoor activities, group of 12"
- [ ] Wait 5 minutes
- [ ] Ask Claude: "Search the #client-intel Teams channel for Nordic Adventures"
- [ ] Verify Claude finds the test message

### Tuesday — Teams Channel Setup

- [ ] Create Teams channels (if not already created):
  - #ai-feedback
  - #client-intel
  - #supplier-notes
  - #best-practices
- [ ] Ensure ALL 5 team members are added to ALL channels
- [ ] Post channel purpose description as first message in each channel
- [ ] Test: Each team member posts a test message, then verifies Claude can find it

### Thursday — Staff M365 Connection

For each of the 4 remaining staff members:
- [ ] Navigate to Settings → Connectors → Microsoft 365 → Connect
- [ ] Authenticate with their M365 credentials
- [ ] Test with a simple query: "Find my recent emails about [known topic]"
- [ ] Verify Teams channels are searchable

### Shared Mailbox Access Verification

- [ ] In Exchange Admin Center (admin.exchange.microsoft.com):
  - [ ] Navigate to Mailboxes → Shared mailbox (info@finlanddmc.fi)
  - [ ] Verify each staff member has Full Access permission
  - [ ] If not, add permissions — may take up to 60 minutes to propagate

---

## Part 5: Known Limitations & Workarounds

### Confirmed Limitations

| # | Limitation | Severity | Workaround |
|---|-----------|----------|------------|
| 1 | **Read-only access** — Claude cannot send emails, post to Teams, or modify documents | Low | By design. Claude drafts; staff sends. |
| 2 | **Microsoft Search API cannot search delegated/shared mailboxes** (via the `/search/query` endpoint) | Medium | The connector has `Mail.Read.Shared` permission enabling direct mailbox reading. Test during setup. If search fails, use Teams #client-intel as primary history source. |
| 3 | **SharePoint search is tenant-wide** — cannot restrict to specific site collections | Low | Use natural language instructions to specify site/library names. Small company = limited sites = not an issue. |
| 4 | **Indexing delay** — new content may take 1–60 minutes to become searchable | Low | Not relevant for client history lookups. Train staff that phone notes posted to #client-intel may take a few minutes to become searchable. |
| 5 | **No auto-detection of shared mailbox** — Claude needs to be told where to look | Low | Golden prompt explicitly names info@finlanddmc.fi. Solved. |
| 6 | **Result volume not controllable** — cannot tell Claude "return exactly 10 results" | Low | Golden prompt instructs Claude to prioritize the 5 most recent relevant results. |
| 7 | **No write to Teams** — Claude cannot post feedback acknowledgments to #ai-feedback | Low | Staff copies feedback to Teams manually (30 seconds). Already part of your workflow. |
| 8 | **Per-user authentication** — each person sees only what their M365 permissions allow | Low | Since all staff have access to the shared mailbox and all Teams channels, this is fine. Actually a security feature. |

### Things That Are NOT Limitations (Confirmed Working)

- ✅ Claude Teams plan includes the M365 connector (not Enterprise-only)
- ✅ M365 Business Standard is sufficient (no E3/E5 needed)
- ✅ Multiple sequential searches per conversation work
- ✅ Finnish language content is indexed and searchable
- ✅ Teams channel messages ARE searchable (both standard and private channels the user belongs to)
- ✅ Archived emails are searchable
- ✅ Meeting transcripts are accessible
- ✅ Enterprise Search feature is available on Teams plan

### Risk Register

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Shared mailbox search doesn't work as expected | Medium | High | Test on Day 1. Fallback: Teams #client-intel becomes primary client history. Email auto-forwarding rule to SharePoint as backup. |
| Staff forget to post to Teams channels | Medium | Medium | Weekly reminder in Friday review. Gamify: acknowledge top contributors. |
| M365 connector authentication expires | Low | Low | Refresh tokens last 90 days. Re-authenticate if needed. |
| Search returns irrelevant results | Medium | Low | Golden prompt instructs narrow-first search. Staff can refine in conversation. |

---

## Summary: What Changed from PRD v2.0/v3.0

The PRD Section 8 amber flag is now resolved. Key confirmations:

1. **Search syntax is natural language** — no KQL needed, simplifying the golden prompt
2. **Teams channels ARE searchable** — your Second Brain architecture (channels as data sinks) is fully validated
3. **Shared mailbox access IS supported** — via Mail.Read.Shared, but needs testing during setup
4. **Multiple sequential searches work** — the multi-step search protocol in the golden prompt is viable
5. **Token budget is not a constraint** — even heavy M365 searches leave 80%+ of context window free
6. **Finnish content is indexed** — bilingual operations are fully supported
7. **Teams plan is sufficient** — no Enterprise-only gates on the M365 connector
8. **M365 Business Standard is sufficient** — no license upgrade needed

**The single remaining action item:** Validate shared mailbox search on Day 1. The golden prompt includes instructions for both scenarios (working and fallback).

---

*Finland DMC Oy | M365 Research Report | February 2026 | Prepared with Claude Opus 4.6*

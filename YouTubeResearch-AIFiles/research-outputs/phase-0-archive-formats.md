# AI-Optimized Research Archive Formats: 2026 Best Practices

## 1. Executive Summary

Based on current 2026 research, **Markdown with YAML frontmatter** emerges as the optimal format for AI-retrievable archives. This hybrid approach balances human readability with machine-structured metadata, enabling both semantic search and precise data retrieval.

**Key Findings:**
- Markdown is the gold standard for embeddings and RAG systems
- YAML frontmatter provides structured metadata without sacrificing readability
- Claude Opus 4.6's 1M token context window (Feb 2026) reduces chunking friction
- Semantic chunking strategies preserve document structure and meaning
- Knowledge graphs enhance retrieval but add complexity—use selectively
- File size sweet spot: 2,000-10,000 tokens per document for optimal retrieval

**Bottom Line:** Structure matters more than size. A well-organized 5KB markdown file with semantic headers and cross-references outperforms a 500KB unstructured dump.

---

## 2. Format Comparison Analysis

### Markdown (Winner for Content)

**Strengths:**
- LLMs are trained on markdown-formatted data (GitHub, documentation)
- Natural chunking boundaries (headers, lists, code blocks)
- Human-readable and editable
- Optimal for embeddings—context-rich and semantically complete
- Future-proof as the de facto language for LLMs
- Lower cost due to efficient tokenization

**Best Use Cases:**
- Documentation, tutorials, research notes
- Conceptual and how-to content
- Mixed human-AI consumption
- Long-form narrative content

**Limitations:**
- Less reliable for precise structured queries
- No schema enforcement
- Requires careful formatting discipline

### YAML (Winner for Metadata)

**Strengths:**
- GPT-5 Nano showed 17.7% higher accuracy with YAML vs XML
- Excellent for frontmatter metadata in markdown files
- Human-readable and editable
- Easy to parse programmatically
- Natural fit for configuration and metadata

**Best Use Cases:**
- Frontmatter in markdown files
- Configuration files
- Structured metadata (tags, dates, authors, categories)
- Hybrid human-AI authoring systems

**Limitations:**
- Whitespace-sensitive (prone to formatting errors)
- Not ideal for deeply nested data structures
- Limited native support for complex relationships

### JSON (Winner for Structured Queries)

**Strengths:**
- Clear, unambiguous key-value structure
- More reliability for structured data queries than markdown
- Strong consistency and precision for information retrieval
- Universal parsing support
- Excellent for API integration

**Best Use Cases:**
- Structured data requiring precise queries
- API responses and integrations
- Configuration with complex nesting
- Data interchange between systems

**Limitations:**
- Less human-readable than markdown or YAML
- Poor for narrative content
- Verbose for simple data
- Not optimized for embedding generation

### Structured Databases (Specialized Use)

**Strengths:**
- Precise queries via SQL or graph query languages
- Relationship modeling (knowledge graphs)
- Data integrity and validation
- Efficient for large-scale retrieval

**Best Use Cases:**
- Enterprise knowledge bases with complex relationships
- Highly structured operational data
- Multi-user collaboration with access controls
- Applications requiring ACID compliance

**Limitations:**
- High setup and maintenance overhead
- Poor for unstructured narrative content
- Requires specialized knowledge
- Overkill for personal/small team use

### Hybrid Recommendation

**Markdown + YAML Frontmatter** is the clear winner for 2026:

```markdown
---
title: Research Finding Title
date: 2026-02-10
tags: [AI, retrieval, knowledge-management]
project: youtube-research
status: complete
key_concepts: [semantic-search, RAG, embeddings]
related: [phase-1-workflow.md, phase-2-tools.md]
---

# Research Finding Title

## Context
[Narrative content in clean markdown...]

## Key Findings
- Finding 1
- Finding 2

## Sources
- [Source Title](URL)
```

This format provides:
- Structured metadata for precise filtering (YAML)
- Semantic content for embedding and RAG (Markdown)
- Human readability and editability
- AI-native format compatibility
- Cross-reference capabilities

---

## 3. File Size Optimization

### Claude Opus 4.6 Context Window (Feb 2026)

**Specifications:**
- **Standard window:** 200,000 tokens
- **Beta window:** 1,000,000 tokens (5x increase)
- **Pricing consideration:** 2x input / 1.5x output premium over 200K tokens
- **Upload limits:** 500MB general files, 30MB images
- **Context compaction:** Auto-summarization for long conversations

### Optimal File Sizes for AI Retrieval

**Token-to-File Size Conversion:**
- ~1 token ≈ 4 characters
- ~1,000 tokens ≈ 750 words ≈ 4KB text file
- 200K token window ≈ 150K words ≈ 600KB-800KB text

**Recommended Granularity:**

| Document Type | Optimal Size | Token Range | Rationale |
|---------------|--------------|-------------|-----------|
| **Single research finding** | 2-5 KB | 500-1,500 | Focused, specific retrieval |
| **Research session notes** | 5-15 KB | 1,500-4,000 | Complete context, single topic |
| **Project documentation** | 15-50 KB | 4,000-12,000 | Full context without chunking |
| **Comprehensive guides** | 50-200 KB | 12,000-50,000 | Use semantic sections |
| **Large reference docs** | 200KB-2MB | 50K-500K | Requires chunking strategy |

**2026 Best Practice:**
- **Structure over size:** A 10KB file with clear semantic sections beats a 100KB wall of text
- **Chunk at semantic boundaries:** Use markdown headers for natural divisions
- **Multi-file over mega-file:** 10 well-structured 10KB files > 1 unstructured 100KB file
- **Leverage 1M context:** For workflows like due diligence, incident response, contract review—entire document sets can be processed without chunking

### Chunking Strategies

**Semantic-Markdown Chunking (Recommended):**
- Recognizes markdown syntax (headings, lists, code blocks)
- Preserves structural hierarchy
- Maintains semantic coherence within chunks
- Configurable join thresholds for related sections

**Multi-Vector Representation:**
- Embed multiple segments (paragraphs/sections) separately
- Increases retrieval granularity
- Surfaces relevant parts rather than entire documents
- Essential for documents >50KB

**Fixed-Size Chunking (Avoid):**
- Breaks semantic meaning
- Arbitrary boundaries
- Degrades retrieval quality

---

## 4. Cross-Reference Systems

### Comparison of Approaches

| Method | Complexity | AI-Friendliness | Human Effort | Best For |
|--------|------------|-----------------|--------------|----------|
| **WikiLinks** | Low | High | Low | Simple bidirectional references |
| **Tags** | Low | Medium | Low | Categorical organization |
| **YAML frontmatter links** | Medium | High | Medium | Explicit structured relationships |
| **Knowledge graphs** | High | Very High | High | Complex relationship modeling |
| **Indexes/TOCs** | Medium | Medium | Medium | Hierarchical navigation |

### WikiLinks (Recommended for Simplicity)

**Format:** `[[filename]]` or `[[filename|display text]]`

**Advantages:**
- Simple syntax
- Bidirectional linking capability
- Obsidian/Notion native support
- Easy to grep and parse
- Low cognitive overhead

**Example:**
```markdown
This finding relates to [[phase-1-workflow]] and builds on [[semantic-search-basics]].
```

### Tags (Recommended for Categorization)

**YAML Frontmatter Approach:**
```yaml
---
tags: [AI, retrieval, markdown, 2026]
categories: [research, knowledge-management]
---
```

**Inline Approach:**
```markdown
#AI #retrieval #markdown
```

**Best Practices:**
- Use hierarchical tags: `project/youtube`, `concept/RAG`, `tool/obsidian`
- Limit to 5-10 tags per document
- Maintain tag taxonomy in separate index file
- Prefer controlled vocabulary over free-form tagging

### YAML Frontmatter Relationships (Recommended for Structure)

**Explicit relationship modeling:**
```yaml
---
related:
  - file: phase-1-workflow.md
    relationship: prerequisite
  - file: phase-2-tools.md
    relationship: next-step
  - file: semantic-search-research.md
    relationship: reference
dependencies: [embedding-models.md, chunking-strategies.md]
---
```

**Advantages:**
- Structured and queryable
- Explicit relationship types
- Machine-parseable
- Version control friendly

### Knowledge Graphs (Use Selectively)

**Tools and Approaches (2026):**
- **LlamaIndex + Obsidian:** Converts notes to structured knowledge graphs for RAG
- **ODIN:** LLM integration via LangChain with link prediction
- **Cognee:** Automated knowledge graph generation
- **InfraNodus:** AI-enhanced graph visualization

**When to Use:**
- Complex relationship modeling requirements
- Large-scale enterprise knowledge bases
- Multi-dimensional concept mapping
- Need for graph query languages (Cypher, SPARQL)

**Trade-offs:**
- High setup and maintenance cost
- Requires specialized tooling
- May be overkill for simple archives
- Better for exploration than direct retrieval

### Hybrid Recommendation

**Start simple, add complexity as needed:**

1. **Layer 1 (Essential):** YAML frontmatter with explicit `related:` links and tags
2. **Layer 2 (Easy wins):** WikiLinks in content for bidirectional references
3. **Layer 3 (Optional):** Knowledge graph if relationships become too complex to manage manually

**Example implementation:**
```yaml
---
title: Semantic Search Fundamentals
date: 2026-02-10
tags: [semantic-search, embeddings, RAG]
related:
  - embedding-models.md
  - chunking-strategies.md
stage: foundational
---

# Semantic Search Fundamentals

Building on [[vector-embeddings-intro]], this research explores...

Key dependency: Understanding [[cosine-similarity]] is essential...
```

---

## 5. Mineable vs. Stored Content

### What Makes Content "Mineable"?

**Mineable content** enables AI to extract, synthesize, and apply knowledge effectively. **Stored content** exists but remains inert—difficult to retrieve, understand, or use.

### Characteristics of Mineable Content

| Dimension | Mineable | Stored (Avoid) |
|-----------|----------|----------------|
| **Structure** | Clear headers, sections, semantic hierarchy | Wall of text, arbitrary formatting |
| **Context** | Explicit problem/solution/outcome | Implicit assumptions, missing context |
| **Metadata** | Rich frontmatter, tags, relationships | No metadata or minimal tagging |
| **Granularity** | Focused topics, 2-15KB files | Mega-files mixing multiple topics |
| **Cross-refs** | Explicit links and relationships | Orphaned documents |
| **Format** | Markdown with semantic structure | PDFs, images, proprietary formats |
| **Language** | Clear, specific, actionable | Vague, jargon-heavy, ambiguous |

### Making Content Mineable: Checklist

**Structure:**
- [ ] Use semantic markdown headers (H1-H4)
- [ ] Break into logical sections
- [ ] Use lists for enumerations
- [ ] Include code blocks with language tags
- [ ] Add horizontal rules for clear boundaries

**Context:**
- [ ] Lead with problem/question being addressed
- [ ] State assumptions and prerequisites
- [ ] Include date and situational context
- [ ] Explain "why" not just "what"
- [ ] Document outcomes and decisions

**Metadata:**
- [ ] YAML frontmatter with title, date, tags
- [ ] Project/category classification
- [ ] Status indicators (draft/complete/obsolete)
- [ ] Key concepts list
- [ ] Related document links

**Retrieval Optimization:**
- [ ] Include summary/TLDR at top
- [ ] Use consistent terminology
- [ ] Add "Key Findings" or "Takeaways" section
- [ ] Link to sources and references
- [ ] Tag with searchable keywords

**Example Transformation:**

**Before (Stored):**
```
Some notes from the meeting about the new system. We talked about
using AI and maybe markdown. John mentioned something about tags.
Need to follow up on the embedding thing. Also discussed budget.
```

**After (Mineable):**
```yaml
---
title: AI Archive System Design Decision
date: 2026-02-10
tags: [knowledge-management, AI, markdown, embeddings]
attendees: [John, Sarah, Patrick]
decision: approved
related: [budget-proposal.md, technical-requirements.md]
---

# AI Archive System Design Decision

## Context
Meeting to finalize format for company-wide AI-retrievable knowledge base.

## Decision
Adopt Markdown + YAML frontmatter as standard format.

## Rationale
- AI-native format (LLM training data)
- Human-readable and editable
- Supports semantic chunking
- Version control friendly

## Key Requirements
1. All documents use YAML frontmatter
2. Semantic header hierarchy (H1-H4)
3. Tag taxonomy: project/category/concept
4. Cross-reference related documents

## Next Steps
- [ ] Create template (John, by 2026-02-15)
- [ ] Pilot with marketing team (Sarah, by 2026-02-28)
- [ ] Budget approval for Obsidian licenses

## Related Decisions
- [[budget-proposal]] - Approved €5K for tooling
- [[technical-requirements]] - System architecture
```

---

## 6. Knowledge Management Systems Review

### Obsidian (Recommended for Personal/Team Use)

**Strengths:**
- Local-first markdown storage
- Native knowledge graph visualization
- WikiLink support with bidirectional linking
- Plugin ecosystem for AI integration
- Version control friendly (Git compatible)
- No vendor lock-in

**AI Integration (2026):**
- **LlamaIndex plugin:** Converts notes to knowledge graphs for RAG
- **ODIN:** LLM integration with link prediction
- **InfraNodus:** AI-enhanced graph views
- **Cognee:** Automated knowledge graph generation

**Best For:**
- Personal knowledge management
- Small team documentation (2-10 people)
- Research and note-taking workflows
- Projects requiring local control and privacy

**Limitations:**
- Manual organization still required
- No native multi-user collaboration
- Plugin ecosystem can be overwhelming

### Notion (Best for Collaboration)

**Strengths:**
- Real-time collaboration
- Unified workspace (docs, wikis, databases)
- Synced blocks for cross-document updates
- AI assistant for search and summarization
- Template system
- Permission management

**AI Features (2026):**
- Native AI assistant for search and retrieval
- Automated summarization
- Question answering across workspace

**Best For:**
- Team collaboration (5-50 people)
- Mixed structured/unstructured content
- Client-facing documentation
- Projects requiring access controls

**Limitations:**
- Proprietary format (vendor lock-in)
- Export to markdown loses structure
- Less control over raw files
- Subscription cost

### Mem (AI-First Approach)

**Strengths:**
- Removes manual organization (no folders)
- AI automatically organizes, surfaces, and connects notes
- Fast capture and retrieval
- Self-organizing over time

**Best For:**
- Rapid capture workflows
- Users who resist manual organization
- Meeting notes and quick references

**Limitations:**
- Less explicit control over structure
- Newer platform (less proven)
- Requires trust in AI organization

### Roam Research / Logseq (Graph-First)

**Strengths:**
- Graph-first mental model
- Bidirectional linking emphasis
- Daily notes structure
- Block-level references

**Best For:**
- Research and interconnected thinking
- Users comfortable with graph paradigms

**Limitations:**
- Steeper learning curve
- Proprietary format (Roam)
- Less mainstream adoption

### Enterprise: Confluence, SharePoint, etc.

**Strengths:**
- Enterprise-grade permissions and compliance
- Integration with existing systems
- IT support and governance
- Large-scale user management

**AI Integration (2026):**
- RAG integration for M365 Copilot (SharePoint)
- Confluence AI for search and summarization

**Best For:**
- Large organizations (50+ people)
- Regulated industries
- Complex permission requirements

**Limitations:**
- Heavy and complex
- Poor user experience vs modern tools
- Often becomes dumping ground for unstructured content

### 2026 Recommendation by Use Case

| Use Case | Primary Tool | Complement With |
|----------|--------------|-----------------|
| **Personal research** | Obsidian | LlamaIndex for RAG |
| **Small team (2-10)** | Obsidian + Git | Shared vault on sync service |
| **Medium team (10-50)** | Notion | Obsidian for individual work |
| **Enterprise (50+)** | SharePoint/Confluence | Semantic search layer (RAG) |
| **AI-first workflow** | Mem or Obsidian + AI plugins | Custom RAG stack |

---

## 7. Simplicity vs. Power Trade-offs

### The Complexity Spectrum

```
Simple                                                      Powerful
|------------|------------|------------|------------|----------|
Plain MD    MD+YAML     MD+YAML       Obsidian      Knowledge
files       +WikiLinks  +Graph        +RAG          Graph DB
```

### Decision Framework

**Start Here (Zone A - Minimum Viable):**
- Markdown files with semantic headers
- YAML frontmatter (title, date, tags)
- Simple related: array in frontmatter
- File naming convention: `YYYY-MM-DD-topic-name.md`

**Add When Needed (Zone B - Sweet Spot):**
- WikiLinks for bidirectional references
- Hierarchical tag taxonomy
- Index files for navigation
- Template files for consistency

**Add Selectively (Zone C - Advanced):**
- Knowledge graph tooling (Obsidian plugins)
- RAG integration (LlamaIndex, custom embedding)
- Automated link prediction
- Graph query capabilities

**Avoid Unless Essential (Zone D - Complexity Hell):**
- Custom database schemas
- Complex relationship ontologies
- Multi-tool integrations requiring maintenance
- Premature automation of organization

### The 80/20 Rule for AI Retrieval

**20% Effort (High Impact):**
1. Semantic markdown structure (H1-H4)
2. YAML frontmatter with title, date, tags
3. One-paragraph summary at top
4. Consistent file naming
5. related: array in frontmatter

**80% Impact Achieved**

**Next 20% Effort (Medium Impact):**
1. WikiLinks for cross-references
2. Hierarchical tag taxonomy
3. Index files for major topics
4. Template standardization
5. Key concepts field in frontmatter

**95% Impact Achieved**

**Final 60% Effort (Diminishing Returns):**
1. Knowledge graph setup and maintenance
2. Custom RAG pipeline
3. Automated relationship extraction
4. Graph query language proficiency
5. Complex ontology management

**100% Impact Achieved (maybe)**

### Warning Signs You've Gone Too Complex

- Spending more time organizing than creating
- System requires frequent maintenance to function
- Onboarding new team members takes days
- Dependencies on specific tools or plugins
- Export/migration seems impossible
- Optimization becomes procrastination

### Recommendation: Progressive Enhancement

**Phase 1 (Week 1):** Plain markdown + YAML frontmatter
- Get content into system
- Establish basic structure
- Learn what you actually need

**Phase 2 (Month 1):** Add WikiLinks and tags
- Connections emerge naturally
- Refine tag taxonomy
- Create index files for major topics

**Phase 3 (Month 3):** Consider knowledge graph
- Only if interconnections become hard to manage manually
- Only if team is committed to maintenance
- Only if retrieval pain is acute

**Never:** Don't build the "perfect system" before capturing content. Structure emerges from use, not theory.

---

## 8. Recommendations

### For Personal/Small Team Use (Recommended)

**Format:**
```yaml
---
title: Descriptive Title
date: 2026-02-10
tags: [category, concept, project]
status: complete
related: [file1.md, file2.md]
---

# Title

## Summary
One paragraph TLDR.

## Content
[Structured markdown with semantic headers]

## Key Takeaways
- Takeaway 1
- Takeaway 2

## Sources
- [Source](URL)
```

**File Structure:**
```
project-root/
├── research-outputs/
│   ├── 2026-02-10-archive-formats.md
│   ├── 2026-02-11-workflow-design.md
│   └── index.md
├── templates/
│   └── research-note-template.md
└── _meta/
    └── tag-taxonomy.md
```

**Tooling:**
- Primary: Obsidian (local-first, Git-friendly)
- Backup: Plain text editor (VS Code with markdown extensions)
- Sync: Git for version control, cloud sync for accessibility
- AI Integration: Bolt on when needed (LlamaIndex, Claude integration)

**Workflow:**
1. Capture in markdown using template
2. Fill YAML frontmatter as you work
3. Add WikiLinks to related documents
4. Tag with 3-7 relevant keywords
5. Commit to Git with descriptive message
6. Review index files monthly

### For Enterprise Use

**Format:** Same as above, but add:
```yaml
---
author: Patrick Heiskanen
department: Research
classification: internal
expires: 2027-02-10
version: 1.0
---
```

**Tooling:**
- Primary: SharePoint with M365 Copilot for AI retrieval
- Alternative: Confluence with AI plugins
- Local: Individuals can use Obsidian, export to enterprise system
- RAG Layer: Custom semantic search over enterprise content

**Governance:**
- Style guide with mandatory fields
- Tag taxonomy managed by knowledge team
- Regular audits for obsolete content
- Training on mineable content principles

### Quick Start Template

**File: `_templates/research-note.md`**
```yaml
---
title: [Replace with descriptive title]
date: YYYY-MM-DD
tags: [tag1, tag2, tag3]
project: [project-name]
status: [draft|in-progress|complete]
key_concepts: [concept1, concept2]
related: []
---

# [Title]

## Summary
[One paragraph: What is this? Why does it matter?]

## Context
[Why did this research happen? What problem does it address?]

## Key Findings
- Finding 1
- Finding 2
- Finding 3

## Detailed Notes
[Structured content with H2-H4 headers]

## Recommendations
[Actionable takeaways]

## Next Steps
- [ ] Action 1
- [ ] Action 2

## Sources
- [Source 1](URL)
- [Source 2](URL)

## Related
- [[related-document-1]]
- [[related-document-2]]
```

### Migration Path

**Moving from existing systems:**

1. **Export to markdown:** Use tools like notion2md, confluence-to-markdown
2. **Clean up structure:** Add semantic headers, remove cruft
3. **Add frontmatter:** Batch add YAML headers with scripts
4. **Generate tags:** Use LLM to suggest tags for existing content
5. **Create index:** Build navigational files
6. **Test retrieval:** Validate AI can find and use content

### Validation Checklist

**Before considering your archive "AI-ready":**

- [ ] Can Claude answer specific questions by reading your files?
- [ ] Can you find documents via tag/keyword search?
- [ ] Do cross-references work bidirectionally?
- [ ] Is metadata consistent across files?
- [ ] Can new team members understand structure in <15 minutes?
- [ ] Would you be comfortable if AI read any file to answer questions?
- [ ] Can you export/migrate to another system if needed?
- [ ] Is critical knowledge captured, not just stored?

---

## 9. Sources

### Format and Structure Best Practices
- [Markdown, JSON, YML, and XML – Best Content Format for AI](https://blog.tech4teaching.net/markdown-json-yml-and-xml-what-is-the-best-content-format-for-both-human-and-ai/)
- [Which Nested Data Format Do LLMs Understand Best?](https://www.improvingagents.com/blog/best-nested-data-format/)
- [Markdown: A Smarter Choice for Embeddings Than JSON or XML](https://medium.com/@kanishk.khatter/markdown-a-smarter-choice-for-embeddings-than-json-or-xml-70791ece24df)
- [MD vs JSON for GPT Knowledge Bases](https://medium.com/@daniel.jackson04956/resmd-vs-json-for-gpt-knowledge-bases-86017b583c09)
- [Boosting AI Performance: The Power of LLM-Friendly Content in Markdown](https://developer.webex.com/blog/boosting-ai-performance-the-power-of-llm-friendly-content-in-markdown)

### Claude Context Window and Optimization
- [Claude Opus 4.6 Brings a 1M-Token Context Window](https://auto-post.io/blog/claude-opus-4-6-enables-1-million-token-context)
- [How to Switch to Claude Opus 4.6 with 1 Million Token Context Window](https://attractgroup.com/blog/how-to-switch-to-claude-opus-4-6-with-1-million-token-context-window-complete-guide-2026/)
- [Context Windows - Claude API Docs](https://platform.claude.com/docs/en/build-with-claude/context-windows)
- [Claude AI Context Window, Token Limits, and Memory](https://www.datastudios.org/post/claude-ai-context-window-token-limits-and-memory-how-large-context-reasoning-actually-works-for-l)
- [How Claude Code Got Better by Protecting More Context](https://hyperdev.matsuoka.com/p/how-claude-code-got-better-by-protecting)

### RAG and Retrieval Systems
- [RAG in 2026: How Retrieval-Augmented Generation Works for Enterprise AI](https://www.techment.com/blogs/rag-in-2026-enterprise-ai/)
- [RAG in 2026: Bridging Knowledge and Generative AI](https://squirro.com/squirro-blog/state-of-rag-genai)
- [Structure Augmented Generation: Bridging Structured and Unstructured Data](https://www.meibel.ai/post/structure-augmented-generation-bridging-structured-and-unstructured-data-for-enhanced-rag-systems)
- [RAG for Structured Data: Benefits, Challenges & Examples](https://www.ai21.com/knowledge/rag-for-structured-data/)
- [Retrieval-Augmented Generation (RAG) - Wikipedia](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)

### Knowledge Management Tools
- [Top 10 Obsidian Alternatives to Take Better Notes in 2026](https://www.lindy.ai/blog/obsidian-alternatives)
- [Notion vs Obsidian – All Features Compared (2026)](https://productive.io/blog/notion-vs-obsidian/)
- [Make Knowledge Graph RAG with LlamaIndex from Own Obsidian Notes](https://medium.com/@haiyangli_38602/make-knowledge-graph-rag-with-llamaindex-from-own-obsidian-notes-b20a350fa354)
- [InfraNodus Obsidian Plugin: AI Enhanced Knowledge Graph View](https://infranodus.com/obsidian-plugin)
- [ODIN - GitHub (Memgraph)](https://github.com/memgraph/odin)

### Semantic Search and Embeddings
- [Chunking Strategies for LLM Applications - Pinecone](https://www.pinecone.io/learn/chunking-strategies/)
- [Top Embedding Models 2026: Complete In-Depth Guide](https://artsmart.ai/blog/top-embedding-models-in-2025/)
- [Chunk and Vectorize by Document Layout - Azure AI Search](https://docs.azure.cn/en-us/search/search-how-to-semantic-chunking)
- [OpenSearch Semantic Search: The Basics (2026 Guide)](https://www.instaclustr.com/education/opensearch/opensearch-semantic-search-the-basics-and-a-quick-tutorial-2026-guide/)
- [QMD - Mini CLI Search Engine for Docs (GitHub)](https://github.com/tobi/qmd)

---

**Document Metadata:**
- Research Date: 2026-02-10
- Author: Patrick Heiskanen (via Claude Code)
- Status: Complete
- Next: Apply these principles to YouTubeResearch-AIFiles project structure

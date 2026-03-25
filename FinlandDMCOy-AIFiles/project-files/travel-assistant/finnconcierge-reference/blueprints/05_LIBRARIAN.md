# BP_05: RAG Librarian Agent (The Knowledge Keeper)

## Overview

The Librarian Agent is FinnConcierge's knowledge retrieval system. It uses RAG (Retrieval Augmented Generation) to answer factual questions about venue amenities, policies, local information, and services.

## Purpose

Provide **accurate, source-backed answers** to guest questions, reducing workload on human staff while maintaining high information quality.

## Implementation Status

✅ **IMPLEMENTED** - `services/ingestion/librarian_agent.py`

## Key Features

### 1. Knowledge Base Search
- Semantic search through structured knowledge base
- Currently: keyword-based matching (mock implementation)
- Future: Azure AI Search + embeddings

### 2. Source Citation
- Every answer includes source documents
- Transparency for users
- Easier fact-checking for staff

### 3. Confidence Scoring
- Each answer has confidence score (0.0-1.0)
- Low confidence → automatic human handover
- Threshold: 0.5 (configurable)

### 4. Graceful Degradation
- If no answer found: requests human assistance
- Better UX than "I don't know"

## Knowledge Base Topics

Current coverage (12 topics):

1. **Restaurant Hours** - Opening times, breakfast schedule
2. **Sauna Booking** - Reservation process, time slots
3. **Ice Safety** - Thickness requirements, daily checks
4. **Weather Info** - Forecast access, typical temperatures
5. **Aurora Viewing** - Best times, alert service
6. **Activities** - Available excursions, guides
7. **WiFi Access** - Network name, password location
8. **Parking** - Location, heating plugs
9. **Checkout Times** - Standard and late checkout
10. **Emergency Contacts** - Phone numbers, hospitals
11. **Local Transportation** - Bus, taxi, airport transfers
12. **General Policies** - House rules, amenities

## Architecture

```
Input:
  - User question (natural language)
  - Context (optional, for better results)

Processing:
  1. Parse question
  2. Search knowledge base
  3. Rank results by relevance
  4. Generate answer (currently: return content)
  5. Check confidence threshold

Output:
  - Answer text
  - Source documents
  - Confidence score
  - Human handover flag (if needed)
```

## Data Models

### KnowledgeSource
```python
@dataclass
class KnowledgeSource:
    document_id: str             # "restaurant_hours"
    title: str                   # "Ravintola aukioloajat"
    chunk_text: Optional[str]    # Excerpt from document
    relevance_score: float       # 0.0-1.0
```

### LibrarianResponse
```python
@dataclass
class LibrarianResponse:
    answer: str                  # The actual answer
    sources: List[KnowledgeSource]  # Source documents
    confidence: float            # 0.0-1.0
    requires_human: bool         # Handover flag
    reasoning: str              # Why this answer?
    timestamp: str
```

## Usage Example

```python
from librarian_agent import LibrarianAgent

# Initialize
librarian = LibrarianAgent(
    tenant_id="jarvisydan",
    confidence_threshold=0.5
)

# Ask question
response = await librarian.query(
    question="Milloin ravintola on auki?",
    context={'location': 'main_building'}
)

# Result
print(response.answer)
# → "Ravintola on avoinna joka päivä klo 18:00-22:00..."

print(response.sources[0].title)
# → "Ravintola aukioloajat"

print(response.confidence)
# → 0.85
```

## Integration Points

### Input Dependencies
- **BP_02 (Master Agent)**: Routes information requests
- **Knowledge Base**: Currently hardcoded, future: Azure AI Search

### Output Consumers
- **BP_02 (Master Agent)**: Uses answers in response synthesis
- **Staff Dashboard**: Monitors handover requests

## Current Limitations (Mock Implementation)

1. **Keyword Matching**: Not true semantic search
2. **Static Knowledge**: Hardcoded, not from database
3. **No Updates**: Knowledge base doesn't refresh
4. **Finnish Only**: No multi-language support
5. **No Context Awareness**: Doesn't use conversation history

## RAG Enhancement Roadmap

### Phase 2 (Short-term)
- [ ] Azure AI Search integration
- [ ] Vector embeddings (OpenAI text-embedding-3)
- [ ] Dynamic knowledge base updates
- [ ] Source document links

### Phase 3 (Medium-term)
- [ ] GPT-4 for answer synthesis
- [ ] Multi-turn context tracking
- [ ] Follow-up question handling
- [ ] Document versioning

### Phase 4 (Long-term)
- [ ] Multi-language knowledge base
- [ ] Image/PDF understanding (GPT-4V)
- [ ] Real-time policy updates
- [ ] Cross-property knowledge sharing

## Search Quality Metrics

| Metric | Target | Current |
|--------|--------|---------|
| Answer Relevance | >85% | TBD |
| Response Time | <500ms | ~30ms (mock) |
| Source Accuracy | 100% | 100% (mock) |
| Handover Rate | <20% | TBD |

## Testing

Test coverage in `test_orchestrator.py`:
- ✅ Restaurant hours query
- ✅ WiFi availability query
- ✅ Ice safety query
- ✅ Confidence threshold behavior
- ✅ Intent-based routing

## Example Knowledge Base Entry

```python
'restaurant_hours': {
    'title': 'Ravintola aukioloajat',
    'content': 'Ravintola on avoinna joka päivä klo 18:00-22:00. 
                Aamiainen tarjotaan klo 7:00-10:00.',
    'keywords': ['ravintola', 'aukiolo', 'ruoka', 'aika', 
                 'restaurant', 'opening', 'hours', 'food', 'time']
}
```

## Error Handling

### Low Confidence (< 0.5)
```python
return LibrarianResponse(
    answer="Löysin joitain tietoja, mutta suosittelen ottamaan 
            yhteyttä vastaanottopalveluumme...",
    requires_human=True
)
```

### No Results Found
```python
return LibrarianResponse(
    answer="En löytänyt tietoa tästä asiasta. 
            Otan yhteyttä kollegoihini...",
    requires_human=True
)
```

## Related Blueprints

- **BP_02**: Master Agent (orchestrator)
- **BP_04**: Chef (complementary recommendations)
- **BP_07**: Staff Dashboard (handover handling)

---

**Status**: Production-ready for mock mode  
**Owner**: FinnConcierge Core Team  
**Last Updated**: December 11, 2025  
**Future**: Full RAG implementation with Azure AI Search

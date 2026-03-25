# BP_04: Chef Agent (The Suggestion Engine)

## Overview

The Chef Agent is FinnConcierge's personalized recommendation engine. It analyzes a user's psychological profile (Mood Matrix from BP_03) and suggests activities that match their current state and preferences.

## Purpose

Provide **mood-aware, context-sensitive activity recommendations** that feel personally tailored to each guest.

## Implementation Status

✅ **IMPLEMENTED** - `services/ingestion/chef_agent.py`

## Key Features

### 1. Mood-Based Recommendations
- Analyzes 7 dimensions of user's Mood Matrix
- Identifies dominant psychological trait
- Suggests activities matching that trait

### 2. Rich Activity Database
7 activity categories mapped to mood dimensions:
- **Energy** → Adventure activities (aurora hunting, skiing, snowmobile)
- **Social Battery** → Group experiences (ice fishing, cooking class)
- **Luxury Affinity** → Premium services (private chalet, helicopter tour)
- **Nature Rawness** → Wilderness experiences (survival, forest trek)
- **Safety Need** → Safe guided activities (guided walks, museum)
- **Foodie Focus** → Culinary experiences (fine dining, foraging)
- **Price Sensitivity** → Budget-friendly options (self-guided trails)

### 3. Multiple Options
- Primary recommendation (highest confidence)
- 2 alternative suggestions
- Reasoning for each recommendation

### 4. Confidence Scoring
Each recommendation includes confidence score (0.0-1.0)

## Architecture

```
Input:
  - MoodMatrix (from BP_03 Mood Evaluator)
  - Context (location, weather, history)
  - User message (optional)

Processing:
  1. Identify dominant mood dimension
  2. Fetch matching activities
  3. Rank by relevance
  4. Generate explanations

Output:
  - Primary recommendation
  - Alternative options
  - Mood summary
  - Reasoning
```

## Data Models

### ActivityRecommendation
```python
@dataclass
class ActivityRecommendation:
    activity_name: str           # "Aurora Hunting Expedition"
    description: str             # Full description
    confidence: float            # 0.0-1.0
    reasoning: str               # Why this was suggested
    metadata: Dict[str, Any]     # Tags, matched dimension, etc.
```

### ChefResponse
```python
@dataclass
class ChefResponse:
    primary_recommendation: ActivityRecommendation
    alternatives: List[ActivityRecommendation]
    mood_summary: str           # "Your profile: Adventure Solo..."
    timestamp: str
```

## Usage Example

```python
from chef_agent import ChefAgent
from mood_evaluator import MoodMatrix

# Initialize
chef = ChefAgent(tenant_id="jarvisydan")

# Get recommendation
response = await chef.recommend(
    mood_matrix=user_mood_matrix,
    context_backpack={'user_name': 'Alice', ...},
    user_message="What should I do today?"
)

# Result
print(response.primary_recommendation.activity_name)
# → "Aurora Hunting Expedition"
```

## Integration Points

### Input Dependencies
- **BP_03 (Mood Evaluator)**: Requires updated MoodMatrix
- **BP_02 (Master Agent)**: Receives context and orchestration

### Output Consumers
- **BP_02 (Master Agent)**: Uses recommendations in response synthesis
- **BP_06 (Booker)**: May convert recommendations to bookings

## Current Limitations (Mock Implementation)

1. **Static Activity Database**: Hardcoded activities, not from real database
2. **Simple Ranking**: No ML-based relevance scoring
3. **No Real-Time Data**: Doesn't check activity availability
4. **No User History**: Doesn't learn from past preferences
5. **Finnish Market Only**: Activities are Lapland-specific

## Future Enhancements

### Phase 2 (Short-term)
- [ ] Connect to activity database (SQL)
- [ ] Real-time availability checking
- [ ] Price information
- [ ] Booking links

### Phase 3 (Medium-term)
- [ ] ML-based activity ranking
- [ ] Collaborative filtering (what similar users liked)
- [ ] Seasonal adjustments
- [ ] Weather-aware suggestions

### Phase 4 (Long-term)
- [ ] Multi-activity itinerary planning
- [ ] Budget optimization
- [ ] Group activity coordination
- [ ] Predictive recommendations

## Testing

Test coverage in `test_orchestrator.py`:
- ✅ High energy user → adventure recommendations
- ✅ Luxury seeker → premium recommendations
- ✅ Mood Matrix integration
- ✅ Intent-based routing

## Performance Targets

| Metric | Target | Current |
|--------|--------|---------|
| Response Time | <200ms | ~50ms (mock) |
| Recommendation Accuracy | >80% | TBD (needs real data) |
| User Satisfaction | >4.0/5.0 | TBD |

## Related Blueprints

- **BP_02**: Master Agent (orchestrator)
- **BP_03**: Mood Evaluator (provides input)
- **BP_05**: Librarian (complementary info)
- **BP_06**: Booker (converts to bookings)

---

**Status**: Production-ready for mock mode  
**Owner**: FinnConcierge Core Team  
**Last Updated**: December 11, 2025

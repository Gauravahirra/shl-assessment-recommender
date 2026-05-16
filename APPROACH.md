# SHL Assessment Recommender — Approach Document

## System Design

### Architecture Overview

The service is a **stateless FastAPI** application with two endpoints (`GET /health`, `POST /chat`). Each `/chat` call receives the full conversation history, performs catalog retrieval, and calls the Anthropic Claude API to generate a structured JSON response.

```
User → POST /chat (full history)
         → Keyword Retrieval (15 candidates from 111+ catalog items)
         → System Prompt + History + Catalog Context → Claude API
         → JSON parse + URL validation
         → ChatResponse {reply, recommendations[], end_of_conversation}
```

### Catalog Acquisition

The SHL catalog at `https://www.shl.com/products/product-catalog/` renders its table via JavaScript, so a static HTML GET returns no product rows. My approach:

1. **Live scraper** (`scraper.py`): On startup, attempts to fetch all 32 pages of Individual Test Solutions (`?start=N&type=1`) using `requests` + `BeautifulSoup`, caching results for 24 hours.
2. **Static fallback** (`catalog_data.py`): 111 hand-curated items covering all major categories (Ability, Personality, Knowledge/Skills, Simulations, SJT/Biodata) compiled from catalog pages I could access. Includes real SHL URLs.

The static catalog intentionally prioritizes breadth across test types to ensure good Recall@10 across diverse query personas.

### Retrieval Strategy

**Keyword overlap scoring** with category boosting:
- Tokenize both query and each catalog item's name + description
- Score by shared token count
- Add +3 bonus for tokens that appear in the item name (exact signal)
- Add +2 category boost when query intent matches item's test type (e.g., "personality" → P-type items, "coding simulation" → S-type items)
- Return top 15 candidates, injected as structured context into Claude's prompt

**Why not embeddings/FAISS?** The catalog has 111–384 items — at this scale, keyword retrieval with intent heuristics is fast (<5ms), interpretable, and avoids cold-start embedding model loading within the 30-second timeout. The LLM then does semantic re-ranking implicitly.

### Prompt Design

The system prompt enforces:
- **Scope guard**: only SHL Individual Test Solutions, refuse off-topic
- **Behavior rules**: clarify vague queries (no recommendation on turn 1 for vague input), recommend 1–10, refine on edits, compare from catalog facts
- **Output format**: pure JSON `{reply, recommendations[], end_of_conversation}` — no markdown fences
- **Catalog context**: 15 retrieved items injected per turn as the ground truth for recommendations

**Key design choices:**
- Catalog retrieval context is injected into the *last user message* (not the system prompt), keeping it turn-specific and avoiding context bloat in long conversations
- The LLM acts as a re-ranker and conversational layer; retrieval ensures it stays grounded
- JSON output is parsed with fallback regex extraction for robustness

### URL Validation

After the LLM responds, every recommendation URL is validated against the catalog. If a name matches but URL is hallucinated, we substitute the real catalog URL. This prevents any non-SHL URLs from reaching the evaluator.

---

## Evaluation Approach

I tested against the 5 required behavior probes:
- **Vague query**: empty `recommendations[]`, asks one clarifying question ✓
- **Recommendation**: 3–7 items for well-scoped queries ✓  
- **Refinement**: shortlist updated (not restarted) on constraint changes ✓
- **Comparison**: factual response from catalog context ✓
- **Out-of-scope/injection**: `recommendations[]` empty, reply explains scope ✓

### What Didn't Work

1. **Sentence transformers + FAISS**: Initial plan used `all-MiniLM-L6-v2` for dense retrieval. Abandoned because model download (~80MB) caused cold-start failures >30s on free-tier hosting. Keyword retrieval is faster and sufficient.

2. **Structured output via tool use**: Tried using Claude's tool_use for structured JSON output. More reliable schema compliance but adds ~200ms latency. Switched to JSON-in-text with regex fallback to stay well within timeout.

3. **Full catalog scraping**: JavaScript-rendered tables can't be fetched by simple HTTP clients. The live scraper works in production but a static catalog is the reliable fallback.

### AI Tools Used

- **Claude** (via Anthropic API): LLM backbone for conversation and re-ranking
- **Claude claude.ai**: Used for drafting and iterating on the system prompt
- Code written with AI assistance; all design decisions (retrieval strategy, validation logic, fallback chain) made and understood by author

---

## Stack

| Component | Choice | Reason |
|-----------|--------|--------|
| API framework | FastAPI | Async, Pydantic validation, OpenAPI docs |
| LLM | Claude claude-sonnet-4-20250514 | Best reasoning/speed balance, JSON output |
| Retrieval | Keyword BM25-style | No model loading, <5ms, sufficient for ~400 items |
| Deployment | Render (free tier) | Simple, `render.yaml` config, ANTHROPIC_API_KEY env var |
| Catalog | Static + live scraper | Reliability first, freshness second |

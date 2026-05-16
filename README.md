# SHL Assessment Recommender

Conversational agent for recommending SHL Individual Test Solutions via dialogue.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --host 0.0.0.0 --port 8000
```

## API

### `GET /health`
```json
{"status": "ok"}
```

### `POST /chat`
**Request:**
```json
{
  "messages": [
    {"role": "user", "content": "I'm hiring a Java developer who works with stakeholders"},
    {"role": "assistant", "content": "Sure. What is their seniority level?"},
    {"role": "user", "content": "Mid-level, around 4 years"}
  ]
}
```

**Response:**
```json
{
  "reply": "Here are 5 assessments for a mid-level Java developer with stakeholder needs.",
  "recommendations": [
    {"name": "Java 8 (New)", "url": "https://www.shl.com/products/product-catalog/view/java-8-new/", "test_type": "K"},
    {"name": "OPQ32r", "url": "https://www.shl.com/products/product-catalog/view/opq32r/", "test_type": "P"}
  ],
  "end_of_conversation": false
}
```

## Testing

```bash
# Start server first, then:
python test_api.py
```

## Deployment (Render)

1. Push to GitHub
2. Create new Web Service on Render
3. Set `ANTHROPIC_API_KEY` environment variable
4. Render uses `render.yaml` configuration automatically

## Architecture

- **FastAPI** stateless REST service
- **Keyword retrieval** with category boosting (no embedding model cold-start)
- **Claude claude-sonnet-4-20250514** as the conversational backbone
- **URL validation** — all recommendations verified against catalog
- **Live scraper** with 24h cache + static fallback catalog

## Test Types Legend
- A = Ability & Aptitude
- B = Biodata & Situational Judgement  
- C = Competencies
- D = Development & 360
- E = Assessment Exercises
- K = Knowledge & Skills
- P = Personality & Behavior
- S = Simulations

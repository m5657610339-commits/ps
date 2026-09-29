# Phase 5 – Project Development

## Implemented Components

### Backend
- FastAPI application
- CORS configuration
- SQLite database
- SQLAlchemy models
- JWT authentication
- Planner endpoints
- Recommendation history
- Health endpoint

### AI Layer
The project includes an optional Gemini integration layer. If the API key is not configured or the AI request fails, the fallback recommendation engine returns deterministic demo results.

### Recommendation Modules
- Home: furniture, lighting, décor and estimated budget allocation
- Party: food, decoration, venue and entertainment allocation
- Jewelry: occasion/style-based suggestions and optional outfit image input

### Frontend
A lightweight landing page and static styling are included. The API is documented through FastAPI Swagger at `/docs`.

## Running the Project

```bash
pip install -r requirements.txt
python run.py
```

Open:
`http://127.0.0.1:8000/docs`

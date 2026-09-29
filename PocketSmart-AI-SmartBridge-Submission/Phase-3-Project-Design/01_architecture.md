# Phase 3 – Project Design

## High-Level Architecture

```text
User
  |
  v
Frontend (HTML/CSS/JS)
  |
  v
FastAPI Backend
  |------ Authentication
  |------ Planner Routes
  |------ History
  |
  v
Recommendation Service
  |
  +------ Gemini AI (optional configured integration)
  |
  +------ Fallback Recommendation Engine
  |
  v
SQLite Database
```

## Modules
- Authentication module
- Home planner
- Party planner
- Jewelry planner
- Recommendation engine
- History module
- Frontend presentation layer

## API Design
- `POST /register`
- `POST /login`
- `POST /token`
- `GET /session-info`
- `POST /generate-home`
- `POST /generate-party`
- `POST /generate-jewelry`
- `GET /history`
- `GET /health`

## Database Design

### User
- id
- name
- email
- password_hash

### RecommendationHistory
- id
- user_id
- category
- request_data
- response_data
- created_at

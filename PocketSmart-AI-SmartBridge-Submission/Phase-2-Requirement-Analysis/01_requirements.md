# Phase 2 – Requirement Analysis

## Functional Requirements
- User registration
- User login and authentication
- User session/token handling
- Home recommendation generation
- Party recommendation generation
- Jewelry recommendation generation
- Optional jewelry outfit image upload
- Recommendation history
- Structured recommendation output
- Input validation and fallback recommendations

## Non-Functional Requirements
- Responsive and simple interface
- Modular backend
- Secure credential handling
- Reliable error handling
- Maintainable project structure
- Budget adherence in generated recommendations

## Input / Output

| Module | Inputs | Output |
|---|---|---|
| Home | Budget, room, style, item needs | Home recommendations |
| Party | Budget, guests, event type, venue/preferences | Food, venue, decoration and allocation suggestions |
| Jewelry | Budget, occasion, style, outfit details/image | Style-matched jewelry suggestions |

## Technology Requirements
- Python
- FastAPI
- HTML/CSS/JavaScript/Jinja2
- SQLite
- Gemini API integration
- JWT authentication

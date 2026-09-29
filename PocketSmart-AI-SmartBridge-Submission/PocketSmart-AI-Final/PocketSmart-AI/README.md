# PocketSmart AI

PocketSmart is a FastAPI-based AI budget planning web app for:
- Home Interior Planning
- Party Planning
- Jewelry Recommendations

## UI update

The project now includes a responsive web UI matching the supplied reference style: navy/blue navigation, hero sections, planner cards, sign-in/sign-up screens, dashboard, planner forms, recommendation results, and history.

## Setup on Windows

From the `PocketSmart-AI` folder:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe run.py
```

If your existing `.venv` is already working, the two install/run commands above are enough.

Open:
- http://127.0.0.1:8000/ — landing page
- http://127.0.0.1:8000/signup — create account
- http://127.0.0.1:8000/signin — sign in
- http://127.0.0.1:8000/dashboard — planner dashboard
- http://127.0.0.1:8000/docs — API documentation

## Environment

Create `.env` from `.env.example` and set a strong `SECRET_KEY`. Add `GEMINI_API_KEY` if you want Gemini-powered responses. The deterministic fallback recommendation engine still works without Gemini.

## Important

Do not commit or share your real API key or `.env` file.

## Windows CMD quick start

From the `PocketSmart-AI` folder:

```cmd
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe run.py
```

Open `http://127.0.0.1:8000` in your browser.

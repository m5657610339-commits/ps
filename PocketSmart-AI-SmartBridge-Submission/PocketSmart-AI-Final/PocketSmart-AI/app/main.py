from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .database import Base, engine
from .routes.auth_routes import router as auth_router
from .routes.planner_routes import router as planner_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="PocketSmart AI", version="1.0.0")

templates = Jinja2Templates(directory="app/templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(auth_router)
app.include_router(planner_router)


@app.get("/")
def root(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.get("/signin")
def signin_page(request: Request):
    return templates.TemplateResponse(request, "signin.html")


@app.get("/signup")
def signup_page(request: Request):
    return templates.TemplateResponse(request, "signup.html")


@app.get("/dashboard")
def dashboard_page(request: Request):
    return templates.TemplateResponse(request, "dashboard.html")


@app.get("/home-planner")
def home_planner_page(request: Request):
    return templates.TemplateResponse(request, "home_planner.html")


@app.get("/party-planner")
def party_planner_page(request: Request):
    return templates.TemplateResponse(request, "party_planner.html")


@app.get("/jewelry-planner")
def jewelry_planner_page(request: Request):
    return templates.TemplateResponse(request, "jewelry_planner.html")


@app.get("/history-page")
def history_page(request: Request):
    return templates.TemplateResponse(request, "history.html")


@app.get("/health")
def health():
    return {"status": "healthy"}

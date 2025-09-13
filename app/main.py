from fastapi import FastAPI
from app.routes import waitlist, notify
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Valido Waitlist API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # during development, allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(waitlist.router, prefix="/waitlist", tags=["Waitlist"])
app.include_router(notify.router, prefix="/notify", tags=["Notify"])

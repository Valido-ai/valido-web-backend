from fastapi import FastAPI
from app.routes import waitlist, notify

app = FastAPI(title="Valido Waitlist API", version="1.0.0")

# Routes
app.include_router(waitlist.router, prefix="/waitlist", tags=["Waitlist"])
app.include_router(notify.router, prefix="/notify", tags=["Notify"])

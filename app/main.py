import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import waitlist

app = FastAPI()

# Enable CORS for frontend (allow all origins for now, restrict in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(waitlist.router, prefix="/waitlist")


# ✅ Azure will call this file directly
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # fallback 8000 for local
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)

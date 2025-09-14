from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from datetime import datetime
from app.database import users_collection

router = APIRouter()

class WaitlistUser(BaseModel):
    email: EmailStr

@router.post("/user")
def add_user(user: WaitlistUser):
    # Check if user already exists
    if users_collection.find_one({"email": user.email}):
        return {
            "status": "exists",
            "message": "You've already signed up for the waitlist"
        }
    
    # Create document
    doc = {
        "email": user.email,
        "created_at": datetime.utcnow()
    }

    # Insert into DB
    users_collection.insert_one(doc)

    return {
        "status": "success",
        "message": "Successfully signed up for waitlist"
    }
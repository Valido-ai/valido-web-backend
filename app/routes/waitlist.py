from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from app.database import users_collection

router = APIRouter()

class WaitlistUser(BaseModel):
    email: EmailStr

@router.post("/user")
def add_user(user: WaitlistUser):
    if users_collection.find_one({"email": user.email}):
        return {
            "status": "exists",
            "message": "You've already signed up for waitlist"
        }
    
    users_collection.insert_one(user.dict())
    return {
        "status": "success",
        "message": "Successfully signed up for waitlist"
    }

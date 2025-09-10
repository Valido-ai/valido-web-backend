from fastapi import APIRouter, HTTPException
from app.models import WaitlistUser, WaitlistOrganization
from app.database import users_collection, organizations_collection

router = APIRouter()

@router.post("/user")
def add_user(user: WaitlistUser):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="User already registered")
    users_collection.insert_one(user.dict())
    return {"message": "User added to waitlist"}

@router.post("/organization")
def add_organization(org: WaitlistOrganization):
    if organizations_collection.find_one({"email": org.email}):
        raise HTTPException(status_code=400, detail="Organization already registered")
    organizations_collection.insert_one(org.dict())
    return {"message": "Organization added to waitlist"}

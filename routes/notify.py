from fastapi import APIRouter, Depends
from app.database import users_collection, organizations_collection
from app.utils.emailer import send_email
from app.utils.security import verify_api_key

router = APIRouter()

@router.post("/launch")
def notify_all(_: bool = Depends(verify_api_key)):
    users = list(users_collection.find({}, {"_id": 0, "email": 1}))
    orgs = list(organizations_collection.find({}, {"_id": 0, "email": 1}))

    recipients = [u["email"] for u in users] + [o["email"] for o in orgs]

    for email in recipients:
        send_email(
            recipient=email,
            subject="Valido is Live! 🚀",
            body="We’re excited to announce that Valido is live! Sign up now at https://valido.com"
        )
    return {"message": f"Notification sent to {len(recipients)} recipients"}

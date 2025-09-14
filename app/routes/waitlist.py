from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel, EmailStr
from datetime import datetime
from app.database import users_collection
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
import os
import logging
import asyncio

router = APIRouter()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Email config (update with Titan or Gmail)
conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("EMAIL_USER"),  # your email
    MAIL_PASSWORD=os.getenv("EMAIL_PASS"),  # your email password / app password
    MAIL_FROM=os.getenv("EMAIL_USER"),
    MAIL_PORT=587,  # 465 if using SSL
    MAIL_SERVER="smtp.gmail.com",  # or "smtp.titan.email"
    MAIL_TLS=True,   # True if using 587
    MAIL_SSL=False,  # True if using 465
    USE_CREDENTIALS=True,
)

class WaitlistUser(BaseModel):
    email: EmailStr

@router.post("/user")
def add_user(user: WaitlistUser, background_tasks: BackgroundTasks):
    # Check if user already exists
    if users_collection.find_one({"email": user.email}):
        return {
            "status": "exists",
            "message": "You've already signed up for the waitlist"
        }

    # Insert user into DB
    doc = {
        "email": user.email,
        "created_at": datetime.utcnow()
    }
    users_collection.insert_one(doc)
    logging.info(f"User {user.email} added to DB")

    # Load HTML template
    try:
        with open("app/templates/welcome.html", "r", encoding="utf-8") as f:
            html_template = f.read()
        html_content = html_template.replace("{{email}}", user.email)
    except Exception as e:
        logging.error(f"Failed to read HTML template: {e}")
        html_content = f"<p>Hi {user.email}, welcome to Valido!</p>"

    # Build email
    message = MessageSchema(
        subject="Welcome to Valido 🎉",
        recipients=[user.email],
        body=html_content,
        subtype="html"
    )

    fm = FastMail(conf)

    # Send email in background with error logging
    def send_email_task():
        try:
            asyncio.run(fm.send_message(message))
            logging.info(f"✅ Welcome email sent to {user.email}")
        except Exception as e:
            logging.error(f"❌ Failed to send email to {user.email}: {e}")

    background_tasks.add_task(send_email_task)

    return {
        "status": "success",
        "message": "Successfully signed up for waitlist & email task queued"
    }

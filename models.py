from pydantic import BaseModel, EmailStr

class WaitlistUser(BaseModel):
    email: EmailStr

class WaitlistOrganization(BaseModel):
    email: EmailStr

from pydantic import BaseSettings, EmailStr
from functools import lru_cache

class Settings(BaseSettings):
    MONGO_URI: str
    DB_NAME: str = "Valido_waitlist"
    EMAIL_SENDER: EmailStr
    EMAIL_PASSWORD: str
    EMAIL_HOST: str = "smtp.gmail.com"
    EMAIL_PORT: int = 587
    ADMIN_API_KEY: str

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()

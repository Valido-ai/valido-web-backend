from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import EmailStr
from functools import lru_cache

class Settings(BaseSettings):
    MONGO_URI: str
    DB_NAME: str = "Valido_waitlist"
    EMAIL_SENDER: EmailStr
    EMAIL_PASSWORD: str
    EMAIL_HOST: str = "smtp.gmail.com"
    EMAIL_PORT: int = 587
    ADMIN_API_KEY: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()

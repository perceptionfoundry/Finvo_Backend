from pydantic import AnyHttpUrl, Field
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    database_url: str = Field(..., alias="DATABASE_URL")
    clerk_secret_key: str = Field(..., alias="CLERK_SECRET_KEY")
    clerk_issuer: AnyHttpUrl = Field(..., alias="CLERK_ISSUER")
    clerk_jwks_url: AnyHttpUrl = Field(..., alias="CLERK_JWKS_URL")
    clerk_audience: str = Field(..., alias="CLERK_AUDIENCE")

    class Config:
        env_file = ".env"
        case_sensitive = True
        populate_by_name = True  # So you can access as settings.clerk_issuer, etc.

@lru_cache()
def get_settings():
    return Settings()

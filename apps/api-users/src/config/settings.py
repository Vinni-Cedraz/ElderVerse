from pydantic import BaseSettings, Field
from typing import List


class Settings(BaseSettings):
    # General settings
    APP_NAME: str = Field(default="API Users", env="APP_NAME")
    DEBUG: bool = Field(default=False, env="DEBUG")

    # Server settings
    HOST: str = Field(default="0.0.0.0", env="HOST")
    PORT: int = Field(default=8000, env="PORT")
    RELOAD: bool = Field(default=False, env="RELOAD")

    # Database settings
    DATABASE_URL: str = Field(
        default="postgresql://user:password@localhost:5432/api_users",
        env="DATABASE_URL",
    )

    # CORS settings
    CORS_ORIGINS: List[str] = Field(
        default=["http://localhost:3000", "https://your-production-domain.com"],
        env="CORS_ORIGINS",
    )

    # NATS settings
    NATS_URL: str = Field(default="nats://localhost:4222", env="NATS_URL")
    NATS_SUBJECT: str = Field(default="api-users.events", env="NATS_SUBJECT")

    # Security settings
    JWT_SECRET_KEY: str = Field(default="supersecretkey", env="JWT_SECRET_KEY")
    JWT_ALGORITHM: str = Field(default="HS256", env="JWT_ALGORITHM")
    JWT_EXPIRATION_MINUTES: int = Field(default=60, env="JWT_EXPIRATION_MINUTES")

    # SSL/TLS settings
    SSL_KEYFILE: str = Field(default=None, env="SSL_KEYFILE")
    SSL_CERTFILE: str = Field(default=None, env="SSL_CERTFILE")

    # Logging settings
    LOG_LEVEL: str = Field(default="info", env="LOG_LEVEL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Create a single settings instance to be imported throughout the app
settings = Settings()

"""Backend Configuration Management."""

from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application Settings loaded from environment variables."""

    # Environment
    ENV: str = "development"
    DEBUG: bool = True

    # FastAPI Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    WORKERS: int = 4
    API_TITLE: str = "KatZ API"
    API_VERSION: str = "0.1.0"
    API_DESCRIPTION: str = "Vision & Voice Katalysator-Wert-App Backend"

    # OpenAI Vision
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-4o"
    OPENAI_VISION_MODEL: str = "gpt-4-vision-preview"
    OPENAI_VISION_DETAIL: str = "high"  # low, auto, high
    OPENAI_VISION_MAX_TOKENS: int = 1024

    # Metals-API
    METALS_API_KEY: str
    METALS_API_BASE_URL: str = "https://metals-api.com/api"
    METALS_API_TIMEOUT: int = 30
    METALS_SYNC_INTERVAL_MINUTES: int = 360  # 6 Stunden

    # PostgreSQL Database
    DATABASE_URL: str
    DATABASE_ECHO: bool = False
    DATABASE_POOL_SIZE: int = 20
    DATABASE_MAX_OVERFLOW: int = 0
    DATABASE_POOL_PRE_PING: bool = True

    # Redis Cache
    REDIS_URL: str
    REDIS_TTL_HOURS: int = 12
    REDIS_POOL_SIZE: int = 10
    REDIS_ENCODING: str = "utf-8"

    # Supabase (Alternative)
    SUPABASE_URL: str = ""
    SUPABASE_KEY: str = ""

    # Web Scraping
    SCRAPER_TIMEOUT: int = 30
    SCRAPER_HEADLESS: bool = True
    SCRAPER_USER_AGENTS_ROTATION: bool = True
    SCRAPER_PROXY_ENABLED: bool = False
    SCRAPER_PROXY_URL: str = ""
    SCRAPER_INTERVAL_MINUTES: int = 120

    # Business Rules
    CATALYST_MIN_PRICE_EUR: float = 250.00
    CATALYST_LOCATION_FILTER: str = "unterboden"
    CATALYST_LOCATIONS_ALLOWED: List[str] = ["unterboden", "unterboden-katalysator"]

    # Security & CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8080",
        "http://localhost:8000",
    ]
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1"]
    API_KEY_HEADER: str = "X-API-Key"
    API_RATE_LIMIT_ENABLED: bool = True
    API_RATE_LIMIT_PER_MINUTE: int = 60

    # Logging
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "json"
    LOG_DIR: str = "logs"

    # Feature Flags
    FEATURE_VISION_AI_ENABLED: bool = True
    FEATURE_SCRAPER_ENABLED: bool = True
    FEATURE_VOICE_QUERY_ENABLED: bool = True

    class Config:
        """Pydantic Config."""

        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()

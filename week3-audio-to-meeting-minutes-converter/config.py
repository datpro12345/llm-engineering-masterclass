# config.py
import os
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    ASSEMBLYAI_API_KEY: str
    PERPLEXITY_API_KEY: Optional[str] = None

    class Config:
        env_file = ".env"

settings = Settings()

from pathlib import Path
from typing import Optional
from pydantic import BaseSettings, Field, validator
import os

class Settings(BaseSettings):
    # OpenAI Configuration
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    openai_model: str = Field("gpt-4-turbo-preview", env="OPENAI_MODEL")
    openai_assistant_id: str = Field(..., env="OPENAI_ASSISTANT_ID")
    
    # Audio Configuration
    sample_rate: int = Field(24000, env="AUDIO_SAMPLE_RATE")
    channels: int = Field(1, env="AUDIO_CHANNELS")
    input_device_id: Optional[int] = Field(None, env="AUDIO_INPUT_DEVICE_ID")
    output_device_id: Optional[int] = Field(None, env="AUDIO_OUTPUT_DEVICE_ID")
    volume: float = Field(0.15, env="AUDIO_VOLUME")
    
    # Debug Configuration
    debug: bool = Field(False, env="DEBUG")
    debug_audio_path: Path = Field(Path("debug_audio"), env="DEBUG_AUDIO_PATH")
    
    # Retry Configuration
    max_retries: int = Field(3, env="MAX_RETRIES")
    retry_delay: float = Field(1.0, env="RETRY_DELAY")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        
    @validator("debug_audio_path")
    def create_debug_path(cls, v: Path) -> Path:
        v.mkdir(parents=True, exist_ok=True)
        (v / "input").mkdir(exist_ok=True)
        (v / "output").mkdir(exist_ok=True)
        return v

# Global settings instance
settings = Settings()

def get_settings() -> Settings:
    """Get the global settings instance."""
    return settings

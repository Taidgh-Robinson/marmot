from pydantic_settings import BaseSettings, SettingsConfigDict
from src.config.env_file_config import ENV_FILE


class LLMConfig(BaseSettings):
    model: str
    local_base: str = None

    model_config = SettingsConfigDict(
        env_file=ENV_FILE, env_prefix="LLM_", extra="ignore"
    )

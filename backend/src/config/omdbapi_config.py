from pydantic_settings import BaseSettings, SettingsConfigDict
from src.config.env_file_config import ENV_FILE


class OMDBAPIConfig(BaseSettings):
    api_key: str = None

    model_config = SettingsConfigDict(
        env_file=ENV_FILE, env_prefix="OMDBAPI_", extra="ignore"
    )

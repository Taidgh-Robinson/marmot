from pydantic_settings import BaseSettings, SettingsConfigDict
from src.config.env_file_config import ENV_FILE


class PostgresConfig(BaseSettings):
    host: str
    user: str
    password: str
    db: str

    model_config = SettingsConfigDict(
        env_file=ENV_FILE, env_prefix="PG_", extra="ignore"
    )

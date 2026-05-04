from typing import ClassVar

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )

    minimax_api_key: str
    minimax_default_model: str
    minimax_uri: str
    openrouter_api_key: str
    openrouter_default_model: str
    openrouter_uri: str


settings = Settings()  # type: ignore[call-arg]

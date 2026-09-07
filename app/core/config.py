from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "voice-agent-backend"
    app_env: str = "dev"
    llm_api_key: str = ""
    llm_base_url: str = ""


settings = Settings()

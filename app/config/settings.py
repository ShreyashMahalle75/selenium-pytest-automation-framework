from functools import lru_cache


from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration loaded from .env.
    """

    # Application
    APP_NAME: str = "Gym Reservation Bot Pro"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = "development"

    # Selenium
    BROWSER: str = "chrome"
    HEADLESS: bool = False
    IMPLICIT_WAIT: int = 10
    EXPLICIT_WAIT: int = 20

    # Website
    BASE_URL: str = ""

    GYM_USERNAME: str = ""
    GYM_PASSWORD: str = ""

    # Screenshot
    SCREENSHOT_PATH: str = "screenshots"

    # Logs
    LOG_PATH: str = "logs"

    # Retry
    MAX_RETRY: int = 3

    # Email
    SMTP_SERVER: str = ""
    SMTP_PORT: int = 587
    EMAIL: str = ""
    EMAIL_PASSWORD: str = ""
    RECEIVER_EMAIL: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()

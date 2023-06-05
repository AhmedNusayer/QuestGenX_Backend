from pydantic import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str
    postgres_user: str
    postgres_password: str
    postgres_server: str
    postgres_port: str
    postgres_db: str
    database_url: str

    class Config:
        env_file = ".env"


settings = Settings()


from pydantic import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool
    MAIN_SERVICE_URL_DEV: str
    MAIN_SERVICE_URL_PROD: str

    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str
    MONGO_INITDB_DATABASE: str
    DATABASE_URL: str

    class Config:
        env_file = "./.env"


settings = Settings()

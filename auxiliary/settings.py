from pydantic import BaseSettings


class Settings(BaseSettings):
    main_service_url_dev: str
    main_service_url_prod: str


settings = Settings()

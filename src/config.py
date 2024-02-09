from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    POSTGRES_URL: str
    POSTGRES_PRISMA_URL: str
    POSTGRES_URL_NO_SSL: str
    POSTGRES_URL_NON_POOLING: str 
    POSTGRES_USER: str
    POSTGRES_HOST: str 
    POSTGRES_PASSWORD: str 
    POSTGRES_DATABASE: str
    class Config:
        env_file = ".env"

settings = Settings()
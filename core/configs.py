from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Configurações gerais usada pela aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/teste_python"


    class Config:
        case_sensitive = True

settings = Settings()
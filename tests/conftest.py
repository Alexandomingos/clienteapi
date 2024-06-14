import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from httpx import AsyncClient

from main import app
from core.configs import settings
from core.database import Base, engine

# Configurar um banco de dados de teste separado
SQLALCHEMY_DATABASE_URL = settings.DB_URL

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, expire_on_commit=False, bind=engine, class_=AsyncSession)

# Criar tabelas
@pytest.fixture(scope="session", autouse=True)
async def initialize_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.drop_all)
        await conn.run_sync(Base.create_all)
    yield
    await engine.dispose()

# Fixture para a sessão assíncrona
@pytest.fixture(scope="function")
async def async_session():
    async with TestingSessionLocal() as session:
        yield session
        await session.rollback()  # Garantir que o banco de dados está limpo após cada teste

# Fixture para o cliente assíncrono
@pytest.fixture(scope="module")
async def async_client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

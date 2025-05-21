from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession,async_sessionmaker
from sqlalchemy.orm import sessionmaker
from typing import AsyncGenerator
from contextlib import asynccontextmanager
from app.config import get_settings

settings = get_settings()

engine = create_async_engine(settings.postgres_url, echo=False, future=True, connect_args={"statement_cache_size": 0})

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session
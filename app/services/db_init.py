import asyncpg
from app.config import get_settings

# Database initialization

settings = get_settings()

db_pool = None  # singleton pool

async def init_db_pool():
    global db_pool
    if db_pool is None:
        db_pool = await asyncpg.create_pool(dsn=settings.postgres_url)
    return db_pool

def get_db_pool():
    return db_pool
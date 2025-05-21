# app/repositories/product_repository.py
from app.utils.errors import DatabaseException
import asyncpg

class ProductRepository:
    def __init__(self, pool: asyncpg.pool.Pool):
        self.pool = pool

    async def get_by_name(self, name: str):
        query = """
        SELECT name, description, price
        FROM products
        WHERE name ILIKE $1
        LIMIT 1
        """
        try:
            async with self.pool.acquire() as conn:
                result = await conn.fetchrow(query, f"%{name}%")
                return dict(result) if result else None
        except Exception as e:
            raise DatabaseException(f"Error querying product by name: {str(e)}")
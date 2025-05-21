from sqlalchemy import text
from app.models.product import ProductInfo
from app.utils.errors import APIError
from sqlalchemy.ext.asyncio import AsyncSession

class ProductRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_name(self, name: str) -> ProductInfo:
        try:
            stmt = text("SELECT name, description, price FROM products WHERE name ILIKE :name LIMIT 1")
            result = await self.session.execute(stmt, {"name": f"%{name}%"})
            row = result.fetchone()
            if not row:
                raise APIError(f"Product '{name}' not found.")
            return ProductInfo(name=row[0], description=row[1], price=float(row[2]))
        except Exception as e:
            raise APIError(f"DB query failed: {e}")
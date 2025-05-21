# app/services/product_tool.py

from app.repositories.product_repository import ProductRepository
from app.utils.errors import DatabaseException

async def fetch_product_info(name: str, db_pool) -> str:
    try:
        repo = ProductRepository(db_pool)
        result = await repo.get_by_name(name)
        if not result:
            return f"No product found with name '{name}'"
        return f"{result['name']}: {result['description']} (${float(result['price'])})"
    except Exception as e:
        raise DatabaseException(f"Database error: {str(e)}")
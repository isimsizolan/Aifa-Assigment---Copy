from app.services.product_db import get_session
from app.repositories.product_repository import ProductRepository

async def fetch_product_info(name: str) -> str:
    async with get_session() as session:
        repo = ProductRepository(session)
        product = await repo.get_by_name(name)
        return f"{product.name}: {product.description} (${product.price})"
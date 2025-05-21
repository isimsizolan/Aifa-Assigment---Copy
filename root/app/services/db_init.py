
from pathlib import Path
from sqlalchemy import text
from app.services.product_db import engine

SCHEMA_SQL = Path(__file__).parent.parent / "database" / "schema.sql"

async def init_db() -> None:
    print("[DB INIT] Executing schema.sql...")
    print("Schema path:", SCHEMA_SQL)
    ddl = SCHEMA_SQL.read_text()
    async with engine.begin() as conn:
        # execute each statement (split on ;)
        for stmt in filter(None, (s.strip() for s in ddl.split(";"))):
            await conn.execute(text(stmt))
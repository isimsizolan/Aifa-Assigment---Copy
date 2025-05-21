from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.requests import Request
from app.router import chat_router
from app.utils.errors import AppError
from app.services.db_init import init_db_pool, get_db_pool
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("[APP] Starting up...")

    # Initialize asyncpg connection pool once
    await init_db_pool()

    try:
        yield
    finally:
        print("[APP] Shutting down...")
        pool = get_db_pool()
        if pool:
            await pool.close()


app = FastAPI(title="Agentic AI Chatbot", lifespan=lifespan)

# Register routes
app.include_router(chat_router, prefix="/chat", tags=["Chat"])

# Serve static frontend
app.mount("/static", StaticFiles(directory="app/frontend"), name="static")

@app.get("/")
async def index():
    return FileResponse("app/frontend/index.html")

# Global error handler
@app.exception_handler(AppError)
async def app_error_handler(request: Request, exc: AppError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"status": "error", "message": exc.message},
    )

@app.get("/healthz", tags=["System"])
async def healthcheck():
    pool = get_db_pool()
    if pool is not None:
        try:
            async with pool.acquire() as conn:
                await conn.execute("SELECT 1")
            return {"status": "ok"}
        except Exception:
            return {"status": "error", "details": "DB unavailable"}
    return {"status": "error", "details": "DB pool not initialized"}
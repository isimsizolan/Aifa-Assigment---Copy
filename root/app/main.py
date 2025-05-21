from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.router import chat_router
from app.services.db_init import init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(title="Agentic AI Chatbot", lifespan=lifespan)
app.include_router(chat_router, prefix="/chat", tags=["Chat"])


# Serve static frontend
app.mount("/static", StaticFiles(directory="app/frontend"), name="static")

@app.get("/")
async def index():
    return FileResponse("app/frontend/index.html")

# API
app.include_router(chat_router, prefix="/chat", tags=["Chat"])


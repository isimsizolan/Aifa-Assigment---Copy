from fastapi import APIRouter, FastAPI
from pydantic import BaseModel
from app.utils.errors import AppError, app_error_handler
from app.agent.executor import invoke_agent

chat_router = APIRouter()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    status: str
    data: dict

@chat_router.post(
    "/",
    response_model=ChatResponse,
    status_code=200,
    summary="Submit a message to the chatbot"
)
async def chat(req: ChatRequest):
    result = await invoke_agent(req.message)
    return {
        "status": "success",
        "data": {
            "answer": result
        }
    }

# Error handler registration
def register_error_handlers(app: FastAPI):
    app.add_exception_handler(AppError, app_error_handler)
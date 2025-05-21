from fastapi import APIRouter
from pydantic import BaseModel
from app.agent.executor import agent_executor
from app.agent.executor import run_agent_with_log  
chat_router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@chat_router.post("/")
async def chat(req: ChatRequest):
    #result = agent_executor.invoke({"input": req.message})
    result = run_agent_with_log(req.message)
    return {"response": result}
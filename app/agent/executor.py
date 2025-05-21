from langchain.agents import initialize_agent, AgentType
from langchain.schema.messages import SystemMessage
from app.agent.tools import tool_list
from app.config import get_settings
from langchain_groq import ChatGroq
from pydantic import SecretStr

settings = get_settings()

# Init LLM once
llm = ChatGroq(api_key=SecretStr(settings.groq_api_key), model="gemma2-9b-it")

# Global agent executor singleton
_agent_executor = None

# System message used for agent instruction, will be used later or if necassary
system_message = SystemMessage(content=(
    "You are a precise and efficient assistant that uses tools to answer user questions.\n"
    "Call a tool only once unless explicitly required.\n"
    "If one tool gives a good answer, do not try others.\n"
    "Never guess. If no tool helps, say so clearly.\n"
    "Do not assume tools are missing. Use only the tools provided.\n"
    "If a tool returns valid info, assume it is sufficient unless the user explicitly asks for more.\n"
    "Avoid using 'query_research' unless the user asks for a research topic explicitly.\n"
))

def get_agent_executor():
    global _agent_executor
    if _agent_executor is None:
        _agent_executor = initialize_agent(
            tools=tool_list,
            llm=llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            handle_parsing_errors=True
        )
    return _agent_executor

async def invoke_agent(message: str) -> str:
    try:
        agent = get_agent_executor()
        result = await agent.ainvoke({"input": message})
        return result["output"]
    except Exception as e:
        return f"[Agent error] {e}"

# For debugging purposes
def debug_llm_raw_response(message: str) -> str:
    return f"DEBUG: Received message '{message}'"
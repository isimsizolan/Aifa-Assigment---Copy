from langchain.agents import initialize_agent, AgentType
from langchain_groq import ChatGroq
from app.config import get_settings
from app.agent.tools import tool_list

settings = get_settings()

from pydantic import SecretStr

llm = ChatGroq(
    api_key=SecretStr(settings.groq_api_key),
    model="llama3-8b-8192"
)

agent_executor = initialize_agent(
    tools=tool_list,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

def run_agent_with_log(user_input: str) -> str:
    print(f"\n[AGENT INPUT] {user_input}")
    try:
        result = agent_executor.invoke({"input": user_input})
        print(f"[AGENT OUTPUT] {result}")
        return result.get("output", str(result))
    except Exception as e:
        print(f"[AGENT ERROR] {e}")
        return "Sorry, something went wrong."
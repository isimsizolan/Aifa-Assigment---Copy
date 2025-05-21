from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain_groq import ChatGroq
from app.config import get_settings
from pydantic import SecretStr

# Load settings and create sync SQL DB connection (not asyncpg)
settings = get_settings()
db = SQLDatabase.from_uri(settings.postgres_url.replace("+asyncpg", ""))

# Set up Groq LLM
llm = ChatGroq(
    api_key=SecretStr(settings.groq_api_key),
    model="gemma2-9b-it"
)

# Create SQL agent executor
agent_executor = create_sql_agent(
    llm=llm,
    db=db,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

# Entry point for tool
def run_sql_query(question: str) -> str:
    try:
        result = agent_executor.invoke({"input": question})
        return result["output"]
    except Exception as e:
        return f"SQL Agent Error: {e}"
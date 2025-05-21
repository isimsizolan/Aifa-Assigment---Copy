from langchain_core.tools import tool
from app.services.wikipedia import get_city_info
from app.services.weather import get_weather_info
from app.services.scholar import get_research_summary
from app.services.product_tool import fetch_product_info
from app.services.db_init import get_db_pool
from app.agent.sql_agent import run_sql_query
from app.utils.logger import log, logsync
from app.utils.exception import catch, catchsync

@tool
@log
@catch
async def search_city_info(city: str) -> str:
    """Get general information about a city using Wikipedia."""
    return await get_city_info(city.strip())

@tool
@log
@catch
async def get_weather(city: str) -> str:
    """Get current weather in a city using a weather API."""
    return await get_weather_info(city.strip())


@tool
@log
@catch
async def query_research(topic: str) -> str:
    """Summarize research papers on a given topic."""
    return await get_research_summary(topic)

@tool
@log
@catch
async def find_product_info(name: str) -> str:
    """Retrieve product information by name from the database."""
    pool = get_db_pool()
    return await fetch_product_info(name.strip(), pool)

@tool
@logsync
@catchsync
def ask_sql(question: str) -> str:
    """Answer questions using SQL on products(name, description, price)."""
    return run_sql_query(question)
    
tool_list = [
    search_city_info,
    get_weather,
    query_research,
    ask_sql
    # find_product_info,  # Uncomment if you want to include DB-based tool

]


# Older tool definition for find_product_info, async version
"""
    Tool(
        name="find_product_info",
        func=find_product_info,
        coroutine=find_product_info,
        description="Retrieve product information by name from the database."
    ),
"""
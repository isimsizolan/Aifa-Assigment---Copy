from langchain_core.tools import tool
from app.services.wikipedia import get_city_info
from app.services.weather import get_weather_info
from app.services.scholar import get_research_summary
from app.services.product_tool import fetch_product_info
from app.utils.logger import log_tool_call

@tool
@log_tool_call
def search_city_info(city: str) -> str:
    """Get general information about a city using Wikipedia."""
    return get_city_info(city)

@tool
@log_tool_call
def get_weather(city: str) -> str:
    """Get current weather in a city using a weather API."""
    return get_weather_info(city)

@tool
@log_tool_call
def query_research(topic: str) -> str:
    """Summarize research papers on a given topic."""
    return get_research_summary(topic)

@tool
@log_tool_call
async def query_product(product_name: str) -> str:
    """Get product info from the product database."""
    return await fetch_product_info(product_name)

tool_list = [search_city_info, get_weather, query_research, query_product]
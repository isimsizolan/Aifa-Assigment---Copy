import httpx
from app.utils.errors import ExternalAPIException

# Nothing is special about this code, it is just a simple function to fetch weather information from Open Meteo

async def get_city_info(city: str) -> str:
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{city}"
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            res = await client.get(url)
            res.raise_for_status()
            return res.json().get("extract", f"No summary found for {city}.")
    except Exception as e:
        raise ExternalAPIException(f"Failed to fetch city info: {str(e)}")
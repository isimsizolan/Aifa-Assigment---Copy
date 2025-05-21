import requests
from app.utils.errors import APIError

def get_city_info(city: str) -> str:
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{city}"
    try:
        res = requests.get(url, timeout=5)
        res.raise_for_status()
        return res.json().get("extract", f"No summary found for {city}.")
    except Exception as e:
        raise APIError(f"Wikipedia error: {e}") 
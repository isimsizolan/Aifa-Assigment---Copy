import requests
from app.utils.errors import APIError

def get_weather_info(city: str) -> str:
    try:
        # Step 1: Geocode
        geo_url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
        geo_res = requests.get(geo_url, timeout=5).json()
        if not geo_res:
            return f"Could not find location for {city}."

        lat, lon = geo_res[0]["lat"], geo_res[0]["lon"]

        # Step 2: Weather API
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_res = requests.get(weather_url, timeout=5).json()

        current = weather_res.get("current_weather")
        if not current:
            return f"No weather data for {city}."

        temp = current["temperature"]
        wind = current["windspeed"]
        return f"{city}: {temp}°C, wind {wind} km/h."
    except Exception as e:
        raise APIError(f"Weather API error: {e}")
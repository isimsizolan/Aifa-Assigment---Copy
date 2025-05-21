import httpx
from app.utils.errors import ExternalAPIException

async def get_weather_info(city: str) -> str:
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; MyApp/1.0; +https://example.com/)"
        }

        async with httpx.AsyncClient(timeout=5.0) as client:
            geo_url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
            geo_res = await client.get(geo_url, headers=headers)

            if geo_res.status_code != 200:
                raise ExternalAPIException(f"Geocoder error: {geo_res.status_code}")

            geo_data = geo_res.json()
            if not geo_data:
                raise ExternalAPIException(f"No geolocation found for '{city}'")

            lat, lon = geo_data[0]["lat"], geo_data[0]["lon"]

            weather_url = (
                f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
            )
            weather_res = await client.get(weather_url)

            if weather_res.status_code != 200:
                raise ExternalAPIException(f"Weather API error: {weather_res.status_code}")

            weather_data = weather_res.json()
            current = weather_data.get("current_weather", {})
            return (
                f"Weather in {city}: {current.get('temperature')}°C, "
                f"Wind {current.get('windspeed')} km/h, "
                f"{current.get('weathercode')}"
            )
    except Exception as e:
        raise ExternalAPIException(f"Failed to fetch weather data: {str(e)}")
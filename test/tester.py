import requests
from sqlalchemy import create_engine
from sqlalchemy import text
from app.config import get_settings
from langchain_groq import ChatGroq

settings = get_settings()

# Initial testing script to check if the APIs are working

print("🔧 Settings:", settings)

# Test Wikipedia
def test_wikipedia():
    city = "Istanbul"
    res = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{city}")
    print("📘 Wikipedia:", res.status_code, "-", res.json().get("extract", "No content"))

# Test weather API + geocoding
def test_weather():
    city = "Istanbul"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MyApp/1.0; +https://example.com/)"}
    response = requests.get(f"https://nominatim.openstreetmap.org/search?q={city}&format=json", headers=headers)
    if response.status_code != 200:
        print(f"❌ Geocoding API error: {response.status_code}")
        return
    try:
        geo_data = response.json()
    except Exception as e:
        print(f"❌ Error decoding geocoding response: {e}")
        return
    if not geo_data:
        print("❌ Geocoding API returned no results.")
        return
    geo = geo_data[0]
    lat, lon = geo["lat"], geo["lon"]
    weather = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    ).json()
    print("🌤️ Weather:", weather.get("current_weather", {}))

# Test Semantic Scholar
def test_scholar():
    q = "machine learning"
    res = requests.get(f"https://api.semanticscholar.org/graph/v1/paper/search?query={q}&limit=1")
    data = res.json()
    print("📚 Scholar:", data["data"][0]["title"])

# Test PostgreSQL
def test_db():
    engine = create_engine(settings.postgres_url)

    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("🐘 PostgreSQL: Connected")
    except Exception as e:
        print("❌ PostgreSQL Error:", e)

def test_groq():
    try:
        from pydantic import SecretStr
        llm = ChatGroq(
            api_key=SecretStr(settings.groq_api_key),
            model="llama3-8b-8192"
        )
        response = llm.invoke("Say hello.")
        if isinstance(response.content, list):
            print("🤖 Groq:", " ".join(str(item).strip() for item in response.content))
        else:
            print("🤖 Groq:", str(response.content).strip())
    except Exception as e:
        print("❌ Groq Error:", e)

if __name__ == "__main__":
    test_wikipedia()
    test_weather()
    test_scholar()
    test_db()
    test_groq()
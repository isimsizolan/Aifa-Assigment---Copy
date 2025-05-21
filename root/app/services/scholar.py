import httpx
from app.utils.errors import ExternalAPIException

async def get_research_summary(topic: str) -> str:
    try:
        url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={topic}&limit=1&fields=title,abstract"
        async with httpx.AsyncClient(timeout=5.0) as client:
            res = await client.get(url)
            res.raise_for_status()

            data = res.json().get("data", [])
            if not data:
                return f"No research papers found on '{topic}'."

            paper = data[0]
            title = paper.get("title", "No title")
            abstract = paper.get("abstract", "No abstract")
            return f"**{title}**\n\n{abstract}"
    except Exception as e:
        raise ExternalAPIException(f"Semantic Scholar error: {str(e)}")
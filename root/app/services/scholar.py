import requests
from app.utils.errors import APIError

def get_research_summary(topic: str) -> str:
    try:
        url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={topic}&limit=1&fields=title,abstract"
        res = requests.get(url, timeout=5)
        res.raise_for_status()

        data = res.json().get("data", [])
        if not data:
            return f"No research papers found on '{topic}'."

        paper = data[0]
        title = paper.get("title", "No title")
        abstract = paper.get("abstract", "No abstract")
        return f"**{title}**\n\n{abstract}"
    except Exception as e:
        raise APIError(f"Semantic Scholar error: {e}")
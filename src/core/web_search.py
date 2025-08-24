from langchain.tools import tool
from tavily import TavilyClient

@tool
def web_search(query: str, max_results: int = 5) -> list:
    """Search the web for current information using Tavily API"""
    try:
        tavily = TavilyClient()
        results = tavily.search(query, max_results=max_results)
        return results.get('results', [])
    except Exception as e:
        return [{"error": f"Web search failed: {str(e)}"}]
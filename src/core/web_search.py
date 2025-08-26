from langchain.tools import tool
from tavily import TavilyClient
import os

@tool
def web_search(query: str, max_results: int = 5) -> list:
    """Search the web for current information using Tavily API"""
    try:
        api_key = os.getenv("TAVILY_API_KEY")
        if not api_key:
            return [{"error": "TAVILY_API_KEY not set in environment variables"}]
            
        tavily = TavilyClient(api_key=api_key)
        results = tavily.search(query, max_results=max_results)
        return results.get('results', [])
    except Exception as e:
        return [{"error": f"Web search failed: {str(e)}"}]
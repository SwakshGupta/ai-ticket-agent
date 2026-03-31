from langchain.tools import tool

@tool
def web_search(query: str) -> str:
    """Search external sources for errors"""
    return f"Simulated web result for: {query}"
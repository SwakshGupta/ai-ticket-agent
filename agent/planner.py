# agent/planner.py

from typing import Dict

def plan_action(user_query: str) -> Dict:
    """
    Very simple rule-based planner (you can later replace with LLM)
    """

    query = user_query.lower()

    if "ticket" in query:
        return {"action": "ticket_tool"}

    elif "error" in query or "issue" in query:
        return {"action": "rag_tool"}

    elif "search" in query or "google" in query:
        return {"action": "web_tool"}

    else:
        return {"action": "fallback"}
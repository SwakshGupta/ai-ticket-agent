# agent/executor.py

from tools.ticket_tool import get_ticket_details
from tools.rag_tool import query_rag
from tools.web_tool import web_search


def execute(action: str, query: str):
    try:
        if action == "ticket_tool":
            return get_ticket_details(query)

        elif action == "rag_tool":
            result = query_rag(query)

            # 🔥 Fallback if no context
            if result == "NO_CONTEXT":
                return web_search(query)

            return result

        elif action == "web_tool":
            return web_search(query)

        else:
            return "Invalid action"

    except Exception as e:
        return f"Error occurred: {str(e)}"
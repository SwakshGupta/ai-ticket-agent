# agent/executor.py

from tools.ticket_tool import get_ticket_details
from tools.rag_tool import query_rag
from tools.web_tool import web_search


def execute(action: str, user_query: str):
    if action == "ticket_tool":
        return get_ticket_details(user_query)

    elif action == "rag_tool":
        return query_rag(user_query)

    elif action == "web_tool":
        return web_search(user_query)

    else:
        return "Sorry, I couldn't understand the request."
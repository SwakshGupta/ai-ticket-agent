import json
from langchain.tools import tool

@tool
def get_ticket_details(ticket_id: str) -> str:
    """Fetch ticket details from internal system"""
    
    with open("data/tickets.json", "r") as f:
        tickets = json.load(f)

    for t in tickets:
        if t["ticket_id"] == ticket_id:
            return str(t)

    return "Ticket not found"
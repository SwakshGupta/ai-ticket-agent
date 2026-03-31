# agent/agent.py

from agent.planner import plan_action
from agent.executor import execute
from utils.logger import log


def run_agent(user_query: str):
    log(f"User Query: {user_query}")

    plan = plan_action(user_query)
    action = plan["action"]

    log(f"Planned Action: {action}")

    result = execute(action, user_query)

    log(f"Result: {result}")

    return result
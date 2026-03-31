# agent/agent.py

from agent.planner import plan_action
from agent.executor import execute
from memory.chat_memory import ChatMemory
from utils.logger import log_step

memory = ChatMemory()


def get_confidence(response: str):
    if "NO_CONTEXT" in response:
        return "Low"
    elif len(response) < 50:
        return "Medium"
    else:
        return "High"


def run_agent(query: str):
    # 🔹 Step 1: Get memory context
    history = memory.get_context()

    full_query = f"""
Previous conversation:
{history}

Current query:
{query}
"""

    log_step("QUERY", query)

    # 🔹 Step 2: Plan action (LLM-based)
    action = plan_action(full_query)
    log_step("ACTION", action)

    # 🔹 Step 3: Execute tool
    result = execute(action, query)
    log_step("RESULT", result)

    # 🔹 Step 4: Confidence scoring
    confidence = get_confidence(result)

    # 🔹 Step 5: Save to memory
    memory.add(query, result)

    return f"{result}\n\nConfidence: {confidence}"
# 🧠 AI Ticket Triage Agent — Project Understanding

## 📌 Overall Idea

This project is an **AI-based ticket resolution system**.

It takes a user query (like a support ticket), understands it, and then:

* decides what to do
* uses tools (RAG, ticket lookup, web search)
* returns a helpful response

👉 Flow:
User → Agent → Decision → Tool → Response

---

# 🏗️ High-Level Flow

1. User enters a query
2. Agent receives the query
3. Planner decides what action to take
4. Executor runs the correct tool
5. Tool returns result
6. Agent gives final response

---

# 📁 Folder-by-Folder Explanation

---

## 🔹 `app.py`

👉 Entry point of the project

* This is the file you run
* Takes user input from terminal
* Sends query to the agent
* Prints response

👉 Think:

> "Start the system and interact with it"

---

## 🔹 `data/`

👉 Contains all raw data used in the project

### `tickets.json`

* Mock ticket data
* Used by ticket tool

### `runbooks/`

* Internal documents (like company knowledge base)
* Used for RAG (retrieval system)

👉 Think:

> "Knowledge + data the agent uses"

---

## 🔹 `rag/`

👉 Handles Retrieval-Augmented Generation (RAG)

### `ingest.py`

* Converts documents into embeddings
* Stores them in vector database

### `retriever.py`

* Fetches relevant documents based on query

👉 Think:

> "Search system for internal knowledge"

---

## 🔹 `tools/`

👉 These are functions the agent can use

### `ticket_tool.py`

* Fetches ticket details
* Used when query is about tickets

### `rag_tool.py`

* Uses retriever to get relevant documents
* Helps answer technical issues

### `web_tool.py`

* Simulates web search
* Used when internal data is not enough

👉 Think:

> "Capabilities of the agent"

---

## 🔹 `agent/`

👉 Brain of the system

---

### `agent.py`

* Main orchestrator
* Connects everything together:

  * planner
  * executor
  * tools

👉 Flow inside:
User → Plan → Execute → Return result

---

### `planner.py`

👉 Decides WHAT to do

* Looks at user query
* Chooses action:

  * ticket_tool
  * rag_tool
  * web_tool

👉 Currently:

* Rule-based (if-else logic)

👉 Future:

* Replace with LLM-based reasoning

---

### `executor.py`

👉 Executes the decision

* Takes action from planner
* Calls correct tool
* Returns result

👉 Think:

> "Planner decides, executor acts"

---

### `prompt.py`

* Contains system prompts (if using LLM)
* Defines agent behavior

---

## 🔹 `memory/`

👉 Stores conversation history

### `chat_memory.py`

* Saves past interactions
* Can be used for multi-turn conversations

👉 Think:

> "Short-term memory of the agent"

---

## 🔹 `evaluation/`

👉 Used to test how well the system works

---

### `test_cases.json`

* Sample queries + expected outputs

---

### `metrics.py`

* Runs test cases
* Checks accuracy

👉 Think:

> "How good is my agent?"

---

## 🔹 `utils/`

👉 Helper functions

### `logger.py`

* Prints logs
* Shows:

  * user query
  * chosen action
  * result

👉 Think:

> "Debugging and visibility"

---

# 🧠 How Everything Connects

```text
User Input
   ↓
app.py
   ↓
agent.py
   ↓
planner.py → decides action
   ↓
executor.py → calls tool
   ↓
tools/ → performs task
   ↓
result returned
   ↓
printed to user
```

---

# 🔥 Current System Capabilities

* Basic agent decision making (rule-based)
* RAG-based document retrieval
* Tool-based architecture
* Simple evaluation system
* Logging for debugging

---

# ⚠️ Current Limitations

* Planner is rule-based (not intelligent yet)
* No advanced memory usage
* No real API/backend
* Basic evaluation only

---

# 🚀 Future Improvements

* Replace planner with LLM reasoning
* Improve RAG (better chunking, embeddings)
* Add UI (Streamlit)
* Add better evaluation metrics
* Add fallback and error handling

---

# 🎯 Final Understanding

👉 This project is:

> A modular AI agent system that can understand queries, decide actions, and use tools to solve problems.

---

# 🧠 One-line summary

> “An AI agent that triages tickets using RAG, tools, and decision logic.”

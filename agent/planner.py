from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

#instead of writing if else statement we have assigned a model which will select the tool automatically 
#by checking from the prompt ( we have created a prompt tempelate)

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

prompt = PromptTemplate(
    input_variables=["query"],
    template="""
You are an AI agent planner.

Decide which tool to use for the query.

Available tools:
- ticket_tool → for ticket related queries
- rag_tool → for internal technical issues
- web_tool → for general or unknown queries

Return ONLY the tool name.

Query: {query}
"""
)

def plan_action(query):
    response = llm.predict(prompt.format(query=query))
    return response.strip()
# tools/rag_tool.py

from rag.retriever import hybrid_search
from langchain.chat_models import ChatOpenAI

# Assume vector_db + docs are initialized globally
# (you should load them in your actual code)

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

def query_rag(query: str):
    results = hybrid_search(query)

    if not results:
        return "NO_CONTEXT"

    context = "\n".join([doc.page_content for doc in results])

    response = llm.predict(f"""
Answer ONLY using the context below.
If answer is not present, say "NOT_FOUND".

Context:
{context}

Query:
{query}
""")

    if "NOT_FOUND" in response:
        return "NO_CONTEXT"

    return response
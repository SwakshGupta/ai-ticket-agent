from langchain.tools import tool
from rag.retriever import get_retriever

retriever = get_retriever()

@tool
def search_runbooks(query: str) -> str:
    """Search internal runbooks for known issues"""
    docs = retriever.get_relevant_documents(query)
    return "\n\n".join([doc.page_content for doc in docs])
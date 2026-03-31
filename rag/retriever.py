# rag/retriever.py

def hybrid_search(query, vector_db=None, docs=None):
    results = []

    # 🔹 Vector search (if available)
    if vector_db:
        vector_results = vector_db.similarity_search(query, k=2)
        results.extend(vector_results)

    # 🔹 Keyword search
    if docs:
        keyword_results = [
            doc for doc in docs if query.lower() in doc.page_content.lower()
        ][:2]
        results.extend(keyword_results)

    return results
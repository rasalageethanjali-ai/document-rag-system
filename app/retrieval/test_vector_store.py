from app.embeddings.embedder import Embedder
from app.retrieval.vector_store import VectorStore

texts = [
    "RAG allows language models to use external knowledge.",
    "Vector databases store embeddings for similarity search.",
    "FastAPI is used to build APIs in Python."
]

embedder = Embedder()
embeddings = embedder.embed(texts)

store = VectorStore()
store.add(texts, embeddings)

query = "How do LLMs use external documents?"
query_embedding = embedder.embed([query])[0]

results = store.search(query_embedding, k=2)

print("Search results:")
for r in results:
    print("-", r)

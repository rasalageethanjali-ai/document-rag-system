from typing import List
import numpy as np

from app.embeddings.embedder import Embedder
from app.retrieval.vector_store import VectorStore


class Retriever:
    """
    Handles semantic retrieval for RAG.
    Converts query → embedding → similarity search.
    """

    def __init__(self):
        self.embedder = Embedder()
        self.vector_store = VectorStore()

    def retrieve(self, query: str, k: int = 5) -> List[str]:
        """
        Retrieve top-k relevant text chunks for a query.
        """
        if not query or not query.strip():
            return []

        # Convert query to embedding
        query_embedding = self.embedder.embed([query])[0]

        # Search vector store
        results = self.vector_store.search(
            query_embedding=query_embedding,
            k=k
        )

        return results

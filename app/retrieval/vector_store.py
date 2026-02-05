import chromadb
from chromadb.config import Settings
from typing import List, Tuple


class VectorStore:
    def __init__(self, embedder=None, persist_dir: str = "data/chroma"):
        self.embedder = embedder

        self.client = chromadb.Client(
            Settings(
                persist_directory=persist_dir,
                anonymized_telemetry=False
            )
        )

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

    def add(self, texts: List[str], embeddings):
        ids = [str(i) for i in range(len(texts))]
        self.collection.add(
            documents=texts,
            embeddings=embeddings.tolist(),
            ids=ids
        )

    def search(self, query, k: int = 3) -> List[Tuple[str, float]]:
        if isinstance(query, str):
            query_embedding = self.embedder.embed([query])[0]
        else:
            query_embedding = query

        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=k
        )

        docs = results["documents"][0]
        scores = results["distances"][0]

        return list(zip(docs, scores))

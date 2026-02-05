import chromadb
from chromadb.config import Settings


class VectorStore:
    def __init__(self, persist_dir: str = "data/vector_db"):
        self.client = chromadb.Client(
            Settings(
                persist_directory=persist_dir,
                anonymized_telemetry=False
            )
        )
        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

    def add(self, documents: list[str], embeddings: list[list[float]]):
        ids = [f"doc_{i}" for i in range(len(documents))]
        self.collection.add(
            documents=documents,
            embeddings=embeddings,
            ids=ids
        )

    def search(self, query_embedding: list[float], k: int = 3) -> list[str]:
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k
        )
        return results["documents"][0]

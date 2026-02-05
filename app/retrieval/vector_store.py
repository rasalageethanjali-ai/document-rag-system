import chromadb
from chromadb.config import Settings


class VectorStore:
    def __init__(self, embedder):
        self.embedder = embedder

        self.client = chromadb.Client(
            Settings(
                persist_directory="data/chroma",  # MUST be a string
                anonymized_telemetry=False
            )
        )

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

    def add_documents(self, texts):
        embeddings = self.embedder.embed(texts)
        ids = [f"doc_{i}" for i in range(len(texts))]

        self.collection.add(
            documents=texts,
            embeddings=embeddings,
            ids=ids
        )

    def search(self, query, k=3):
        query_embedding = self.embedder.embed([query])[0]

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k
        )

        return results["documents"][0]


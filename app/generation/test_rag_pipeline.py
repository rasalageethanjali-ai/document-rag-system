from app.ingestion.loader import load_document
from app.ingestion.cleaner import clean_text
from app.ingestion.chunker import chunk_text
from app.embeddings.embedder import Embedder
from app.retrieval.vector_store import VectorStore
from app.generation.llm import LLM


def run_rag_test():
    # Load + clean
    text = load_document("data/sample_docs/sample.txt")
    cleaned = clean_text(text)

    # Chunk
    chunks = chunk_text(cleaned)

    # Embed + store
    embedder = Embedder()
    store = VectorStore(embedder)
    store.add_documents(chunks)

    # Query
    question = "What does RAG enable LLMs to do?"
    results = store.search(question, k=2)

    context = "\n".join(results)

    # Generate
    llm = LLM()
    answer = llm.generate(context, question)

    print("=== CONTEXT ===")
    print(context)
    print("\n=== ANSWER ===")
    print(answer)


if __name__ == "__main__":
    run_rag_test()

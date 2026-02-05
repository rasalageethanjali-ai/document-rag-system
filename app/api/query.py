from fastapi import APIRouter, Query
from app.embeddings.embedder import Embedder
from app.retrieval.vector_store import VectorStore
from app.generation.llm import LLM

router = APIRouter()

embedder = Embedder()
store = VectorStore(embedder)
llm = LLM()

@router.post("/")
def query_document(question: str = Query(...)):
    results = store.search(question, k=3)

    if not results:
        return {"answer": "No relevant information found."}

    context = "\n".join([doc for doc, _ in results])
    answer = llm.generate(context=context, question=question)

    return {
        "question": question,
        "answer": answer,
        "context_used": context
    }

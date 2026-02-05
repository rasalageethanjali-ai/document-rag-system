from fastapi import APIRouter, UploadFile, File
from app.embeddings.embedder import Embedder
from app.retrieval.vector_store import VectorStore
import PyPDF2

router = APIRouter()

embedder = Embedder()
store = VectorStore(embedder)

def extract_text_from_pdf(file: UploadFile) -> str:
    reader = PyPDF2.PdfReader(file.file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

@router.post("/")
async def upload_document(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file)

    if not text.strip():
        return {"error": "No text extracted"}

    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    embeddings = embedder.embed(chunks)
    store.add(chunks, embeddings)

    return {"filename": file.filename, "chunks_added": len(chunks)}

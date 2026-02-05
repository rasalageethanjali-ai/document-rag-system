from fastapi import APIRouter, UploadFile, File
from pypdf import PdfReader
from app.embeddings.embedder import Embedder
from app.retrieval.vector_store import VectorStore

router = APIRouter()
embedder = Embedder()
store = VectorStore(embedder)

def extract_text(pdf_file: UploadFile) -> str:
    reader = PdfReader(pdf_file.file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"
    return text

@router.post("/")
async def upload_document(file: UploadFile = File(...)):
    text = extract_text(file)
    if not text:
        return {"error": "No text extracted"}
    chunks = [text[i:i+500] for i in range(0, len(text), 500)]
    embeddings = embedder.embed(chunks)
    store.add(chunks, embeddings)
    return {"filename": file.filename, "chunks_added": len(chunks)}

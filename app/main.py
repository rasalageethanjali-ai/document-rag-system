from fastapi import FastAPI
from app.api.upload import router as upload_router
from app.api.query import router as query_router

app = FastAPI(title="Document RAG System")

app.include_router(upload_router, prefix="/upload")
app.include_router(query_router, prefix="/query")

@app.get("/")
def health():
    return {"status": "RAG backend running"}

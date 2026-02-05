\# 📄 Document RAG System (Retrieval-Augmented Generation)



An end-to-end \*\*Retrieval-Augmented Generation (RAG)\*\* backend that allows users to upload documents and ask questions grounded strictly in the uploaded content.



This project demonstrates a \*\*production-style RAG pipeline\*\* built using Python, FastAPI, vector embeddings, and semantic search.



---



\## 🚀 Features



\- 📂 Upload PDF documents  

\- ✂️ Chunk and embed document text  

\- 🧠 Semantic search using vector similarity  

\- 🧾 Strict RAG prompt (no hallucinations)  

\- ⚡ FastAPI backend with REST endpoints  

\- 🧪 Modular, testable architecture  



---



\## 🏗️ System Architecture



User Query

↓

Embedding Model

↓

Vector Store (Similarity Search)

↓

Relevant Context

↓

RAG Prompt

↓

LLM Response





---



\## 📁 Project Structure





document-rag-system/

│

├── app/

│ ├── api/

│ │ ├── upload.py # PDF upload endpoint

│ │ └── query.py # Question answering endpoint

│ │

│ ├── ingestion/ # Loading, cleaning, chunking

│ ├── embeddings/ # Embedding model wrapper

│ ├── retrieval/ # Vector store logic

│ ├── generation/ # RAG prompt + LLM interface

│ │

│ └── main.py # FastAPI entry point

│

├── data/

│ └── chroma/ # Vector store persistence

│

├── requirements.txt

├── README.md

└── .gitignore







---



\## ⚙️ Tech Stack



\- \*\*Python 3.11\*\*

\- \*\*FastAPI\*\* – API framework

\- \*\*SentenceTransformers\*\* – Text embeddings

\- \*\*Vector Store (Chroma-style)\*\* – Semantic retrieval

\- \*\*PyPDF2\*\* – PDF parsing

\- \*\*Uvicorn\*\* – ASGI server



---



\## 🧠 RAG Design Principles



\- Answers are generated \*\*only from retrieved context\*\*

\- If context is missing → model explicitly says so

\- No guessing, no hallucination

\- Clear separation of ingestion, retrieval, and generation



---

### 2️⃣ Create & activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate

---

3️⃣ Install dependencies
pip install -r requirements.txt

----

4️⃣ Start the server
uvicorn app.main:app --reload

----
📘 API Documentation
FastAPI auto-generated docs available

---

Upload Document

POST /upload

Description

Upload a PDF document

Text is extracted, chunked, embedded, and stored in the vector database
------
🔹 Ask Question
POST /query?question=
Description

Performs semantic search on stored documents

Generates a grounded answer using a strict RAG prompt
----

🧪 Example Workflow

Upload a PDF document

Ask:
What does the document say about RAG?
System:
Retrieves relevant chunks
Builds context
Generates a grounded answer
------

🚀 Future Improvements

🌍 Cloud deployment (Render / Railway / AWS)

🔑 Authentication & user sessions

🗄️ Persistent vector database

🤖 Real LLM integration (OpenAI / Ollama / HuggingFace)

📊 Frontend UI
-------

👩‍💻 Author

Rasala Geethanjali
AI & ML Engineering Student
Focused on building real-world GenAI systems

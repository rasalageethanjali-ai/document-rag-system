# \# 📄 Document RAG System (Retrieval-Augmented Generation)

# 

# An end-to-end \*\*Retrieval-Augmented Generation (RAG)\*\* backend that allows users to upload documents and ask questions grounded strictly in the uploaded content.

# 

# This project demonstrates a \*\*production-style RAG pipeline\*\* built using Python, FastAPI, vector embeddings, and semantic search.

# 

# ---

# 

# \## 🚀 Features

# 

# \- 📂 Upload PDF documents

# \- ✂️ Chunk and embed document text

# \- 🧠 Semantic search using vector similarity

# \- 🧾 Strict RAG prompt (no hallucinations)

# \- ⚡ FastAPI backend with REST endpoints

# \- 🧪 Modular, testable architecture

# 

# ---

# 

# \## 🏗️ System Architecture

# 

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

\- \*\*Chroma / Vector Store\*\* – Semantic retrieval

\- \*\*PyPDF2\*\* – PDF parsing

\- \*\*Uvicorn\*\* – ASGI server



---



\## 🧠 RAG Design Principles



\- Answers are generated \*\*only from retrieved context\*\*

\- If context is missing → model explicitly says so

\- No guessing, no hallucination

\- Clear separation of ingestion, retrieval, and generation



---



\## ▶️ Running Locally



\### 1️⃣ Clone the repository

```bash

git clone https://github.com/rasalageethanjali-ai/document-rag-system.git

cd document-rag-system





2️⃣ Create \& activate virtual environment

python -m venv venv

venv\\Scripts\\activate



3️⃣ Install dependencies

pip install -r requirements.txt



4️⃣ Start the server

uvicorn app.main:app --reload



4️⃣ Start the server

uvicorn app.main:app --reload



📘 API Documentation



FastAPI auto-docs available



🔹 Upload Document



POST /upload



Upload a PDF file



Text is extracted, chunked, embedded, and stored



🔹 Ask Question



POST /query?question=...



Performs semantic search



Generates answer using RAG prompt





🧪 Example Workflow



Upload a PDF



Ask:



“What does the document say about RAG?”



System:



Retrieves relevant chunks



Builds context



Generates grounded answer





🚀 Future Improvements



🌍 Cloud deployment (Render / Railway / AWS)



🔑 Auth \& user sessions



🗄️ Persistent vector DB



🤖 Real LLM integration



📊 UI frontend





👩‍💻 Author



Rasala Geethanjali

AI \& ML Engineering Student

Focused on building real-world GenAI systems








from loader import load_document
from cleaner import clean_text
from chunker import chunk_text

text = load_document("data/sample_docs/sample.txt")
cleaned = clean_text(text)
chunks = chunk_text(cleaned)

print(f"Total chunks: {len(chunks)}\n")

for i, chunk in enumerate(chunks):
    print(f"--- Chunk {i+1} ---")
    print(chunk)
    print()

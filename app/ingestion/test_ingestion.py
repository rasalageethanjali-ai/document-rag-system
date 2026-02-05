from loader import load_document
from cleaner import clean_text

path = "data/sample_docs/sample.txt"

raw = load_document(path)
cleaned = clean_text(raw)

print("RAW:")
print(raw)
print("\nCLEANED:")
print(cleaned)

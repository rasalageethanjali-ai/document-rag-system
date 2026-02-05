from pathlib import Path
from pypdf import PdfReader


def load_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    pages = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages.append(text)

    return "\n".join(pages)


def load_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def load_document(file_path: str) -> str:
    path = Path(file_path)

    if path.suffix.lower() == ".pdf":
        return load_pdf(file_path)
    elif path.suffix.lower() == ".txt":
        return load_txt(file_path)

    raise ValueError(f"Unsupported file type: {path.suffix}")

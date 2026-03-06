"""Chapter 7-2: Load PDF, split it into chunks, and persist chunks for Chapter 8."""

import json
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = BASE_DIR / "sample_data" / "vertex_guide.pdf"
OUTPUT_PATH = BASE_DIR / "sample_data" / "split_docs.jsonl"


def _safe_metadata(metadata: dict) -> dict:
    """Convert metadata values to JSON-safe primitives."""
    safe = {}
    for key, value in metadata.items():
        if isinstance(value, (str, int, float, bool)) or value is None:
            safe[key] = value
        else:
            safe[key] = str(value)
    return safe


loader = PyPDFLoader(str(FILE_PATH))
documents = loader.load()
print(f"Loaded pages: {len(documents)}")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n", "\n", " ", ""],
)

split_docs = text_splitter.split_documents(documents)
print(f"Total chunks: {len(split_docs)}")

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
with OUTPUT_PATH.open("w", encoding="utf-8") as f:
    for doc in split_docs:
        payload = {
            "page_content": doc.page_content,
            "metadata": _safe_metadata(doc.metadata),
        }
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")

print(f"Saved chunks to: {OUTPUT_PATH}")

first_chunk = split_docs[0]
print("\n=== First chunk preview ===")
print(first_chunk.page_content[:300])
print("\n=== First chunk metadata ===")
print(first_chunk.metadata)

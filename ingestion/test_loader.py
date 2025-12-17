from pathlib import Path
from loader import load_documents

docs = load_documents(Path("data/raw"))
print(f"Loaded {len(docs)} chunks")

print(docs[0])
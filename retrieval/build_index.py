from pathlib import Path
from ingestion.loader import load_documents
from retrieval.chunking import FixedSizeChunker
from retrieval.embeddings import embed_texts
from retrieval.vector_store import add_documents

docs = load_documents(Path("data/raw"))

chunker = FixedSizeChunker()
chunks = chunker.chunk(docs)

texts = [c["content"] for c in chunks]
embeddings = embed_texts(texts)

add_documents(chunks, embeddings)

print("Index built successfully")

from pathlib import Path
from ingestion.loader import load_documents
from retrieval.chunking import FixedSizeChunker, ParagraphChunker

docs = load_documents(Path("data/raw"))

fixed = FixedSizeChunker()
para = ParagraphChunker()

fixed_chunks = fixed.chunk(docs)
para_chunks = para.chunk(docs)

print(f"Fixed chunks: {len(fixed_chunks)}")
print(f"Paragraph chunks: {len(para_chunks)}")

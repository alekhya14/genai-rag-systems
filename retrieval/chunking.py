from typing import List, Dict

Document = Dict[str, any]

class BaseChunker:
    def chunk(self, documents: List[Document]) -> List[Document]:
        raise NotImplementedError

class FixedSizeChunker(BaseChunker):
    def __init__(self, chunk_size: int = 500, overlap: int = 50):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, documents: List[Document]) -> List[Document]:
        chunks = []

        for doc in documents:
            text = doc["content"]
            start = 0

            while start < len(text):
                end = start + self.chunk_size
                chunk_text = text[start:end]

                chunks.append({
                    "content": chunk_text,
                    "metadata": {
                        **doc.get("metadata", {}),
                        "chunk_start": start
                    }
                })

                start += self.chunk_size - self.overlap

        return chunks

class ParagraphChunker(BaseChunker):
    def __init__(self, max_length: int = 800):
        self.max_length = max_length

    def chunk(self, documents: List[Document]) -> List[Document]:
        chunks = []

        for doc in documents:
            paragraphs = doc["content"].split("\n\n")
            current_chunk = ""

            for para in paragraphs:
                if len(current_chunk) + len(para) <= self.max_length:
                    current_chunk += para + "\n\n"
                else:
                    chunks.append({
                        "content": current_chunk.strip(),
                        "metadata": doc.get("metadata", {})
                    })
                    current_chunk = para + "\n\n"

            if current_chunk.strip():
                chunks.append({
                    "content": current_chunk.strip(),
                    "metadata": doc.get("metadata", {})
                })

        return chunks

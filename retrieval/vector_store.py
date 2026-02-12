import chromadb
from chromadb.config import Settings

client = chromadb.Client(
    Settings(persist_directory="data/chroma")
)

collection = client.get_or_create_collection(
    name="documents"
)

def add_documents(chunks, embeddings):
    for chunk, embedding in zip(chunks, embeddings):
        collection.add(
            documents=[chunk["content"]],
            metadatas=[chunk["metadata"]],
            embeddings=[embedding],
            ids=[str(hash(chunk["content"]))]
        )

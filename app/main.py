from fastapi import FastAPI
from app.api.health import router as health_router

app = FastAPI(
    title="GenAI RAG System",
    description="Production-oriented RAG system with evaluation and reliability considerations",
    version="0.1.0",
)

app.include_router(health_router)

@app.get("/")
def root():
    return {"message": "GenAI RAG System is running"}

"""FastAPI application for free RAG chatbot using local models."""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from .config import settings
from .rag_service import rag_service
from .ollama_client import ollama_service
from .chroma_client import chroma_manager

app = FastAPI(
    title="Physical AI Book RAG Chatbot (Free Version)",
    description="Retrieval-Augmented Generation chatbot using local models (Ollama + ChromaDB)",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    """Request model for chat queries."""
    question: str
    selected_text: Optional[str] = None
    top_k: Optional[int] = None


class QueryResponse(BaseModel):
    """Response model for chat queries."""
    answer: str
    sources: list
    context_used: int
    has_selected_text: bool


@app.on_event("startup")
async def startup_event():
    """Initialize services on startup."""
    print("=" * 50)
    print("Starting FREE RAG Chatbot Backend")
    print("=" * 50)
    print("✅ Using local models (NO API KEYS needed!)")
    print(f"✅ LLM: Ollama - {settings.ollama_model}")
    print(f"✅ Embeddings: {settings.embedding_model}")
    print(f"✅ Vector DB: ChromaDB (local)")
    print("=" * 50)

    # Ensure Ollama model is ready
    try:
        ollama_service.ensure_model_ready()
    except Exception as e:
        print(f"⚠️  Warning: Could not verify Ollama model: {e}")
        print("   Make sure Ollama is installed and running!")

    # Initialize ChromaDB collection
    try:
        chroma_manager.create_collection()
        doc_count = chroma_manager.count_documents()
        print(f"✅ ChromaDB ready: {doc_count} documents loaded")
    except Exception as e:
        print(f"⚠️  Warning: ChromaDB issue: {e}")


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Physical AI Book RAG Chatbot API (FREE VERSION)",
        "version": "1.0.0",
        "features": [
            "✅ Completely FREE - no API keys needed",
            "✅ Local LLM (Ollama)",
            "✅ Local embeddings (sentence-transformers)",
            "✅ Local vector DB (ChromaDB)",
            "✅ 100% privacy - all data stays local"
        ],
        "endpoints": {
            "/query": "POST - Ask a question about the book",
            "/health": "GET - Health check",
            "/stats": "GET - Database statistics"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    ollama_ready = ollama_service.check_model_available()
    doc_count = chroma_manager.count_documents()

    return {
        "status": "healthy" if ollama_ready and doc_count > 0 else "warning",
        "service": "free-rag-chatbot",
        "ollama_model": settings.ollama_model,
        "ollama_ready": ollama_ready,
        "embedding_model": settings.embedding_model,
        "documents_loaded": doc_count,
        "message": "All local - NO API costs!" if ollama_ready else "Ollama not ready"
    }


@app.get("/stats")
async def get_stats():
    """Get database statistics."""
    doc_count = chroma_manager.count_documents()
    return {
        "total_documents": doc_count,
        "collection_name": settings.chroma_collection_name,
        "embedding_model": settings.embedding_model,
        "llm_model": settings.ollama_model,
        "cost": "FREE - $0.00"
    }


@app.post("/query", response_model=QueryResponse)
async def query_chatbot(request: QueryRequest):
    """
    Query the RAG chatbot with a question.

    Args:
        request: Query request with question and optional selected text

    Returns:
        Answer with sources and metadata
    """
    try:
        if not request.question or not request.question.strip():
            raise HTTPException(status_code=400, detail="Question cannot be empty")

        # Check if Ollama is ready
        if not ollama_service.check_model_available():
            raise HTTPException(
                status_code=503,
                detail=f"Ollama model '{settings.ollama_model}' not available. "
                       "Please install Ollama and pull the model."
            )

        result = rag_service.query(
            question=request.question,
            selected_text=request.selected_text,
            top_k=request.top_k
        )

        return QueryResponse(**result)

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

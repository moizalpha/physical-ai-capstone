"""FastAPI application for RAG chatbot."""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from .config import settings
from .rag_service import rag_service

app = FastAPI(
    title="Physical AI Book RAG Chatbot",
    description="Retrieval-Augmented Generation chatbot for the Physical AI book",
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


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Physical AI Book RAG Chatbot API",
        "version": "1.0.0",
        "endpoints": {
            "/query": "POST - Ask a question about the book",
            "/health": "GET - Health check"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "rag-chatbot",
        "model": settings.chat_model,
        "embedding_model": settings.embedding_model
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

        result = rag_service.query(
            question=request.question,
            selected_text=request.selected_text,
            top_k=request.top_k
        )

        return QueryResponse(**result)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

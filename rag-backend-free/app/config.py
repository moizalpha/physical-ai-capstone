"""Configuration management for the free RAG backend."""
from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Ollama Configuration (Local LLM)
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.2:3b"

    # Local Embedding Configuration
    embedding_model: str = "all-MiniLM-L6-v2"

    # ChromaDB Configuration (Local Vector DB)
    chroma_persist_directory: str = "./chroma_db"
    chroma_collection_name: str = "physical_ai_book"

    # RAG Configuration
    chunk_size: int = 1000
    chunk_overlap: int = 200
    top_k_results: int = 5

    # CORS Configuration
    allowed_origins: str = "http://localhost:3000"

    @property
    def allowed_origins_list(self) -> List[str]:
        """Parse comma-separated origins into a list."""
        return [origin.strip() for origin in self.allowed_origins.split(",")]

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()

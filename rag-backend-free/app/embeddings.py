"""Local embedding generation using sentence-transformers."""
from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np
from .config import settings


class EmbeddingService:
    """Service for generating embeddings using local models."""

    def __init__(self):
        """Initialize local embedding model."""
        print(f"Loading embedding model: {settings.embedding_model}")
        self.model = SentenceTransformer(settings.embedding_model)
        print("Embedding model loaded successfully!")

    def create_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Create embeddings for a list of texts.

        Args:
            texts: List of text strings to embed

        Returns:
            List of embedding vectors
        """
        embeddings = self.model.encode(texts, show_progress_bar=True)
        return embeddings.tolist()

    def create_embedding(self, text: str) -> List[float]:
        """
        Create embedding for a single text.

        Args:
            text: Text string to embed

        Returns:
            Embedding vector
        """
        embedding = self.model.encode([text])[0]
        return embedding.tolist()

    @property
    def embedding_dimension(self) -> int:
        """Get the dimension of the embedding vectors."""
        return self.model.get_sentence_embedding_dimension()


# Singleton instance
embedding_service = EmbeddingService()

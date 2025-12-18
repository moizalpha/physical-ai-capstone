"""Embedding generation using OpenAI."""
from openai import OpenAI
from typing import List
from .config import settings


class EmbeddingService:
    """Service for generating embeddings using OpenAI."""

    def __init__(self):
        """Initialize OpenAI client."""
        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = settings.embedding_model

    def create_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Create embeddings for a list of texts.

        Args:
            texts: List of text strings to embed

        Returns:
            List of embedding vectors
        """
        response = self.client.embeddings.create(
            model=self.model,
            input=texts
        )

        return [data.embedding for data in response.data]

    def create_embedding(self, text: str) -> List[float]:
        """
        Create embedding for a single text.

        Args:
            text: Text string to embed

        Returns:
            Embedding vector
        """
        response = self.client.embeddings.create(
            model=self.model,
            input=[text]
        )

        return response.data[0].embedding


# Singleton instance
embedding_service = EmbeddingService()

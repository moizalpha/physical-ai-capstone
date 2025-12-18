"""Qdrant client for vector storage and retrieval."""
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from typing import List, Dict, Any
import uuid
from .config import settings


class QdrantManager:
    """Manages Qdrant vector database operations."""

    def __init__(self):
        """Initialize Qdrant client."""
        self.client = QdrantClient(
            url=settings.qdrant_url,
            api_key=settings.qdrant_api_key,
        )
        self.collection_name = settings.qdrant_collection_name

    def create_collection(self, vector_size: int = 1536):
        """
        Create a collection in Qdrant if it doesn't exist.

        Args:
            vector_size: Dimension of embedding vectors (1536 for text-embedding-3-small)
        """
        collections = self.client.get_collections().collections
        collection_names = [collection.name for collection in collections]

        if self.collection_name not in collection_names:
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=vector_size,
                    distance=Distance.COSINE
                ),
            )
            print(f"Created collection: {self.collection_name}")
        else:
            print(f"Collection {self.collection_name} already exists")

    def upsert_documents(self, documents: List[Dict[str, Any]], embeddings: List[List[float]]):
        """
        Insert or update documents in the collection.

        Args:
            documents: List of document dicts with metadata
            embeddings: Corresponding embedding vectors
        """
        points = [
            PointStruct(
                id=str(uuid.uuid4()),
                vector=embedding,
                payload=doc
            )
            for doc, embedding in zip(documents, embeddings)
        ]

        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )
        print(f"Upserted {len(points)} documents")

    def search(self, query_vector: List[float], limit: int = 5, filter_dict: Dict = None) -> List[Dict]:
        """
        Search for similar documents.

        Args:
            query_vector: Query embedding vector
            limit: Maximum number of results
            filter_dict: Optional metadata filters

        Returns:
            List of matching documents with scores
        """
        search_result = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            limit=limit,
            query_filter=filter_dict
        )

        return [
            {
                "id": hit.id,
                "score": hit.score,
                "payload": hit.payload
            }
            for hit in search_result
        ]

    def delete_collection(self):
        """Delete the collection (use with caution)."""
        self.client.delete_collection(collection_name=self.collection_name)
        print(f"Deleted collection: {self.collection_name}")


# Singleton instance
qdrant_manager = QdrantManager()

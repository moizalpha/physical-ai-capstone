"""ChromaDB client for local vector storage and retrieval."""
import chromadb
from chromadb.config import Settings as ChromaSettings
from typing import List, Dict, Any
import uuid
from .config import settings


class ChromaManager:
    """Manages ChromaDB local vector database operations."""

    def __init__(self):
        """Initialize ChromaDB client."""
        self.client = chromadb.PersistentClient(
            path=settings.chroma_persist_directory,
            settings=ChromaSettings(anonymized_telemetry=False)
        )
        self.collection_name = settings.chroma_collection_name
        self.collection = None

    def create_collection(self):
        """
        Create or get a collection in ChromaDB.
        """
        try:
            self.collection = self.client.get_or_create_collection(
                name=self.collection_name,
                metadata={"description": "Physical AI book content"}
            )
            print(f"Collection ready: {self.collection_name}")
        except Exception as e:
            print(f"Error creating collection: {e}")
            raise

    def upsert_documents(self, documents: List[Dict[str, Any]], embeddings: List[List[float]]):
        """
        Insert or update documents in the collection.

        Args:
            documents: List of document dicts with metadata
            embeddings: Corresponding embedding vectors
        """
        if not self.collection:
            self.create_collection()

        ids = [str(uuid.uuid4()) for _ in documents]

        # Extract text content
        texts = [doc["text"] for doc in documents]

        # Prepare metadata (ChromaDB requires all metadata values to be simple types)
        metadatas = [
            {
                "title": doc.get("title", ""),
                "file_path": doc.get("file_path", ""),
                "source": doc.get("source", ""),
                "chunk_id": doc.get("chunk_id", 0),
                "total_chunks": doc.get("total_chunks", 1)
            }
            for doc in documents
        ]

        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=texts,
            metadatas=metadatas
        )
        print(f"Upserted {len(documents)} documents")

    def search(self, query_vector: List[float], limit: int = 5) -> List[Dict]:
        """
        Search for similar documents.

        Args:
            query_vector: Query embedding vector
            limit: Maximum number of results

        Returns:
            List of matching documents with scores
        """
        if not self.collection:
            self.create_collection()

        results = self.collection.query(
            query_embeddings=[query_vector],
            n_results=limit
        )

        # Format results
        formatted_results = []
        if results and results['ids'] and len(results['ids'][0]) > 0:
            for i in range(len(results['ids'][0])):
                formatted_results.append({
                    "id": results['ids'][0][i],
                    "score": 1 - results['distances'][0][i],  # Convert distance to similarity
                    "payload": {
                        "text": results['documents'][0][i],
                        "title": results['metadatas'][0][i].get('title', ''),
                        "file_path": results['metadatas'][0][i].get('file_path', ''),
                        "chunk_id": results['metadatas'][0][i].get('chunk_id', 0),
                        "source": results['metadatas'][0][i].get('source', '')
                    }
                })

        return formatted_results

    def delete_collection(self):
        """Delete the collection (use with caution)."""
        try:
            self.client.delete_collection(name=self.collection_name)
            print(f"Deleted collection: {self.collection_name}")
        except Exception as e:
            print(f"Error deleting collection: {e}")

    def count_documents(self) -> int:
        """Get the number of documents in the collection."""
        if not self.collection:
            self.create_collection()
        return self.collection.count()


# Singleton instance
chroma_manager = ChromaManager()

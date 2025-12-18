"""Script to ingest documents and create embeddings."""
import sys
import os
from pathlib import Path

# Add app directory to path
sys.path.insert(0, str(Path(__file__).parent))

from app.document_processor import document_processor
from app.embeddings import embedding_service
from app.qdrant_client import qdrant_manager
from app.config import settings


def ingest_documents(docs_dir: str):
    """
    Ingest documents from a directory and store in Qdrant.

    Args:
        docs_dir: Path to directory containing markdown files
    """
    print(f"Starting document ingestion from: {docs_dir}")

    # Step 1: Load markdown files
    print("\n1. Loading markdown files...")
    documents = document_processor.load_markdown_files(docs_dir)
    print(f"   Loaded {len(documents)} documents")

    if not documents:
        print("   No documents found. Exiting.")
        return

    # Step 2: Chunk documents
    print("\n2. Chunking documents...")
    chunked_docs = document_processor.chunk_documents(documents)
    print(f"   Created {len(chunked_docs)} chunks")

    # Step 3: Create collection in Qdrant
    print("\n3. Setting up Qdrant collection...")
    qdrant_manager.create_collection(vector_size=1536)

    # Step 4: Generate embeddings in batches
    print("\n4. Generating embeddings...")
    batch_size = 100
    total_batches = (len(chunked_docs) + batch_size - 1) // batch_size

    for i in range(0, len(chunked_docs), batch_size):
        batch = chunked_docs[i:i + batch_size]
        batch_num = i // batch_size + 1

        print(f"   Processing batch {batch_num}/{total_batches}...")

        # Extract texts for embedding
        texts = [doc["text"] for doc in batch]

        # Generate embeddings
        embeddings = embedding_service.create_embeddings(texts)

        # Store in Qdrant
        qdrant_manager.upsert_documents(batch, embeddings)

    print(f"\n✓ Successfully ingested {len(chunked_docs)} document chunks!")
    print(f"  Collection: {settings.qdrant_collection_name}")
    print(f"  Embedding model: {settings.embedding_model}")


def main():
    """Main entry point."""
    # Default to docs directory in parent folder
    default_docs_dir = Path(__file__).parent.parent / "docs" / "docs"

    if len(sys.argv) > 1:
        docs_dir = sys.argv[1]
    else:
        docs_dir = str(default_docs_dir)

    if not os.path.exists(docs_dir):
        print(f"Error: Directory not found: {docs_dir}")
        print(f"\nUsage: python ingest_documents.py [docs_directory]")
        sys.exit(1)

    try:
        ingest_documents(docs_dir)
    except Exception as e:
        print(f"\nError during ingestion: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

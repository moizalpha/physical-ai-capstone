# RAG Chatbot Backend

FastAPI backend for the Physical AI Book RAG (Retrieval-Augmented Generation) chatbot.

## Features

- **RAG Architecture**: Combines document retrieval with OpenAI's GPT models
- **Vector Search**: Uses Qdrant Cloud for fast semantic search
- **Text Selection Support**: Can answer questions about user-selected text
- **Document Processing**: Automatically chunks and embeds markdown content
- **RESTful API**: Clean FastAPI endpoints for querying

## Prerequisites

- Python 3.9+
- OpenAI API key
- Qdrant Cloud account (free tier available)

## Quick Start

### 1. Install Dependencies

```bash
cd rag-backend
pip install -r requirements.txt
```

### 2. Configure Environment

Create a `.env` file from the template:

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```env
# OpenAI Configuration
OPENAI_API_KEY=sk-your-key-here

# Qdrant Configuration (sign up at https://cloud.qdrant.io)
QDRANT_URL=https://your-cluster.qdrant.io
QDRANT_API_KEY=your-qdrant-key-here
QDRANT_COLLECTION_NAME=physical_ai_book

# Application Configuration
EMBEDDING_MODEL=text-embedding-3-small
CHAT_MODEL=gpt-4o-mini
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
TOP_K_RESULTS=5

# CORS Configuration
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
```

### 3. Ingest Documents

Process and embed your markdown documents:

```bash
python ingest_documents.py ../docs/docs
```

This will:
1. Load all markdown files from the docs directory
2. Chunk them into smaller pieces
3. Generate embeddings using OpenAI
4. Store in Qdrant Cloud

Expected output:
```
Starting document ingestion from: ../docs/docs
1. Loading markdown files...
   Loaded 15 documents
2. Chunking documents...
   Created 87 chunks
3. Setting up Qdrant collection...
   Created collection: physical_ai_book
4. Generating embeddings...
   Processing batch 1/1...
✓ Successfully ingested 87 document chunks!
```

### 4. Start the Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Health Check

```bash
GET /health
```

Response:
```json
{
  "status": "healthy",
  "service": "rag-chatbot",
  "model": "gpt-4o-mini",
  "embedding_model": "text-embedding-3-small"
}
```

### Query Chatbot

```bash
POST /query
Content-Type: application/json

{
  "question": "What is Physical AI?",
  "selected_text": "optional user-selected text",
  "top_k": 5
}
```

Response:
```json
{
  "answer": "Physical AI refers to...",
  "sources": [
    {
      "title": "Introduction to Physical AI",
      "file_path": "docs/intro.md",
      "chunk_id": 0,
      "score": 0.92
    }
  ],
  "context_used": 5,
  "has_selected_text": false
}
```

## Project Structure

```
rag-backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── config.py            # Configuration management
│   ├── qdrant_client.py     # Qdrant vector DB client
│   ├── embeddings.py        # OpenAI embedding service
│   ├── document_processor.py # Document chunking
│   └── rag_service.py       # RAG query logic
├── ingest_documents.py      # Document ingestion script
├── requirements.txt         # Python dependencies
├── .env.example            # Environment template
└── README.md
```

## Configuration Options

### Embedding Models

- `text-embedding-3-small` (1536 dims, recommended)
- `text-embedding-3-large` (3072 dims, higher quality)
- `text-embedding-ada-002` (1536 dims, legacy)

### Chat Models

- `gpt-4o-mini` (recommended, fast and affordable)
- `gpt-4o` (higher quality)
- `gpt-3.5-turbo` (fastest, most affordable)

### Chunking Parameters

- **chunk_size**: Maximum characters per chunk (default: 1000)
- **chunk_overlap**: Overlap between chunks (default: 200)
- Adjust based on your content and use case

### Retrieval Parameters

- **top_k_results**: Number of chunks to retrieve (default: 5)
- Higher values provide more context but increase token usage

## Qdrant Cloud Setup

1. Sign up at https://cloud.qdrant.io (free tier available)
2. Create a new cluster
3. Copy your cluster URL and API key
4. Add them to your `.env` file

Free tier includes:
- 1 GB storage
- Unlimited requests
- Perfect for development and small projects

## Development

### Running Tests

```bash
pytest
```

### Debugging

Enable debug mode:
```bash
uvicorn app.main:app --reload --log-level debug
```

### Re-ingesting Documents

To update the knowledge base:
```bash
# Delete existing collection (optional)
python -c "from app.qdrant_client import qdrant_manager; qdrant_manager.delete_collection()"

# Re-ingest
python ingest_documents.py ../docs/docs
```

## Troubleshooting

### Error: "Collection not found"

Solution: Run document ingestion first:
```bash
python ingest_documents.py ../docs/docs
```

### Error: "OpenAI API key not found"

Solution: Ensure `.env` file exists with valid `OPENAI_API_KEY`

### Error: "Connection refused to Qdrant"

Solution: Check your `QDRANT_URL` and `QDRANT_API_KEY` in `.env`

### CORS Errors

Solution: Add your frontend URL to `ALLOWED_ORIGINS` in `.env`:
```env
ALLOWED_ORIGINS=http://localhost:3000,https://yourdomain.com
```

## Cost Estimation

### OpenAI Costs (as of Dec 2024)

**Embedding (text-embedding-3-small)**:
- $0.02 per 1M tokens
- ~100 pages ≈ 50,000 tokens ≈ $0.001

**Chat (gpt-4o-mini)**:
- Input: $0.150 per 1M tokens
- Output: $0.600 per 1M tokens
- Typical query: ~1,000 input + 200 output tokens ≈ $0.0003

**Example**: 1,000 queries on 100 pages:
- Initial embedding: $0.001
- 1,000 queries: $0.30
- **Total: ~$0.30**

### Qdrant Cloud

Free tier includes 1GB storage (sufficient for most books)

## Production Deployment

### Environment Variables

Set these in your production environment:
```env
OPENAI_API_KEY=your-production-key
QDRANT_URL=your-production-cluster
QDRANT_API_KEY=your-production-key
ALLOWED_ORIGINS=https://yourdomain.com
```

### Using Docker

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/
COPY .env .env

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Health Monitoring

Monitor the `/health` endpoint for service status

### Scaling

- Qdrant Cloud handles scaling automatically
- For high traffic, consider:
  - Caching frequently asked questions
  - Rate limiting
  - Load balancing multiple FastAPI instances

## License

MIT License - see project root for details

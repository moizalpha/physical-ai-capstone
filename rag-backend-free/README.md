# FREE RAG Chatbot Backend

**100% Free** FastAPI backend using local open-source models - no API keys needed!

## Why This Version?

✅ **$0.00 forever** - No API costs
✅ **No sign-ups** - No OpenAI, no Qdrant accounts
✅ **100% private** - All data stays on your machine
✅ **Offline capable** - Works without internet
✅ **No rate limits** - Use as much as you want

## Technology Stack

- **LLM**: Ollama (llama3.2:3b) - Local, free, open-source
- **Embeddings**: sentence-transformers (all-MiniLM-L6-v2) - Local
- **Vector DB**: ChromaDB - Local SQLite-based storage
- **API**: FastAPI - Same as paid version

## Quick Start

### 1. Install Ollama

**Windows**: Download from https://ollama.com/download

**Mac/Linux**:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Download Model

```bash
ollama pull llama3.2:3b
```

Or use setup script:
```bash
# Windows
setup_ollama.bat

# Mac/Linux
chmod +x setup_ollama.sh
./setup_ollama.sh
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure

```bash
cp .env.example .env
```

No API keys to add!

### 5. Ingest Documents

```bash
python ingest_documents.py ../docs/docs
```

### 6. Start Server

```bash
uvicorn app.main:app --reload
```

## API Endpoints

Same as paid version:
- `POST /query` - Ask questions
- `GET /health` - Health check
- `GET /stats` - Database statistics

## Performance

- **First query**: ~10-15 seconds (model loading)
- **Subsequent queries**: ~5-10 seconds
- **Embedding**: ~2-5 seconds per batch
- **Storage**: Local disk (~2GB for models + data)

## Requirements

- **Python**: 3.9+
- **RAM**: 8GB+ recommended
- **Disk**: 10GB+ for models and data
- **CPU**: Multi-core recommended

## Comparing to Paid Version

| Aspect | Free | Paid |
|--------|------|------|
| Cost | $0 | ~$0.30/1K queries |
| Speed | 5-10s | 2-3s |
| Quality | Very Good | Excellent |
| Setup | 10 min | 5 min |
| Privacy | 100% local | Cloud APIs |
| RAM needed | 8GB+ | Minimal |

## Customization

### Change LLM Model

Edit `.env`:
```env
# Faster, smaller
OLLAMA_MODEL=phi3:mini

# Slower, better quality
OLLAMA_MODEL=llama3.1:8b
```

Browse models: https://ollama.com/library

### Change Embedding Model

Edit `.env`:
```env
# Larger, more accurate
EMBEDDING_MODEL=all-mpnet-base-v2

# Smaller, faster
EMBEDDING_MODEL=all-MiniLM-L12-v2
```

## Troubleshooting

### Ollama not found

```bash
# Verify installation
ollama --version

# Start Ollama service
ollama serve
```

### Model not available

```bash
# List models
ollama list

# Pull model
ollama pull llama3.2:3b
```

### Out of memory

Use smaller model:
```bash
ollama pull phi3:mini
```

Then update `.env`:
```env
OLLAMA_MODEL=phi3:mini
```

### Slow responses

1. Use smaller model (phi3:mini)
2. Reduce TOP_K_RESULTS in `.env`
3. Close other applications
4. Use GPU if available (automatic)

## File Structure

```
rag-backend-free/
├── app/
│   ├── main.py              # FastAPI app
│   ├── ollama_client.py     # Local LLM
│   ├── embeddings.py        # Local embeddings
│   ├── chroma_client.py     # Local vector DB
│   ├── rag_service.py       # RAG logic
│   └── document_processor.py
├── ingest_documents.py      # Document ingestion
├── requirements.txt         # Dependencies
├── setup_ollama.sh/.bat    # Ollama setup
└── README.md
```

## Production Deployment

Can be deployed to:
- ✅ Your own server (VPS)
- ✅ Local network
- ✅ Docker container
- ✅ Self-hosted

Not suitable for:
- ❌ Serverless (models too large)
- ❌ Low-RAM hosting
- ❌ High-traffic public sites

For public deployment, consider the paid version.

## Advantages

**Cost**: Zero forever
**Privacy**: Everything local
**Control**: Full customization
**Limits**: None

## Trade-offs

**Speed**: Slower than cloud APIs
**Setup**: More complex
**Resources**: Needs decent hardware
**Quality**: Slightly lower than GPT-4

## Support

- **Ollama**: https://ollama.com
- **ChromaDB**: https://www.trychroma.com
- **Models**: https://ollama.com/library

## License

MIT - Same as main project

---

**Status**: Production Ready
**Cost**: $0.00
**Privacy**: 100% Local
**Speed**: 5-10s per query

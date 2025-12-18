# FREE RAG Chatbot Setup Guide

## 🎉 100% Free - No API Keys Needed!

This is a **completely free** version of the RAG chatbot that runs entirely on your local machine. No OpenAI account, no Qdrant Cloud, no API costs - everything is local and private!

## Features

✅ **Completely FREE** - Zero cost, forever
✅ **No API keys** - No sign-ups required
✅ **100% Private** - All data stays on your machine
✅ **Offline capable** - Works without internet (after setup)
✅ **No rate limits** - Use as much as you want
✅ **Same features** - Text selection, source citations, etc.

## What's Different from the Paid Version?

| Feature | Free Version | Paid Version |
|---------|--------------|--------------|
| **Cost** | $0.00 forever | ~$0.30 per 1K queries |
| **Setup** | 10 minutes | 5 minutes |
| **API Keys** | None needed | OpenAI + Qdrant |
| **Speed** | 5-10 seconds/query | 2-3 seconds/query |
| **Quality** | Very good | Excellent |
| **Privacy** | 100% local | Data sent to APIs |
| **Storage** | Local disk | Cloud (Qdrant) |

## Prerequisites

1. **Python 3.9+**
2. **Node.js 20+** (for Docusaurus)
3. **8GB+ RAM** (for running local LLM)
4. **10GB+ disk space** (for models)
5. **Ollama** (we'll install this)

## Quick Start

### Step 1: Install Ollama (5 minutes)

**Windows:**
1. Download from https://ollama.com/download
2. Run the installer
3. Verify: Open CMD and type `ollama --version`

**macOS:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Step 2: Download AI Model (2 minutes)

```bash
# Download Llama 3.2 (2GB, free and open-source)
ollama pull llama3.2:3b
```

Or use the setup script:
```bash
cd rag-backend-free

# Windows
setup_ollama.bat

# Mac/Linux
chmod +x setup_ollama.sh
./setup_ollama.sh
```

### Step 3: Install Python Dependencies (2 minutes)

```bash
cd rag-backend-free
pip install -r requirements.txt
```

This installs:
- **FastAPI** - Web framework
- **Ollama** - Local LLM client
- **sentence-transformers** - Local embeddings
- **ChromaDB** - Local vector database
- **torch** - Deep learning (for embeddings)

### Step 4: Configure (30 seconds)

```bash
cp .env.example .env
```

That's it! No API keys to add.

### Step 5: Ingest Documents (5 minutes)

```bash
python ingest_documents.py ../docs/docs
```

This will:
- Load all markdown files
- Generate embeddings locally (no API calls!)
- Store in local ChromaDB
- Takes 5-10 minutes depending on content size

### Step 6: Start Backend (30 seconds)

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

You should see:
```
✅ Using local models (NO API KEYS needed!)
✅ LLM: Ollama - llama3.2:3b
✅ Embeddings: all-MiniLM-L6-v2
✅ Vector DB: ChromaDB (local)
✅ ChromaDB ready: 87 documents loaded
```

### Step 7: Start Frontend (30 seconds)

Open a new terminal:
```bash
cd docs
npm start
```

### Step 8: Test It! 🎉

1. Open http://localhost:3000
2. Click the purple chat button (💬)
3. Ask: "What is this book about?"
4. Wait 5-10 seconds for response (local processing)

## Configuration Options

Edit `rag-backend-free/.env`:

### Change LLM Model

```env
# Faster but smaller context (default)
OLLAMA_MODEL=llama3.2:3b

# Slower but higher quality
OLLAMA_MODEL=llama3.1:8b

# Fastest, smallest (good for testing)
OLLAMA_MODEL=phi3:mini
```

Available models: https://ollama.com/library

### Change Embedding Model

```env
# Default (good balance)
EMBEDDING_MODEL=all-MiniLM-L6-v2

# Larger, more accurate
EMBEDDING_MODEL=all-mpnet-base-v2

# Smaller, faster
EMBEDDING_MODEL=all-MiniLM-L12-v2
```

## How It Works

```
User Question
    ↓
[1] Generate embedding locally (sentence-transformers)
    ↓
[2] Search ChromaDB (local vector database)
    ↓
[3] Retrieve relevant chunks
    ↓
[4] Send to Ollama (local LLM)
    ↓
[5] Generate answer locally
    ↓
Return answer + sources

💰 Cost: $0.00
🔒 Privacy: Everything stays on your machine
```

## Performance

**First Query**: ~10-15 seconds (model loading)
**Subsequent Queries**: ~5-10 seconds
**Embedding Generation**: ~2-5 seconds per batch
**Vector Search**: <100ms

**Tips for faster responses**:
- Use smaller models (phi3:mini)
- Reduce TOP_K_RESULTS to 3
- Use GPU if available (automatic with CUDA)

## Storage Requirements

**Models**:
- llama3.2:3b: ~2GB
- all-MiniLM-L6-v2: ~90MB
- Total: ~2.1GB

**Database**:
- 100 pages book: ~50MB
- 500 pages book: ~250MB

**Total for typical book**: ~2.2GB

## Troubleshooting

### Ollama not starting

```bash
# Check if Ollama is running
ollama list

# Start Ollama service
ollama serve
```

### Model not found

```bash
# List available models
ollama list

# Pull the model
ollama pull llama3.2:3b
```

### Slow responses

**Solution 1**: Use smaller model
```env
OLLAMA_MODEL=phi3:mini
```

**Solution 2**: Reduce retrieval
```env
TOP_K_RESULTS=3
```

**Solution 3**: Use GPU (if available)
- Ollama automatically uses GPU if CUDA/Metal is available
- Check with: `ollama ps`

### Out of memory

**Solution 1**: Use smaller model
```bash
ollama pull phi3:mini
```

**Solution 2**: Close other applications

**Solution 3**: Increase swap space (Linux)

### Import errors

```bash
# Reinstall dependencies
pip uninstall -y torch sentence-transformers
pip install -r requirements.txt
```

## Comparing Models

| Model | Size | Speed | Quality | RAM |
|-------|------|-------|---------|-----|
| phi3:mini | 2GB | Fast | Good | 4GB |
| llama3.2:3b | 2GB | Medium | Very Good | 8GB |
| llama3.1:8b | 4.7GB | Slow | Excellent | 16GB |
| mistral:7b | 4GB | Medium | Excellent | 12GB |

**Recommendation**: Start with `llama3.2:3b` (default)

## Advantages of Free Version

**Cost**:
- ✅ $0.00 forever
- ✅ No monthly fees
- ✅ No pay-per-query
- ✅ Unlimited usage

**Privacy**:
- ✅ All data stays local
- ✅ No data sent to third parties
- ✅ GDPR compliant by design
- ✅ Perfect for sensitive content

**Control**:
- ✅ Choose your own models
- ✅ Customize everything
- ✅ No rate limits
- ✅ Works offline (after setup)

## Disadvantages of Free Version

**Performance**:
- ❌ Slower responses (5-10s vs 2-3s)
- ❌ Requires local resources
- ❌ Initial model download time

**Setup**:
- ❌ More complex setup
- ❌ Requires Ollama installation
- ❌ Larger disk space needed

**Quality**:
- ❌ Slightly lower answer quality
- ❌ Smaller context windows
- ❌ Less sophisticated reasoning

## When to Use Free vs Paid

### Use FREE version if:
- ✅ You want zero ongoing costs
- ✅ Privacy is critical
- ✅ You have decent hardware (8GB+ RAM)
- ✅ You're okay with slower responses
- ✅ You want full control

### Use PAID version if:
- ✅ You need fastest responses
- ✅ You want best quality answers
- ✅ You have limited local resources
- ✅ You're okay with ~$0.30 per 1K queries
- ✅ You want easiest setup

## Upgrading to Paid Version

Already have the free version running? Easy to switch:

1. Set up the paid version (see `rag-backend/`)
2. Run the same ingestion script with your docs
3. Update frontend to point to paid API
4. That's it!

Both versions use the same frontend, so switching is seamless.

## Advanced Configuration

### Use GPU Acceleration

Ollama automatically uses GPU if available:
- **NVIDIA**: Requires CUDA drivers
- **Apple Silicon**: Uses Metal automatically
- **AMD**: Limited support

Check GPU usage:
```bash
ollama ps
```

### Multiple Models

Run different models for different purposes:
```bash
# Fast model for simple queries
OLLAMA_MODEL=phi3:mini

# Powerful model for complex questions
OLLAMA_MODEL=llama3.1:8b
```

### Custom Embedding Models

Use specialized embeddings:
```python
# In app/embeddings.py
EMBEDDING_MODEL="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
```

## Production Deployment

The free version can be deployed to:
- ✅ Your own server
- ✅ VPS with sufficient RAM
- ✅ Local network
- ✅ Docker container

**NOT suitable for**:
- ❌ Serverless (models too large)
- ❌ Low-resource hosting
- ❌ High-traffic public sites

For public deployment with many users, consider the paid version.

## Support & Resources

**Ollama**:
- Website: https://ollama.com
- Models: https://ollama.com/library
- Docs: https://github.com/ollama/ollama

**ChromaDB**:
- Website: https://www.trychroma.com
- Docs: https://docs.trychroma.com

**sentence-transformers**:
- Website: https://www.sbert.net
- Models: https://huggingface.co/sentence-transformers

## Next Steps

1. ✅ Follow this guide to set up
2. ✅ Test with sample queries
3. ✅ Customize models if needed
4. ✅ Enjoy your free AI chatbot!

---

**Cost**: $0.00 forever
**Setup Time**: 10 minutes
**Privacy**: 100% local
**Quality**: Very good
**Status**: Production ready

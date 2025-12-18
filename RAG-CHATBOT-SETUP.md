# RAG Chatbot Integration Guide

Complete guide to setting up and using the embedded RAG (Retrieval-Augmented Generation) chatbot in your Physical AI book.

## Overview

This RAG chatbot allows readers to:
- Ask questions about the book content
- Get AI-powered answers based on the actual text
- Select specific text and ask questions about it
- Access the chatbot from any page in the documentation

## Architecture

```
┌─────────────────┐      ┌──────────────────┐      ┌─────────────────┐
│   Docusaurus    │ ───▶ │  FastAPI Backend │ ───▶ │  Qdrant Cloud   │
│  (React UI)     │ HTTP │   (Python)       │      │  (Vector DB)    │
└─────────────────┘      └──────────────────┘      └─────────────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │   OpenAI API     │
                         │  (Embeddings +   │
                         │   Chat GPT)      │
                         └──────────────────┘
```

**Components**:
1. **Frontend**: React chatbot widget in Docusaurus
2. **Backend**: FastAPI server handling RAG logic
3. **Vector DB**: Qdrant Cloud for semantic search
4. **AI Models**: OpenAI for embeddings and chat

## Prerequisites

Before starting, you'll need:

1. **OpenAI API Key**
   - Sign up at https://platform.openai.com
   - Create an API key
   - Cost: ~$0.30 per 1,000 queries (using gpt-4o-mini)

2. **Qdrant Cloud Account**
   - Sign up at https://cloud.qdrant.io
   - Free tier: 1GB storage (perfect for books)
   - Create a cluster and get credentials

3. **Node.js & Python**
   - Node.js 20+ (for Docusaurus)
   - Python 3.9+ (for backend)

## Installation

### Step 1: Backend Setup

```bash
# Navigate to backend directory
cd rag-backend

# Install Python dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
```

Edit `.env` with your credentials:

```env
OPENAI_API_KEY=sk-your-openai-key-here
QDRANT_URL=https://your-cluster.qdrant.io
QDRANT_API_KEY=your-qdrant-api-key-here
```

### Step 2: Ingest Documents

Process your book content and create embeddings:

```bash
# From rag-backend directory
python ingest_documents.py ../docs/docs
```

This will:
- Load all markdown files
- Split them into chunks
- Create embeddings
- Store in Qdrant Cloud

Expected output:
```
✓ Successfully ingested 87 document chunks!
  Collection: physical_ai_book
  Embedding model: text-embedding-3-small
```

### Step 3: Start Backend Server

```bash
# From rag-backend directory
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Server will be available at `http://localhost:8000`

Test it:
```bash
curl http://localhost:8000/health
```

### Step 4: Start Docusaurus

```bash
# From docs directory
cd docs
npm start
```

Site will open at `http://localhost:3000` with the chatbot enabled!

## Using the Chatbot

### Basic Usage

1. **Open the chatbot**: Click the purple chat button (💬) in the bottom-right corner
2. **Ask a question**: Type your question and press Enter or click send
3. **View answer**: The AI will respond with relevant information and sources

### Text Selection Feature

1. **Select text**: Highlight any text on the page
2. **Ask about it**: The chatbot will show the selected text and prioritize it when answering
3. **Clear selection**: Click the ✕ button in the selected text banner

### Example Queries

- "What is Physical AI?"
- "Explain the ROS 2 architecture"
- "How do I set up a simulation environment?"
- "What are the key concepts in this section?" (with text selected)

## Configuration

### Backend Configuration

Edit `rag-backend/.env`:

```env
# Models
EMBEDDING_MODEL=text-embedding-3-small  # or text-embedding-3-large
CHAT_MODEL=gpt-4o-mini                  # or gpt-4o, gpt-3.5-turbo

# Retrieval
TOP_K_RESULTS=5        # Number of chunks to retrieve
CHUNK_SIZE=1000        # Characters per chunk
CHUNK_OVERLAP=200      # Overlap between chunks

# CORS (add production URLs)
ALLOWED_ORIGINS=http://localhost:3000,https://yourdomain.com
```

### Frontend Configuration

Edit `docs/src/theme/Root.tsx` to change the API URL:

```tsx
<RAGChatbot apiUrl="https://your-api-domain.com" />
```

Or use environment variables:

```bash
# .env.local in docs directory
REACT_APP_API_URL=https://your-api-domain.com
```

## Production Deployment

### Backend Deployment

**Option 1: Railway**
1. Push code to GitHub
2. Connect Railway to your repo
3. Set environment variables
4. Deploy

**Option 2: Render**
1. Create new Web Service
2. Connect GitHub repo
3. Build: `pip install -r requirements.txt`
4. Start: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

**Option 3: Docker**
```bash
cd rag-backend
docker build -t rag-backend .
docker run -p 8000:8000 --env-file .env rag-backend
```

### Frontend Deployment

Deploy Docusaurus normally (Netlify, Vercel, GitHub Pages):

```bash
cd docs
npm run build
```

Update `docs/src/theme/Root.tsx` with production API URL.

### Security Considerations

1. **CORS**: Update `ALLOWED_ORIGINS` to include only your domains
2. **API Keys**: Never commit `.env` files
3. **Rate Limiting**: Consider adding rate limits for production
4. **Authentication**: Add authentication for private books

## Customization

### Chatbot Appearance

Edit `docs/src/components/RAGChatbot/styles.module.css`:

```css
/* Change chatbot colors */
.chatbotToggle {
  background: linear-gradient(135deg, #your-color1, #your-color2);
}

/* Change window size */
.chatbotWindow {
  width: 500px;  /* Adjust width */
  height: 700px; /* Adjust height */
}
```

### Chatbot Behavior

Edit `docs/src/components/RAGChatbot/index.tsx`:

```tsx
// Change initial message
const [messages, setMessages] = useState<Message[]>([
  {
    role: 'assistant',
    content: 'Your custom welcome message here!'
  }
]);

// Change number of results
top_k: 10  // Retrieve more chunks
```

### Backend Prompts

Edit `rag-backend/app/rag_service.py`:

```python
# Customize the system prompt
system_prompt = """Your custom instructions here..."""
```

## Troubleshooting

### Chatbot Not Appearing

**Issue**: Chat button doesn't show up

**Solutions**:
1. Ensure `docs/src/theme/Root.tsx` exists
2. Restart Docusaurus: `npm start`
3. Clear browser cache

### Backend Connection Errors

**Issue**: "Failed to get response from server"

**Solutions**:
1. Verify backend is running: `curl http://localhost:8000/health`
2. Check CORS settings in `.env`
3. Check browser console for errors

### No Search Results

**Issue**: Chatbot says "I cannot find information about that"

**Solutions**:
1. Re-run document ingestion: `python ingest_documents.py ../docs/docs`
2. Verify documents were ingested: Check Qdrant Cloud dashboard
3. Try more specific questions

### Slow Responses

**Issue**: Chatbot takes long to respond

**Solutions**:
1. Switch to faster model: `CHAT_MODEL=gpt-3.5-turbo`
2. Reduce chunks retrieved: `TOP_K_RESULTS=3`
3. Check OpenAI API status

### High Costs

**Issue**: OpenAI bills are high

**Solutions**:
1. Use cheaper models: `gpt-4o-mini` or `gpt-3.5-turbo`
2. Reduce retrieval: Lower `TOP_K_RESULTS`
3. Add caching for common questions
4. Implement rate limiting

## Development Tips

### Testing Backend

```bash
# Test health endpoint
curl http://localhost:8000/health

# Test query endpoint
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What is Physical AI?"}'
```

### Debugging

Enable debug logging:
```bash
uvicorn app.main:app --reload --log-level debug
```

### Hot Reload

Both services support hot reload:
- Backend: `--reload` flag in uvicorn
- Frontend: Automatic in `npm start`

### Re-ingesting After Content Changes

```bash
# Update markdown files
# Then re-ingest
cd rag-backend
python ingest_documents.py ../docs/docs
```

## File Structure

```
physical-ai/
├── rag-backend/              # FastAPI backend
│   ├── app/
│   │   ├── main.py          # API endpoints
│   │   ├── rag_service.py   # RAG logic
│   │   ├── embeddings.py    # OpenAI embeddings
│   │   ├── qdrant_client.py # Vector DB
│   │   └── ...
│   ├── ingest_documents.py  # Document processor
│   ├── requirements.txt     # Python deps
│   └── .env                 # Config (create this)
│
├── docs/                     # Docusaurus site
│   ├── src/
│   │   ├── components/
│   │   │   └── RAGChatbot/  # Chatbot component
│   │   │       ├── index.tsx
│   │   │       └── styles.module.css
│   │   └── theme/
│   │       └── Root.tsx     # Global wrapper
│   └── ...
│
└── RAG-CHATBOT-SETUP.md     # This file
```

## Cost Breakdown

### Development (100 pages, 100 queries)
- Initial ingestion: ~$0.001
- 100 queries: ~$0.03
- **Total: ~$0.03**

### Production (100 pages, 1,000 users, 5 queries each)
- Initial ingestion: ~$0.001
- 5,000 queries: ~$1.50
- **Total: ~$1.50/month**

### Optimization Tips
1. Use `gpt-4o-mini` (10x cheaper than GPT-4)
2. Cache common questions
3. Reduce chunk overlap
4. Use Qdrant free tier (1GB)

## Advanced Features

### Add Authentication

```python
# app/main.py
from fastapi import Header, HTTPException

async def verify_token(authorization: str = Header(...)):
    if authorization != f"Bearer {settings.api_token}":
        raise HTTPException(status_code=401)

@app.post("/query")
async def query_chatbot(request: QueryRequest, token: str = Depends(verify_token)):
    # ... existing code
```

### Add Caching

```python
# app/rag_service.py
from functools import lru_cache

@lru_cache(maxsize=100)
def query_cached(question: str) -> Dict[str, Any]:
    # ... RAG logic
```

### Add Analytics

```python
# Track query statistics
import logging

logging.info(f"Query: {question}, Response time: {elapsed}, Chunks: {len(chunks)}")
```

## Support

For issues or questions:
1. Check this guide's troubleshooting section
2. Review backend logs: `uvicorn` output
3. Check browser console: DevTools → Console
4. Verify Qdrant Cloud status
5. Check OpenAI API status

## Next Steps

1. ✅ Complete setup steps above
2. 📝 Customize chatbot appearance
3. 🧪 Test with sample queries
4. 🚀 Deploy to production
5. 📊 Monitor usage and costs
6. 🔧 Optimize based on user feedback

## Resources

- **FastAPI**: https://fastapi.tiangolo.com
- **Qdrant**: https://qdrant.tech/documentation
- **OpenAI API**: https://platform.openai.com/docs
- **Docusaurus**: https://docusaurus.io
- **RAG Concepts**: https://python.langchain.com/docs/use_cases/question_answering/

---

**Created**: December 2024
**Version**: 1.0.0
**Status**: Production Ready

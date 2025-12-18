# RAG Chatbot Quick Start

Get your chatbot running in 5 minutes!

## Prerequisites

- Python 3.9+
- Node.js 20+
- OpenAI API key ([Get one here](https://platform.openai.com))
- Qdrant Cloud account ([Sign up here](https://cloud.qdrant.io) - free tier)

## 🚀 Quick Setup

### 1. Backend Setup (2 minutes)

```bash
# Navigate to backend
cd rag-backend

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
```

**Edit `.env` with your keys:**
```env
OPENAI_API_KEY=sk-your-key-here
QDRANT_URL=https://your-cluster.qdrant.io
QDRANT_API_KEY=your-qdrant-key
```

### 2. Ingest Documents (1 minute)

```bash
python ingest_documents.py ../docs/docs
```

Wait for: `✓ Successfully ingested N document chunks!`

### 3. Start Backend (30 seconds)

**Option A: Windows**
```bash
start.bat
```

**Option B: Mac/Linux**
```bash
chmod +x start.sh
./start.sh
```

**Option C: Manual**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Server running at: http://localhost:8000

### 4. Start Frontend (30 seconds)

```bash
# New terminal
cd docs
npm install  # First time only
npm start
```

Site opens at: http://localhost:3000

### 5. Test It! (1 minute)

1. Click the purple chat button (💬) in bottom-right
2. Ask: "What is this book about?"
3. Select any text on the page
4. Ask: "Explain this in simple terms"

## ✅ Success Checklist

- [ ] Backend responds at http://localhost:8000/health
- [ ] Frontend opens at http://localhost:3000
- [ ] Chat button appears in bottom-right
- [ ] Chatbot opens and shows welcome message
- [ ] Test query returns an answer

## ❌ Troubleshooting

### Backend won't start

```bash
# Check Python version
python --version  # Should be 3.9+

# Verify .env file exists
cat .env  # or: type .env (Windows)

# Test API keys
curl http://localhost:8000/health
```

### No documents ingested

```bash
# Check if docs directory exists
ls ../docs/docs  # or: dir ..\docs\docs (Windows)

# Re-run ingestion
python ingest_documents.py ../docs/docs
```

### Chat button not appearing

```bash
# Verify Root.tsx exists
ls docs/src/theme/Root.tsx

# Restart Docusaurus
cd docs
npm start
```

### Connection errors

1. Verify backend is running: http://localhost:8000/health
2. Check browser console (F12) for errors
3. Verify CORS settings in `.env`:
   ```env
   ALLOWED_ORIGINS=http://localhost:3000
   ```

## 🎯 Next Steps

1. ✅ Chatbot working? Great!
2. 📖 Read [RAG-CHATBOT-SETUP.md](RAG-CHATBOT-SETUP.md) for full docs
3. 🎨 Customize appearance in `docs/src/components/RAGChatbot/styles.module.css`
4. 🚀 Deploy (see [deployment guide](RAG-CHATBOT-SETUP.md#production-deployment))

## 💰 Cost Estimate

For testing (100 queries):
- Ingestion: $0.001
- Queries: $0.03
- **Total: ~$0.03**

## 🆘 Need Help?

1. Check [RAG-CHATBOT-SETUP.md](RAG-CHATBOT-SETUP.md) troubleshooting section
2. Verify OpenAI API status: https://status.openai.com
3. Check Qdrant Cloud dashboard
4. Review backend logs in terminal

## 📋 Commands Reference

```bash
# Backend
cd rag-backend
python ingest_documents.py ../docs/docs  # Ingest docs
uvicorn app.main:app --reload            # Start server

# Frontend
cd docs
npm start                                 # Start Docusaurus
npm run build                            # Build for production

# Testing
curl http://localhost:8000/health        # Health check
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"question": "test"}'              # Test query
```

---

**Time to complete**: 5 minutes
**Difficulty**: Easy
**Status**: Ready to use

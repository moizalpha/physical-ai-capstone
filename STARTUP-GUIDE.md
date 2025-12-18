# Complete Startup Guide - See Your Chatbot Now!

## Choose Your Version and Start

### 🆓 Option 1: FREE Version (Recommended - No API Keys!)

#### Step 1: Install Ollama (First Time Only)

**Windows**:
1. Download: https://ollama.com/download
2. Install and run
3. Verify in CMD: `ollama --version`

**Mac/Linux**:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

#### Step 2: Download AI Model (First Time Only)
```bash
ollama pull llama3.2:3b
```
*This downloads 2GB - only needed once!*

#### Step 3: Setup Backend (First Time Only)
```bash
cd rag-backend-free
pip install -r requirements.txt
cp .env.example .env
```

#### Step 4: Load Your Documents (First Time Only)
```bash
python ingest_documents.py ../docs/docs
```
*Wait 5-10 minutes while it processes your documents*

#### Step 5: Start Backend (Every Time)
```bash
cd rag-backend-free
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Keep this terminal open!** You should see:
```
✅ Using local models (NO API KEYS needed!)
✅ LLM: Ollama - llama3.2:3b
✅ Embeddings: all-MiniLM-L6-v2
✅ Vector DB: ChromaDB (local)
✅ ChromaDB ready: 87 documents loaded
INFO:     Uvicorn running on http://0.0.0.0:8000
```

#### Step 6: Start Frontend (Every Time)

**Open a NEW terminal**:
```bash
cd docs
npm start
```

Browser opens automatically to: **http://localhost:3000**

🎉 **Look for the purple chat button (💬) in the bottom-right corner!**

---

### 💳 Option 2: PAID Version (Faster Responses)

#### Step 1: Get API Keys (First Time Only)

1. **OpenAI**: https://platform.openai.com
   - Create account
   - Add payment method
   - Create API key

2. **Qdrant Cloud**: https://cloud.qdrant.io
   - Sign up (free tier)
   - Create cluster
   - Copy API key and URL

#### Step 2: Setup Backend (First Time Only)
```bash
cd rag-backend
pip install -r requirements.txt
cp .env.example .env
```

**Edit `.env` file** and add your keys:
```env
OPENAI_API_KEY=sk-your-key-here
QDRANT_URL=https://your-cluster.qdrant.io
QDRANT_API_KEY=your-qdrant-key-here
```

#### Step 3: Load Your Documents (First Time Only)
```bash
python ingest_documents.py ../docs/docs
```
*Faster than free version - takes 2-3 minutes*

#### Step 4: Start Backend (Every Time)
```bash
cd rag-backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Keep this terminal open!** You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

#### Step 5: Start Frontend (Every Time)

**Open a NEW terminal**:
```bash
cd docs
npm start
```

Browser opens automatically to: **http://localhost:3000**

🎉 **Look for the purple chat button (💬) in the bottom-right corner!**

---

## What You'll See

### 1. Documentation Page Loads
Your Physical AI book appears normally.

### 2. Chat Button Appears
Look at the **bottom-right corner** - you'll see a **purple circular button with 💬**

### 3. Click the Button
The chat window opens with:
- Header: "📚 Ask About the Book"
- Welcome message from the bot
- Input field at the bottom

### 4. Try These Questions

**Simple Test**:
```
What is this book about?
```

**Text Selection Test**:
1. Highlight any text on the page
2. Blue banner appears in chat showing selected text
3. Ask: "Explain this in simple terms"

**Follow-up Test**:
```
Tell me more about that
```

---

## Response Times

### FREE Version
- First query: **10-15 seconds** (model loading)
- Subsequent queries: **5-10 seconds**
- Quality: Very good

### PAID Version
- All queries: **2-3 seconds**
- Quality: Excellent

---

## Visual Guide

```
┌─────────────────────────────────────────────────┐
│  # Physical AI Book                             │
│                                                 │
│  ## Introduction                                │
│                                                 │
│  This book covers Physical AI concepts...       │
│                                                 │
│                                                 │
│                                    ┌──────────┐│
│                                    │📚 Ask    ││
│                                    │About Book││
│                                    │       ✕  ││
│                                    ├──────────┤│
│                                    │          ││
│                                    │ Bot: Hi! ││
│                                    │ I can    ││
│                                    │ answer   ││
│                                    │ questions││
│                                    │          ││
│                                    ├──────────┤│
│                                    │Type... ➤ ││
│                                    └──────────┘│
│                                           ╔════╗
│                                           ║ 💬 ║
│                                           ╚════╝
└─────────────────────────────────────────────────┘
```

---

## Troubleshooting

### Backend Not Starting?

**FREE Version**:
```bash
# Check Ollama is running
ollama list

# If empty, pull model
ollama pull llama3.2:3b

# Check if port 8000 is available
# Windows: netstat -ano | findstr :8000
# Mac/Linux: lsof -i :8000
```

**PAID Version**:
```bash
# Verify .env exists
cat .env  # or: type .env (Windows)

# Check API keys are valid
curl http://localhost:8000/health
```

### Chat Button Not Appearing?

```bash
# Verify Root.tsx exists
ls docs/src/theme/Root.tsx

# Clear cache and restart
cd docs
npm run clear
npm start
```

### Connection Errors?

**Check CORS in backend `.env`**:
```env
ALLOWED_ORIGINS=http://localhost:3000
```

Then restart backend.

### "Model not found" (FREE version)?

```bash
# List available models
ollama list

# Pull the model
ollama pull llama3.2:3b

# Restart backend
```

---

## Quick Commands Reference

### First Time Setup - FREE
```bash
# 1. Install Ollama (download from ollama.com)
# 2. Pull model
ollama pull llama3.2:3b

# 3. Setup
cd rag-backend-free
pip install -r requirements.txt
cp .env.example .env
python ingest_documents.py ../docs/docs
```

### First Time Setup - PAID
```bash
cd rag-backend
pip install -r requirements.txt
cp .env.example .env
# Edit .env with API keys
python ingest_documents.py ../docs/docs
```

### Every Time You Want to Use It

**Terminal 1 - Backend**:
```bash
# FREE version
cd rag-backend-free
uvicorn app.main:app --reload

# PAID version
cd rag-backend
uvicorn app.main:app --reload
```

**Terminal 2 - Frontend**:
```bash
cd docs
npm start
```

---

## Testing Checklist

After running `npm start`, verify:

- [ ] Browser opens to http://localhost:3000
- [ ] Documentation page loads
- [ ] Purple chat button visible bottom-right
- [ ] Clicking button opens chat window
- [ ] Welcome message appears
- [ ] Can type in input field
- [ ] Pressing Enter sends message
- [ ] Loading indicator appears (●●● or "...")
- [ ] Answer appears with sources
- [ ] Can select text on page
- [ ] Selected text shows in chat (blue banner)
- [ ] Can ask about selected text
- [ ] Dark mode toggle works
- [ ] Mobile view works (resize browser)

---

## What to Expect

### FREE Version
✅ Takes 10-15 seconds first query (loading models)
✅ 5-10 seconds for subsequent queries
✅ Very good answer quality
✅ Shows source citations
✅ Completely private and free

### PAID Version
✅ Takes 2-3 seconds all queries
✅ Excellent answer quality
✅ Shows source citations
✅ Costs ~$0.0003 per query

---

## Stop Everything

When done:

1. **Stop Frontend**: Press `Ctrl+C` in the frontend terminal
2. **Stop Backend**: Press `Ctrl+C` in the backend terminal

That's it! Everything is local, nothing to clean up.

---

## Next Time

Just run these two commands:

**Terminal 1**:
```bash
cd rag-backend-free  # or rag-backend for paid
uvicorn app.main:app --reload
```

**Terminal 2**:
```bash
cd docs
npm start
```

No reinstalling, no re-ingestion needed!

---

## Need More Help?

- **FREE Version**: Read `FREE-RAG-SETUP.md`
- **PAID Version**: Read `QUICKSTART.md`
- **Visual Guide**: Read `CHATBOT-VISUAL-GUIDE.md`
- **Comparison**: Read `FREE-VS-PAID-COMPARISON.md`

---

**Ready? Pick your version above and start!** 🚀

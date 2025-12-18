# RAG Chatbot for Physical AI Book

## Choose Your Version

### 🆓 FREE Version (100% Free, Local, Private)
**Perfect if you want**: Zero cost, complete privacy, full control

👉 **[Start Here: FREE Version](START-HERE-FREE.md)**

### 💳 PAID Version (Fast, Easy, Cloud-based)
**Perfect if you want**: Fastest responses, easiest setup, best quality

👉 **[Start Here: PAID Version](QUICKSTART.md)**

---

## Quick Comparison

| Aspect | FREE | PAID |
|--------|------|------|
| **Cost** | $0 forever | ~$0.30/1K queries |
| **Speed** | 5-10 seconds | 2-3 seconds |
| **Setup Time** | 10 minutes | 5 minutes |
| **API Keys** | None needed | 2 required |
| **Privacy** | 100% local | Cloud-based |
| **Quality** | Very Good | Excellent |
| **Hardware** | 8GB+ RAM | Minimal |

📊 **[Detailed Comparison](FREE-VS-PAID-COMPARISON.md)**

---

## Documentation

### Getting Started
- 🆓 **[START-HERE-FREE.md](START-HERE-FREE.md)** - Quick start for FREE version
- 💳 **[QUICKSTART.md](QUICKSTART.md)** - Quick start for PAID version

### Setup Guides
- 🆓 **[FREE-RAG-SETUP.md](FREE-RAG-SETUP.md)** - Complete FREE setup guide
- 💳 **[RAG-CHATBOT-SETUP.md](RAG-CHATBOT-SETUP.md)** - Complete PAID setup guide

### Reference
- 📊 **[FREE-VS-PAID-COMPARISON.md](FREE-VS-PAID-COMPARISON.md)** - Detailed comparison
- 📝 **[FREE-CHATBOT-SUMMARY.md](FREE-CHATBOT-SUMMARY.md)** - FREE version summary
- 📝 **[RAG-CHATBOT-SUMMARY.md](RAG-CHATBOT-SUMMARY.md)** - PAID version summary
- 🏗️ **[rag-backend/ARCHITECTURE.md](rag-backend/ARCHITECTURE.md)** - System architecture
- ✨ **[rag-backend/FEATURES.md](rag-backend/FEATURES.md)** - Feature documentation

---

## What You Get

Both versions include:
- ✅ AI-powered question answering
- ✅ Text selection support (highlight text, ask about it)
- ✅ Source citations with relevance scores
- ✅ Beautiful embedded chat widget
- ✅ Mobile-responsive design
- ✅ Dark mode support
- ✅ Same React frontend

---

## File Structure

```
physical-ai/
├── rag-backend/              # PAID version (OpenAI + Qdrant)
│   ├── app/                  # FastAPI application
│   ├── requirements.txt      # Dependencies
│   └── README.md            # Backend docs
│
├── rag-backend-free/         # FREE version (Ollama + ChromaDB)
│   ├── app/                  # FastAPI application
│   ├── requirements.txt      # Dependencies
│   ├── setup_ollama.sh/.bat # Ollama setup
│   └── README.md            # Backend docs
│
├── docs/                     # Docusaurus site (shared)
│   └── src/
│       ├── components/RAGChatbot/  # Chatbot widget
│       └── theme/Root.tsx          # Integration
│
└── Documentation/            # All guides
    ├── START-HERE-FREE.md
    ├── FREE-RAG-SETUP.md
    ├── QUICKSTART.md
    ├── RAG-CHATBOT-SETUP.md
    └── ...
```

---

## Technology Stack

### FREE Version
- **LLM**: Ollama (llama3.2:3b)
- **Embeddings**: sentence-transformers
- **Vector DB**: ChromaDB (local)
- **Cost**: $0.00

### PAID Version
- **LLM**: OpenAI GPT-4o-mini
- **Embeddings**: OpenAI text-embedding-3-small
- **Vector DB**: Qdrant Cloud
- **Cost**: ~$0.30 per 1,000 queries

### Both Use
- **Backend**: FastAPI
- **Frontend**: React + TypeScript
- **UI**: Docusaurus

---

## Quick Decision Guide

### Choose FREE if:
- ✅ Budget is $0
- ✅ Privacy is critical
- ✅ You have 8GB+ RAM
- ✅ 5-10 second responses are okay
- ✅ You want full control

### Choose PAID if:
- ✅ You need 2-3 second responses
- ✅ You want easiest setup
- ✅ Limited local hardware
- ✅ ~$0.30/1K queries is acceptable
- ✅ You want best quality

### Can't Decide?
**Start with FREE** - it's zero risk! You can always switch to PAID later (takes 10 minutes).

---

## Support

### FREE Version
- **Ollama**: https://ollama.com
- **ChromaDB**: https://www.trychroma.com
- **Models**: https://ollama.com/library

### PAID Version
- **OpenAI**: https://platform.openai.com/docs
- **Qdrant**: https://qdrant.tech/documentation

### General
- **FastAPI**: https://fastapi.tiangolo.com
- **Docusaurus**: https://docusaurus.io

---

## Next Steps

1. **Choose your version** (FREE or PAID)
2. **Read the quick start guide**:
   - FREE: [START-HERE-FREE.md](START-HERE-FREE.md)
   - PAID: [QUICKSTART.md](QUICKSTART.md)
3. **Follow the setup instructions**
4. **Test your chatbot**
5. **Customize as needed**

---

## Status

✅ **Both versions are production-ready**
✅ **Full documentation included**
✅ **Same frontend for both**
✅ **Easy to switch between versions**
✅ **Well-tested architecture**

---

## License

MIT License - See project root for details

---

**Questions?** Check the detailed documentation for your chosen version!

**Want to compare?** Read [FREE-VS-PAID-COMPARISON.md](FREE-VS-PAID-COMPARISON.md)

**Ready to start?**
- 🆓 FREE: [START-HERE-FREE.md](START-HERE-FREE.md)
- 💳 PAID: [QUICKSTART.md](QUICKSTART.md)

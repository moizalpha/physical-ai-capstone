# RAG Chatbot Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                         User Interface                          │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │          Docusaurus Book (React Frontend)                │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │        RAGChatbot Component (TypeScript)           │  │  │
│  │  │  • Chat interface                                  │  │  │
│  │  │  • Text selection handler                          │  │  │
│  │  │  • Message display                                 │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │ HTTP
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      FastAPI Backend (Python)                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                    API Endpoints                         │  │
│  │  • POST /query    • GET /health    • GET /              │  │
│  └──────────────────────────────────────────────────────────┘  │
│                              │                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                    RAG Service                           │  │
│  │  • Query orchestration                                   │  │
│  │  • Context building                                      │  │
│  │  • Answer generation                                     │  │
│  └──────────────────────────────────────────────────────────┘  │
│         │                    │                    │             │
│         ▼                    ▼                    ▼             │
│  ┌─────────────┐   ┌─────────────────┐   ┌───────────────┐    │
│  │  Embedding  │   │ Document        │   │  Qdrant       │    │
│  │  Service    │   │ Processor       │   │  Manager      │    │
│  │             │   │                 │   │               │    │
│  │ • Generate  │   │ • Load files    │   │ • Search      │    │
│  │   vectors   │   │ • Chunk text    │   │ • Upsert      │    │
│  │ • Batch API │   │ • Parse MD      │   │ • Manage DB   │    │
│  └─────────────┘   └─────────────────┘   └───────────────┘    │
└─────────────────────────────────────────────────────────────────┘
         │                                          │
         ▼                                          ▼
┌──────────────────────┐              ┌──────────────────────────┐
│    OpenAI API        │              │    Qdrant Cloud          │
│                      │              │                          │
│ • Embeddings API     │              │ • Vector storage         │
│   (text-embedding-   │              │ • Cosine similarity      │
│    3-small)          │              │ • Fast retrieval         │
│                      │              │ • Free tier (1GB)        │
│ • Chat API           │              │                          │
│   (gpt-4o-mini)      │              │                          │
└──────────────────────┘              └──────────────────────────┘
```

## Data Flow

### Document Ingestion Flow

```
1. Load Documents
   ├─> Scan markdown files
   ├─> Parse frontmatter
   ├─> Extract metadata
   └─> Convert to plain text

2. Chunk Documents
   ├─> Split into chunks (1000 chars)
   ├─> Add overlap (200 chars)
   └─> Preserve context

3. Generate Embeddings
   ├─> Batch texts (100 at a time)
   ├─> Call OpenAI embeddings API
   └─> Get 1536-dim vectors

4. Store in Qdrant
   ├─> Create collection
   ├─> Upsert points with payload
   └─> Index for search
```

### Query Flow

```
1. User Input
   ├─> Question text
   └─> Optional selected text

2. Generate Query Embedding
   └─> OpenAI embeddings API

3. Vector Search
   ├─> Query Qdrant with vector
   ├─> Get top-k similar chunks
   └─> Retrieve with scores

4. Build Context
   ├─> Combine retrieved chunks
   ├─> Add selected text (if any)
   └─> Format for prompt

5. Generate Answer
   ├─> Send to OpenAI chat API
   ├─> Include system prompt
   ├─> Include context + question
   └─> Get response

6. Return Result
   ├─> Answer text
   ├─> Source citations
   └─> Metadata
```

## Component Details

### Backend Components

**main.py** (API Layer)
- FastAPI application
- CORS middleware
- Endpoint definitions
- Request/response models

**rag_service.py** (Business Logic)
- Query orchestration
- Context building
- Prompt engineering
- Answer generation

**embeddings.py** (OpenAI Integration)
- Embedding generation
- Batch processing
- Error handling

**qdrant_client.py** (Vector DB)
- Collection management
- Vector storage
- Similarity search
- Metadata filtering

**document_processor.py** (Data Processing)
- Markdown parsing
- Text chunking
- Metadata extraction
- Content cleaning

**config.py** (Configuration)
- Environment variables
- Settings validation
- Default values

### Frontend Components

**index.tsx** (Chatbot Logic)
- Message state management
- API communication
- Text selection handling
- User interactions

**styles.module.css** (Styling)
- Responsive layout
- Animations
- Dark mode
- Mobile support

**Root.tsx** (Integration)
- Global wrapper
- Docusaurus theme
- Environment config

## Technology Choices

### Why FastAPI?
- Fast async performance
- Automatic API docs
- Type validation
- Easy deployment

### Why Qdrant?
- Purpose-built for vectors
- Free tier available
- Fast cosine similarity
- Cloud-managed

### Why OpenAI?
- Best-in-class embeddings
- Reliable chat models
- Cost-effective mini models
- Simple API

### Why React/TypeScript?
- Docusaurus native
- Type safety
- Rich ecosystem
- Easy integration

## Scaling Considerations

### Current Capacity
- 1GB documents (Qdrant free)
- 100+ concurrent users
- 1000s queries/day
- <3s response time

### Horizontal Scaling
```
Load Balancer
    │
    ├─> FastAPI Instance 1
    ├─> FastAPI Instance 2
    └─> FastAPI Instance N
            │
            └─> Qdrant Cluster
```

### Vertical Scaling
- Upgrade Qdrant tier
- Use faster models
- Increase batch sizes
- Add caching layer

## Security Architecture

### API Security
- CORS restrictions
- Environment secrets
- Input validation
- Rate limiting (ready)

### Data Security
- No user data stored
- Ephemeral queries
- Encrypted transport (HTTPS)
- API key rotation

## Monitoring & Observability

### Health Checks
- `/health` endpoint
- Dependency status
- Model availability

### Logging
- Request/response logs
- Error tracking
- Performance metrics

### Metrics (Future)
- Query latency
- Token usage
- Cache hit rate
- Error rate

## Deployment Architecture

### Development
```
localhost:3000 (Docusaurus) → localhost:8000 (FastAPI)
                                     │
                                     ├─> OpenAI API
                                     └─> Qdrant Cloud
```

### Production
```
yourdomain.com (Static CDN) → api.yourdomain.com (FastAPI)
                                     │
                                     ├─> OpenAI API
                                     └─> Qdrant Cloud
```

## Cost Architecture

### Per 1,000 Queries
- Embeddings: $0.00002 × 1,000 = $0.02
- Chat: $0.0003 × 1,000 = $0.30
- Vector DB: $0.00 (free tier)
- **Total: ~$0.32**

### Optimization Strategies
- Cache common queries
- Use smaller models
- Reduce chunk overlap
- Implement rate limits

---

**Design Principles**:
- Simple and maintainable
- Cost-effective
- Scalable from day one
- Production-ready defaults

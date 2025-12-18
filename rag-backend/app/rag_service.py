"""RAG (Retrieval-Augmented Generation) service for answering questions."""
from openai import OpenAI
from typing import List, Dict, Any, Optional
from .embeddings import embedding_service
from .qdrant_client import qdrant_manager
from .config import settings


class RAGService:
    """Service for retrieving context and generating answers."""

    def __init__(self):
        """Initialize RAG service."""
        self.client = OpenAI(api_key=settings.openai_api_key)
        self.chat_model = settings.chat_model

    def query(
        self,
        question: str,
        selected_text: Optional[str] = None,
        top_k: int = None
    ) -> Dict[str, Any]:
        """
        Answer a question using RAG.

        Args:
            question: User's question
            selected_text: Optional text selected by user for context
            top_k: Number of chunks to retrieve

        Returns:
            Dictionary with answer and sources
        """
        top_k = top_k or settings.top_k_results

        # Generate embedding for the question
        question_embedding = embedding_service.create_embedding(question)

        # Search for relevant documents
        search_results = qdrant_manager.search(
            query_vector=question_embedding,
            limit=top_k
        )

        # Build context from retrieved documents
        context_chunks = []
        sources = []

        for result in search_results:
            payload = result["payload"]
            context_chunks.append(payload["text"])
            sources.append({
                "title": payload.get("title", "Unknown"),
                "file_path": payload.get("file_path", ""),
                "chunk_id": payload.get("chunk_id", 0),
                "score": result["score"]
            })

        # If user selected text, prioritize it
        if selected_text:
            context = f"User-selected text:\n{selected_text}\n\n"
            context += "Additional context from the book:\n"
            context += "\n\n".join(context_chunks)
        else:
            context = "\n\n".join(context_chunks)

        # Generate answer using OpenAI
        answer = self._generate_answer(question, context, selected_text)

        return {
            "answer": answer,
            "sources": sources,
            "context_used": len(context_chunks),
            "has_selected_text": selected_text is not None
        }

    def _generate_answer(
        self,
        question: str,
        context: str,
        selected_text: Optional[str] = None
    ) -> str:
        """
        Generate an answer using OpenAI chat completion.

        Args:
            question: User's question
            context: Retrieved context
            selected_text: Optional selected text

        Returns:
            Generated answer
        """
        system_prompt = """You are a helpful AI assistant answering questions about a Physical AI book.
Use the provided context to answer the user's question accurately and concisely.
If the answer cannot be found in the context, say so clearly.
Always cite specific information from the context when possible."""

        if selected_text:
            system_prompt += """

IMPORTANT: The user has selected specific text from the book.
Pay special attention to this selected text when answering their question.
If their question is about the selected text, answer based primarily on that text."""

        user_prompt = f"""Context from the book:
{context}

Question: {question}

Please provide a clear, accurate answer based on the context above."""

        try:
            response = self.client.chat.completions.create(
                model=self.chat_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"Error generating answer: {str(e)}"


# Singleton instance
rag_service = RAGService()

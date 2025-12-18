"""Document processing and chunking utilities."""
import os
import re
from typing import List, Dict, Any
from pathlib import Path
import markdown
from bs4 import BeautifulSoup
from .config import settings


class DocumentProcessor:
    """Processes and chunks documents for embedding."""

    def __init__(self, chunk_size: int = None, chunk_overlap: int = None):
        """
        Initialize document processor.

        Args:
            chunk_size: Maximum size of text chunks
            chunk_overlap: Overlap between consecutive chunks
        """
        self.chunk_size = chunk_size or settings.chunk_size
        self.chunk_overlap = chunk_overlap or settings.chunk_overlap

    def load_markdown_files(self, docs_dir: str) -> List[Dict[str, Any]]:
        """
        Load all markdown files from a directory.

        Args:
            docs_dir: Path to directory containing markdown files

        Returns:
            List of document dictionaries
        """
        documents = []
        docs_path = Path(docs_dir)

        for md_file in docs_path.rglob("*.md"):
            # Skip node_modules and build directories
            if "node_modules" in str(md_file) or "build" in str(md_file):
                continue

            try:
                with open(md_file, "r", encoding="utf-8") as f:
                    content = f.read()

                # Extract title from first heading or filename
                title = self._extract_title(content) or md_file.stem

                # Convert markdown to plain text
                text = self._markdown_to_text(content)

                # Get relative path for reference
                rel_path = md_file.relative_to(docs_path.parent)

                documents.append({
                    "title": title,
                    "content": text,
                    "file_path": str(rel_path),
                    "source": md_file.name
                })
            except Exception as e:
                print(f"Error loading {md_file}: {e}")

        return documents

    def chunk_documents(self, documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Split documents into smaller chunks.

        Args:
            documents: List of document dictionaries

        Returns:
            List of chunked document dictionaries
        """
        chunked_docs = []

        for doc in documents:
            content = doc["content"]
            chunks = self._split_text(content)

            for i, chunk in enumerate(chunks):
                chunked_doc = {
                    "text": chunk,
                    "chunk_id": i,
                    "total_chunks": len(chunks),
                    "title": doc["title"],
                    "file_path": doc["file_path"],
                    "source": doc["source"]
                }
                chunked_docs.append(chunked_doc)

        return chunked_docs

    def _split_text(self, text: str) -> List[str]:
        """
        Split text into chunks with overlap.

        Args:
            text: Text to split

        Returns:
            List of text chunks
        """
        if len(text) <= self.chunk_size:
            return [text]

        chunks = []
        start = 0

        while start < len(text):
            end = start + self.chunk_size

            # Try to break at sentence boundary
            if end < len(text):
                # Look for sentence ending
                sentence_end = text.rfind(". ", start, end)
                if sentence_end != -1:
                    end = sentence_end + 1
                else:
                    # Look for paragraph break
                    para_break = text.rfind("\n\n", start, end)
                    if para_break != -1:
                        end = para_break + 2

            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)

            start = end - self.chunk_overlap

        return chunks

    def _markdown_to_text(self, md_content: str) -> str:
        """
        Convert markdown to plain text.

        Args:
            md_content: Markdown content

        Returns:
            Plain text
        """
        # Convert markdown to HTML
        html = markdown.markdown(md_content)

        # Parse HTML and extract text
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()

        # Clean up whitespace
        text = re.sub(r'\n\s*\n', '\n\n', text)
        text = text.strip()

        return text

    def _extract_title(self, md_content: str) -> str:
        """
        Extract title from markdown content.

        Args:
            md_content: Markdown content

        Returns:
            Title string or None
        """
        # Look for frontmatter title
        frontmatter_match = re.search(r'^---\s*\ntitle:\s*["\']?([^"\'\n]+)["\']?\s*\n', md_content, re.MULTILINE)
        if frontmatter_match:
            return frontmatter_match.group(1)

        # Look for first H1 heading
        h1_match = re.search(r'^#\s+(.+)$', md_content, re.MULTILINE)
        if h1_match:
            return h1_match.group(1)

        return None


# Singleton instance
document_processor = DocumentProcessor()

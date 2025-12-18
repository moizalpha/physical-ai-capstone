#!/bin/bash

echo "========================================="
echo "Ollama Setup Script"
echo "========================================="
echo ""

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo "❌ Ollama is not installed!"
    echo ""
    echo "Please install Ollama first:"
    echo "  macOS/Linux: curl -fsSL https://ollama.com/install.sh | sh"
    echo "  Windows: Download from https://ollama.com/download"
    echo ""
    exit 1
fi

echo "✅ Ollama is installed"
echo ""

# Check if Ollama is running
if ! curl -s http://localhost:11434/api/tags &> /dev/null; then
    echo "⚠️  Ollama is not running. Starting Ollama..."
    ollama serve &
    sleep 3
fi

echo "✅ Ollama is running"
echo ""

# Pull the recommended model
echo "Downloading recommended model: llama3.2:3b"
echo "(This is a 2GB download and may take a few minutes)"
echo ""

ollama pull llama3.2:3b

echo ""
echo "========================================="
echo "✅ Setup Complete!"
echo "========================================="
echo ""
echo "Available models:"
ollama list
echo ""
echo "You can now run: python ingest_documents.py ../docs/docs"

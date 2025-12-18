@echo off

REM Startup script for RAG backend (Windows)

echo 🚀 Starting RAG Chatbot Backend
echo ================================

REM Check if .env exists
if not exist .env (
    echo ❌ Error: .env file not found
    echo Please create .env from .env.example and add your credentials
    exit /b 1
)

REM Check if venv exists
if not exist venv (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📥 Installing dependencies...
pip install -r requirements.txt

REM Start server
echo ✅ Starting FastAPI server...
echo Server will be available at http://localhost:8000
echo Press Ctrl+C to stop
echo.

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

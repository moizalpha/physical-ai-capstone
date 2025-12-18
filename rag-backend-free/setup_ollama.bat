@echo off

echo =========================================
echo Ollama Setup Script (Windows)
echo =========================================
echo.

REM Check if Ollama is installed
where ollama >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Ollama is not installed!
    echo.
    echo Please download and install Ollama first:
    echo   https://ollama.com/download
    echo.
    pause
    exit /b 1
)

echo ✅ Ollama is installed
echo.

REM Pull the recommended model
echo Downloading recommended model: llama3.2:3b
echo (This is a 2GB download and may take a few minutes)
echo.

ollama pull llama3.2:3b

echo.
echo =========================================
echo ✅ Setup Complete!
echo =========================================
echo.
echo Available models:
ollama list
echo.
echo You can now run: python ingest_documents.py ..\docs\docs
pause

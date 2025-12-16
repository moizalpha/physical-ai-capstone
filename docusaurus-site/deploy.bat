@echo off
echo ========================================
echo Deploying Physical AI Capstone to GitHub
echo ========================================
echo.

cd /d "%~dp0"

echo Step 1: Checking git status...
git status >nul 2>&1
if errorlevel 1 (
    echo Initializing git repository...
    git init
    git add .
    git commit -m "Initial commit: Physical AI Capstone Docusaurus site"
    git branch -M main
    git remote add origin https://github.com/moizalpha/physical-ai-capstone.git
) else (
    echo Git repository already exists
)

echo.
echo Step 2: Committing latest changes...
git add .
git commit -m "Update: %date% %time%"

echo.
echo Step 3: Pushing to GitHub main branch...
git push -u origin main

if errorlevel 1 (
    echo.
    echo ERROR: Failed to push to GitHub.
    echo Please check:
    echo 1. Repository exists at: https://github.com/moizalpha/physical-ai-capstone
    echo 2. You are logged into GitHub
    echo 3. You have push permissions
    echo.
    pause
    exit /b 1
)

echo.
echo Step 4: Building and deploying to GitHub Pages...
set GIT_USER=moizalpha
set USE_SSH=false
call npm run deploy

if errorlevel 1 (
    echo.
    echo ERROR: Deployment failed. Check the output above for errors.
    pause
    exit /b 1
)

echo.
echo ========================================
echo SUCCESS! Site deployed to:
echo https://moizalpha.github.io/physical-ai-capstone/
echo ========================================
echo.
echo It may take 2-5 minutes to appear online.
echo.
pause

@echo off
echo ================================
echo Anuj Nandal's Fake News Detector
echo Deployment Script
echo ================================
echo.

echo Checking if git is initialized...
if not exist .git (
    echo Initializing git repository...
    git init
    git add .
    git commit -m "Initial commit - Anuj Nandal's Fake News Detector"
) else (
    echo Git repository found. Adding changes...
    git add .
    git commit -m "Updated project for deployment"
)

echo.
echo Choose deployment platform:
echo 1. Heroku
echo 2. Render
echo 3. Vercel
echo 4. Manual Setup Guide
echo.

set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    echo.
    echo ==================
    echo HEROKU DEPLOYMENT
    echo ==================
    echo.
    echo Please follow these steps:
    echo 1. Install Heroku CLI from: https://devcenter.heroku.com/articles/heroku-cli
    echo 2. Run: heroku login
    echo 3. Run: heroku create anuj-fake-news-detector
    echo 4. Run: git push heroku main
    echo 5. Run: heroku open
    echo.
    echo Your app will be live at: https://anuj-fake-news-detector.herokuapp.com
    echo.
    pause
) else if "%choice%"=="2" (
    echo.
    echo ================
    echo RENDER DEPLOYMENT
    echo ================
    echo.
    echo Please follow these steps:
    echo 1. Go to: https://render.com
    echo 2. Create account and connect GitHub
    echo 3. Create new Web Service
    echo 4. Build Command: pip install -r requirements.txt
    echo 5. Start Command: python app/app.py
    echo.
    pause
) else if "%choice%"=="3" (
    echo.
    echo ================
    echo VERCEL DEPLOYMENT
    echo ================
    echo.
    echo Please follow these steps:
    echo 1. Install Vercel CLI: npm i -g vercel
    echo 2. Run: vercel login
    echo 3. Run: vercel --prod
    echo.
    pause
) else if "%choice%"=="4" (
    echo.
    echo Opening hosting guide...
    start HOSTING_GUIDE.md
) else (
    echo Invalid choice. Opening hosting guide...
    start HOSTING_GUIDE.md
)

echo.
echo Deployment script completed!
echo Check HOSTING_GUIDE.md for detailed instructions.
pause

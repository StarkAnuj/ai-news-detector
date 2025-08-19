@echo off
echo ================================================================
echo              UPLOAD TO GITHUB - FAKE NEWS DETECTION
echo ================================================================
echo.

echo This script will help you upload your project to GitHub
echo Repository: https://github.com/AnujNandal/fake_news_detection
echo.

pause

echo Step 1: Initializing Git repository...
git init

echo Step 2: Adding remote repository...
git remote add origin https://github.com/AnujNandal/fake_news_detection.git

echo Step 3: Adding files to Git...
git add .

echo Step 4: Checking status...
git status

echo.
echo Step 5: Committing changes...
git commit -m "Initial commit: Complete fake news detection system with ML models and web interface"

echo Step 6: Setting main branch and pushing...
git branch -M main
git push -u origin main

echo.
echo ================================================================
echo                    UPLOAD COMPLETED!
echo ================================================================
echo.
echo Your project is now available at:
echo https://github.com/AnujNandal/fake_news_detection
echo.
echo Next steps:
echo 1. Visit your GitHub repository
echo 2. Add a description and topics
echo 3. Star your repository!
echo.
pause

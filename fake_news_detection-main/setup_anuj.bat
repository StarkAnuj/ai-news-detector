@echo off
echo ================================================================
echo           ANUJ NANDAL'S FAKE NEWS DETECTION SYSTEM
echo ================================================================
echo.
echo Welcome to your personalized Fake News Detection System!
echo Created by: Anuj Nandal
echo.
echo This script will set up your project automatically.
echo.
pause

echo Setting up virtual environment...
python -m venv venv
call venv\Scripts\activate

echo Installing requirements...
pip install --upgrade pip
pip install -r requirements.txt

echo Setting up NLTK data...
python setup_nltk.py

echo Training the machine learning model...
python model/train_model.py

echo.
echo ================================================================
echo                    SETUP COMPLETED!
echo ================================================================
echo.
echo Your Fake News Detection System is ready!
echo.
echo To start the application:
echo 1. Run: python app/app.py
echo 2. Open browser to: http://localhost:5000
echo.
echo To upload to GitHub:
echo 1. Create a repository named 'fake_news_detection' on GitHub
echo 2. Run: upload_to_github.bat
echo.
pause

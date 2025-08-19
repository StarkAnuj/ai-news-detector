@echo off
echo ================================================================
echo                  FAKE NEWS DETECTION SYSTEM
echo                      Quick Start Guide
echo ================================================================
echo.

REM Set the Python executable path
set PYTHON_EXE="C:/Users/Honey/Downloads/files (2)/.venv/Scripts/python.exe"

echo Step 1: Python environment already configured!
echo Using Python: %PYTHON_EXE%
echo Packages already installed!

echo.
echo Step 2: Checking model files...
if exist "model\model.pkl" (
    echo Model files found! Skipping training...
    goto :run_app
) else (
    echo No model found. Training new model...
    goto :train_model
)

:train_model
echo.
echo Training the machine learning model...
echo This will download NLTK data and the fake news dataset...
cd model
%PYTHON_EXE% train_model.py
if errorlevel 1 (
    echo ERROR: Model training failed!
    echo Please check the error messages above.
    pause
    exit /b 1
)
cd ..
echo Model training completed successfully!

:run_app
echo.
echo Step 3: Starting the web application...
cd app
echo Opening web browser to http://localhost:5000
start http://localhost:5000
%PYTHON_EXE% app.py

echo.
echo Application stopped.
pause

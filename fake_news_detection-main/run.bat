@echo off
echo Starting Fake News Detection System...
echo.

echo Installing required packages...
pip install -r requirements.txt

echo.
echo Checking if model exists...
if not exist "model\model.pkl" (
    echo Model not found. Training model first...
    cd model
    python train_model.py
    cd ..
) else (
    echo Model found!
)

echo.
echo Starting Flask application...
cd app
python app.py

pause

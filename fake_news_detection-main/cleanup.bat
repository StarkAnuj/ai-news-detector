@echo off
echo ================================
echo Project Cleanup Script
echo Removing unnecessary files...
echo ================================
echo.

REM Remove unnecessary Python scripts
if exist "check_status.py" del /Q "check_status.py"
if exist "main.py" del /Q "main.py"
if exist "quick_start.py" del /Q "quick_start.py"
if exist "test_system.py" del /Q "test_system.py"
if exist "setup_nltk.py" del /Q "setup_nltk.py"
if exist "app.py" del /Q "app.py"

REM Remove unnecessary batch files
if exist "run.bat" del /Q "run.bat"
if exist "start.bat" del /Q "start.bat"
if exist "upload_to_github.bat" del /Q "upload_to_github.bat"

REM Remove unnecessary documentation
if exist "folder-structure.txt" del /Q "folder-structure.txt"
if exist "UPLOAD_GUIDE.md" del /Q "UPLOAD_GUIDE.md"
if exist "README_GITHUB.md" del /Q "README_GITHUB.md"
if exist "HEROKU_DEPLOYMENT.md" del /Q "HEROKU_DEPLOYMENT.md"

REM Remove virtual environments (these shouldn't be in production)
if exist "venv" rmdir /S /Q "venv"
if exist ".venv" rmdir /S /Q ".venv"

REM Remove duplicate static/templates (we have them in app folder)
if exist "static" rmdir /S /Q "static"
if exist "templates" rmdir /S /Q "templates"

REM Remove large data files (model is already trained)
if exist "data" rmdir /S /Q "data"

echo.
echo ================================
echo Cleanup completed!
echo.
echo KEPT FILES (Production Ready):
echo - app/ (main application)
echo - model/ (trained ML model)
echo - requirements.txt
echo - LICENSE
echo - README.md
echo - README_ANUJ.md
echo - PROJECT_SUMMARY_ANUJ.md
echo - Procfile (for Heroku)
echo - runtime.txt (for Heroku)
echo - vercel.json (for Vercel)
echo - deploy.bat (deployment helper)
echo - setup_anuj.bat (setup helper)
echo - HOSTING_GUIDE.md
echo - .gitignore
echo ================================
echo.
pause

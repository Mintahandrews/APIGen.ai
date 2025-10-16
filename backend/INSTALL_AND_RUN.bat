@echo off
echo ========================================
echo Universal API Client Generator v2.0
echo Backend Installation and Startup
echo ========================================
echo.

echo [1/2] Installing Python dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Failed to install dependencies
    echo Please ensure Python and pip are installed
    pause
    exit /b 1
)

echo.
echo [2/2] Starting FastAPI server...
echo.
echo Server will be available at:
echo   - http://localhost:8000
echo   - API Docs: http://localhost:8000/docs
echo.
echo Press Ctrl+C to stop the server
echo.

python main.py

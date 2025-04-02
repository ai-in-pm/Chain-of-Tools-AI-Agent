@echo off
rem Chain-of-Tools AI Agent Showcase Runner
rem Date: April 2, 2025

echo Chain-of-Tools AI Agent Showcase
echo ===============================
echo.

rem Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python is not installed or not in PATH.
    echo Please install Python and try again.
    goto end
)

rem Check if the database directory exists, create if not
if not exist database (
    echo Creating database directory...
    mkdir database
)

rem Check if the models directory exists, create if not
if not exist models (
    echo Creating models directory...
    mkdir models
    echo Note: In a real implementation, you would need to download or train a model.
    echo       For this demonstration, we're using a simulated model.
    echo.
)

rem Install required packages if they're not already installed
echo Checking dependencies...
pip install -r requirements.txt

echo.
echo Running the Chain-of-Tools AI Agent Showcase...
echo.

python showcase_scenarios.py

:end
echo.
pause

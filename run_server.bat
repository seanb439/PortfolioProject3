@echo off
REM Portfolio Website - Startup Script

echo.
echo ================== Portfolio Website ==================
echo Starting Django Development Server...
echo.

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Start the development server
python manage.py runserver

pause

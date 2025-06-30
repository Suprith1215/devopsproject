@echo off
title Run CEW App - Docker
echo ================================
echo Starting CEW App in Docker...
echo ================================

REM Navigate to project folder
cd /d "C:\Users\supri\OneDrive\Desktop\DEVOPS PROJECT"

REM Check Docker status
docker info >nul 2>&1
IF ERRORLEVEL 1 (
    echo ❌ Docker is not running! Please start Docker Desktop and try again.
    pause
    exit /b
)

REM Build Docker image
echo 🔧 Building Docker image...
docker build -t cew-app .

IF ERRORLEVEL 1 (
    echo ❌ Build failed!
    pause
    exit /b
)

REM Run the Docker container
echo 🚀 Running CEW App on port 5000...
start http://localhost:5000
docker run -p 5000:5000 cew-app

REM Hold the window open if the container exits
pause

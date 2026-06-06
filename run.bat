@echo off
chcp 65001 >nul 2>&1
title share_tool工具
echo ==============================
echo   share_tool工具 v1.0.0
echo ==============================
echo.
echo 启动中，请稍候...
cd /d "%~dp0"
"%~dp0venv\Scripts\python.exe" "%~dp0src\main.py"
echo.
echo 应用已关闭。
pause

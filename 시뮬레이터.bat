@echo off
rem Opens the simulator: starts serve.js in a small window, then opens the page.
rem If the server is already running, the new window just exits and the running one is used.
cd /d "%~dp0"
start "uch server" /min cmd /c node serve.js
timeout /t 1 /nobreak >nul
start "" "http://localhost:8788/%%EC%%8B%%9C%%EB%%AE%%AC%%EB%%A0%%88%%EC%%9D%%B4%%ED%%84%%B0.html"

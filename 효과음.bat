@echo off
rem Opens the sound-effect tool: starts serve.js in a small window, then opens the page.
rem If the server is already running, the new window just exits and the running one is used.
cd /d "%~dp0"
start "uch server" /min cmd /c node serve.js
timeout /t 1 /nobreak >nul
start "" "http://localhost:8788/%%ED%%9A%%A8%%EA%%B3%%BC%%EC%%9D%%8C.html"

@echo off
rem Opens the mock-battle tool: starts serve.js in a small window, then opens the page.
rem If the server is already running, the new window just exits and the running one is used.
cd /d "%~dp0"
start "uch server" /min cmd /c node serve.js
timeout /t 1 /nobreak >nul
start "" "http://localhost:8788/%%EB%%AA%%A8%%EC%%9D%%98%%EC%%A0%%84%%ED%%88%%AC.html"

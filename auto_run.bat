@echo off
if not "%~1"=="" (
    python auto_runner.py %1
    exit /b
)

:menu
cls
echo [0] Run All Labs (1 to 10)
echo [1] Lab 1
echo [2] Lab 2
echo [3] Lab 3
echo [4] Lab 4
echo [5] Lab 5
echo [6] Lab 6
echo [7] Lab 7
echo [8] Lab 8
echo [9] Lab 9
echo [10] Lab 10
echo [Q] Exit
echo.
set /p choice="Select: "

if /i "%choice%"=="Q" exit /b
if "%choice%"=="0" ( python auto_runner.py all & pause & goto menu )
if "%choice%"=="1" ( python auto_runner.py 1 & pause & goto menu )
if "%choice%"=="2" ( python auto_runner.py 2 & pause & goto menu )
if "%choice%"=="3" ( python auto_runner.py 3 & pause & goto menu )
if "%choice%"=="4" ( python auto_runner.py 4 & pause & goto menu )
if "%choice%"=="5" ( python auto_runner.py 5 & pause & goto menu )
if "%choice%"=="6" ( python auto_runner.py 6 & pause & goto menu )
if "%choice%"=="7" ( python auto_runner.py 7 & pause & goto menu )
if "%choice%"=="8" ( python auto_runner.py 8 & pause & goto menu )
if "%choice%"=="9" ( python auto_runner.py 9 & pause & goto menu )
if "%choice%"=="10" ( python auto_runner.py 10 & pause & goto menu )
goto menu

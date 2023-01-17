@ECHO OFF
if exist .venv (
    echo virtual environment already exist!
) else (
    python3 -m venv .venv 
)
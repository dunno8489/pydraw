@echo off

echo PyDraw Launcher
if "%1"=="-gui" (
    python "pydraw_gui.py"
)
if "%1"=="-cli" (
    python "pydraw_cli.py"
) else (
    echo please provide an argument -gui, -cli
)
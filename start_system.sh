#!/bin/bash

# Absolute paths
DIR="/home/user/programs"
VENV_DIR="$DIR/venv"
VENV_PYTHON="$VENV_DIR/bin/python3"

# Switch into the working directory
cd "$DIR" || { echo "Directory not found: $DIR"; exit 1; }

# Create venv if missing
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment not found — creating one..."
    python3 -m venv "$VENV_DIR"
fi

# Upgrade pip + ensure scratchattach is installed
echo "Updating pip and installing dependencies..."
"$VENV_PYTHON" -m pip install --upgrade pip
"$VENV_PYTHON" -m pip install --upgrade scratchattach

# Kill any existing bot processes
echo "Stopping old bot processes..."
pkill -f follow.py
pkill -f commentbot.py

# Start fresh bot instance
echo "Launching bot..."
nohup "$VENV_PYTHON" follow.py > follow.log 2>&1 &
nohup "$VENV_PYTHON" commentbot.py > commentbot.log 2>&1 &
/home/user/programs/venv/bin/python3 donecomment.py &


echo "Bot started successfully."


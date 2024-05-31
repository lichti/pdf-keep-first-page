#!/bin/bash

# Check if virtual environment exists, if not create it
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment created."
fi

# Load virtual environment
source venv/bin/activate
echo "Virtual environment activated."

# Install requirements
pip install -r requirements.txt
echo "Requirements installed."

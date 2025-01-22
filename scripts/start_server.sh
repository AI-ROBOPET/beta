#!/bin/bash
# start_server.sh
# Script to start the AI ROBOPET backend and frontend servers.

# Variables
BACKEND_SCRIPT="app.py"
FRONTEND_DIR="frontend"

# Activate virtual environment for backend (if applicable)
if [ -d "venv" ]; then
    echo "Activating virtual environment..."
    source venv/bin/activate
fi

# Start the backend server
echo "Starting backend server..."
nohup python3 $BACKEND_SCRIPT > logs/backend.log 2>&1 &
BACKEND_PID=$!

# Navigate to the frontend directory
cd $FRONTEND_DIR || exit

# Install frontend dependencies if not already installed
if [ ! -d "node_modules" ]; then
    echo "Installing frontend dependencies..."
    npm install
fi

# Start the frontend server
echo "Starting frontend server..."
nohup npm start > ../logs/frontend.log 2>&1 &
FRONTEND_PID=$!

echo "Backend server running with PID $BACKEND_PID"
echo "Frontend server running with PID $FRONTEND_PID"
echo "Logs are available in the 'logs/' directory."

# Optional: Keep script running to manage servers
echo "Press Ctrl+C to stop both servers."
trap "kill $BACKEND_PID $FRONTEND_PID; exit" INT
wait

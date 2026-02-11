#!/bin/bash

echo "Starting Apex Digital AI Deployment..."

# Build frontend
cd ../frontend || exit
npm install
npm run build
cd ../backend || exit

# Setup Python environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Start backend server
uvicorn app.main:app --host 0.0.0.0 --port 8000

echo "Deployment complete. Access frontend at http://localhost:3000 and backend at http://localhost:8000"

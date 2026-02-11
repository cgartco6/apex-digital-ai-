#!/bin/bash
echo "Updating system..."
sudo apt update && sudo apt upgrade -y

echo "Installing Python and Node..."
sudo apt install python3-pip python3-venv nodejs npm docker.io docker-compose -y

echo "Installing backend dependencies..."
python3 -m pip install --upgrade pip
pip3 install -r backend/requirements.txt

echo "Installing frontend dependencies..."
cd frontend
npm install
cd ..

echo "Starting Docker Compose..."
sudo docker-compose up --build

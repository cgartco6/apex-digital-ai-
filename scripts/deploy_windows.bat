@echo off
echo Installing Python dependencies...
python -m pip install --upgrade pip
pip install -r backend/requirements.txt

echo Installing frontend dependencies...
cd frontend
npm install
cd ..

echo Starting Docker Compose...
docker-compose up --build

pause

#!/bin/bash
# For shared hosting with limited resources (Afrihost 2GB, 1x SQL DB)
echo "Deploying Apex Digital AI on cPanel..."

echo "1. Setting up virtual environment"
python3 -m venv venv
source venv/bin/activate

echo "2. Installing dependencies"
pip install -r backend/requirements.txt

echo "3. Creating database in MySQL (use your cPanel DB credentials)"
DB_HOST="localhost"
DB_USER="cpaneluser"
DB_PASS="cpanelpassword"
DB_NAME="apex_ai_db"
mysql -h $DB_HOST -u $DB_USER -p$DB_PASS -e "CREATE DATABASE IF NOT EXISTS $DB_NAME;"

echo "4. Setting environment variables"
cp .env.example .env
nano .env   # update with your database & payment credentials

echo "5. Starting backend"
nohup uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 &

echo "6. Starting frontend"
cd frontend
nohup npm run build &
cd ..

echo "Deployment finished. Access via your domain or IP."

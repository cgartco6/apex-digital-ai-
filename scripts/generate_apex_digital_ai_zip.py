import os
import zipfile

# =========================
# BASE REPO FOLDER
# =========================
repo_folder = "/mnt/data/apex-digital-ai-full-ready"
zip_file_path = "/mnt/data/apex_digital_ai_full_robyn_ready.zip"

# =========================
# HELPER TO CREATE FILES
# =========================
def create_file(path, content=""):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# =========================
# 1. BACKEND
# =========================

# main.py
create_file(f"{repo_folder}/backend/app/main.py", """
from fastapi import FastAPI
from routes import chat_routes, project_routes, analytics_routes

app = FastAPI(title="Apex Digital AI")
app.include_router(chat_routes.router, prefix="/chat")
app.include_router(project_routes.router, prefix="/projects")
app.include_router(analytics_routes.router, prefix="/analytics")
""")

# auth.py
create_file(f"{repo_folder}/backend/app/auth.py", """
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(data: dict):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
""")

# database.py
create_file(f"{repo_folder}/backend/app/database.py", """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
""")

# ai_services/chatbot.py (Robyn)
create_file(f"{repo_folder}/backend/app/ai_services/chatbot.py", """
from ai_models.local_llm import LocalLLM

robyn_llm = LocalLLM(model_name="robyn-base", temperature=0.7)
conversation_history = {}

def chat(user_id: str, message: str) -> str:
    if user_id not in conversation_history:
        conversation_history[user_id] = []
    conversation_history[user_id].append({"role": "user", "content": message})
    response = robyn_llm.generate(conversation_history[user_id], system_prompt="You are Robyn, expert AI support assistant.")
    conversation_history[user_id].append({"role": "assistant", "content": response})
    return response
""")

# ai_services/content_creator.py
create_file(f"{repo_folder}/backend/app/ai_services/content_creator.py", """
def create_project_content(project_name: str):
    return {"mockups": ["design1.png", "design2.png"], "marketing": ["campaign1", "campaign2"]}
""")

# routes/chat_routes.py
create_file(f"{repo_folder}/backend/app/routes/chat_routes.py", """
from fastapi import APIRouter
from ai_services import chatbot

router = APIRouter()

@router.post("/chat")
def chat_endpoint(user_id: str, message: str):
    response = chatbot.chat(user_id, message)
    return {"response": response}
""")

# routes/project_routes.py
create_file(f"{repo_folder}/backend/app/routes/project_routes.py", """
from fastapi import APIRouter
from ai_services.content_creator import create_project_content

router = APIRouter()

@router.post("/generate_project")
def generate_project(client_id: int, project_name: str):
    project = {
        "client_id": client_id,
        "name": project_name,
        "designs": create_project_content(project_name),
    }
    return {"project": project}
""")

# routes/analytics_routes.py
create_file(f"{repo_folder}/backend/app/routes/analytics_routes.py", """
from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard/{client_id}")
def dashboard(client_id: int):
    return {"stats": {"projects": 5, "revenue": 1200}}
""")

# backend requirements.txt
create_file(f"{repo_folder}/backend/requirements.txt", """
fastapi
uvicorn
sqlalchemy
pymysql
stripe
paypalrestsdk
fpdf2
Pillow
requests
python-dotenv
pandas
numpy
""")

# Dockerfile
create_file(f"{repo_folder}/backend/Dockerfile", """
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app ./app
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
""")

# =========================
# 2. FRONTEND
# =========================
create_file(f"{repo_folder}/frontend/src/components/Chatbot.jsx", """
import React, { useState } from "react";
import axios from "axios";

export default function Chatbot({ userId }) {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");
    const sendMessage = async () => {
        if (!input) return;
        setMessages([...messages, { role: "user", content: input }]);
        const res = await axios.post("http://localhost:8000/chat/chat", { user_id: userId, message: input });
        setMessages([...messages, { role: "user", content: input }, { role: "assistant", content: res.data.response }]);
        setInput("");
    };
    return (
        <div className="chatbot p-4 border rounded w-96">
            <div className="messages h-64 overflow-auto mb-2">
                {messages.map((m, idx) => (
                    <div key={idx} className={m.role==="user"?"text-right":"text-left"}>
                        <span className={`px-2 py-1 rounded ${m.role==="user"?"bg-blue-500 text-white":"bg-gray-200"}`}>{m.content}</span>
                    </div>
                ))}
            </div>
            <div className="input flex">
                <input className="flex-1 border px-2 py-1" value={input} onChange={(e)=>setInput(e.target.value)} placeholder="Ask Robyn..." />
                <button className="ml-2 px-4 bg-blue-600 text-white" onClick={sendMessage}>Send</button>
            </div>
        </div>
    );
}
""")

# frontend Dashboard page
create_file(f"{repo_folder}/frontend/src/pages/Dashboard.jsx", """
import React from "react";
import Chatbot from "../components/Chatbot";

export default function Dashboard() {
    const userId = "user_123";
    return (
        <div>
            <h1>Dashboard</h1>
            <Chatbot userId={userId} />
        </div>
    );
}
""")

# =========================
# 3. README.md
# =========================
create_file(f"{repo_folder}/README.md", "# Apex Digital AI with Robyn Chatbot\nFully autonomous AI design & marketing studio with live human-like support.\n")

# =========================
# 4. CREATE ZIP
# =========================
with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(repo_folder):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, repo_folder)
            zipf.write(file_path, arcname)

print(f"✅ ZIP file created: {zip_file_path}")

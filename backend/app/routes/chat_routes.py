from fastapi import APIRouter
from ai_services import chatbot

router = APIRouter()

@router.post("/chat")
def chat_endpoint(user_id: str, message: str):
    """
    Endpoint for live chatbot interaction
    """
    response = chatbot.chat(user_id, message)
    return {"response": response}

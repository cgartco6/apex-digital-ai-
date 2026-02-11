from typing import List
from ai_models.local_llm import LocalLLM

# Initialize the Robyn chatbot
robyn_llm = LocalLLM(model_name="robyn-base", temperature=0.7)

conversation_history = {}

def chat(user_id: str, message: str) -> str:
    """
    Handle user message and return response.
    Maintains conversation history per user.
    """
    if user_id not in conversation_history:
        conversation_history[user_id] = []
    
    conversation_history[user_id].append({"role": "user", "content": message})

    # Generate response using LLM
    response = robyn_llm.generate(
        conversation_history[user_id],
        system_prompt="You are Robyn, an expert AI support assistant. Solve all user problems politely and efficiently."
    )
    
    conversation_history[user_id].append({"role": "assistant", "content": response})
    return response

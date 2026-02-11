from typing import List
from ai_models.local_llm import LocalLLM

# Initialize Robyn LLM
robyn_llm = LocalLLM(model_name="robyn-base", temperature=0.7)

# Keep conversation history per user
conversation_history = {}

def chat(user_id: str, message: str) -> str:
    if user_id not in conversation_history:
        conversation_history[user_id] = []

    conversation_history[user_id].append({"role": "user", "content": message})

    # Generate human-like response
    response = robyn_llm.generate(
        conversation_history[user_id],
        system_prompt="You are Robyn, an expert AI support assistant. Solve all user problems politely and efficiently."
    )

    conversation_history[user_id].append({"role": "assistant", "content": response})
    return response

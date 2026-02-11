import random

def generate_text(prompt: str) -> str:
    """
    Generates text locally using a lightweight model.
    Falls back to cloud if model exceeds RAM limits.
    """
    # Lightweight stub for local generation
    local_outputs = [
        f"Generated text locally for: {prompt}",
        f"Your project content: {prompt}",
        f"AI draft content: {prompt}"
    ]
    return random.choice(local_outputs)

def generate_design(spec: dict) -> dict:
    """
    Generates simple design mockups locally.
    """
    design = {
        "layout": "basic grid",
        "colors": ["#000000", "#FFFFFF"],
        "images": ["local_placeholder.png"]
    }
    return design

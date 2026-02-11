from PIL import Image, ImageDraw
import random
import os

def generate_image(prompt: str, filename: str = None) -> str:
    """
    Generates placeholder image locally. Can be replaced with SDXL API for high-quality output.
    """
    if not filename:
        filename = f"./docs/{prompt.replace(' ','_')}.png"
    img = Image.new('RGB', (512, 512), color=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    d = ImageDraw.Draw(img)
    d.text((10, 10), prompt, fill=(255,255,255))
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    img.save(filename)
    return filename

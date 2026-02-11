import os
import json
from fpdf import FPDF
from PIL import Image, ImageDraw

def generate_client_project(project_id="project_001"):
    base_path = f"client_project_flow/{project_id}"
    os.makedirs(f"{base_path}/design", exist_ok=True)
    os.makedirs(f"{base_path}/documents", exist_ok=True)
    os.makedirs(f"{base_path}/marketing", exist_ok=True)
    os.makedirs(f"{base_path}/analytics", exist_ok=True)

    # Design
    for name, text, size in [
        ("logo.png", "Apex Digital AI", (512,512)),
        ("website_mockup.png", "Website Mockup", (1024,768)),
        ("social_media_banner.png", "Promote Your Brand!", (1200,628))
    ]:
        img = Image.new('RGB', size, color=(30,144,255))
        d = ImageDraw.Draw(img)
        d.text((10,10), text, fill=(255,255,255))
        img.save(f"{base_path}/design/{name}")

    # Documents
    docs = {
        "contract.pdf": "Contract for Client X...",
        "t&c.pdf": "Terms & Conditions...",
        "popia.pdf": "POPIA Compliance...",
        "privacy_policy.pdf": "Privacy Policy..."
    }
    for filename, content in docs.items():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0,10, content)
        pdf.output(f"{base_path}/documents/{filename}")

    # Marketing
    campaigns = [
        {"campaign_name": "Logo Launch", "platform": "Facebook", "content":"Check out your new logo!", "predicted_roi": 320},
        {"campaign_name": "Website Reveal", "platform": "Instagram", "content":"Your new website is live!", "predicted_roi": 280},
        {"campaign_name": "Banner Boost", "platform": "LinkedIn", "content":"Boost your brand with banners!", "predicted_roi": 410}
    ]
    for i, c in enumerate(campaigns,1):
        with open(f"{base_path}/marketing/campaign_{i}.json", "w") as f:
            json.dump(c, f, indent=4)

    # Analytics
    analytics = {
        "project_id": project_id,
        "total_clients": 1,
        "total_revenue": 1500.0,
        "average_per_client": 1500.0
    }
    with open(f"{base_path}/analytics/report.json", "w") as f:
        json.dump(analytics, f, indent=4)

if __name__=="__main__":
    generate_client_project()
    print("Sample client project generated.")

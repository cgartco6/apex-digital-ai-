import random

def generate_campaign(project: dict, target_audience: dict) -> list:
    """
    Generates multiple marketing campaign variations
    """
    campaigns = []
    for i in range(3):
        campaigns.append({
            "campaign_name": f"{project['design']['layout']} Campaign {i+1}",
            "content": f"Marketing content for {project['text']} targeting {target_audience.get('region','global')}",
            "predicted_roi": random.uniform(50, 500)  # Scoring for content scorer
        })
    return campaigns

from fastapi import FastAPI
from routes import payment_routes
from ai_services import social_media_ai, pricing_ai

app = FastAPI(title="Apex Digital AI")

# Routes
app.include_router(payment_routes.router, prefix="/payments")

# Example endpoint for AI recommendation
@app.post("/recommend_tier")
async def recommend(client_profile: dict):
    tier = pricing_ai.recommend_tier(client_profile)
    credits = pricing_ai.recommend_credits(client_profile, tier_limit={
        "Starter Tier":5, "Business Tier":20, "Pro Tier":100, "Enterprise":1000
    }[tier])
    return {"recommended_tier": tier, "recommended_credits": credits}

# Example endpoint for scheduling social media posts
@app.post("/schedule_posts")
async def schedule_posts(project: dict, platforms: list = None):
    return social_media_ai.generate_campaign_posts(project, platforms)

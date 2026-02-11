def recommend_tier(client_profile):
    project_weight = client_profile["monthly_projects"] * client_profile["design_complexity"]
    marketing_weight = client_profile["marketing_campaigns"] * 2
    total_score = project_weight + marketing_weight

    if total_score <= 5:
        return "Starter Tier"
    elif total_score <= 25:
        return "Business Tier"
    elif total_score <= 100:
        return "Pro Tier"
    else:
        return "Enterprise"

def recommend_credits(client_profile, tier_limit):
    extra_projects = max(0, client_profile["monthly_projects"] - tier_limit)
    if extra_projects == 0: return 0
    if extra_projects <= 10: return "10 Credits Pack"
    elif extra_projects <= 25: return "25 Credits Pack"
    elif extra_projects <= 50: return "50 Credits Pack"
    else: return "100 Credits Pack"

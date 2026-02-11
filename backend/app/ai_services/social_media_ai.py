import datetime

SOCIAL_PLATFORMS = ["TikTok", "Instagram", "YouTube", "X", "LinkedIn", "Facebook"]

def schedule_post(content, platform, scheduled_time=None):
    """
    Schedule a post to the specified social media platform
    """
    if platform not in SOCIAL_PLATFORMS:
        raise ValueError(f"Platform {platform} not supported")
    
    if scheduled_time is None:
        scheduled_time = datetime.datetime.now() + datetime.timedelta(minutes=10)

    return {
        "platform": platform,
        "content": content,
        "scheduled_time": scheduled_time.isoformat(),
        "status": "scheduled"
    }

def generate_campaign_posts(project, target_platforms=None):
    """
    Generate posts for multiple platforms automatically
    """
    if target_platforms is None:
        target_platforms = SOCIAL_PLATFORMS

    posts = []
    for platform in target_platforms:
        content = f"{project['name']} - AI generated content for {platform}"
        posts.append(schedule_post(content, platform))
    return posts

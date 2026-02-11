from fastapi import APIRouter
from ai_services.analytics import get_project_stats, get_marketing_roi

router = APIRouter()

@router.get("/dashboard/{client_id}")
def dashboard(client_id: int):
    stats = get_project_stats(client_id)
    roi = get_marketing_roi(client_id)
    return {"stats": stats, "roi": roi}

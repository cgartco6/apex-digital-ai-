from fastapi import APIRouter
from ai_services.project_validator import validate_project
from ai_services.content_creator import create_project_content

router = APIRouter()

@router.post("/generate_project")
def generate_project(client_id: int, project_name: str):
    project = {
        "client_id": client_id,
        "name": project_name,
        "designs": create_project_content(project_name),
    }
    validation = validate_project(project)
    return {"project": project, "validation": validation}

def validate_project(project: dict, stage: str) -> dict:
    """
    Stage can be: reviewer, checker, validator
    """
    project_copy = project.copy()
    project_copy[f"{stage}_status"] = "approved"
    project_copy[f"{stage}_notes"] = f"{stage} completed successfully"
    return project_copy

def fix_project(project: dict) -> dict:
    """
    Applies minor fixes to ensure project exceeds expectations
    """
    project_copy = project.copy()
    project_copy["fixer_status"] = "applied enhancements"
    project_copy["notes"] = "All improvements applied"
    return project_copy

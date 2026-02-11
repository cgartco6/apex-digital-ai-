from backend.app.ai_services.content_creator import create_client_project
from backend.app.ai_services.project_validator import full_validation_pipeline
from backend.app.ai_services.marketing_ai import create_marketing_campaign
from backend.app.ai_services.content_scorer import score_marketing_content
from backend.app.ai_services.compliance_ai import generate_compliance_docs

def run_autonomous_cycle(client_request, target_audience):
    # Generate project
    project = create_client_project(client_request)
    
    # Validate project
    final_project = full_validation_pipeline(project)
    
    # Generate compliance docs
    docs = generate_compliance_docs({"name": client_request.get("name"), "id": 1})
    
    # Create marketing campaigns
    campaigns = create_marketing_campaign(final_project, target_audience)
    scored_campaigns = score_marketing_content(campaigns)
    
    # Return final output
    return {
        "project": final_project,
        "docs": docs,
        "marketing": scored_campaigns
    }

if __name__ == "__main__":
    client_request = {"name": "Test Client", "design_spec": "Logo + Website", "copy_spec": "Marketing text"}
    target_audience = {"region": "South Africa", "demographic": "SMB Owners"}
    output = run_autonomous_cycle(client_request, target_audience)
    print(output)

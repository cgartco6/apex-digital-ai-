from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]

def test_project_creation():
    request_data = {"name": "Test Client", "design_spec": "Logo", "copy_spec": "Marketing text"}
    response = client.post("/projects/create", json=request_data)
    assert response.status_code == 200
    assert "project" in response.json()

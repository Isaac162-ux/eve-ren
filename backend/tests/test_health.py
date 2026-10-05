from fastapi.testclient import TestClient
from app.main import app
def test_health_reports_eve_online():
    response=TestClient(app).get("/health")
    assert response.status_code==200
    assert response.json()["status"]=="online"
    assert response.json()["system"]=="E.V.E.9"

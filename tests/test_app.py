
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_predict():
    payload = {"features": [[5.1, 3.5, 1.4, 0.2]], "return_proba": True}
    r = client.post("/predict", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert "predictions" in data
    assert isinstance(data["predictions"], list)

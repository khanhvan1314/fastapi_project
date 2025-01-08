from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_version():
    response = client.get("/get_version")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

def test_check_prime_true():
    response = client.get("/check_prime/7")
    assert response.status_code == 200
    assert response.json() == {"number": 7, "is_prime": True}

def test_check_prime_false():
    response = client.get("/check_prime/8")
    assert response.status_code == 200
    assert response.json() == {"number": 8, "is_prime": False}

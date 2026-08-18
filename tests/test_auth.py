import pytest

def test_register(client):
    response = client.post("/auth/register", json={"email": "a@a.com", "password": "testpass123"})
    assert response.status_code == 200

def test_register_duplicate_email(client):
    response_1 = client.post("/auth/register", json={"email": "a@a.com", "password": "testpass1234"})
    response_2 = client.post("/auth/register", json={"email": "a@a.com", "password": "testpass12345"})
    assert response_1.status_code == 200
    assert response_2.status_code == 400

def test_login_success(client):
    response_r = client.post("/auth/register", json={"email": "a@a.com", "password": "testpass123"})
    response_l = client.post("/auth/login", data={"username": "a@a.com", "password": "testpass123"})
    assert response_r.status_code == 200
    assert response_l.status_code == 200
    assert "access_token" in response_l.json()
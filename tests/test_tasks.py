def register_and_login(client, email):
    credentials = {"email": email, "password": "testpass123"}
    assert client.post("/auth/register", json=credentials).status_code == 200
    response = client.post("/auth/login", data={"username": email, "password": credentials["password"]})
    assert response.status_code == 200
    return {"Authorization": "Bearer " + response.json()["access_token"]}


def test_task_lifecycle(client):
    headers = register_and_login(client, "owner@example.com")
    response = client.post("/tasks/", json={"title": "Ship a tested API"}, headers=headers)
    assert response.status_code == 200
    task = response.json()
    assert task["title"] == "Ship a tested API" and not task["is_done"]
    assert client.get("/tasks/", headers=headers).json() == [task]
    assert client.patch(f"/tasks/{task['id']}", headers=headers).json()["is_done"]
    assert not client.patch(f"/tasks/{task['id']}", headers=headers).json()["is_done"]
    assert client.delete(f"/tasks/{task['id']}", headers=headers).status_code == 200
    assert client.get("/tasks/", headers=headers).json() == []
    assert client.patch(f"/tasks/{task['id']}", headers=headers).status_code == 404


def test_users_cannot_access_each_others_tasks(client):
    owner = register_and_login(client, "owner@example.com")
    other = register_and_login(client, "other@example.com")
    task = client.post("/tasks/", json={"title": "Private"}, headers=owner).json()
    assert client.get("/tasks/", headers=other).json() == []
    assert client.patch(f"/tasks/{task['id']}", headers=other).status_code == 403
    assert client.delete(f"/tasks/{task['id']}", headers=other).status_code == 403
    assert client.get("/tasks/", headers=owner).json()[0]["is_done"] is False


def test_auth_required_and_invalid_tokens(client):
    for headers in [{}, {"Authorization": "Bearer invalid"}]:
        assert client.get("/tasks/", headers=headers).status_code == 401
        assert client.post("/tasks/", json={"title": "Private"}, headers=headers).status_code == 401


def test_wrong_password(client):
    register_and_login(client, "owner@example.com")
    assert client.post("/auth/login", data={"username": "owner@example.com", "password": "wrongpass"}).status_code == 401


def test_bcrypt_unicode_byte_limit(client):
    # Pydantic's character limit alone is insufficient for multibyte input.
    assert client.post("/auth/register", json={"email": "long@example.com", "password": "я" * 37}).status_code == 422
    assert client.post("/auth/register", json={"email": "boundary@example.com", "password": "я" * 36}).status_code == 200


def test_missing_tasks(client):
    headers = register_and_login(client, "owner@example.com")
    assert client.patch("/tasks/999", headers=headers).status_code == 404
    assert client.delete("/tasks/999", headers=headers).status_code == 404

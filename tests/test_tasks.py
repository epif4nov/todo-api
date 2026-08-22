from app.models import User


def get_token(client):
    client.post(
        "/auth/register",
        json={
            "email": "test@test.com",
            "password": "testpass123"
        }
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "test@test.com",
            "password": "testpass123"
        }
    )

    return response.json()["access_token"]

def auth_headers(token):
    return {
        "Authorization": f"Bearer {token}"
    }

def test_create_task(client):
    token = get_token(client)

    response = client.post(
        "/tasks/",
        json={
            "title": "Первая задача"
        },
        headers=auth_headers(token)
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Первая задача"
    assert data["is_done"] is False


def test_get_tasks(client):
    token = get_token(client)

    client.post(
        "/tasks/",
        json={
            "title": "Задача 1"
        },
        headers=auth_headers(token)
    )

    response = client.get(
        "/tasks/",
        headers=auth_headers(token)
    )

    assert response.status_code == 200

    tasks = response.json()

    assert len(tasks) == 1
    assert tasks[0]["title"] == "Задача 1"


def test_toggle_task(client):
    token = get_token(client)

    create_response = client.post(
        "/tasks/",
        json={
            "title": "Сделать тесты"
        },
        headers=auth_headers(token)
    )

    task_id = create_response.json()["id"]

    response = client.patch(
        f"/tasks/{task_id}",
        headers=auth_headers(token)
    )

    assert response.status_code == 200

    assert response.json()["is_done"] is True


def test_delete_task(client):
    token = get_token(client)

    create_response = client.post(
        "/tasks/",
        json={
            "title": "Удалить меня"
        },
        headers=auth_headers(token)
    )

    task_id = create_response.json()["id"]

    response = client.delete(
        f"/tasks/{task_id}",
        headers=auth_headers(token)
    )

    assert response.status_code == 200

    assert response.json()["detail"] == "Задача удалена"
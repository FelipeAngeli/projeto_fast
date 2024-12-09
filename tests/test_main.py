from http import HTTPStatus


def test_read_rood_deve_retornar_ok_e_ola_mundo(client):
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá Mundo!"}


def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "username": "testeUsername",
            "password": "testePassword",
            "email": "test@test.com",
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "id": 1,
        "username": "testeUsername",
        "email": "test@test.com",
    }


def test_read_users(client):
    response = client.get("/users/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "id": 1,
                "username": "testeUsername",
                "email": "test@test.com",
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "username": "testeUsername2",
            "password": "testePassword2",
            "email": "email2@email.com",
            "id": 1,
        },
    )
    assert response.json() == {
        "username": "testeUsername2",
        "email": "email2@email.com",
        "id": 1,
    }


def test_delete_user(client):
    response = client.delete("/users/1")
    assert response.json() == {"message": "usuário deletado com sucesso"}
    assert response.status_code == HTTPStatus.OK

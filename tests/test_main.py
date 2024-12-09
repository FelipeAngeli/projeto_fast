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

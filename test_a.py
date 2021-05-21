import requests


def test_create_user():
    user_example = {
        "id": 44445,
        "username": "asipkov",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }
    req = requests.post('https://petstore.swagger.io/v2/user', json=user_example)
    assert req.status_code == 200, """Создание профиля пользователя"""


def test_get_user():
    username = 'asipkov'
    req = requests.get(f'https://petstore.swagger.io/v2/user/{username}')
    assert req.status_code == 200, """Получение профиля пользователя по username"""


def test_update_user():
    username = 'asipkov'
    new_username = {
        "id": 44445,
        "username": "asipkov111",
        "firstName": "string",
        "lastName": "string",
        "email": "string",
        "password": "string",
        "phone": "string",
        "userStatus": 0
    }
    req = requests.put(f'https://petstore.swagger.io/v2/user/{username}', json=new_username)
    assert req.status_code == 200, """Изменение профиля пользователя"""


def test_delete_user():
    username = 'asipkov111'
    req = requests.delete(f'https://petstore.swagger.io/v2/user/{username}')
    assert req.status_code == 200, """Удаление профиля пользователя"""

import allure
import pytest
import requests
import random
import string
from helpers import *


@allure.step('Создание пользователя с последующим удалением')
@pytest.fixture(scope='function')
def create_user_with_del():
    data_user = []

    email = f'{generator_str(5)}@yandex.ru'
    password = generator_str(6)
    name = generator_str(6)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    response_create = create_user(payload)
    if response_create.status_code == 200:
        data_user.append(email)
        data_user.append(password)
        data_user.append(name)
        data_user.append(response_create.json()['accessToken'])

    yield data_user
    token = data_user[3]
    delete_user(token)


@pytest.fixture(scope='function')
def login(create_user_with_del):
    payload = {
        'email': create_user_with_del[0],
        'password': create_user_with_del[1],
        'name': create_user_with_del[2]
    }
    headers = get_headers(create_user_with_del[3])
    return login_user(payload, headers)



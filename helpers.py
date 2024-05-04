from endpoints import *
import requests
import allure
import string
import random


@allure.step('Получение рандомной строки')
def generator_str(length):
    characters = string.ascii_letters + string.ascii_lowercase
    random_str = ''.join(random.choice(characters) for _ in range(length))
    return random_str


@allure.step('Создание пользователя')
def create_user(payload):
    response_create = requests.post(f'{Endpoints.URL + Endpoints.CREATE_USER}', json=payload)
    return response_create


@allure.step('Регистрация пользователя')
def login_user(payload, headers):
    response_login = requests.post(f'{Endpoints.URL + Endpoints.LOGIN_USER}', json=payload, headers=headers)
    return response_login


@allure.step('Удаление курьера')
def delete_user(token):
    headers = get_headers(token)
    response_delete = requests.delete(f'{Endpoints.URL + Endpoints.DELETE_PATCH_GET_USER}', headers=headers)
    return response_delete


@allure.step('Обновление данных')
def update_data_user(payload, headers):
    response_patch = requests.patch(f'{Endpoints.URL+Endpoints.DELETE_PATCH_GET_USER}',
                                    json=payload, headers=headers)
    return response_patch


@allure.step('Создание заказа')
def create_order(ingredients):

    response_post = requests.post(f'{Endpoints.URL+Endpoints.CREATE_ORDER}', data=ingredients)
    return response_post


@allure.step('создание списка ингредиентов')
def create_list_ingredient(col):
    for col in range(col):
        ingredients = {'ingredients': [get_ingredients(col)]}
        return ingredients


@allure.step('Получение списка ингредиентов')
def get_ingredients(num):
    response_get = requests.get(f'{Endpoints.URL+Endpoints.GET_INGREDIENTS}')
    result = response_get.json()['data'][num]['_id']
    return result


@allure.step('Получение токена')
def get_headers(token):
    headers = {'Authorization': token}
    return headers


@allure.step('Получение заказов пользователя')
def get_orders_by_user(headers):
    response_get = requests.get(f'{Endpoints.URL+Endpoints.CREATE_ORDER}', headers=headers)
    return response_get


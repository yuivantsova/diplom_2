import allure
import pytest
from helpers import *


class TestLoginUser:

    @allure.title('Проверка регистрации пользователя')
    def test_login_user(self, create_user_with_del):
        payload = {
            'email': create_user_with_del[0],
            'password': create_user_with_del[1],
            'name': create_user_with_del[2]
        }
        headers = get_headers(create_user_with_del[3])
        response = login_user(payload, headers)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('проверка регистрации пользователя с неверным логином')
    def test_login_user_incorrect_data_email(self, create_user_with_del):
        payload = {
            'email': generator_str(6),
            'password': create_user_with_del[1],
            'name': create_user_with_del[2]
        }
        headers = get_headers(create_user_with_del[3])
        response = login_user(payload, headers)
        assert response.status_code == 401 and response.json()['success'] == False

    @allure.title('проверка регистрации пользователя с неверным паролем')
    def test_login_user_incorrect_data_passord(self, create_user_with_del):
        payload = {
            'email': create_user_with_del[0],
            'password': generator_str(6),
            'name': create_user_with_del[2]
        }
        headers = get_headers(create_user_with_del[3])
        response = login_user(payload, headers)
        assert response.status_code == 401 and response.json()['success'] == False
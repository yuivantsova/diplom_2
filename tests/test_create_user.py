import allure
import pytest
from helpers import *


class TestCreateUser:

    @allure.title('Проверка создания пользователя')
    def test_create_new_user(self):
        payload = {
                "email": f'{generator_str(5)}@yandex.ru',
                "password": generator_str(6),
                "name": generator_str(6)
        }
        response = create_user(payload)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Проверка создания пользователя, который уже зарегестрирован')
    def test_create_user_double_user(self):
        payload = {
            "email": f'{generator_str(5)}@yandex.ru',
            "password": generator_str(6),
            "name": generator_str(6)
        }
        create_user(payload)
        response = create_user(payload)
        assert response.status_code == 403 and response.json()['success'] == False

    @allure.title('Проверка создания пользователя с пустыми обязательными полями')
    @pytest.mark.parametrize('payload',[({"email":'',"password": generator_str(6), "name": generator_str(6)}),
                                        ({"email":'f{generator_str(5)}@yandex.ru',"password": '', "name": generator_str(6)}),
                                        ({"email":'f{generator_str(5)}@yandex.ru',"password": generator_str(8), "name": ''})
                                        ], ids=['empty_email','empty_password','empty_name'])
    def test_create_user_with_empty_field(self, payload):
        response = create_user(payload)
        assert response.status_code == 403 and response.json()['success'] == False


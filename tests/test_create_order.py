import pytest
from helpers import *
import allure


class TestOrder:

    @allure.title('Проверка создания заказа с авторизацией')
    def test_create_order_with_auth(self, login):
        response = create_order(ingredients=create_list_ingredient(5))
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Проверка создания заказа без авторизации')
    def test_create_order_without_auth(self):
        response = create_order(ingredients=create_list_ingredient(4))
        assert response.status_code == 401 # тест падает с кодом 200, ошибка апи? (200 != 401)

    @allure.title('Проверка создания заказа без передачи хэш и с невалидной хэш суммой')
    @pytest.mark.parametrize('hash', [None, f'{generator_str}'],
                             ids=['without hash', 'invalid hash'])
    def test_create_order_without_ingredients(self, login, hash):
        response = create_order(hash)
        assert response.status_code == 400 and response.json()['success'] == False

from helpers import *


class TestGetOrdersByUser:

    @allure.title('Получение списка заказов пользователя с авторизацией')
    def test_get_orders_with_auth(self, create_user_with_del):
        payload = {
            'email': create_user_with_del[0],
            'password': create_user_with_del[1],
            'name': create_user_with_del[2]
        }
        headers = get_headers(create_user_with_del[3])
        login_user(payload, headers)
        create_order(ingredients=create_list_ingredient(5))
        response = get_orders_by_user(headers)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title('Получение списка заказов пользователя без авторизации')
    def test_get_orders_without_auth(self):
        response = get_orders_by_user(None)
        assert response.status_code == 401 and response.json()['success'] == False

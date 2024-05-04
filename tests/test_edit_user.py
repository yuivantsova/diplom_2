from helpers import *


class TestEditDataUser:

    @allure.title('Изменение данных пользователя с авторизацией')
    def test_edit_user_data(self, create_user_with_del):

        payload_new = {
            'email': 'yuri@ya.ru',
            'name': 'Маша'
        }
        headers = get_headers(create_user_with_del[3])
        response_patch = update_data_user(payload_new, headers)
        assert (response_patch.status_code == 200 and response_patch.json()['user']['name'] == 'Маша'
                and response_patch.json()['user']['email'] == 'yuri@ya.ru')

    @allure.title('Изменение данных пользователя без авторизации')
    def test_edit_data_user_without_login(self, create_user_with_del):
        payload_new = {
            'email': 'yuri@ya.ru',
            'name': 'Маша'
        }
        headers = None
        response_patch = update_data_user(payload_new, headers)
        assert response_patch.status_code == 401 and response_patch.json()['success'] == False
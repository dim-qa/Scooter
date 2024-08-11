import pytest
import requests
import data
import links
import allure


class TestApi:
    # Создание курьера

    # курьера можно создать;

    @allure.title('1. Курьера можно создать')
    @pytest.mark.parametrize('api, code', [
        (data.METHOD_CODE[1]['create'], data.METHOD_CODE[1]['Created'])
    ])
    def test_can_create_account(self, new_account, api, code):
        requests.delete(f'{links.MAIN}{data.METHOD_CODE[2]["delete"]}{new_account[1]}')
        response = requests.post(f'{links.MAIN}{api}', data=new_account[0])
        assert response.status_code == code

    # нельзя создать двух одинаковых курьеров
    @allure.title('2. нельзя создать двух одинаковых курьеров')
    @pytest.mark.parametrize('api, code', [
        (data.METHOD_CODE[1]['create'], data.METHOD_CODE[1]['Conflict'])
    ])
    def test_failed_create_copy_account(self, new_account, api, code):
        response = requests.post(f'{links.MAIN}{api}', data=new_account[0])
        assert response.status_code == code

    # чтобы создать курьера, нужно передать в ручку все обязательные поля
    @allure.title('3. чтобы создать курьера, нужно передать в ручку все обязательные поля')
    @pytest.mark.parametrize('api, code, account_value', [
        (data.METHOD_CODE[1]['create'], data.METHOD_CODE[1]['Bad Request'], 'login'),
        (data.METHOD_CODE[1]['create'], data.METHOD_CODE[1]['Bad Request'], 'password'),
        (data.METHOD_CODE[1]['create'], data.METHOD_CODE[1]['Bad Request'], 'firstName')
    ])
    def test_failed_create_copy_account(self, new_account, api, code, account_value):
        account = new_account[0]
        account[account_value] = ''
        response = requests.post(f'{links.MAIN}{api}', data=account)
        assert response.status_code == code

    # запрос возвращает правильный код ответа
    @allure.title('4. запрос возвращает код ответа')
    @pytest.mark.parametrize('api, code', [
        (data.METHOD_CODE[1]['create'], '{"ok":true}')
    ])
    def test_can_create_account(self, new_account, api, code):
        requests.delete(f'{links.MAIN}{data.METHOD_CODE[2]["delete"]}{new_account[1]}')
        response = requests.post(f'{links.MAIN}{api}', data=new_account[0])
        assert response.text == code

    # если одного из полей нет, запрос возвращает ошибку
    @allure.title('5. если одного из полей нет, запрос возвращает ошибку')
    @pytest.mark.parametrize('api, code, account_value', [
        (data.METHOD_CODE[1]['create'], '{"code":400,"message":"Недостаточно данных для создания учетной записи"}',
         'login'),
        (data.METHOD_CODE[1]['create'], '{"code":400,"message":"Недостаточно данных для создания учетной записи"}',
         'password')
    ])
    def test_failed_create_copy_account(self, new_account, api, code, account_value):
        account = new_account[0]
        account[account_value] = ''
        response = requests.post(f'{links.MAIN}{api}', data=account)
        assert response.text == code

    # если создать пользователя с логином, который уже есть, возвращается ошибка
    @allure.title('6. если создать пользователя с логином, который уже есть, возвращается ошибка')
    @pytest.mark.parametrize('api, code', [
        (data.METHOD_CODE[1]['create'], '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}')
    ])
    def test_failed_create_copy_account(self, new_account, api, code):
        response = requests.post(f'{links.MAIN}{api}', data=new_account[0])
        assert response.text == code

    # Логин курьера
    # курьер может авторизоваться
    @allure.title('Логин курьера')
    @allure.title('7. курьер может авторизоваться')
    @pytest.mark.parametrize('api, code', [
        (data.METHOD_CODE[0]['login'], data.METHOD_CODE[0]['OK'])
    ])
    def test_inner(self, new_account, api, code):
        response = requests.post(f'{links.MAIN}{api}', data=new_account[0])
        assert response.status_code == code

    # для авторизации нужно передать все обязательные поля
    @allure.title('8. для авторизации нужно передать все обязательные поля')
    @pytest.mark.parametrize('api, code, account_value', [
        (data.METHOD_CODE[0]['login'], "Недостаточно данных для входа", 'login'),
        (data.METHOD_CODE[0]['login'], "Недостаточно данных для входа", 'password')
    ])
    def test_inner_without_param(self, new_account, api, code, account_value):
        account = new_account[0]
        account.pop(account_value, None)
        response = requests.post(f'{links.MAIN}{api}', data=account)
        assert response.json()['message'] == code, f'Респонс выдал ошибку с {response.json()["message"]}'

    # система вернёт ошибку, если неправильно указать логин или пароль
    @allure.title('9. система вернёт ошибку, если неправильно указать логин или пароль')
    @pytest.mark.parametrize('api, code, account_value, value', [
        (data.METHOD_CODE[0]['login'], 'Учетная запись не найдена', 'login', 'qwerty'),
        (data.METHOD_CODE[0]['login'], 'Учетная запись не найдена', 'password', 'qwerty')
    ])
    def test_fail_with_not_validate_param(self, new_account, api, code, account_value, value):
        account = new_account[0]
        account[account_value] = value
        response = requests.post(f'{links.MAIN}{api}', data=account)
        assert response.json()['message'] == code

    # если какого-то поля нет, запрос возвращает ошибку НЕ ВЫПОЛНЕНО
    @allure.title('10. если какого-то поля нет, запрос возвращает ошибку')
    @pytest.mark.parametrize('api, code, account_value', [
        (data.METHOD_CODE[0]['login'], "Недостаточно данных для входа", 'login'),
        (data.METHOD_CODE[0]['login'], "Недостаточно данных для входа", 'password')
    ])
    def test_failed_inner_without_param(self, new_account, api, code, account_value):
        account = new_account[0]
        account.pop(account_value, None)
        response = requests.post(f'{links.MAIN}{api}', data=account)
        assert response.json()['message'] == code, f'Респонс выдал ошибку с {response.json()["message"]}'

    # если авторизоваться под несуществующим пользователем, запрос возвращает ошибку
    @allure.title('11. если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    @pytest.mark.parametrize('api, code, account_value, value', [
        (data.METHOD_CODE[0]['login'], 'Учетная запись не найдена', 'login', 'qwerty')
    ])
    def test_fail_with_not_create_param(self, new_account, api, code, account_value, value):
        account = new_account[0]
        account[account_value] = value
        response = requests.post(f'{links.MAIN}{api}', data=account)
        assert response.json()['message'] == code

    # успешный запрос возвращает id
    @allure.title('12. успешный запрос возвращает id')
    @pytest.mark.parametrize('api, code', [
        (data.METHOD_CODE[0]['login'], data.METHOD_CODE[0]['OK'])
    ])
    def test_inner_get_id(self, new_account, api, code):
        response = requests.post(f'{links.MAIN}{api}', data=new_account[0])
        assert response.json()['id'] == new_account[1]

    # Создание заказа
    # можно указать один из цветов — BLACK или GREY
    @allure.title('Создание заказа')
    @allure.title('13. можно указать один из цветов — BLACK или GREY')
    @pytest.mark.parametrize('api, code, colour', [
        (data.METHOD_CODE[3]['create_buy'], data.METHOD_CODE[3]['Created'], data.BUY_BLACK),
        (data.METHOD_CODE[3]['create_buy'], data.METHOD_CODE[3]['Created'], data.BUY_GREY)
    ])
    def test_colour_buy(self, new_account, api, code, colour):
        data.BUY_BLACK['firstName'] = new_account[0]['firstName']
        response = requests.post(f'{links.MAIN}{api}', json=colour)
        assert response.status_code == code
        requests.delete(f'{links.MAIN}{data.METHOD_CODE[2]["delete"]}{new_account[1]}')

    # можно указать оба цвета
    @allure.title('14. можно указать оба цвета')
    @pytest.mark.parametrize('api, code, colour', [
        (data.METHOD_CODE[3]['create_buy'], data.METHOD_CODE[3]['Created'], data.BUY_BLACK_AND_GREY)
    ])
    def test_colour_black_and_grey(self, new_account, api, code, colour):
        data.BUY_BLACK['firstName'] = new_account[0]['firstName']
        response = requests.post(f'{links.MAIN}{api}', json=colour)
        assert response.status_code == code
        requests.delete(f'{links.MAIN}{data.METHOD_CODE[2]["delete"]}{new_account[1]}')

    # можно совсем не указывать цвет
    @allure.title('15. можно не указывать цвет')
    @pytest.mark.parametrize('api, code, colour', [
        (data.METHOD_CODE[3]['create_buy'], data.METHOD_CODE[3]['Created'], data.BUY_NOT_COLOUR)
    ])
    def test_colour_black_and_grey(self, new_account, api, code, colour):
        data.BUY_BLACK['firstName'] = new_account[0]['firstName']
        response = requests.post(f'{links.MAIN}{api}', json=colour)
        assert response.status_code == code
        requests.delete(f'{links.MAIN}{data.METHOD_CODE[2]["delete"]}{new_account[1]}')

    # тело ответа содержит track
    @allure.title('16. тело ответа содержит track')
    @pytest.mark.parametrize('api, code, colour', [
        (data.METHOD_CODE[3]['create_buy'], 'track', data.BUY_NOT_COLOUR)
    ])
    def test_colour_black_and_grey(self, new_account, api, code, colour):
        data.BUY_BLACK['firstName'] = new_account[0]['firstName']
        response = requests.post(f'{links.MAIN}{api}', json=colour)
        assert code in response.text
        requests.delete(f'{links.MAIN}{data.METHOD_CODE[2]["delete"]}{new_account[1]}')

    # Проверь, что в тело ответа возвращается список заказов
    @allure.title('17. в тело ответа возвращается список заказов')
    @pytest.mark.parametrize('api, code, colour', [
        (data.METHOD_CODE[3]['create_buy'], 'track', data.BUY_NOT_COLOUR)
    ])
    def test_colour_black_and_grey(self, new_account, api, code, colour):
        data.BUY_BLACK['firstName'] = new_account[0]['firstName']
        response = requests.post(f'{links.MAIN}{api}', json=colour)
        id_track = response.json()['track']
        track = requests.get(f'{links.MAIN}{data.METHOD_CODE[4]["get_buy"]}{id_track}')
        assert type(track.json()) == dict
        requests.delete(f'{links.MAIN}{data.METHOD_CODE[2]["delete"]}{new_account[1]}')

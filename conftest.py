import pytest
import requests
import data
import links
from pages import new_log_pass


@pytest.fixture()
def new_account():
    data_account = new_log_pass.register_new_courier_and_return_login_password()
    id_account = requests.post(f'{links.MAIN}{data.METHOD_CODE[0]["login"]}', data=data_account)
    id_ele = id_account.json()['id']
    data.account = id_account
    data.id_account = id_ele
    return data_account, id_ele



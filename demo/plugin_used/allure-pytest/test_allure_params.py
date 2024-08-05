from os.path import basename, expanduser

import allure
import pytest


@pytest.mark.parametrize("login", [
    "johndoe",
    "johndoe@example.com",
])
# @allure.title("Test Authentication (as {login})") # 将参数纳入标题
def test_authentication(login):
    ...


def test_no_dynamic_parameter():
    ...


def test_authentication_with_empty_login():
    allure.dynamic.parameter("login", "(空)")
    ...


@pytest.mark.parametrize("ssh_key", [
    expanduser("~/.ssh/id_rsa1"),
    expanduser("~/.ssh/id_rsa2"),
    expanduser("~/.ssh/id_rsa3"),
])
def test_authentication_with_ssh_key(ssh_key):
    allure.dynamic.parameter("ssh_key", basename(ssh_key))
    ...

import pytest


@pytest.fixture()
def error_setup():
    raise Exception("这是一个错误")


def test_pass():
    """用例通过"""
    assert True


def test_fail():
    """用例失败"""
    assert False


def test_error(error_setup):
    """用例错误"""
    pass


@pytest.mark.skip(reason="这是一个跳过的用例")
def test_skip():
    """用例跳过"""
    assert True

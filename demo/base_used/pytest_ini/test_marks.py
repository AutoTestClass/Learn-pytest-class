import pytest
from time import sleep


@pytest.mark.slow
def test_slow():
    sleep(3)


@pytest.mark.high
def test_check_login():
    assert True


@pytest.mark.slow
@pytest.mark.high
def test_more_mark():
    assert True


def test_no_mark():
    assert True

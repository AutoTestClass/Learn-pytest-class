import pytest
from time import sleep


@pytest.fixture(scope="class")
def clearenv_one():
    pass


@pytest.fixture(scope="class")
def clearenv_two():
    pass


class TestClassOne:

    def test_one(self, clearenv_one):
        sleep(2)

    def test_two(self, clearenv_one):
        sleep(3)


class TestClassTwo:

    def test_three(self, clearenv_two):
        sleep(4)

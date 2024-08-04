import pytest


@pytest.fixture
def cleanenv():
    raise OSError("This is an OSError")


def test_error():
    with open("abc.txt") as f:
        pass


def test_fail():
    assert 2 + 2 == 3


def test_fixture_error(cleanenv):
    pass


class TestClass:

    @classmethod
    def setup_class(cls):
        raise OSError("This is an OSError")

    def test_case(self):
        assert True

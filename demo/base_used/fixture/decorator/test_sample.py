import pytest


@pytest.fixture()
def init_env():
    print("init env...")
    return True


def test_case(init_env, clean_env):
    if init_env is True:
        print("exe test case")

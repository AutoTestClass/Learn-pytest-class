import pytest


@pytest.fixture(scope="session")
def my_base_url():
    return "https://httpbin.org"

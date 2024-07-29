import pytest


@pytest.fixture
def clearenv():
    print("\n setUp")

    yield

    print("\n tearDown")

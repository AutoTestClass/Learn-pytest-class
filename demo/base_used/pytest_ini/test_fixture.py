import pytest
from time import sleep


# 使用 pytest.ini 配置代替下面的代码
# pytestmark = pytest.mark.usefixtures("clearenv")

@pytest.fixture
def clearenv():
    print("\n setUp")

    yield

    print("\n tearDown")


def test_case():
    print("this is case")
    assert True

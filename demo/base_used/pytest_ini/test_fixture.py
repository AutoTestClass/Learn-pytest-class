import pytest
from time import sleep


# 使用 pytest.ini 配置代替下面的代码
# pytestmark = pytest.mark.usefixtures("clearenv")  # 只作用于当前文件下面的用例


@pytest.fixture
def clearenv():
    print("\n setUp")
    yield
    print("\n tearDown")


def test_one():
    print("this is case")
    assert True


def test_two():
    print("this is case")
    assert True

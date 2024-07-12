import pytest


class Counter:
    """简单的计数器类"""

    def __init__(self):
        self.value = 0

    def increment(self):
        """+1"""
        self.value += 1

    def get_value(self):
        """获取value"""
        return self.value


@pytest.fixture
def counter():
    # setup 部分
    c = Counter()
    print("setup value-->", c.value)

    yield c

    # 当 counter() 不被调用之后执行
    c.value = 0  # 在测试完成后重置计数器
    print("teardown c.value-->", c.value)


# 使用 counter fixture 的测试函数
def test_counter_increment(counter):
    print("exe test_counter_increment")
    assert counter.get_value() == 0
    counter.increment()
    assert counter.get_value() == 1
    counter.increment()
    assert counter.get_value() == 2

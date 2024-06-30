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
    c = Counter()
    yield c
    c.value = 0  # 在测试完成后重置计数器
    print("end c.value-->", c.value)


# 使用 counter fixture 的测试函数
def test_counter_increment(counter):
    assert counter.get_value() == 0
    counter.increment()
    assert counter.get_value() == 1
    counter.increment()
    assert counter.get_value() == 2

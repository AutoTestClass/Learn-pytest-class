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
def counter(request):
    c = Counter()
    print("setup c.value-->", c.value)

    def reset_counter():
        c.value = 0  # 重置vlaue值 = 0
        print("teardown c.value-->", c.value)

    request.addfinalizer(reset_counter)  # 注册清理函数

    return c


# 使用 counter fixture 的测试函数
def test_counter_increment(counter):
    print("exe test_counter_increment")
    assert counter.get_value() == 0
    counter.increment()
    assert counter.get_value() == 1
    counter.increment()
    assert counter.get_value() == 2

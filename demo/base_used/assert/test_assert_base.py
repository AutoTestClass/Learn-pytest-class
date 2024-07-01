"""
test_assert_base.py
功能：用于计算a与b 相加的和
"""


def add(a, b):
    return a + b


# 功能：用于判断素数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        return True


# 测试相等
def test_add_1():
    assert add(3, 4) == 7


# 测试不相等
def test_add_2():
    assert add(17, 22) != 50


# 测试小于或等于
def test_add_3():
    assert add(17, 22) <= 50


# 测试大于或等于
def test_add_4():
    assert add(17, 22) >= 38


# 测试包含
def test_in():
    a = "hello"
    b = "he"
    assert b in a


# 测试不包含
def test_not_in():
    a = "hello"
    b = "hi"
    assert b not in a


# 判断是否为True
def test_true_1():
    assert is_prime(13)


# 判断是否为True
def test_is_true():
    assert is_prime(7) is True


# 判断是否为False
def test_is_false():
    assert is_prime(8) is False


# 判断是否不为True
def test_not_true():
    assert not is_prime(4)


# 判断是否不为True
def test_is_not_true():
    assert is_prime(6) is not True


# 判断是否不为False
def test_is_not_false():
    assert is_prime(7) is not False

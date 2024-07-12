def func(x):
    """被测函数"""
    return x + 1


def test_answer():
    """测试函数"""
    assert func(3) == 5


class TestClass:
    """测试类"""

    def test_one(self):
        """测试方法"""
        x = "this"
        print("assert h in this..")
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")

    
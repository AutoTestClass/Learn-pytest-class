# content of test_assert_more.py
import pytest


def f():
    return 7


def test_f():
    """自定义错误信息"""
    assert f() % 2 == 0, "value was odd, should be even"


def myfunc():
    raise ValueError("Exception 123 raised")


def test_match():
    """匹配异常错误信息"""
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()


def test_zero_division():
    """断言异常类型 """
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_recursion_depth():
    """断言异常信息 -- 最大递归 """
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()

        f()
        assert "maximum recursion" in str(excinfo.value)


def test_set_comparison():
    """断言组 - set 比较"""
    # 一般情况，断言第一个失败，不会走到第二个断言
    # print("assert 1")
    # assert 1 == 2
    # print("assert 2")
    # assert 2 == 2

    # set()断言可以识别列表中的所有差异。
    set11 = set(["身高", "年龄", "性别", "体重"])
    set22 = set(["身材", "年龄", "性名", "体重"])
    assert set11 == set22

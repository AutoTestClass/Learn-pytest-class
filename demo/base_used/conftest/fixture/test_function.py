"""
说明：function_scope_fixture 只是确每个函数只被执行一次
"""


def test_function_monkey(function_scope_fixture):
    print("monkey dance...")
    assert function_scope_fixture == "function scope fixture"


def test_function_lion(function_scope_fixture):
    print("lion Drilling ring ...")
    assert function_scope_fixture == "function scope fixture"

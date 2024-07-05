"""
说明：module_scope_fixture 只是确保文件下面只被执行一次
"""


def test_one():
    assert True


def test_two(module_scope_fixture):
    assert module_scope_fixture == "module scope fixture"


def test_three(module_scope_fixture):
    assert module_scope_fixture == "module scope fixture"


def test_four():
    assert True

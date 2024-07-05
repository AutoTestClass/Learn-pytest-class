import pytest


@pytest.fixture
def function_scope_fixture():
    """
    function fixture
    """
    print("\n开始登台")
    yield "function scope fixture"
    print("\n谢幕退出")


@pytest.fixture(scope="class")
def class_scope_fixture():
    """
    class fixture
    """
    print("\n动物歌唱比赛开始")
    yield "class scope fixture"
    print("\n动物歌唱比赛结束")


@pytest.fixture(scope="module")
def module_scope_fixture():
    """
    module fixture
    """
    print("\n动物表演开始")
    yield "module scope fixture"
    print("\n动物表演结束")


@pytest.fixture(scope="session")
def session_scope_fixture():
    """
    session fixture
    """
    print("\n欢迎进入动物园")
    yield "session scope fixture"
    print("\n下次再来动物园")

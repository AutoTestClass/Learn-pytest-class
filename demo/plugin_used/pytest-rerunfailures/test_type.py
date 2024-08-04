def test_pass():
    """这个测试会成功"""
    assert True


def test_always_fail():
    """这个测试总是失败，并且抛出的是TypeError，应该被重新运行"""
    raise TypeError("This is a TypeError")


def test_assert_error():
    """这个测试失败时抛出AssertionError，根据配置不应该被重新运行"""
    assert False, "This is an AssertionError"


def test_os_error():
    """这个测试失败时抛出OSError，根据配置也不应该被重新运行"""
    raise OSError("This is an OSError")


def test_runtime_error():
    """这个测试失败时抛出RuntimeError，应该被重新运行"""
    raise RuntimeError("This is a RuntimeError")

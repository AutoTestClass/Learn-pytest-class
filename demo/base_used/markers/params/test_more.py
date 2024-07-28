import pytest


@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y ", [2, 3])
def test_foo(x, y):
    pass

import pytest


@pytest.mark.parametrize("id, str", [
    (1, "hello"),
    (2, "你好")
])
def test_eval(id, str):
    pass

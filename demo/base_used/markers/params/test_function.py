import pytest


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("3+5", 8),
        ("6*9", 42),
        ("2+4", 6),
        ("用例1", "恭喜你，支付成功，你的支付订单号是：87598134759")
    ],
    ids=["001", "002", "003", "004"]
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected

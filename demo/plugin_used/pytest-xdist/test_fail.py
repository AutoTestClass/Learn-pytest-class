from random import randint


def test_pass():
    pass


def test_fail():
    num = randint(2, 2)
    print(f"num:{num}")
    assert num == 2

import sys
import pytest


@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    assert 0


@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    assert 1 == 2


@pytest.mark.skipif(sys.version_info > (3, 10), reason="requires python3.10 or higher→")
def test_skip_if_function():
    assert 1 == 2


def valid_config():
    return False


def test_function():
    if not valid_config():
        pytest.skip("unsupported configuration")
    print("exe test function")


@pytest.mark.xfail
def test_fail():
    assert 1 == 1

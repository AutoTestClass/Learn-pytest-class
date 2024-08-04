import sys
import pytest


@pytest.mark.flaky(reruns=2)
def test_example_one():
    import random
    assert random.choice([True, False])


@pytest.mark.flaky(reruns=2, reruns_delay=2)
def test_example_two():
    import random
    assert random.choice([True, False])


@pytest.mark.flaky(reruns=5, condition=sys.platform.startswith("win32"))
def test_example_three():
    import random
    assert random.choice([True, False])


@pytest.mark.flaky(rerun_except="AssertionError")
def test_example_four():
    raise AssertionError()


@pytest.mark.flaky(only_rerun=["AssertionError", "ValueError"])
def test_example_five():
    raise AssertionError()

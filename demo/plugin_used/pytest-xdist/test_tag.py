import pytest


@pytest.mark.xdist_group(name="group1")
def test1():
    pass


@pytest.mark.xdist_group(name="group2")
def test2():
    pass


class TestA:
    @pytest.mark.xdist_group("group1")
    def test3(self):
        pass

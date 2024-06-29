# import pytest
#
#
# @pytest.fixture()
def init_env():
    print("init env...")
    return True


def test_case(init_env):
    ret = init_env
    if ret is True:
        print("exe test case")


if __name__ == '__main__':
    ie = init_env()
    test_case(init_env=ie)

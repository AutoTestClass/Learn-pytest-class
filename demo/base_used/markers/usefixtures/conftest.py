import os
import tempfile
import pytest


@pytest.fixture
def cleandir():
    with tempfile.TemporaryDirectory() as newpath:
        old_cwd = os.getcwd()
        print("新目录", newpath)
        os.chdir(newpath)
        yield
        print("当前目录", old_cwd)
        os.chdir(old_cwd)

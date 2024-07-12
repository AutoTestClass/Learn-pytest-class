import os
import pytest


@pytest.mark.usefixtures("cleandir")
class TestDirectoryInit:

    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        print("current dir", os.listdir(os.getcwd()))
        with open("myfile.txt", "w", encoding="utf-8") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []

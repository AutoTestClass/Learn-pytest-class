# run.py
import pytest

if __name__ == '__main__':
    pytest.main()
    # pytest.main(["-s"])
    # pytest.main(["-x"])
    # pytest.main(["-v"])
    # pytest.main(["-q"])
    # pytest.main(["--no-header"])
    # pytest.main(["--no-summary"])
    # pytest.main(["--no-header", "--no-summary"])  # 多个参数一起用。
    # pytest.main(["-qs", "test_sample.py"])

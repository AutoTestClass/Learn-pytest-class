# myplugin.py

# 这是 pytest 的一个钩子函数，它会在每个测试函数之前被调用
def pytest_runtest_setup(item):
    print(f"\nSetting up for test: {item.name}")


# 这是 pytest 的一个钩子函数，它会在每个测试函数之后被调用
def pytest_runtest_teardown(item):
    print(f"\nTearing down after test: {item.name}")

def pytest_runtest_setup(item):
    #  called  for  running  each  test  in   'a'  directory
    print(f"setting  up: {item}")

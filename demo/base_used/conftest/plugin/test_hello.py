def test_hello_name(pytestconfig):
    name = pytestconfig.getoption("name")
    assert name != "None"
    print(f"hello {name}")

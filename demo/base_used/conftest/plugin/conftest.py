def pytest_addoption(parser):
    """
    添加命令行参数
    :param parser:
    :return:
    """
    parser.addoption("--name", action="store", default="None", help="say hello")

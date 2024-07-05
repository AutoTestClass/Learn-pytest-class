import pytest


def pytest_configure(config):
    """
    在测试运行开始之前调用，可以用来修改 pytest 的配置。
    :param config:
    :return:
    """
    print("Configuring pytest")


def pytest_unconfigure(config):
    """
    在测试运行结束后调用，用于清理资源。
    :param config:
    :return:
    """
    print("Unconfiguring pytest")


def pytest_collection_modifyitems(session, config, items):
    """
    在收集到所有测试用例之后调用，可以用来修改或重新排序测试用例。
    :param session:
    :param config:
    :param items:
    :return:
    """
    print("Modifying collected items")


def pytest_runtest_setup(item):
    """
    在每个测试用例运行之前调用。
    :param item:
    :return
    """
    print(f"Setting up {item.name}")


def pytest_runtest_call(item):
    """
    在每个测试用例调用时执行。
    :param item:
    :return:
    """
    print(f"Calling test {item.name}")


def pytest_runtest_teardown(item):
    """
    在每个测试用例执行后调用。
    :param item:
    :return:
    """
    print(f"Tearing down {item.name}")


def pytest_sessionstart(session):
    """
    在测试会话开始时调用。
    :param session:
    :return:
    """
    print("Session started")


def pytest_sessionfinish(session, exitstatus):
    """
    在测试会话结束时调用。
    :param session:
    :param exitstatus:
    :return:
    """
    print("Session finished")


def pytest_addoption(parser):
    """
    用于向 pytest 添加命令行选项。
    :param parser:
    :return:
    """
    parser.addoption("--myoption", action="store", default="default", help="My custom option")


def pytest_report_header(config):
    """
    用于在测试报告的头部添加自定义信息。
    :param config:
    :return:
    """
    return "My custom report header"


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """
    用于在测试报告的终端总结部分添加自定义信息。
    :param terminalreporter:
    :param exitstatus:
    :param config:
    :return:
    """
    terminalreporter.write_line("My custom terminal summary")

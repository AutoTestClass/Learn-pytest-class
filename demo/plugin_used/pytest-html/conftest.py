import pytest
import logging
from selenium.webdriver import Chrome

# driver = Chrome()
# driver.get("https://www.baidu.com")
# # ...
# driver.save_screenshot("./baidu.png")
# driver.get_screenshot_as_base64()

from datetime import datetime


def pytest_configure(config):
    # 配置日志 debug info warn error
    logging.basicConfig(level=logging.DEBUG)


def pytest_html_report_title(report):
    report.title = "xx项目自动化测试报告!"


# @pytest.fixture(scope="session", autouse=True)
# def browser():
#     global driver
#     driver = Chrome()  # 集成了浏览器驱动 chromedriver.exe
#
#     yield driver
#
#     driver.quit()


def pytest_html_results_table_header(cells):
    """描述和运行时间-表头"""
    cells.insert(2, "<th>描述</th>")
    cells.insert(3, '<th class="sortable time" data-column-type="time">运行时间</th>')


def pytest_html_results_table_row(report, cells):
    """描述和运行时间-表格"""
    cells.insert(2, f"<td>{report.description}</td>")
    cells.insert(3, f'<td class="col-time">{datetime.utcnow()}</td>')


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    用于向测试用例中添加用例的开始时间、内部注释，和失败截图等.
    :param item:
    """
    # global driver
    # pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    # extra = getattr(report, 'extra', [])
    # if report.when == 'call' or report.when == "setup":
    #     xfail = hasattr(report, 'wasxfail')
    #     if (report.skipped and xfail) or (report.failed and not xfail):
    #         img_base64 = "data:image/jpg;base64," + driver.get_screenshot_as_base64()
    #         if img_base64:
    #             html = '<div><img src="%s" align="right" style="width:304px;height:228px;" class="img"/></div>' % img_base64
    #             extra.append(pytest_html.extras.html(html))
    #     report.extras = extra

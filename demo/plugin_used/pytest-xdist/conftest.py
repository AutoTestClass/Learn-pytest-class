import pytest
import random


@pytest.fixture()
def user_account(worker_id):
    """在每个 xdist 工作进程中使用不同的账户"""
    print("worker id", worker_id)
    if worker_id == "gw0":
        return "tom"
    elif worker_id == "gw1":
        return "jack"
    else:
        return "master"


@pytest.fixture(scope="session", autouse=True)
def session_data(tmp_path_factory, worker_id):
    data = random.randint(1, 9999)
    with open(f"{data}.txt", "w") as f:
        f.write("")
    return data


@pytest.fixture(scope="session", autouse=True)
def create_unique_database(testrun_uid):
    """为特定的测试运行创建一个唯一的数据库"""
    database_url = f"psql://myapp-{testrun_uid}"
    return database_url

# from selenium import webdriver
# @pytest.fixture(scope="session")
# def selenium_session():
#     """Fixture to create and return a shared Selenium session."""
#     driver = webdriver.Edge()
#     yield driver
#     # Teardown code, if needed
#     driver.quit()
#
#
# @pytest.fixture()
# def browser(selenium_session):
#     """Fixture to provide Selenium driver instance using the shared session."""
#     yield selenium_session
#

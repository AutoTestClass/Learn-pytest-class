import logging


def pytest_configure(config):
    # 配置日志  
    logging.basicConfig(level=logging.INFO)

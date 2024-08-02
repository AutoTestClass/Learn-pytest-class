import logging

# 配置logging  
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


def test_something():
    # 条件：1. 日志级别大于等于 warning , 2. 用例必须错误/失败。
    logger.warning("This is a warning message")
    # 这里可能有一些断言，如果失败，上面的日志会在失败报告中显示  
    assert 1 == 2

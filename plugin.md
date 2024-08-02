## 插件使用

pytest的插件非常的多，截止目前将近 1500 个插件。

Pytest Plugin List: https://docs.pytest.org/en/stable/reference/plugin_list.html

注：这些插件是PyPI上可用的pytest插件的自动编译。它包括名称以`pytest-`或`pytest_`开头的PyPI项目，以及一些手动选择的项目。归类为非活动的包不包括在内。

这么多插件肯定是良莠不齐的，也并不是所有功能都会用得到的，我们这里挑选一些最为常用的介绍其使用。


### pytest-html

pytest-HTML是pytest的一个插件，它为测试结果生成HTML报告。

####  安装与使用

**安装：**

```shell
> pip install pytest-html
```

**使用**

* 使用示例

```py
import pytest


def test_pass():
    """用例通过"""
    assert True


def test_fail():
    """用例失败"""
    assert False


def test_error():
    """用例错误"""
    raise Exception("这是一个错误")


@pytest.mark.skip(reason="这是一个跳过的用例")
def test_skip():
    """用例跳过"""
    assert True
```

* 运行结果

```py
> pytest --html=report.html
```

* 查看报告

![](./image/pytest-html.png)


#### HTML报告支持log

默认情况下我们无法将 log 日志信息打印到报告中，但是，大多数时候我们需要在报告中看log日志信息。

可以通过下面的配置实现这个功能呢。

* pytest.ini 配置日志格式

```ini
[pytest]
log_format = %(asctime)s %(levelname)s %(message)s
log_date_format = %Y-%m-%d %H:%M:%S
```

* conftest.py 配置日志级别

```py
import logging


def pytest_configure(config):
    # 配置日志  
    logging.basicConfig(level=logging.INFO)
```

* 测试用例中使用日志

```py
# test_log.py

import logging


def test_example():
    logging.info("这是一条测试用例的日志信息")
    logging.warning("这是一条告警信息")
```


* 运行结果

```py
> pytest --html=report.html test_log.py
```

* 查看报告截图

![](./image/pytest-html-log.png)

#### HTML报告支持截图

默认情况下我们无法将截图信息打印到报告中，但是，大多数时候我们需要在报告中看截图信息。

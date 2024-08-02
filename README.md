# Learn-pytest-class

📺[B站视频课程](https://space.bilibili.com/524416851/channel/collectiondetail?sid=3348861)，正在同步更新中~~！

## 前言

我们在学习自动化测试的时候，核心就是学习三个技术：

* 编程语言
* 单元测试框架 ⭐︎
* 测试库

`pytest` 是一个 Python 第三方的开源测试框架，因为其简单易用、功能强大，正在变得越来越流行。

本课程将全面的介绍 `pytest`的使用，从`基本使用`、`扩展插件使用`，以及`插件开发` 三个层次介绍。

* google趋势

![](./image/trends.png)

### pytest发展简史

以下是 `pytest` 单元测试框架的发展历史：

- **2004年**: Holger Krekel（霍尔格·克雷克尔） 创建了 `sdt` 包。`sdt`
  最初是一个集合工具和库，旨在帮助开发者更高效地编写测试代码和脚本。`sdt` 包包含了多种实用工具，例如用于文件操作、路径管理、*
  *测试执行** 等功能。这些工具设计上都力求简洁和高效，以提高开发者的生产力。
  其中，`sdt`集成了`py.test`。它最初作为 `sdt` 库的一部分推出，旨在提供比标准库中的 unittest 更为灵活和简单的测试工具。

- **2005年**：为了更好地反映包的用途和功能，Holger Krekel 决定将 `sdt` 包更名为 `py`。更名后的 `py`
  包不仅保留了原有的功能，还在此基础上进行了扩展和改进。py 包逐渐成为一个更加全面和成熟的工具集合。

- **2007年**：Holger Krekel 从 py 库中分离出 py.test，作为独立的 `pytest` 项目继续发展。这个分离使得 `pytest`
  得以专注于测试功能的增强和优化。

- **2011年**：推出了插件机制，允许用户通过插件扩展 `pytest` 的功能。这一机制使得 `pytest` 成为一个高度可扩展的测试框架。

- **2016年**：发布的 pytest 3.0 版本开始，正式将 `py.test` 命令更名为 `pytest` 。虽然在此之前，`py.test`
  一直是推荐的命令行调用方式，但为了统一命名并避免混淆，从 3.0 版本开始，官方建议使用 `pytest` 命令。

- **2019年**：`pytest` 获得了 Python 软件基金会的资助，用于进一步改进和推广该项目。

- **现在**：``pytest``已经变得越来越流行，我们可以在许多Python项目中看到`pytest`的身影。在自动化测试领域也得到了广泛的应用。

![](./image/history.png)

### pytest优点

`pytest` 作为 Python的第三方单元测试框架，相较于Python集成的`unittest` 有以下几个主要优点：

1. **更简洁的测试代码**：
    - `pytest` 直接创建测试函数使用，断言方法也可以直接使用 `assert` 语句。这使得测试代码更加直观和简洁。

2. **自动发现测试**：
    - `pytest` 命令能够自动发现符合特定命名模式的测试函数和测试类（通常以 `test_` 开头的函数和 `Test`
      开头的类），这使得运行测试也更加简单，直接在测试目录下执行`pytest`命令，可以不用跟任何参数。

3. **conftest.py文件**：
    - `pytest` 提供了 `conftest.py` 文件，是`pytest`中一个强大且灵活的配置工具，用于定义 fixture、自定义 hook
      函数、添加命令行选项和共享测试代码。

4. **丰富的插件生态**：
    - `pytest` 拥有强大的插件系统，允许用户轻松地扩展其功能。社区贡献了许多有用的插件，如 `pytest-cov`
      （用于代码覆盖率）、`pytest-html`（用于生成HTML报告）、`pytest-xdist`（用于分布式执行用例）等，极大地增强了 `pytest` 的适用性。

总结，`pytest` 在简洁性、灵活性和功能性方面表现优秀，这也是为什么 `pytest` 能够在 Python 开发者社区中迅速流行的原因。

## 基本使用

### 安装

最新`pytest 8.2.2`支持Python版本:

* Python 3.8+
* PyPy3

通过pip命令安装。

```shell
$ pip install -U pytest
```

查看`pytest`版本。

```shell
$ pytest --version
pytest 8.2.2
```

### 基本例子

```py
# test_sample.py

def func(x):
    """被测函数"""
    return x + 1


def test_answer():
    """测试函数"""
    assert func(3) == 5


class TestClass:
    """测试类"""

    def test_one(self):
        """测试方法"""
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")

```

**代码说明**

1. 我们可以直接创建测试函数，例如`test_answer()`，也可以创建测试类`TestClass` 和测试方法`test_one()`、`test_two()`。

2. 直接使用Python提供的`assert` 语句进行断言，方法用更加简洁，当然，这个有利有弊。

### 运行测试（默认发现）

pytest 运行测试有两种方式：`pytest` 命令 和 `pytest.main()` 方法。

#### pytest命令

在测试目录下使用`pytest`命令，`pytest`命令会自动查找当前目录下的用例。

__直接执行__

```shell
$  pytest
================================= test session starts ===============================
platform win32 -- Python 3.11.9, pytest-8.2.2, pluggy-1.5.0
rootdir: D:\github\AutoTestClass\Learn-pytest-class\demo\base_used\sample
collected 3 items

test_sample.py F.F                                                    [100%]

================================= FAILURES ==========================================
_________________________________ test_answer _______________________________________

    def test_answer():
        """测试函数"""
>       assert func(3) == 5
E       assert 4 == 5
E        +  where 4 = func(3)

test_sample.py:8: AssertionError
_________________________________ TestClass.test_two ________________________________

self = <test_sample.TestClass object at 0x000001E2A0505690>

    def test_two(self):
        x = "hello"
>       assert hasattr(x, "check")
E       AssertionError: assert False
E        +  where False = hasattr('hello', 'check')

test_sample.py:21: AssertionError
============================== short test summary info =============================
FAILED test_sample.py::test_answer - assert 4 == 5
FAILED test_sample.py::TestClass::test_two - AssertionError: assert False
============================ 2 failed, 1 passed in 0.19s ===========================

```

__跟参数执行__

```shell
$ pytest -s

$ pytest -x

$ pytest -v

$ pytest -q

$ pytest --no-header

$ pytest --no-summary

$ pytest --no-header --no-summary  # 多个参数一起用
```

- `-s`：--capture=no 的简写，可以打印`print()`信息。
- `-x`/`--exitfirst`：在第一个错误或失败的测试上立即退出。
- `-v`/ `--verbose`：增加详细输出。
- `-q`/ `--quiet`：减少详细输出。
- `--no-header`：禁用头部信息。
- `--no-summary`：禁用总结信息，不再显示具体的报错。

#### main方法

我们需要创建一个Python文件，使用`pytest.main()`方法执行用例。

```python
# run.py
import pytest

if __name__ == '__main__':
    pytest.main()
```

__执行文件__

```shell
$ python run.py

================================== test session starts =================================
platform win32 -- Python 3.11.9, pytest-8.2.2, pluggy-1.5.0
rootdir: D:\github\AutoTestClass\Learn-pytest-class\demo\base_used\sample
collected 3 items

test_sample.py F.F                                                              [100%]

======================================= FAILURES =======================================
______________________________________ test_answer _____________________________________

    def test_answer():
        """测试函数"""
>       assert func(3) == 5
E       assert 4 == 5
E        +  where 4 = func(3)

test_sample.py:8: AssertionError
__________________________________ TestClass.test_two _________________________________

self = <test_sample.TestClass object at 0x0000018FF6507510>

    def test_two(self):
        x = "hello"
>       assert hasattr(x, "check")
E       AssertionError: assert False
E        +  where False = hasattr('hello', 'check')

test_sample.py:22: AssertionError
============================== short test summary info ================================
FAILED test_sample.py::test_answer - assert 4 == 5
FAILED test_sample.py::TestClass::test_two - AssertionError: assert False
============================= 2 failed, 1 passed in 0.08s =============================
```

__使用参数__

在文件中依然可以使用参数。通过list 设置多个参数。

```python
# run.py
import pytest

if __name__ == '__main__':
    # pytest.main(["-s"])
    # pytest.main(["-x"])
    # pytest.main(["-v"])
    # pytest.main(["-q"])
    # pytest.main(["--no-header"])
    # pytest.main(["--no-summary"])
    pytest.main(["--no-header", "--no-summary"])  # 多个参数一起用。
```

### 运行测试（控制粒度）

除了默认`pytest`发现测试用例并执行，更多时候，我们需要控制测试用例的颗粒度，就是说，我们仅仅想执行某个`目录`或`文件`
用例，甚至是某个`类`或`方法`。

**目录结构:**

```
└───sample
|   └───test_sample.py
```

#### 用例粒度

以下是单个粒度的执行。

```shell
$ pytest sample   # 目录

$ pytest sample\test_sample.py  # 文件

$ pytest sample\test_sample.py  # 文件

$ pytest sample\test_sample.py::test_answer  # 函数

$ pytest sample\test_sample.py::TestClass  # 类

$ pytest sample\test_sample.py::TestClass::test_one  # 方法
```

#### 多个组合

有时候，我们想同时执行A文件b测试用例 和 B文件的a测试用例。`pytest`允许指定多个用例。

```shell
$ pytest sample\test_sample.py::TestClass::test_one  sample\test_sample.py::TestClass::test_two
```

🔖 `pytest 8.2` 新写法 。

显然，上面的写法有些麻烦，所以，我们可以将其放到一个文件中执行。

```txt
sample/test_sample.py::TestClass::test_one
sample/test_sample.py::test_answer
```

通过`pytest @file_name.txt`运行测试。

```shell
$ pytest @tests_to_run.txt
============================= test session starts =============================
platform win32 -- Python 3.11.9, pytest-8.2.2, pluggy-1.5.0
rootdir: D:\github\AutoTestClass\Learn-pytest-class\demo\base_used
collected 2 items / 2 deselected / 0 selected

============================ 2 deselected in 0.01s ============================
```

注明：windows `PowerShell` 不支持。可以使用`git bash`执行。

#### 筛选方法

在一个范围内通过`关键字`筛选，无疑是简单的用法。`pytest -k`参数可以实现。

为了更好的演示，我们先准备一组测试用例。

```py
# test_calculator.py

class Calculator:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b


class TestAdd:

    def test_add_int_1(self):
        cal = Calculator()
        ret = cal.add(1, 2)
        assert ret == 3

    def test_add_str_2(self):
        cal = Calculator()
        ret = cal.add("hello", "world")
        assert ret == "helloworld"


class TestSub:

    def test_sub_int_1(self):
        cal = Calculator()
        ret = cal.sub(1, 2)
        assert ret == -1

    def test_sub_float_2(self):
        cal = Calculator()
        ret = cal.sub(1.1, 2.2)
        assert ret == -1.1
```

__运行测试__

```shell
$ pytest -k add test_calculator.py
================================== test session starts ==================================
platform win32 -- Python 3.11.9, pytest-8.2.2, pluggy-1.5.0
rootdir: D:\github\AutoTestClass\Learn-pytest-class\demo\base_used\sample
collected 4 items / 2 deselected / 2 selected

test_calculator.py ..                                                    [100%]

============================= 2 passed, 2 deselected in 0.01s ============================
```

__参数说明__

- `-k EXPRESSION`：仅运行与给定子字符串表达式匹配的测试。表达式是一个 Python
  可评估的表达式，其中所有名称都将与测试名称及其父类进行子字符串匹配。例如：`-k test_method or test_other`
  匹配名称中包含 `test_method` 或 `test_other` 的所有测试函数和类，而 `-k 'not test_method'` 匹配名称中不包含 '
  test_method' 的测试。`-k 'not test_method and not test_other'`
  将排除这些匹配项。此外，关键字还会与在 `'extra_keyword_matches'` 集合中包含额外名称的类和函数，以及直接为其分配名称的函数进行匹配。匹配是不区分大小写的。

```shell
$ pytest -k add test_calculator.py  # 测试用例名称包含 “add”

$ pytest -k 'not add' test_calculator.py  # 测试用例名称不包含 “add”

$ pytest -vk 'not add and not 1' test_calculator.py # 测试用例名称不包含 “add” 并且 不包含 “1”
```

### 运行测试时间

分析测试的运行时间是比较重要的功能。`pytest` 提供了 `--durations`参数来执行。

为了更好的演示，我们先准备一组测试用例。

```py
# test_slow.py
from time import sleep


def test_sleep_one():
    """测试函数"""
    sleep(1)


def test_sleep_two():
    """测试函数"""
    sleep(2)


def test_sleep_three():
    """测试函数"""
    sleep(3)
```

__运行测试__

找最慢的1条用例。

```shell
$ pytest --durations=1
=================================== test session starts ==================================
platform win32 -- Python 3.11.9, pytest-8.2.2, pluggy-1.5.0
rootdir: D:\github\AutoTestClass\Learn-pytest-class\demo\base_used\slow
collected 3 items

test_slow.py ...                                                                [100%]

=================================== slowest 1 durations ===================================
3.00s call     test_slow.py::test_sleep_three
=================================== 3 passed in 6.03s =====================================
```

找出超过1s，最慢的2条用例。

```shell
pytest --durations=2 --durations-min=1.0
=================================== test session starts ==================================
platform win32 -- Python 3.11.9, pytest-8.2.2, pluggy-1.5.0
rootdir: D:\github\AutoTestClass\Learn-pytest-class\demo\base_used\slow
collected 3 items

test_slow.py ...                                                               [100%]

=================================== slowest 2 durations ===================================
3.00s call     test_slow.py::test_sleep_three
2.00s call     test_slow.py::test_sleep_two
=================================== 3 passed in 6.02s =====================================

```

__参数说明__

- `--durations=N`：显示最慢的N个设置/测试时长（N=0表示全部）
- `--durations-min=N`：要包含在最慢列表中的最小时长（秒）。默认：0.005。

### 运行unittest

`pytest` 支持运行unittest编写的测试用例。

```py
# test_unittest.py
from unittest import TestCase


class MyTest(TestCase):

    def test_case(self):
        self.assertEqual(2 + 2, 4)
```

__运行测试__

```shell
$ pytest -v test_unittest.py
======================================= test session starts =========================================
platform win32 -- Python 3.11.9, pytest-8.2.2, pluggy-1.5.0 -- C:\Users\fnngj\.virtualenvs\Learn-pytest-class-k2175urw\Scripts\python.exe
cachedir: .pytest_cache
rootdir: D:\github\AutoTestClass\Learn-pytest-class\demo\base_used\unit_test
collected 1 item

test_unittest.py::MyTest::test_case PASSED                                                   [100%]

========================================= 1 passed in 0.01s =========================================
```

### 测试断言 - assert

在`pytest`中，使用Python的`assert`语句进行断言。

#### 基本使用

通过一个例子演示基本用法。

```py
"""
test_assert_base.py
"""


def add(a, b):
    return a + b


# 功能：用于判断素数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        return True


# 测试相等
def test_add_1():
    assert add(3, 4) == 7


# 测试不相等
def test_add_2():
    assert add(17, 22) != 50


# 测试小于或等于
def test_add_3():
    assert add(17, 22) <= 50


# 测试大于或等于
def test_add_4():
    assert add(17, 22) >= 38


# 测试包含
def test_in():
    a = "hello"
    b = "he"
    assert b in a


# 测试不包含
def test_not_in():
    a = "hello"
    b = "hi"
    assert b not in a


# 判断是否为True
def test_true_1():
    assert is_prime(13)


# 判断是否为True
def test_is_true():
    assert is_prime(7) is True


# 判断是否为False
def test_is_false():
    assert is_prime(8) is False


# 判断是否不为True
def test_not_true():
    assert not is_prime(4)


# 判断是否不为True
def test_is_not_true():
    assert is_prime(6) is not True


# 判断是否不为False
def test_is_not_false():
    assert is_prime(7) is not False

```

__使用说明__

跟`if`语句相似，我们可以通过`assert`语句写各种判断条件。

* `==`: 等于
* `!=`: 不等于
* `>=`: 大于等于
* `<=`: 小于等于
* `is`: 是
* `not is`: 不是
* `in`: 包含
* `not in`: 不包含
* `is True`: 是`True`
* `is False`: 是`False`
* ...

#### 更多使用

* 断言，自定义异常信息

```py
def f():
    return 7


def test_f():
    """自定义错误信息"""
    assert f() % 2 == 0, "value was odd, should be even"
```

* 断言，自定义异常信息

```py
def f():
    return 7


def test_f():
    """自定义错误信息"""
    assert f() % 2 == 0, "value was odd, should be even"
```

* 断言， 异常类型

```py
import pytest


def test_zero_division():
    """断言异常类型 """
    with pytest.raises(ZeroDivisionError):
        1 / 0
```

* 断言， 匹配异常类型

```py
import pytest


def myfunc():
    raise ValueError("Exception 123 raised")


def test_match():
    """匹配异常错误信息"""
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()
```

* 断言， 异常信息

```py
import pytest


def test_recursion_depth():
    """断言异常信息 -- 最大递归 """
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()

        f()
        assert "maximum recursion" in str(excinfo.value)
```

* 断言， `set()`列表比较

```py

def test_set_comparison():
    """断言组- set 比较"""
    set11 = set(["身高", "年龄", "性别", "体重"])
    set22 = set(["身材", "年龄", "性名", "体重"])
    assert set11 == set22
```

断言`set()`列表，运行结果，可以识别：`名别`和`姓名`，`身高`和`身材`的差异。

```
....

    def test_set_comparison():
        set11 = set(["身高", "年龄", "性别", "体重"])
        set22 = set(["身材", "年龄", "性名", "体重"])
>       assert set11 == set22
E       AssertionError: assert {'体重', '年龄', '性别', '身高'} == {'体重', '年龄', '性名', '身材'}
E
E         Extra items in the left set:
E         '身高'
E         '性别'
E         Extra items in the right set:
E         '性名'
E         '身材'
E         Use -v to get more diff
```

### 测试脚手架 - fixture

Pytest fixture被设计成显式的、模块化的和可扩展的。

在测试中，fixture为测试提供了一个定义的、可靠的和一致的上下文。这可以包括环境(例如配置了已知参数的数据库)或内容(
例如数据集)。

fixture定义了构成测试安排阶段的步骤和数据(参见测试剖析)。在`pytest`
中，它们是您定义的用于此目的的函数。它们也可以用来定义测试的行为阶段;对于设计更复杂的测试，这是一种强大的技术。由fixture设置的服务、状态或其他操作环境由测试函数访问。

#### xUnit风格的fixture

`pytest`支持类似 `unittest`风格的fixture，即 `setup`和`teardown`。

__函数fixtrue__

首先，创建`test_func.py`测试文件。

```py
# 功能函数
def multiply(a, b):
    return a * b


# =====fixtures========
def setup_module(module):
    print("setup_module================>")


def teardown_module(module):
    print("teardown_module=============>")


def setup_function(function):
    print("setup_function------>")


def teardown_function(function):
    print("teardown_function--->")


# =====测试用例========
def test_multiply_3_4():
    print('test_numbers_3_4')
    assert multiply(3, 4) == 12


def test_multiply_a_3():
    print('test_strings_a_3')
    assert multiply('a', 3) == 'aaa'
```

__代码说明__

`setup_module`/`teardown_module`: 测试`模块`级别的fixture，即 文件级别。

`setup_function`/`teardown_function`: 测试`函数`级别的fixture。

__执行测试：__

```shell
$ pytest -qs test_func.py

setup_module================>
setup_function------>
test_numbers_3_4
.teardown_function--->
setup_function------>
test_strings_a_3
.teardown_function--->
teardown_module=============>

2 passed in 0.01s

```

__方法fixture__

首先，创建`test_method.py`测试文件。

```py
# 功能函数
def multiply(a, b):
    return a * b


class TestMultiply:
    # =====fixtures========
    @classmethod
    def setup_class(cls):
        print("setup_class=========>")

    @classmethod
    def teardown_class(cls):
        print("teardown_class=========>")

    def setup_method(self, method):
        print("setup_method----->>")

    def teardown_method(self, method):
        print("teardown_method-->>")

    # =====测试用例========
    def test_numbers_5_6(self):
        print('test_numbers_5_6')
        assert multiply(5, 6) == 30

    def test_strings_b_2(self):
        print('test_strings_b_2')
        assert multiply('b', 2) == 'bb'
```

__代码说明__

`setup_class`/`teardown_class`: 测试`类`级别的fixture，需要使用`@classmethod`装饰器。

`setup_method`/`teardown_method`: 测试`方法`级别的fixture。

__执行测试：__

```shell
$ pytest -qs test_method.py

setup_class=========>
setup_method----->>
test_numbers_5_6
.teardown_method-->>
setup_method----->>
test_strings_b_2
.teardown_method-->>
teardown_class=========>

2 passed in 0.01s
```

#### `@pytest.fixture` 装饰器

在一个基本级别上，测试函数通过将它们声明为参数来请求它们所需的fixture。

当`pytest`运行测试时，它会查看该测试函数签名中的参数，然后搜索与这些参数名称相同的`fixture`。一旦`pytest`
找到它们，它就运行这些`fixture`，捕获它们返回的内容(如果有的话)，并将这些对象作为参数传递给test函数。

__基本使用__

```py
import pytest


@pytest.fixture()
def init_env():
    print("init env...")
    return True


def test_case(init_env):
    ret = init_env
    if ret:
        print("exe test case")
```

在这个例子中，`test_case` “*Requests*”了`init_env`(即`def test_case(init_env):`)，当`pytest`看到这个时，它将执行`init_env`
固定函数，并将它返回的对象作为`init_env`参数传递给`test_case`。

如果我们用手来做，大概会发生这样的情况:

```py
def init_env():
    print("init env...")
    return True


def test_case(init_env):
    ret = init_env
    if ret is True:
        print("exe test case")


if __name__ == '__main__':
    ie = init_env()
    test_case(init_env=ie)
```

__fixture请求其他fixture__

`pytest`
最大的优势之一是其极其灵活的夹具系统。它允许我们将复杂的测试需求简化为更简单和有组织的功能，我们只需要让每个功能描述它们所依赖的东西。我们将在后面进一步讨论这个问题，但是现在，这里有一个快速示例来演示`fixture`
如何使用其他`fixture`。

```py
import pytest


# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order(first_entry):
    return [first_entry]


def test_string(order):
    # Act
    order.append("b")
    # Assert
    assert order == ["a", "b"]
```

__一个`test`/`fixture`可以请求多个fixture__

测试和fixture并不局限于一次请求一个fixture。他们想要多少就可以要多少。下面是另一个快速演示的例子:

```py
import pytest


# Arrange
@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def second_entry():
    return 2


# Arrange
@pytest.fixture
def order(first_entry, second_entry):
    return [first_entry, second_entry]


# Arrange
@pytest.fixture
def expected_list():
    return ["a", 2, 3.0]


def test_string_1(order, expected_list):
    # Act
    order.append(3.0)
    # Assert
    assert order == expected_list


def test_string_2(order, expected_list):
    # Act
    order.append(4.0)
    # Assert
    assert order == expected_list
```

__自动的使用fixture__

有时，您可能希望拥有一个(甚至几个)您知道所有测试都将依赖的fixture。“自动使用”
fixture是一种方便的方法，可以使所有测试自动请求它们。这可以减少大量冗余请求，甚至可以提供更高级的fixture使用(
后面会详细介绍)。

```py
import pytest


@pytest.fixture
def first_entry():
    return "a"


@pytest.fixture
def order(first_entry):
    return []


@pytest.fixture(autouse=True)
def append_first(order, first_entry):
    return order.append(first_entry)


def test_string_only(order, first_entry):
    assert order == [first_entry]


def test_string_and_int(order, first_entry):
    order.append(2)
    assert order == [first_entry, 2]

```

在本例中，`append_first` fixture是一个自定义fixture。因为它是自动发生的，所以两个测试都是
受到它的影响，即使没有测试要求它。但这并不意味着他们不能被要求;只是事实并非如此
必要的。

__fixture范围__

fixture在第一次被测试请求时创建，并根据它们的作用域销毁:

- `function`: 默认作用域，测试结束时销毁夹具。

- `class`: 在类中最后一个测试的拆解期间，fixture被销毁。

- `module`: 在模块中最后一次测试的拆卸过程中，夹具被销毁。

- `package`: 在定义fixture的包(包括其中的子包和子目录)中的最后一个测试的拆解期间，fixture被销毁。

- `session`: 夹具在测试会话结束时被销毁。

> 涉及到`conftest.py` 文件，后面介绍到`conftest.py`时候再介绍。


__Teardown/Cleanup (Fixture的后置)__

1. 使用 `yield` 迭代器

```py
import pytest


class Counter:
    """简单的计数器类"""

    def __init__(self):
        self.value = 0

    def increment(self):
        """+1"""
        self.value += 1

    def get_value(self):
        """获取value"""
        return self.value


@pytest.fixture
def counter():
    c = Counter()
    yield c
    c.value = 0  # 在测试完成后重置计数器
    print("end c.value-->", c.value)


# 使用 counter fixture 的测试函数
def test_counter_increment(counter):
    assert counter.get_value() == 0
    counter.increment()
    assert counter.get_value() == 1
    counter.increment()
    assert counter.get_value() == 2
```

注意：在这个例子中，我们并没有真正"迭代" `counter`对象，但`yield`的使用允许我们在测试结束后执行清理代码（将counter的值重置为0）。

然而，`yield`的这种用法在创建和管理测试所需的临时资源（如数据库连接、临时文件、模拟对象等）时非常有用。

2. 直接添加`finalizer`终结器

虽然产量固定装置被认为是更干净、更直接的选择，但还有另一种选择，那就是是将`“finalizer”`
函数直接添加到测试的请求上下文对象中。它带来了与`yield` fixture类似的结果，但是需要更多的篇幅。

使用 `request.addfinalizer` 的 fixture。

```py
import pytest


class Counter:
    """简单的计数器类"""

    def __init__(self):
        self.value = 0

    def increment(self):
        """+1"""
        self.value += 1

    def get_value(self):
        """获取value"""
        return self.value


@pytest.fixture
def counter(request):
    c = Counter()

    def reset_counter():
        c.value = 0

    request.addfinalizer(reset_counter)  # 注册清理函数
    print("end c.value-->", c.value)
    return c


# 使用 counter fixture 的测试函数
def test_counter_increment(counter):
    assert counter.get_value() == 0
    counter.increment()
    assert counter.get_value() == 1
    counter.increment()
    assert counter.get_value() == 2
```

在这个例子中，当 `test_counter_increment` 测试函数执行完毕后，`reset_counter`函数会被自动调用，将计数器的值重置为
0。这与我们在前面的例子中使用 `yield` 实现的功能相同，但使用了不同的 API。


> 终结器按照先入后出的顺序执行。对于yield fixture，要运行的第一个拆装代码是从最右边的fixture，即最后一个测试参数开始的。

__Fixture参数化__

Fixture函数可以参数化，在这种情况下，它们将被多次调用，每次执行一组相关测试，即依赖于此fixture的测试。测试函数通常不需要知道它们的重新运行。fixture参数化有助于为组件编写详尽的功能测试，这些组件本身可以在其中配置多种方式。

```py
import pytest


@pytest.fixture(params=["www.baidu.com", "www.bing.com"], ids=["baidu", "bing"])
def urls(request):
    return request.param


def test_url(urls):
    url = urls
    print(f"visit - > http://{url}")
```

在这个例子中，`@pytest.fixture()`使用`params`设置两个参数，`request.param`可以将参数返回给用例。`test_url()`测试函数会被执行两次。

### 强大的`conftest.py`

`conftest.py` 是 `pytest` 框架中一个特殊的配置文件，用于定义共享的`fixtures`、`hooks`、和`插件`
，使测试代码更加简洁和可维护。它在测试目录中被自动发现和加载，提供了以下功能：

1. **Fixtures**: 可以在 `conftest.py` 中定义全局或跨文件共享的 fixtures。fixtures 是 `pytest` 提供的一种用于准备测试环境的机制。

2. **Hooks**: 允许在测试的不同阶段（例如，测试运行前、测试运行后等）执行特定的代码。可以在 `conftest.py` 中定义自定义 hooks。

3. **Plugins**: 可以在 `conftest.py` 中加载或配置 `pytest` 插件。

👉 [查看示例](./demo/base_used/conftest/)

#### 配置 fixture

在 conftest.py 中定义 fixtures，然后可以在测试文件中使用它们：

```py
import pytest


@pytest.fixture
def function_scope_fixture():
    """
    function fixture
    """
    print("\n开始登台")
    yield "function scope fixture"
    print("\n谢幕退出")

```

使用配置的fixture。

```py
"""
说明：function_scope_fixture 只是确每个函数只被执行一次
"""


def test_function_monkey(function_scope_fixture):
    print("monkey dance...")
    assert function_scope_fixture == "function scope fixture"


def test_function_lion(function_scope_fixture):
    print("lion Drilling ring ...")
    assert function_scope_fixture == "function scope fixture"
```

#### 定义 Hooks

在 conftest.py 中定义 hooks，以便在测试的不同阶段执行特定的代码：

```py
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
```

使用配置的钩子函数：

```py
# test_example.py
def test_one():
    print("running test one")
    assert True


def test_two():
    print("running test two")
    assert True
```

#### 配置 Plugins

在 conftest.py 中配置和加载 pytest 插件：

```py
def pytest_addoption(parser):
    """
    添加命令行参数
    :param parser:
    :return:
    """
    parser.addoption("--name", action="store", default="None", help="say hello")
```

使用配置的插件参数。

```py
# test_hello.py
def test_hello_name(pytestconfig):
    name = pytestconfig.getoption("name")
    assert name != "None"
    print(f"hello {name}")
```

### mark 标记

通过使用`pytest.mark`帮助你可以轻松地在测试函数上设置元数据。你可以在API参考中找到内置标记的完整列表。或者，可以使用CLI-`pytest --markers`列出所有标记，包括内置标记和自定义标记。

```shell
$ pytest --markers
```

pytest 内置的一些标记:

• `usefixtures` - 在测试函数或类上使用fixture。
• `filterwarnings` - 过滤测试函数的某些警告.
• `skip` - 总是跳过测试函数
• `skipif` - 如果满足某些条件，则跳过测试函数
• `xfail` - 如果满足某个条件，则产生“预期失败”结果。
• `parametrize` - 对同一个测试函数执行多次调用。

👉 [查看示例](./demo/base_used/markers/)

#### usefixtures

有时测试函数不直接需要访问fixture对象。例如，测试可能需要使用将空目录作为当前工作目录，否则不关心具体目录。下面是方法您可以使用标准的`tempfile`
和`pytest fixture`来实现它。

创建分为`conftest.py`文件:

```py
import os
import tempfile
import pytest


@pytest.fixture
def cleandir():
    with tempfile.TemporaryDirectory() as newpath:
        old_cwd = os.getcwd()
        os.chdir(newpath)
        yield
        os.chdir(old_cwd)
```

代码说明:

`cleandir` fixture函数用于创建一个临时目录作为当前目录使用。当用例执行完，再改回当前目录。

然后，创建测试用例 `test_setenv.py` 文件。

```py
import os
import pytest


@pytest.mark.usefixtures("cleandir")
class TestDirectoryInit:

    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        print("current dir", os.listdir(os.getcwd()))
        with open("myfile.txt", "w", encoding="utf-8") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
```

代码说明:

`@pytest.mark.usefixtures("cleandir")` 将`cleandir`
fixture函数应用于测试类。这样，在测试类中的每个测试函数都会执行`cleandir` fixture函数。

`test_cwd_starts_empty` 测试函数将创建一个临时目录作为当前目录，然后创建一个文件。

`test_cwd_again_starts_empty` 测试函数将再次创建一个临时目录作为当前目录，但此时目录为空，因为`cleandir`
fixture函数在每个测试函数执行后都会执行。

#### filterwarnings

可以使用 `@pytest.mark.filterwarnings` 向特定的测试项添加警告过滤器，更好地控制应该在测试、类甚至模块级别捕获哪些警告:

```py
import pytest
import warnings


def api_v1():
    warnings.warn(UserWarning("api v1, should use functions from v2"))
    return 1


@pytest.mark.filterwarnings("ignore:api v1")
def test_one():
    assert api_v1() == 1
```

代码说明：

这个其实很好理解，正常情况下调用 `api_v1()` 函数会报一个警告，但是用 `@pytest.mark.filterwarnings("ignore:api v1")` 忽略警告。

#### skip

你可以对无法在某些平台上运行或预计会失败的函数进行mark测试，以便pytest可以相应地处理它们，呈现测试会话的摘要，同时保持测试套件的 "
绿色"。

1. `@pytest.mark.skip`: 跳过测试函数。
2. `@pytest.mark.skipif`: 如果满足某些条件，则跳过测试函数。
3. `@pytest.mark.xfail`: 如果满足某个条件，则产生“预期失败”结果。

```py
import sys
import pytest


@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    assert 0

@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    assert 1 == 2

@pytest.mark.skipif(sys.version_info > (3, 10), reason="requires python3.10 or higher→")
def test_skip_if_function():
    assert 1 == 2

@pytest.mark.xfail
def test_fail():
    assert 1 == 1

def valid_config():
    return False

def test_function():
    if not valid_config():
        pytest.skip("unsupported configuration")
    print("exe test function")
```

#### parametrize

pytest 提供了哪些功能的参数化。

* `pytest.fixeture()` 允许对fixture函数进行参数化。--**前面已经介绍使用**
* `@pytest.mark.parameterize` 允许在测试函数或类中定义多组参数和fixture。
* `pytest_generate_tests` 允许定义自定义参数化方案或扩展。--**略**

`@pytest.mark.parametrize` 可以将同一个测试函数执行多次，并传递不同的参数。

__参数化函数__

最基本的用法，当某个用例运行步骤相同，测试数据不同时，可以使用参数化。

* 示例代码

```py
import pytest


@pytest.mark.parametrize(", expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
```

* 运行结果

```shell
> pytest -vs test_function.py

============================ test session starts =========================================
test_function.py::test_eval[3+5-8] PASSED
test_function.py::test_eval[2+4-6] PASSED
test_function.py::test_eval[6*9-42] FAILED

============================== FAILURES ==================================================
____________________________ test_eval[6*9-42] ___________________________________________

test_input = '6*9', expected = 42

    @pytest.mark.parametrize("test_input, expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
    def test_eval(test_input, expected):
>       assert eval(test_input) == expected
E       AssertionError: assert 54 == 42
E        +  where 54 = eval('6*9')

test_function.py:6: AssertionError
============================= short test summary info =====================================
FAILED test_function.py::test_eval[6*9-42] - AssertionError: assert 54 == 42
============================= 1 failed, 2 passed in 0.07s =================================
```

本例中特意设置一条测试失败的数据，进一步说明参数化之后的测试用例，测试数据之间是相互独立的。

__参数化类__

最基本的用法，当某个测试类下面的用例使用的是相同的测试数据，可以使用参数化测试类。

* 示例代码

```py
import pytest


@pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])
class TestClass:

    def test_simple_case(self, n, expected):
        assert n + 1 == expected

    def test_weird_simple_case(self, n, expected):
        assert (n * 1) + 1 == expected
```

* 运行结果

```shell
> pytest -vs test_class.py
================================== test session starts ====================================
test_class.py::TestClass::test_simple_case[1-2] PASSED
test_class.py::TestClass::test_simple_case[3-4] PASSED
test_class.py::TestClass::test_weird_simple_case[1-2] PASSED
test_class.py::TestClass::test_weird_simple_case[3-4] PASSED

=============================== 4 passed in 0.01s =========================================
```

本例中特意设置一条测试失败的数据，进一步说明参数化之后的测试用例，测试数据之间是相互独立的。

__参数化模块__

此外，pytest还支持全局的设置参数化，当然，这个全局仅限于模块，即单个.py文件。

* 示例代码

```py
import pytest

pytestmark = pytest.mark.parametrize("n,expected", [(1, 2), (3, 4)])


class TestClass:
    def test_simple_case(self, n, expected):
        assert n + 1 == expected

    def test_weird_simple_case(self, n, expected):
        assert (n * 1) + 1 == expected


def test_func_case(n, expected):
    assert n + 1 == expected
```

* 运行结果

```shell
>  pytest -vs test_global.py

================================== test session starts ====================================

test_global.py::TestClass::test_simple_case[1-2] PASSED
test_global.py::TestClass::test_simple_case[3-4] PASSED
test_global.py::TestClass::test_weird_simple_case[1-2] PASSED
test_global.py::TestClass::test_weird_simple_case[3-4] PASSED
test_global.py::test_func_case[1-2] PASSED
test_global.py::test_func_case[3-4] PASSED

=================================== 6 passed in 0.02s =====================================
```

本例中特意设置一条测试失败的数据，进一步说明参数化之后的测试用例，测试数据之间是相互独立的。

__参数化使用标记__

也可以在参数化中标记单独的测试实例，例如使用内置的`mark.xfail`。

* 示例代码

```py
import pytest


@pytest.mark.parametrize(
    "test_input,expected ",
    [
        ("3+5 ", 8), ("2+4 ", 6),
        pytest.param(" 6*9 ", 42, marks=pytest.mark.xfail)
    ],
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected
```

* 运行结果

```shell
>  pytest -vs .\test_mark.py
================================== test session starts =====================================

test_mark.py::test_eval[3+5 -8] PASSED
test_mark.py::test_eval[2+4 -6] PASSED
test_mark.py::test_eval[ 6*9 -42] XFAIL

============================== 2 passed, 1 xfailed in 0.07s ================================
```

本例中特意设置一条测试失败的数据，进一步说明参数化之后的测试用例，测试数据之间是相互独立的。

__参数化叠加__

pytest多个参数化叠加使用，产生的效果就是笛卡尔积。

* 示例代码

```py
import pytest


@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y ", [2, 3])
def test_foo(x, y):
    pass
```

* 运行结果

```shell
> pytest -vs test_more.py
================================== test session starts =====================================

test_more.py::test_foo[2-0] PASSED
test_more.py::test_foo[2-1] PASSED
test_more.py::test_foo[3-0] PASSED
test_more.py::test_foo[3-1] PASSED

================================== 4 passed in 0.01s =======================================
```

### 重新运行失败用例

pytest提供了两个命令行选项来重新运行上次调用的失败:

* `--lf`、`--last-failed` — 只重新运行失败。
* `--ff`、`--failed-first` — 先运行失败测试，然后再运行其余测试。

对于清理(通常不需要)，`--cache-clear` 选项允许在测试运行之前删除所有跨会话缓存内容。

* 示例代码

```py
import pytest


@pytest.mark.parametrize("i ", range(50))
def test_num(i):
    if i in (17, 25):
        pytest.fail("bad  luck ")
```

* 运行结果

```shell
> pytest  -qs

.................F.......F........................
====================================== FAILURES ============================================
_____________________________________ test_num[17] _________________________________________

i = 17

    @pytest.mark.parametrize("i ", range(50))
    def test_num(i):
        if i in (17, 25):
>           pytest.fail("bad  luck ")
E           Failed: bad  luck

test_50.py:7: Failed
___________________________________ test_num[25] ___________________________________________

i = 25

    @pytest.mark.parametrize("i ", range(50))
    def test_num(i):
        if i in (17, 25):
>           pytest.fail("bad  luck ")
E           Failed: bad  luck

test_50.py:7: Failed
============================ short test summary info =======================================
FAILED test_50.py::test_num[17] - Failed: bad  luck
FAILED test_50.py::test_num[25] - Failed: bad  luck
2 failed, 48 passed in 0.11s
```

在运行的当前目录下会产生一个`.pytest_cache`文件夹，里面有缓存文件。

`.pytest_cache/v/cache/lastfailed`文件记录了上次运行失败的测试用例。

```json
{
  "test_50.py::test_num[17]": true,
  "test_50.py::test_num[25]": true
}
```

**再次运行**

* 使用`--lf`参数只运行失败的用例。

```shell
> pytest --lf -qs
FF
====================================== FAILURES ===========================================
...
2 failed in 0.07s
```

* 使用`--ff`参数优先运行失败的用例。

```shell
> pytest --ff -qs
FF................................................
===================================== FAILURES ============================================
...
2 failed, 48 passed in 0.10s
```

* 使用 `--cache-clear` 参数每次运行前清理缓存。

```shell
> pytest --cache-clear
```

* 使用 `--cache-show` 参数检查用例运行的缓存。

```shell
> pytest  --cache-show

cachedir: D:\github\AutoTestClass\Learn-pytest-class\demo\base_used\rerun\.pytest_cache
---------------------------------- cache values for '*' -------------------------------
cache\lastfailed contains:
  {'test_50.py::test_num[17]': True, 'test_50.py::test_num[25]': True}
cache\nodeids contains:
  ['test_50.py::test_num[0]',
   'test_50.py::test_num[10]',
   'test_50.py::test_num[11]',
   'test_50.py::test_num[12]',
    ...
   'test_50.py::test_num[8]',
   'test_50.py::test_num[9]']
cache\stepwise contains:
  []

no tests ran in 0.01s
```

### 配置文件`pytest.ini`

在pytest中，`pytest.ini`是一个配置文件，用于配置pytest测试运行时的各种选项和行为。它可以帮助你定制化你的测试执行环境。

以下是一些常见的配置选项和作用：

#### usefixtures 配置

`usefixtures`选项允许你指定在哪些测试用例中需要使用哪些fixture。

如果要配置模块下面的所有用例使用，下面的配置：

```py
import pytest

pytestmark = pytest.mark.usefixtures("clearenv")
```

* 示例代码

```py
import pytest


@pytest.fixture
def clearenv():
    print("\n setUp")
    yield
    print("\n tearDown")


# 使用 pytest.ini 配置代替下面的代码
# pytestmark = pytest.mark.usefixtures("clearenv")

def test_case():
    print("this is case")
    assert True
```

现在通过 `pytest.ini` 配置文件配置 `usefixtures`可以达到 pytestmark 同等的效果。

* `pytest.ini` 配置

```ini
[pytest]
usefixtures = clearenv
```

#### markers 配置

`markers`选项允许你为测试用例添加自定义的标记，以便于分类和过滤。

* `pytest.ini` 配置

```ini
[pytest]
markers =
 slow: marks tests as slow (deselect with '-m "not slow"')
 serial
 high: marks test as level high (deselect with '-m "not high"')
 serial
```

配置自定义标签`slow`和`high`。

* 示例代码

```py
import pytest
from time import sleep


@pytest.mark.slow
def test_slow():
    sleep(3)


@pytest.mark.high
def test_check_login():
    assert True

@pytest.mark.slow
@pytest.mark.high
def test_more_mark():
    assert True

def test_no_mark():
    assert True
```

* 运行结果

```shell
> pytest -m "slow"  # 运行slow标签用例
> pytest -m "high"  # 运行high标签用例
> pytest -m "not slow" # 不运行 slow 标签用例
> pytest -m "not high" # 不运行 slow 标签用例
```

#### parametrize 配置

默认情况下，Pytest转义用于参数化的unicode字符串中使用的任何非ascii字符，因为它具有几个缺点。但是，如果您希望在参数化中使用unicode字符串，并在终端中原样看到它们(
非转义)，在pytest.ini中使用此选项:

* `pytest.ini` 配置

```ini
[pytest]
disable_test_id_escaping_and_forfeit_all_rights_to_community_support = True
```

* 示例代码

```py
import pytest


@pytest.mark.parametrize("id, str", [
    (1, "hello"),
    (2, "你好")
])
def test_eval(id, str):
    pass
```

* 运行结果

```shell
> pytest -vs  test_params.py

==================================== test session starts =================================
test_params.py::test_eval[1-hello]
 setUp
PASSED
 tearDown

test_params.py::test_eval[2-你好]   # 这里正常显示中文。
 setUp
PASSED
 tearDown

=============================== 2 passed in 0.01s ==========================================
```

#### log 配置

pytest自动捕获WARNING或更高级别的日志消息，并将其显示在各自的部分中以与捕获标准输出和标准错误相同的方式测试失败。

执行命令配置日志格式:

```shell
pytest --log-format="%(asctime)s %(levelname)s %(message)s"  --log-date-format="%Y-%m-%d %H:%M:%S"
```

这样的配置的在命令行配置显然不方便，可以在`pytest.ini`配置文件中配置。

* `pytest.ini` 配置

```ini
[pytest]
log_format = %(asctime)s %(levelname)s %(message)s
log_date_format = %Y-%m-%d %H:%M:%S
```

* 示例代码

```py
import logging

# 配置logging  
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


def test_something():
    logger.warning("This is a warning message")
    # 这里可能有一些断言，如果失败，上面的日志会在失败报告中显示  
    assert 1 == 2
```

* 运行结果

```shell
> pytest  -vs test_log.py
==================================== test session starts =================================

test_log.py::test_something
 setUp
FAILED
 tearDown

===================================== FAILURES ============================================
_____________________________________ test_something ______________________________________

    def test_something():
        logger.warning("This is a warning message")
        # 这里可能有一些断言，如果失败，上面的日志会在失败报告中显示
>       assert 1 == 2
E       assert 1 == 2

test_log.py:11: AssertionError
------------------------------- Captured log call ------------------------------------------
2024-07-30 00:04:19 WARNING This is a warning message  # 这里，打印的告警日志。
============================== short test summary info =====================================
FAILED test_log.py::test_something - assert 1 == 2
==================================== 1 failed in 0.07s =====================================
```

#### addopts 配置

`addopts`选项允许你为pytest添加命令行参数。

因为要看打印信息，我一般会使用`-vs`参数，每次使用`pytest`命令的时候都需要输入`pytest -vs`
参数不是太方便，那么就可以通过 `addopts`配置参数来解决这个问题。

* `pytest.ini` 配置

```ini
[pytest]
addopts = -vs
```

#### 运行`目录`和`文件`配置

我们可以通过`pytest.ini`文件配置运行的目录和文件。

* `pytest.ini` 配置

```ini
[pytest]
testpaths =
 test_dir   # 指定运行目录
python_files =
 t_*.py    # 指定运行文件
```

不管是目录或文件均支持指定多个。

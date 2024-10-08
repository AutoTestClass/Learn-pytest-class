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

## 开始学习

[pytest基本使用](/base.md)

[pytest扩展插件使用](/plugin.md)

import allure


@allure.title("测试认证")
@allure.description("此测试尝试使用登录名和密码登录网站。如果发生任何错误则失败。\n\n注意，此测试不测试双因素认证。")
@allure.tag("新界面", "基础", "认证")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="网站")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
def test_authentication():
    ...


@allure.epic("Web 界面")  # 史诗
@allure.feature("基础功能")  # 特征
@allure.story("认证")  # 故事
def test_story_level():
    """web 界面 -> 基础功能 -> 认证"""
    ...


@allure.parent_suite("Web 界面测试")  # 父套件
@allure.suite("基础功能测试")  # 套件
@allure.sub_suite("认证测试")  # 子套件
def test_suite_level():
    """Web 界面测试 -> 基础功能测试 -> 认证测试"""
    ...

import allure


def test_example():
    steps = Steps()
    steps.step1()
    steps.step2()


class Steps:
    @allure.step("步骤 1")
    def step1(self):
        ...

    @allure.step("步骤 2")
    def step2(self):
        ...


def test_login():
    step = Login()
    step.step_with_input("admin", "pw123")
    step.step_with_click("登录")


class Login:
    @allure.step("输入用户名和密码: {first} and {second}")
    def step_with_input(self, first="first", second="second"):
        print(f"输入用户名{first}")
        print(f"输入用密码{second}")

    @allure.step("点击{1}按钮.")
    def step_with_click(self, first):
        print(f"点击{first} 按钮")

class TestClassScope:
    """
    说明：class_scope_fixture 只是确保每个类下面只被执行一次
    """
    
    def test_class_scope_1(self, class_scope_fixture):
        assert class_scope_fixture == "class scope fixture"

    def test_class_scope_2(self, class_scope_fixture):
        assert class_scope_fixture == "class scope fixture"

    def test_cat_sing(self):
        print("miao~, miao~")

    def test_dog_sing(self):
        print("wang~, wang~")

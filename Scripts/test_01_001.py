import allure


class Test_001:
    @allure.step(title="test_01步骤")
    def test_01_001(self):
        print("-----test_01_001")
        assert True

    @allure.step(title="test_02步骤")
    def test_02_002(self):
        print("-----test_02_002")
        assert False

    @allure.step(title="test_03步骤")
    def test_03_003(self):
        print("-----test_02_002")
        assert True
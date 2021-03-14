import pytest
from pythoncode.caculator import Calculator

class TestCalc:
    def setup_method(self):
        # 如果有多组测试数据，那么每次都要实例化对象，这就是所有代码共有的，可以抽出来，每次在代码测试前参数化对象，可以放在setup中，
        # 同理，每次结束后相同的操作可以放在teardown中
        self.cacl = Calculator()
        print("计算开始")
    def teardown_method(self):
        print("计算结束")

    @pytest.mark.parametrize("a, b, expected", [
        (1, 2, 3), (-4, -5, -9), (1000, 2000,3400)], ids=["int", "mimus", "bigint"])
    def test_add(self, a, b, expected):
        assert expected == self.cacl.add(a, b)
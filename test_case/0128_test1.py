import sys

import pytest

sys.path.append('../..')


from test_package.test_calc import Calc

#测试类
class TestCalc:
    def test_add(self):
        calc = Calc()
        assert 2 == calc.add(1,1)

    @pytest.mark.login #装饰器，pytest中可以用标签的形式执行这类用例
    def test_sub(self):
        calc = Calc()
        assert 0 == calc.sub(1, 1)

    def test_mul(self):
        calc = Calc()
        assert 1 == calc.mul(1, 1)

    def test_div(self):
        calc = Calc()
        assert 1 == calc.div(1, 1)


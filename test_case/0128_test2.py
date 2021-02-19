##前置条件，后置条件


import sys

import pytest

sys.path.append('../..')


from test_package.test_calc import Calc

#测试类

class TestCalc:
    #前置条件（一般用于执行用例前打开浏览器这种前置操作）
    def setup_class(self):
        print('开始计算')
        self.calc = Calc()  # 初始化一个对象，alt+enter键，导入包

    #后置条件（一般用于用例跑完关闭浏览器这种后置操作）
    def teardown_class(self):
        print('结束计算')

    def test_add(self):
        assert 2 == self.calc.add(1,1)

    @pytest.mark.login #装饰器，pytest中可以用标签的形式执行这类用例
    def test_sub(self):
        assert 0 == self.calc.sub(1, 1)

    def test_mul(self):
        assert 1 == self.calc.mul(1, 1)

    def test_div(self):
        assert 1 == self.calc.div(1, 1)


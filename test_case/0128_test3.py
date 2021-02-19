##参数化


import pytest
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

    #参数化
    @pytest.mark.parametrize("a,b,result",[[1,1,2],[100,100,200],[0,1,1],[1,-1,0]])
    def test_add(self,a,b,result):
        print(f"a={a},b={b},result={result}")
        assert result == self.calc.add(a,b)




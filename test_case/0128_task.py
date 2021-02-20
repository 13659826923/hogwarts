#Todo：完善相加功能
#Todo：相除功能

import pytest
import yaml
from test_package.test_calc import Calc

def get_datas(name,type='int'):
    with open("../test_data/test_yaml_data.yml", encoding='gb18030', errors='ignore') as f:
        all_datas = yaml.safe_load(f)
    datas = all_datas[name][type]['datas']
    ids = all_datas[name][type]['ids']
    return (datas,ids)

#测试类
class TestCalc:
   # datas:list = get_datas()  #初始化对象data，给他一个类型list

    add_int_data =get_datas('add','int')
    add_float_data = get_datas('add', 'float')
    div_int_data = get_datas('div', 'int')
    div_zeor_data = get_datas('div', 'float')

    #前置条件（一般用于执行用例前打开浏览器这种前置操作）
    def setup_class(self):
        print('开始计算')
        self.calc = Calc()  # 初始化一个对象，alt+enter键，导入包

    #后置条件（一般用于用例跑完关闭浏览器这种后置操作）
    def teardown_class(self):
        print('结束计算')

    @pytest.mark.parametrize("a,b,result", add_int_data[0],ids=add_int_data[1])  #给测试用例命名
    #相加功能
    def test_add(self,a,b,result):
        assert result == self.calc.add(a,b)

    #相加，浮点数0.1+0.2!=0.3情况特殊处理
    @pytest.mark.parametrize("a,b,result", add_float_data[0],ids=add_float_data[1])  #给测试用例命名
    def test_add_fload(self,a,b,result):
        assert result == round(self.calc.add(a,b),2)

    #相除功能
    @pytest.mark.parametrize("a,b,result", div_int_data[0], ids=div_int_data[1])  # 给测试用例命名
    def test_div(self, a, b, result):
        assert result == self.calc.div(a, b)

    #除数为零的情况，特殊处理
    @pytest.mark.parametrize("a,b,result", div_zeor_data[0], ids=div_zeor_data[1])  # 给测试用例命名
    def test_div_zeor(self, a, b, result):
          with pytest.raises(ZeroDivisionError):
              result = a/b





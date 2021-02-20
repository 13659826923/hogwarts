##读yaml文件中写的数据，并使用

import pytest
import yaml

from test_package.test_calc import Calc


def get_datas():
    with open("../test_data/test_yaml_data.yml", encoding='gb18030', errors='ignore') as f:
        test_data = yaml.safe_load(f)
        print(test_data)
    return (test_data['add']['datas'],test_data['add']['ids'])

#测试类
class TestCalc:
    datas:list = get_datas()  #初始化对象data，给他一个类型list

    #前置条件（一般用于执行用例前打开浏览器这种前置操作）
    def setup_class(self):
        print('开始计算')
        self.calc = Calc()  # 初始化一个对象，alt+enter键，导入包

    #后置条件（一般用于用例跑完关闭浏览器这种后置操作）
    def teardown_class(self):
        print('结束计算')

    @pytest.mark.parametrize("a,b,result", datas[0],ids=datas[1])  #给测试用例命名

    #相加功能
    def test_add(self,a,b,result):
        print(f"a={a},b={b},result={result}")
        assert result == self.calc.add(a,b)




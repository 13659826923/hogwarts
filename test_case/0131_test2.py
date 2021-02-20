
import datetime
import pytest

@pytest.fixture(autouse=True)
def test_login():
    print('登录操作')
    token = datetime.datetime.now()
    print(token)
    yield token  #相当于return
    print('登出操作')



def test_search():
    print('搜索')

def test_cart(test_login): ##这样调用yield会执行yield之前的操作，yield之后的在teardown中执行
    print('购物')


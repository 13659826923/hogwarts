import pytest

@pytest.fixture(autouse=True)
def test_login():
    print('登录')

@pytest.fixture()
def get_username():
    name='吱吱'
    print('吱吱')
    return name

def test_search():
    print('搜索')

def test_cart(test_login,get_username): #调用多个fixture
    print('购物')


@pytest.mark.usefixtures('get_username')
@pytest.mark.usefixtures('test_login')
def test_order():
    print('下单')
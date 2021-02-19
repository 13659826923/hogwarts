# 计算器，定义相加功能
def add(a,b):
    return a+b

# 计算器，定义相减功能
def sub(a,b):
    return a-b

# 计算器，定义相乘功能
def mul(a,b):
    return a*b

# 计算器，定义相除功能
def div(a,b):
    return a/b

# 测试用例加断言，测试加减乘除是否通过
# 注 pytest框架中，测试用例的命名规范：文件要以test_开头,或者_test结尾；类要以Test开头，方法要以test_开头

def test_add():
    assert 2 == add(1,1)

def test_sub():
    assert 0 == sub(1, 1)

def test_mul():
    assert 1 == mul(1, 1)

def test_div():
    assert 1 == div(1, 1)
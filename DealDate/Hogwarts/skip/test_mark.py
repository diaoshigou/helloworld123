
import pytest

def double(a):
    return a * 2

# 测试数据：整型
@pytest.mark.int
def test_double_int():
    print("test double int")
    assert 2 == double(1)

# 测试数据：负数
@pytest.mark.minus
def test_double1_minux():
    print("test double minus")
    assert -2 == double(-1)

@pytest.mark.float
def test_double_float():
    assert 0.2 == double(0.1)

@pytest.mark.float
def test_double_minus():
    assert -0.2 == double(-0.1)


@pytest.mark.zero
def test_double_0():
    assert 10 == double(0)

@pytest.mark.bignum
def test_double_bignum():
    assert 200 == double(100)

@pytest.mark.str
def test_double_str():
    assert "aa" == double('a')

@pytest.mark.str
def test_double_str1():
    assert "a$a$" == double('a$')
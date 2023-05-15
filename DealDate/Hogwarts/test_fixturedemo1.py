import pytest

@pytest.fixture(scope="class")
def login():
    print("登录")

def test_buy(login):
    print("买东西")

def test_get():
    print("进货")

def test_order():
    print("下单")

class TestDemo():
    def test_case1(self,login):
        print("case1")


    def test_case2(self,login):
        print("case2")
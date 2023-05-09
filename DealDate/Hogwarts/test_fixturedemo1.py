import pytest

@pytest.fixture()
def login():
    print("登录")

def test_buy(login):
    print("买东西")

def test_get():
    print("进货")

def test_order():
    print("下单")


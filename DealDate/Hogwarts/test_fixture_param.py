import pytest

@pytest.fixture(params=[["selenium","123"],["appium"]])
def login(request): # request为内置函数，名称不可改变
    print(request.param)
    return request.param

def test_demo1(login):
    print(login)
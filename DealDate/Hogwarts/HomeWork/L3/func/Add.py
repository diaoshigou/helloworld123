import pytest


@pytest.fixture()
def login():
    print('登录操作')
    yield
    print('退出登录')
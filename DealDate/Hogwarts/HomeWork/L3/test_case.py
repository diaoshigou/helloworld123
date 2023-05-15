import pytest
data = ['anjing', 'test', 'admin']

@pytest.fixture(params=data, ids=['user=anjing','user=test','user=admin'])
def login(request):
    print('登录功能')
    yield request.param
    print('退出登录')

class Test_01:
    def test_01(self, login):
        print('---用例01---')
        print('登录的用户名：%s' %login)
    def test_02(self):
        print('---用例02---')

if __name__ == '__main__':
    pytest.main(['-vs'])
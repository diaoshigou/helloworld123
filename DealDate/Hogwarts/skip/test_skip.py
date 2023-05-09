
import pytest


@pytest.mark.skip
def test_aaa():
    assert True

@pytest.mark.skip(reason="代码没有实现")
def test_bbb():
    assert False




def check_login():
    return True

def test_function():
    print("start")
    # 如果未登录，则跳过后续步骤
    if not check_login():
        pytest.skip("unsupported configuration")
    print("end")
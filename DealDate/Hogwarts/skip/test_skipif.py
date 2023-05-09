
import sys

import pytest


print(sys.platform)
@pytest.mark.skipif(sys.platform == 'darwin',reason="does not run no mac")
def test_case1():
    assert True
@pytest.mark.skipif(sys.platform == 'win32',reason="does not run on windows")
def test_case2():
    assert True
@pytest.mark.skipif(sys.version_info < (3,6),reason="requires python3.6 or higher")
def test_case3():
    assert True
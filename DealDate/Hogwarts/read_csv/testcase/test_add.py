import pytest
from DealDate.Hogwarts.read_excel.func.operation import my_add
import csv

def get_csv():
    """
    获取csv数据
    :return: 返回数据的结构：[[1, 1, 2], [3, 6, 9], [100, 200, 300]]
    """
    with open('../data/params.csv', 'r',encoding='utf-8') as file:
        raw = csv.reader(file)
        data = []
        for line in raw:
            data.append(line)
    return data

class TestWithEXCEL:
    @pytest.mark.parametrize('x,y,expected', get_csv())
    def test_add(self, x, y, expected):
        assert my_add(int(x), int(y)) == int(expected)
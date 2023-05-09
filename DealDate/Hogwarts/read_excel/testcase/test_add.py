import pytest
from DealDate.Hogwarts.read_excel.func.operation import my_add
import openpyxl

def get_excel():
    # 获取工作簿
    book = openpyxl.load_workbook('../data/params.json')

    # 获取活动行（非空白的）
    sheet = book.worksheets[0]
    cells = sheet["A1":"C3"]
    print(cells)

    # 提取数据，格式：[[1, 2, 3], [3, 6, 9], [100, 200, 300]]
    values = []
    for row in sheet:
        line = []
        for cell in row:
            line.append(cell.value)
        values.append(line)
    print(values)
    return values

class TestWithEXCEL:
    @pytest.mark.parametrize('x,y,expected', get_excel())
    def test_add(self, x, y, expected):
        assert my_add(int(x), int(y)) == int(expected)
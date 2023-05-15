import openpyxl
import pytest

# conftest.py 名字不可改变，作为共享数据文件
@pytest.fixture(scope="session")
def login():
    print("111111")
    # 获取工作簿
    book = openpyxl.load_workbook(r'D:\software\Anaconda3\envs\helloworld123\DealDate\Hogwarts\read_excel\data\params.xlsx')

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
a=0
b=0


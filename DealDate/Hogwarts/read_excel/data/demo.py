import openpyxl

# 获取工作簿
book = openpyxl.load_workbook('../data/params.json')

# 读取工作表1
sheet = book.active

# 读取工作表2
sheet2 = book.worksheets[1]

# 读取单个单元格
cell_a1 = sheet['A1']
cell_a3 = sheet.cell(column=1, row=3)  # A3
cell2_a1 = sheet2['A1']

# 读取多个连续单元格
cells = sheet["A1":"C3"]

# 获取单元格的值
# print(cell2_a1.value)
print(cells)
import random
import xlrd

# 本人认为最有趣的东西，我的青春啊
ExcelFile = xlrd.open_workbook(r'test.xlsx')

sheet = ExcelFile.sheet_by_name('Sheet1')

i = []
x = input("请输入具体事件：")
y = int(input("老师要求的字数："))
while len(str(i)) < y * 1.2:
    s = random.randint(1, 60)
    rows = sheet.row_values(s)
    i.append(*rows)
print(" " * 8 + "检讨书" + "\n" + "老师：")
print("我不应该" + str(x) + "，", *i)
print("再次请老师原谅！")

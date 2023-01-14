# pip install xlsxwriter

import xlsxwriter

data = [
    {
        'name': "João",
        'age': 31
    },
    {
        'name': "José",
        'age': 35
    }
]

workbook = xlsxwriter.Workbook("ExcelTest.xlsx")
worksheet = workbook.add_worksheet("fisrtSheet")

worksheet.write(0, 0, "#")
worksheet.write(0, 1, "Name")
worksheet.write(0, 2, "Age")

for index, entry in enumerate(data):
    worksheet.write(index + 1,0, str(index))
    worksheet.write(index + 1,1, entry["name"])
    worksheet.write(index + 1,2, entry["age"])

workbook.close()

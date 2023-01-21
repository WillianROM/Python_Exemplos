# https://www.youtube.com/watch?v=rE2v-FopUkw&ab_channel=AISciences
# pip instal pywin32

# Create a New Excel Workbook

import win32com.client as win32
import os

x1App = win32.Dispatch('Excel.Application')
x1App.Visible = True

wb = x1App.Workbooks.Add()
print(wb.name)


# Save de Excel File
wb.SaveAs (os.path.join(os.getcwd(),'test.xlsx'))
print(wb.Fullname)

ws_sheet1 = wb.WorkSheets(1)
print(ws_sheet1.name)

wb.WorkSheets(1).name = 'Teste'
print(ws_sheet1.name)


# Write Date
ws_sheet1.Cells(1,'A').value = 'Cell A1'
ws_sheet1.Cells(1,'B').value = 'Cell B1'


# Write data to multiple cell
ws_sheet1.Range("A2:E5").value = 'Teste nas células'
ws_sheet1.Cells(3,3).ClearContents()


# Read Data
for i in range(1,6):
    print(ws_sheet1.Range(ws_sheet1.Cells(i,1),ws_sheet1.Cells(i,5)).value)



wb.close(False)

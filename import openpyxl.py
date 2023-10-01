import openpyxl
from openpyxl import Workbook, load_workbook
out = load_workbook('Assignment_Timecard.xlsr')
sheet = book.active

count = 0
for i in range (600):
    if count>=7:
        print i
        count += 1

print('sheet.Count: ', count)


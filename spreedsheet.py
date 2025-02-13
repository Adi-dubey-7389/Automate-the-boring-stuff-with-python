Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import openpyxl
>>> import openpyxl
>>> import os
>>> os.getcwd()
'C:\\windows\\System32'
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> type(wb)
<class 'openpyxl.workbook.workbook.Workbook'>
>>> wb.sheetnames
['Sheet1']
>>> wb.sheetnames
['Sheet1']
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> wb.sheetnames
['Sheet1']
>>> typw(wb)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    typw(wb)
NameError: name 'typw' is not defined
>>> type(wb)
<class 'openpyxl.workbook.workbook.Workbook'>
>>> wb.sheetnames
['Sheet1']
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> wb.sheetnames
['Sheet1']
>>> wb = openpyxl.load_workbook('example.xlsx')
>>> b.sheetnames
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    b.sheetnames
NameError: name 'b' is not defined
>>> wb.sheetnames
['Sheet1', 'Sheet2', 'Sheet3']
>>> sheet=wb[sheet3]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    sheet=wb[sheet3]
NameError: name 'sheet3' is not defined
>>> sheet=wb['sheet3']
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    sheet=wb['sheet3']
  File "C:\Users\hp\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\openpyxl\workbook\workbook.py", line 278, in __getitem__
    raise KeyError("Worksheet {0} does not exist.".format(key))
KeyError: 'Worksheet sheet3 does not exist.'
>>> sheet=wb['Sheet3']
>>> sheet
<Worksheet "Sheet3">
>>> type(sheet)
<class 'openpyxl.worksheet.worksheet.Worksheet'>
>>> sheet.title
'Sheet3'
>>> anothersheet=wb.active
>>> anothersheet
<Worksheet "Sheet3">
>>> sheet=wb['Sheet1']
>>> sheet['A1']
<Cell 'Sheet1'.A1>
>>> sheet['A1'].value
1
>>> sheet['B1'].value
'04-05-2015  13:34:02 PM'
>>> sheet.cell(row=1, column=3).value
'Apples'
>>> for i in range(1,8,2):
	print(i,sheet.cell(row=1,column=3).value)

	
1 Apples
3 Apples
5 Apples
7 Apples
>>> for i in range(1,8,2):
	print(i,sheet.cell(row=i,column=3).value)

	
1 Apples
3 Pears
5 Apples
7 Strawberries
>>> sheet=wb['Sheet1']
>>> tuple(sheet['B1':'D3'])
((<Cell 'Sheet1'.B1>, <Cell 'Sheet1'.C1>, <Cell 'Sheet1'.D1>), (<Cell 'Sheet1'.B2>, <Cell 'Sheet1'.C2>, <Cell 'Sheet1'.D2>), (<Cell 'Sheet1'.B3>, <Cell 'Sheet1'.C3>, <Cell 'Sheet1'.D3>))
>>>  for rowOfCellObjects in sheet['B1':'D3']:
	 
SyntaxError: unexpected indent
>>> for rowOfCellObjects in sheet['B1':'D3']:
	for cellObj in rowOfCellObjects:
		print(cellObj.coordinate, cellObj.value)
	print('--- END OF ROW ---')

	
B1 04-05-2015  13:34:02 PM
C1 Apples
D1 73
--- END OF ROW ---
B2 2015-05-04 03:41:23
C2 cherries
D2 85
--- END OF ROW ---
B3 2015-06-04 12:46:51
C3 Pears
D3 14
--- END OF ROW ---
>>>  sheet = wb.active
 
SyntaxError: unexpected indent
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
>>> sheet = wb.active
>>> print(sheet = wb.active)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    print(sheet = wb.active)
TypeError: 'sheet' is an invalid keyword argument for print()
>>> sheet = wb.active
>>> sheet
<Worksheet "Sheet3">
>>> sheet='Sheet1'
>>> sheet
'Sheet1'
>>>  list(sheet.columns)[1]
 
SyntaxError: unexpected indent
>>> list(sheet.columns)[1]
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    list(sheet.columns)[1]
AttributeError: 'str' object has no attribute 'columns'
>>> 
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> sheet=wb['Sheet1']
>>> list(sheet.column)[1]
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    list(sheet.column)[1]
AttributeError: 'Worksheet' object has no attribute 'column'
>>> list(sheet.columns)[1]
(<Cell 'Sheet1'.B1>, <Cell 'Sheet1'.B2>, <Cell 'Sheet1'.B3>, <Cell 'Sheet1'.B4>, <Cell 'Sheet1'.B5>, <Cell 'Sheet1'.B6>, <Cell 'Sheet1'.B7>)
>>> list(sheet.columns)[2]
(<Cell 'Sheet1'.C1>, <Cell 'Sheet1'.C2>, <Cell 'Sheet1'.C3>, <Cell 'Sheet1'.C4>, <Cell 'Sheet1'.C5>, <Cell 'Sheet1'.C6>, <Cell 'Sheet1'.C7>)
>>> for cellObj in list(sheet.columns)[2]:
	print(cellObj.value)

	
Apples
cherries
Pears
Oranges
Apples
Bananas
Strawberries
>>> wb=openpyxl.Workbook()
>>> wb.sheetnames
['Sheet']
>>> sheet=wb.active
>>> sheet.title
'Sheet'
>>> 
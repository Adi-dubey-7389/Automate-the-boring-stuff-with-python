Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import csv
>>> file=open('example.csv')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    file=open('example.csv')
FileNotFoundError: [Errno 2] No such file or directory: 'example.csv'
>>> import os
>>> os.getcwd()
'C:\\windows\\system32'
>>> os.chdir('C;/python')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    os.chdir('C;/python')
FileNotFoundError: [WinError 3] The system cannot find the path specified: 'C;/python'
>>> os.chdir('C:/python')
>>> file=open('example.csv')
>>> read=csv.reader(file)
>>> data=list(read)
>>> data
[['4/5/2015 13:34', 'Apples', '73'], ['4/5/2015 3:41', 'Cherries', '85'], ['4/6/2015 12:46', 'Pears', '14'], ['4/8/2015 8:59', 'Oranges', '52'], ['4/10/2015 2:07', 'Apples', '152'], ['4/10/2015 18:10', 'Bananas', '23'], ['4/10/2015 2:40', 'Strawberries', '98']]
>>> exampleData[0][0]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    exampleData[0][0]
NameError: name 'exampleData' is not defined
>>> data.exampleData[0][0]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    data.exampleData[0][0]
AttributeError: 'list' object has no attribute 'exampleData'
>>> data[0][0]
'4/5/2015 13:34'
>>> data[0][1]
'Apples'
>>> data[0][2]
'73'
>>> for r in read:
	print('Row#'+ str(read.line_num)+ ""+ str(r))

	
>>> 
>>> 
>>> 
>>> file=open('example.csv')
>>> read=csv.reader(file)
>>> for r in read:
	print('Row#'+str(read.line_num)+''+str(r))

	
Row#1['4/5/2015 13:34', 'Apples', '73']
Row#2['4/5/2015 3:41', 'Cherries', '85']
Row#3['4/6/2015 12:46', 'Pears', '14']
Row#4['4/8/2015 8:59', 'Oranges', '52']
Row#5['4/10/2015 2:07', 'Apples', '152']
Row#6['4/10/2015 18:10', 'Bananas', '23']
Row#7['4/10/2015 2:40', 'Strawberries', '98']
>>> file=open('output.csv','w',newline='')
>>> write=csv.writer(file)
>>> write.writerrow([['spam','eggs','bacon','ham'])
		
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> write.writerow(['spam','eggs','bacon','ham'])
21
>>> write.writerow(['Hello, world!','eggs','bacon','ham'])
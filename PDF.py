Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import ezsheets
>>> import PyPDF2
>>> pdffileobj=open('Software Architecture.pdf','rb')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    pdffileobj=open('Software Architecture.pdf','rb')
FileNotFoundError: [Errno 2] No such file or directory: 'Software Architecture.pdf'
>>> import os
>>> os.cwd()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    os.cwd()
AttributeError: module 'os' has no attribute 'cwd'
>>> import os.path
>>> import os.path.cwd()
SyntaxError: invalid syntax
>>> import csv
>>> examplefile=open('example.csv')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    examplefile=open('example.csv')
FileNotFoundError: [Errno 2] No such file or directory: 'example.csv'
>>> os.getcwd()
'C:\\windows\\system32'
>>> os.chdir('C:\\python')
>>> os.getcwd()
'C:\\python'
>>> examplefile=open('dte_cse_it_fw.pdf')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    examplefile=open('dte_cse_it_fw.pdf')
FileNotFoundError: [Errno 2] No such file or directory: 'dte_cse_it_fw.pdf'
>>> examplefile=open('dte_cse_it_fw')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    examplefile=open('dte_cse_it_fw')
FileNotFoundError: [Errno 2] No such file or directory: 'dte_cse_it_fw'
>>> 
KeyboardInterrupt
>>> examplefile=open('dte_cse_it_fw.pdf')
>>> pdffile=open('dte_cse_it_fw.pdf','rb')
>>> pdfreader=PyPDF2.PdfFileReader(pdffile)
>>> pdfreader.numPages
4
>>> page=pdfreader.getPage(0)
>>> page.extractText()
'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
>>> file=open('software_Engineering.pdf')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    file=open('software_Engineering.pdf')
FileNotFoundError: [Errno 2] No such file or directory: 'software_Engineering.pdf'
>>> file=open('software_Engineering.pdf')
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> file=open('software_Engineering.pdf','rb')
>>> read=PyPDF2.PdfFileReader(file)
>>> read.numPages
5
>>> page=read.getPage(0)
>>> page.extractText()
'What is software Engineering?\n \nSoftware engineering is a detailed study of engineering to the design, \ndevelopment and maintenance of software. Software engineering was \nintroduced to address the issues of low\n-\nquality software projects. Problems \narise when a\n \nsoftware generally exceeds timelines, budgets, and reduced \nlevels of quality. It ensures that the application is built consistently, correctly, \non time and on budget and within requirements.\n \nSoftware engineering\n \nis an engineering branch associated with de\nvelopment \nof software product using well\n-\ndefined scientific principles, methods and \nprocedures. The outcome of software engineering is an efficient and reliable \nsoftware product.\n \nWhat is a software?\n \nSoftware\n \nis more than just a program code. A program is a\nn executable code, \nwhich serves some computational purpose. Software is considered to be \ncollection of executable programming code, associated libraries and \ndocumentations. Software, when made for a specific requirement is \ncalled\n \nsoftware product.\n \nSoftware\n \nEvolution\n \n:\n \nThe process of developing a software product using software engineering \nprinciples and methods is referred to as\n \nsoftware evolution.\n \nThis includes the \ninitial development of software and its maintenance and updates, till desired \nsoftware \nproduct is developed, which satisfies the expected requirements.\n \n \n \n'
>>> file.close()
>>> file1=open('software_Engineering.pdf','rb')
>>> file2=open('project_file.pdf','rb')
>>> read1=PyPDF2.PdfFileReader(file1)
>>> read2=PyPDF2.PdfFileReader(file2)
>>> wreite=PyPDF2.PdfFileWriter()
>>> for pn in range(read1,read2):
	page=read1.getPage(pn)
	wreite.addPage(page)

	
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    for pn in range(read1,read2):
TypeError: 'PdfFileReader' object cannot be interpreted as an integer
>>> for pn in range(read1.numPages)
SyntaxError: invalid syntax
>>> for pn in range(read1.numPages)
SyntaxError: invalid syntax
>>> for pn in range(read1.numPages):
	page=read1.getPage(pn)
	wreite.addPage(page)

	
>>> for pn in range(read2.numPages)
SyntaxError: invalid syntax
>>> for pn in range(read2.numPages):
	page=read2.getPage(pn)
	wreite.addPage(page)

	
>>> output=open("combine.pdf","wb")
>>> wriete.write(output)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    wriete.write(output)
NameError: name 'wriete' is not defined
>>> wreite.write(output)
>>> output.close()
>>> file1.close()
>>> file2.close()
>>> 

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> file=open('software_Engineering.pdf','rb')
>>> read=PyPDF2.PdfFileReader(file)
>>> page=read.getPage(0)
>>> page.rotateClockwise(90)
{'/Type': '/Page', '/MediaBox': [0, 0, 612, 792], '/Resources': {'/ExtGState': {'/GS5': IndirectObject(10, 0), '/GS8': IndirectObject(11, 0)}, '/Font': {'/F1': IndirectObject(12, 0), '/F2': IndirectObject(16, 0)}, '/XObject': {'/Image11': IndirectObject(20, 0)}, '/ProcSet': ['/PDF', '/Text', '/ImageB', '/ImageC', '/ImageI']}, '/Contents': IndirectObject(21, 0), '/Group': {'/Type': '/Group', '/S': '/Transparency', '/CS': '/DeviceRGB'}, '/Tabs': '/S', '/StructParents': 0, '/Parent': IndirectObject(2, 0), '/Rotate': 90}
>>> writer=PyPDF.PdfFileWriter()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    writer=PyPDF.PdfFileWriter()
NameError: name 'PyPDF' is not defined
>>> writer=PyPDF2.PdfFileWriter()
>>> writer.addPage(page)
>>> result=open("rotatepage.pdf","wb")
>>> writer.write(result)
>>> result.close()
>>> file.close()
>>> 
>>> 
>>> 
\
>>> \

  \
    
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> 
>>> 
>>> 
>>> file=open('software_Engineering.pdf','rb')
>>> read=PyPDF2.PdfFileReader(file)
>>> page=read.getPage(0)
>>> mark=PyPDF.PdfFileReader(open('dragon_ball.pdf','rb'))
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    mark=PyPDF.PdfFileReader(open('dragon_ball.pdf','rb'))
NameError: name 'PyPDF' is not defined
>>> mark=PyPDF2.PdfFileReader(open('dragon_ball.pdf','rb'))
>>> page.mergePage(mark.getPage(0))
>>> writer=PyPDF2.PdfFileWriter()
>>> writer.addPage(page)
>>> 
>>> for pn in range(1,read.numPages):
	pageo=read.getPage(pn)
	writer.addPage(pageo)

	
>>> result=open('dragon_ball.pdf','wb')
>>> writer.write(result)
>>> file.close
<built-in method close of _io.BufferedReader object at 0x000002D88F180720>
>>> 
>>> file.close
<built-in method close of _io.BufferedReader object at 0x000002D88F180720>
>>> result.close()
>>> file.close()
>>> os.listdir()
['bluetooth_content_share.html', 'class 12 cs practical', 'combine.pdf', 'dragon_ball.pdf', 'dte_cse_it_fw.pdf', 'FLAG.py', 'game.py', 'h shape.py', 'PDF.py', 'project_file.pdf', 'pygame-1.9.2a0.win32-py3.2.msi', 'rotatepage.pdf', 'snake game.py', 'software_Engineering.pdf', 'start.py', 'WIFI PASSWORD.py']
>>> 

>>> 
>>> 
>>> 
>>> 
>>> 
>>> import docx
>>> doc=docx.Document('demo.docx')
>>> len(doc.paragraphs)
3
>>> 
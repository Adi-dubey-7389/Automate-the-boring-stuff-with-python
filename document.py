Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import docx
>>> doc=docx.Document('demo.docx')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    doc=docx.Document('demo.docx')
  File "C:\Users\hp\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\docx\api.py", line 25, in Document
    document_part = Package.open(docx).main_document_part
  File "C:\Users\hp\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\docx\opc\package.py", line 128, in open
    pkg_reader = PackageReader.from_file(pkg_file)
  File "C:\Users\hp\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\docx\opc\pkgreader.py", line 32, in from_file
    phys_reader = PhysPkgReader(pkg_file)
  File "C:\Users\hp\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages\docx\opc\phys_pkg.py", line 30, in __new__
    raise PackageNotFoundError(
docx.opc.exceptions.PackageNotFoundError: Package not found at 'demo.docx'
>>> import os
>>> os.getcwd()
'C:\\windows\\system32'
>>> os.chdir('C:/python')
>>> os.getcwd()
'C:\\python'
>>> doc=docx.Document('demo.docx')
>>> len(doc.paragraphs)
3
>>> doc.paragraphs[0].text
"At\xa0➊, we open a\xa0.docx\xa0file in Python, call\xa0docx.Document(), and pass the filename\xa0demo.docx. This will return a\xa0Document\xa0object, which has a\xa0paragraphs\xa0attribute that is a list of\xa0Paragraph\xa0objects. When we call\xa0len()\xa0on\xa0doc.paragraphs, it returns\xa07, which tells us that there are seven\xa0Paragraph\xa0objects in this document\xa0➋. Each of these\xa0Paragraph\xa0objects has a\xa0text\xa0attribute that contains a string of the text in that paragraph (without the style information). Here, the first\xa0text\xa0attribute contains\xa0'DocumentTitle'\xa0➌, and the second contains\xa0'A plain paragraph with some bold and some italic'\xa0➍."
>>> doc.paragraph[1].text
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    doc.paragraph[1].text
AttributeError: 'Document' object has no attribute 'paragraph'
>>> doc.paragraphs[1].text
"Each\xa0Paragraph\xa0object also has a\xa0runs\xa0attribute that is a list of\xa0Run\xa0objects.\xa0Run\xa0objects also have a\xa0text\xa0attribute, containing just the text in that particular run. Let’s look at the\xa0text\xa0attributes in the second\xa0Paragraph\xa0object,\xa0'A plain paragraph with some bold and some italic'. Calling\xa0len()\xa0on this\xa0Paragraph\xa0object tells us that there are four\xa0Run\xa0objects\xa0➎. The first run object contains\xa0'A plain paragraph with some '\xa0➏. Then, the text changes to a bold style, so\xa0'bold'\xa0starts a new\xa0Run\xa0object\xa0➐. The text returns to an unbolded style after that, which results in a third\xa0Run\xa0object,\xa0' and some '\xa0➑. Finally, the fourth and last\xa0Run\xa0object contains\xa0'italic'\xa0in an italic style\xa0➒."
>>> 
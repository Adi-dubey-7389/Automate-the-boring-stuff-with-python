Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import time
>>> time.time
<built-in function time>
>>> time.time()
1739773563.3714247
>>> time.ctime()
'Mon Feb 17 11:58:31 2025'
>>> 
>>> 
>>> for i in range(3)
SyntaxError: invalid syntax
>>> for i in range(3):
	print('Tick')
	time.sleep(1)
	print('Tock')
	time.sleep(1)

	
Tick
Tock
Tick
Tock
Tick
Tock
>>> time.sleep(5)
>>> 
>>> 
>>> 
>>> n=time.time()
>>> n
1739775573.741627
>>> round(n,3)
1739775573.742
>>> round(n)
1739775574
>>> 
>>> 
>>> 
>>> import os
>>> os.chdir('/python')
>>> os.getcwd()
'C:\\python'
>>> 
>>> 
>>> 
>>> 
>>> import datetime
>>> datetime.datetime.now()
datetime.datetime(2025, 2, 17, 13, 13, 46, 824496)
>>> datetime.datetime()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    datetime.datetime()
TypeError: function missing required argument 'year' (pos 1)
>>> datetime.datetime(now)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    datetime.datetime(now)
NameError: name 'now' is not defined
>>> datetime.datetime.now()
datetime.datetime(2025, 2, 17, 13, 15, 57, 304258)
>>> 
>>> 
>>> 
>>> 
>>> 
KeyboardInterrupt
>>> datetime.datetime.now()
datetime.datetime(2025, 2, 17, 13, 18, 31, 701003)
>>> 
>>> 
>>> datetime.datetime.fromtimestamp()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    datetime.datetime.fromtimestamp()
TypeError: fromtimestamp() missing required argument 'timestamp' (pos 1)
>>> datetime.datetime.fromtimestamp(1000000)
datetime.datetime(1970, 1, 12, 19, 16, 40)
>>> datetime.datetime.fromtimestamp(time.time())
datetime.datetime(2025, 2, 17, 13, 23, 3, 970027)
>>> 
>>> 
>>> 
>>> 
>>> 
=========== RESTART: C:\python\multithreaded.py ===========
Start of program.
End of program.
>>> Wake up!
End of program.
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> import threading
>>> thread=threading.thread(target=print,args=['cats','dogs','frogs'])
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    thread=threading.thread(target=print,args=['cats','dogs','frogs'])
AttributeError: module 'threading' has no attribute 'thread'
>>> thread=threading.Thread(target=print,args=['cats','dogs','frogs'])
>>> thread=threading.Thread(target=print,args=['cats','dogs','frogs'],kwargs=['sep':'&'])
SyntaxError: invalid syntax
>>> thread=threading.Thread(target=print,args=['cats','dogs','frogs'],kwargs={'sep': '&'})
>>> thread.start()
cats
>>> &dogs&frogs

>>> 
>>> 
>>> 
>>> 
>>> thread=threading.Thread(target=print,args=['cats','dogs','frogs'],kwargs={'sep':'&'})
>>> thread.start()
cats
>>> &dogs&frogs

>>> 
>>> 
>>> 
>>> 
>>> import subprocess
>>> subprocess.Popen('C:\\python\\demo.docx')
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    subprocess.Popen('C:\\python\\demo.docx')
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.8_3.8.2032.0_x64__qbz5n2kfra8p0\lib\subprocess.py", line 854, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.8_3.8.2032.0_x64__qbz5n2kfra8p0\lib\subprocess.py", line 1307, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
PermissionError: [WinError 32] The process cannot access the file because it is being used by another process
>>>  subprocess.Popen('C:\\python\\exam.tsv')
 
SyntaxError: unexpected indent
>>> subprocess.Popen('C:\\python\\exam.tsv')
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    subprocess.Popen('C:\\python\\exam.tsv')
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.8_3.8.2032.0_x64__qbz5n2kfra8p0\lib\subprocess.py", line 854, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.8_3.8.2032.0_x64__qbz5n2kfra8p0\lib\subprocess.py", line 1307, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
OSError: [WinError 193] %1 is not a valid Win32 application
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
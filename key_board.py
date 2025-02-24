Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pyautogui
pyautigui.scroll
>>> 
>>> 
>>> pyautigui.scroll(200)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    pyautigui.scroll(200)
NameError: name 'pyautigui' is not defined
>>> 
KeyboardInterrupt
>>> pyautogui.scroll(200)
>>> 

>>> fw = pyautogui.getActiveWindow()
>>> fw
Win32Window(hWnd=196768)
>>> 

>>> pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y'])
Xab
>>> 
>>> 
>>>  pyautogui.pixel((0, 0))
 
SyntaxError: unexpected indent
>>> pyautogui.pixel((0, 0))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    pyautogui.pixel((0, 0))
TypeError: pixel() missing 1 required positional argument: 'y'
>>> pyautogui.pixel((0,0))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    pyautogui.pixel((0,0))
TypeError: pixel() missing 1 required positional argument: 'y'
>>> pyautogui.pixel((0, 0))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    pyautogui.pixel((0, 0))
TypeError: pixel() missing 1 required positional argument: 'y'
>>> pyautogui.pixel((50, 200))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    pyautogui.pixel((50, 200))
TypeError: pixel() missing 1 required positional argument: 'y'
>>> 
>>> 
>>> pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))
False
>>> pyautogui.pixel((50, 200))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    pyautogui.pixel((50, 200))
TypeError: pixel() missing 1 required positional argument: 'y'
>>> 
>>> 
>>> 
>>> pyautogui.pixelMatchesColor(50, 200, (255, 135, 144))
False
>>> pyautogui.pixel((50, 200))
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    pyautogui.pixel((50, 200))
TypeError: pixel() missing 1 required positional argument: 'y'
>>> 
KeyboardInterrupt
>>> pyautogui.pixel((50, 200))
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    pyautogui.pixel((50, 200))
TypeError: pixel() missing 1 required positional argument: 'y'
>>> 
>>> fw = pyautogui.getActiveWindow()
>>> fw.isMaximized
False
>>> fw.isActive
True
>>> fw.maximize()
>>> 
>>> 
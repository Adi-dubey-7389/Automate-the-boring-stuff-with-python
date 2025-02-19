Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import json
>>> string= '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'
>>> data=json.loads(string)
>>> data
{'name': 'Zophie', 'isCat': True, 'miceCaught': 0, 'felineIQ': None}
>>> 
#!python3.6
#coding:utf-8
import re

try:
    pattern = r'(ab'
    pattern1 = re.compile(pattern)
except Exception as e:
    print('msg:', e.msg)
    print('pattern:', e.pattern)
    print('pos:', e.pos)
    print('lineno:', e.lineno)
    print('colno:', e.colno)
finally: re.purge()

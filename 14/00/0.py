#!python3.6
#coding:utf-8
import re
match = re.search(r'^ab', 'ABC', re.IGNORECASE)
if match: print('一致した。')
else: print('一致しない。')

match = re.search(r'^ab', 'CDE', re.IGNORECASE)
if match: print('一致した。')
else: print('一致しない。')

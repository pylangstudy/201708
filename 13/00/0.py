#!python3.6
#coding:utf-8
import re
regex = re.compile(r'^ab', re.IGNORECASE)
print(regex)
print('regex.flags:', regex.flags)
print('regex.groups:', regex.groups)
print('regex.groupindex:', regex.groupindex)
print('regex.pattern:', regex.pattern)

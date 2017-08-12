#!python3.6
#coding:utf-8
import re
import string

print(re.escape('python.exe'))

legal_chars = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`|~:"
print('[%s]+' % re.escape(legal_chars))

operators = ['+', '-', '*', '/', '**']
print('|'.join(map(re.escape, sorted(operators, reverse=True))))

print(re.escape('あいうえお'))

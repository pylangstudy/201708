#!python3.6
#coding:utf-8
print('abc'.encode())
print('abc'.encode(encoding='utf-8'))
print('abc'.encode(encoding='utf-8', errors='strict'))
print('abc'.encode(encoding='utf-8', errors='ignore'))
print('abc'.encode(encoding='utf-8', errors='replace'))
print('abc'.encode(encoding='utf-8', errors='xmlcharrefreplace'))
print('abc'.encode(encoding='utf-8', errors='backslashreplace'))

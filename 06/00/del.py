#!python3.6
#coding:utf-8
d = {}; print(len(d))
d = {'k1':'v1', 'k2':'v2'}; print(len(d))
for k in d.keys(): print(f"d['{k}']={d[k]}")
print()
del d['k1']
for k in d.keys(): print(f"d['{k}']={d[k]}")


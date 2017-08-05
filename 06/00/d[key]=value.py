#!python3.6
#coding:utf-8
d = {}; print(len(d))
d = {'k1':'v1', 'k2':'v2'}; print(len(d))
for k in d.keys(): print(f"d['{k}']={d[k]}")
d['k1'] = 'v11'
for k in d.keys(): print(f"d['{k}']={d[k]}")
#print(d['k999']) #KeyError: 'k999'
d['k999'] = 'v999'
for k in d.keys(): print(f"d['{k}']={d[k]}")

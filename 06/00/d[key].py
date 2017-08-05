#!python3.6
#coding:utf-8
d = {}; print(len(d))
d = {'k1':'v1', 'k2':'v2'}; print(len(d))
print("d['k1']=", d['k1'])
print("d['k2']=", d['k2'])
for k in d.keys(): print("d['{}']={}".format(k, d[k]))
for k in d.keys(): print(f"d['{k}']={d[k]}")
#print(d['k999']) #KeyError: 'k999'

class Counter(dict):
    def __missing__(self, key): return 0
c = Counter()
print(c['red'])
c['red'] += 1
print(c['red'])

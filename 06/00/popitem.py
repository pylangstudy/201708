d = {'k1':'v1', 'k2':'v2'}; print(d)
while 0 < len(d): print(d.popitem())
d = {'k3':'v3', 'k4':'v4'}; print(d)
while 0 < len(d):
    k,v = d.popitem()
    print(k, v)

d = {'k0':'v0', 'k1':'v1'}; print(d)
#print(len(d.keys()))
#print(len(d.values()))
#print(len(d.items()))
e = zip(d.values(), d.keys())
print(e)
print(dict(e))
e = [(v, k) for (k, v) in d.items()]
print(e)
print(dict(e))

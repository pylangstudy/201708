d = {'k0':'v0', 'k1':'v1'}; print(d)
print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))

del d['k0']
print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))

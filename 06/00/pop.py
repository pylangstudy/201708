d = {'k1':'v1', 'k2':'v2'}; print(d)
print(d.pop('k1')); print(d)
print(d.pop('k2')); print(d)
#print(d.pop('k3'))#KeyError: 'k3'
print(d.pop('k3', None)); print(d)

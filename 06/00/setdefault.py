d = {'k1':'v1', 'k2':'v2'}; print(d)
print(d.setdefault('k1')); print(d)
print(d.setdefault('k1', None)); print(d)
print(d.setdefault('k100')); print(d)
print(d.setdefault('k999', 'v999')); print(d)
d['k200'] = 'v200'; print(d)


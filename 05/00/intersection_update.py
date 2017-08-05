s = set([1,2,3])
tl = [1,4]
print(s)
s.intersection_update(tl)
print(s)

s = set([1,2,3])
print(s)
s &= set(tl)
print(s)


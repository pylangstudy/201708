sl = [1,2,3]
tl = [1,4]
print(sl, tl)

s = set(sl)
print(s)
s.difference_update(tl)
print(s)

s = set(sl)
print(s)
s -= set(tl)
print(s)


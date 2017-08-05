s = set([1,2,3])
t = s.copy()
print(s, t)
s.remove(1)
#s.clear()
print(s, t)


s = frozenset([1,2,3])
t = s.copy()
print(s, t)
#s.remove(1)
#s.clear()
print(s, t)

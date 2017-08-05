s = set([1,2,3,2,1]);
t = set([4,5,6]);
print(s, t)
print(s.issuperset(t))
print(s >= t)
t = set([4,5,1]);
print(s, t)
print(s.issuperset(t))
print(s >= t)
t = set([1,2,3]);
print(s, t)
print(s.issuperset(t))
print(s >= t)
t = set([1,2,3,4]);
print(s, t)
print(s.issuperset(t))
print(s >= t)
t = set([2,3]);
print(s, t)
print(s.issuperset(t))
print(s >= t)

s = frozenset([1,2,3,2,1]);
t = frozenset([4,5,6]);
print(s, t)
print(s.issuperset(t))
print(s >= t)
t = frozenset([4,5,1]);
print(s, t)
print(s.issuperset(t))
print(s >= t)
t = frozenset([1,2,3]);
print(s, t)
print(s.issuperset(t))
print(s >= t)
t = frozenset([1,2,3,4]);
print(s, t)
print(s.issuperset(t))
print(s >= t)
t = frozenset([2,3]);
print(s, t)
print(s.issuperset(t))
print(s >= t)

s = list(range(10))
print(s)
s[3] = 333
print(s)
s[3:6] = [33,44,55]
print(s)
del s[3:6]
print(s)

s = list(range(10))
del s[2:9:3]
print(s)

s = []
print(s)
s.append(111)
print(s)
s.append(222)
print(s)
s.clear()
print(s)

s0 = s.copy()
print(s0, s)
s0.append(123)
print(s0, s)

s = [1,2] + [3,4]
print(s)
s.extend([5,6])
print(s)
s.insert(3, 34)
print(s)
print(s.pop())
print(s)
s.reverse()
print(s)
s.remove(34)
print(s)
del s[0]
print(s)

s = [1,2]
print(s)
s *= 2
print(s)

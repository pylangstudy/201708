s = [2,4,3,1]
s.sort()
print(s)
s.reverse()
print(s)

s = ['1', '2', '12']
print(s)
s.sort()
print(s)
s.sort(key=lambda x:int(x))
print(s)

s.sort(reverse=True)
print(s)
s.sort(key=lambda x:int(x), reverse=True)
print(s)

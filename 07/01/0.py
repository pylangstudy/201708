class C:
    def method(self): print('C.method()')

c = C()
#c.method.whoami = 'my name is method'  # AttributeError: 'method' object has no attribute 'whoami'
c.method()
print(c.method)
print(c.method.__func__)
print(c.method.__self__)
c.method.__func__(c.method.__self__)

c.method.__func__.whoami = 'my name is method'
print(c.method.whoami)


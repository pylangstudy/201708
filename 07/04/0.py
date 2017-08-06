class A:
    def MyMethod(self): pass

a = A()
print(A.__dict__)
print(a.__dict__)
print(a.__class__)
print(A.__bases__)
print(A.__name__)
print(A.__qualname__)

print(A.__mro__)
#print(a.__mro__)
print(A.mro())
#print(a.mro())
#print(A.__subclasses__())
print(int.__subclasses__())

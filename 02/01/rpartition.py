s = 'a,b,c'; print(s.rpartition(','))
s = 'a,b,c'; print(s.rpartition('-'))
#s = 'a,b,c'; print(s.rpartition(None)) #TypeError: must be str, not NoneType
#s = 'a,b,c'; print(s.rpartition('')) #ValueError: empty separator

s = 'a,b,c'; print(s.partition(','))
s = 'a,b,c'; print(s.partition('-'))
#s = 'a,b,c'; print(s.partition(None)) #TypeError: must be str, not NoneType
#s = 'a,b,c'; print(s.partition('')) #ValueError: empty separator

s = b'	a	b	c	'
print(s.expandtabs())
print(s.expandtabs(4))
print(s.expandtabs(2))
print(s.expandtabs(1))
print(s.expandtabs(0))
s = bytearray(b'	a	b	c	')
print(s.expandtabs())
print(s.expandtabs(4))
print(s.expandtabs(2))
print(s.expandtabs(1))
print(s.expandtabs(0))

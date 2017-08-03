print(b'abc'.startswith(b'a'))
print(b'abc'.startswith(b'b'))
print(b'abc'.startswith(b'c'))
print(b'abc'.startswith(b'bc'))
print(b'abc'.startswith(b'abc'))
"""
print(b'aBc'.casefold().startswith(('b', 'c')))
print(b'aBc'.casefold().startswith(('x', 'y')))

print(b'aBc'.casefold().startswith(b'A'.casefold()))
print(b'aBc'.casefold().startswith(b'b'.casefold()))
print(b'aBc'.casefold().startswith(b'C'.casefold()))
print(b'aBc'.casefold().startswith(b'bC'.casefold()))
print(b'aBc'.casefold().startswith(b'AbC'.casefold()))
"""


print()
print(b'abc'.endswith(b'a'))
print(b'abc'.endswith(b'b'))
print(b'abc'.endswith(b'c'))
print(b'abc'.endswith(b'bc'))
print(b'abc'.endswith(b'abc'))
"""
print(b'aBc'.casefold().endswith(('b', 'c')))
print(b'aBc'.casefold().endswith(('x', 'y')))

print(b'aBc'.casefold().endswith(b'A'.casefold()))
print(b'aBc'.casefold().endswith(b'b'.casefold()))
print(b'aBc'.casefold().endswith(b'C'.casefold()))
print(b'aBc'.casefold().endswith(b'bC'.casefold()))
print(b'aBc'.casefold().endswith(b'AbC'.casefold()))
"""

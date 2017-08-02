print('abc'.endswith('a'))
print('abc'.endswith('b'))
print('abc'.endswith('c'))
print('abc'.endswith('bc'))
print('abc'.endswith('abc'))

print('aBc'.casefold().endswith(('b', 'c')))
print('aBc'.casefold().endswith(('x', 'y')))

print('aBc'.casefold().endswith('A'.casefold()))
print('aBc'.casefold().endswith('b'.casefold()))
print('aBc'.casefold().endswith('C'.casefold()))
print('aBc'.casefold().endswith('bC'.casefold()))
print('aBc'.casefold().endswith('AbC'.casefold()))



print()
print('abc'.startswith('a'))
print('abc'.startswith('b'))
print('abc'.startswith('c'))
print('abc'.startswith('bc'))
print('abc'.startswith('abc'))

print('aBc'.casefold().startswith(('b', 'c')))
print('aBc'.casefold().startswith(('x', 'y')))

print('aBc'.casefold().startswith('A'.casefold()))
print('aBc'.casefold().startswith('b'.casefold()))
print('aBc'.casefold().startswith('C'.casefold()))
print('aBc'.casefold().startswith('bC'.casefold()))
print('aBc'.casefold().startswith('AbC'.casefold()))


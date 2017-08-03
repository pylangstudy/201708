print('%s' % b'abc')
print(b'%(language)s has %(number)03d quote types.' % {b'language': b"Python", b"number": 2})

print('%s' % 'abc')
#print('%c' % 'abc') #TypeError: %c requires int or char
#print('%c' % b'A') #TypeError: %c requires int or char
print('%c' % 'A')
print('%d' % 15)
print('%i' % 15)
print('%x' % 15)
print('%o' % 15)
print('%e' % 1000)
print('%E' % 1000)
print('%g' % 1.23)
print('%G' % 1.23)
print('%r' % 15) # repr()
print('%s' % 15) # str()
print('%a' % 15) # ascii()

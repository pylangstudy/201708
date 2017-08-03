b = b'abcdefg'
print(b)
print('c:', b.index(b'c'))
#print('z:', b.index(b'z')) #ValueError: subsection not found


b = bytearray(b'abcdefg')
print(b)
print('c:', b.index(b'c'))
#print('z:', b.index(b'z')) #ValueError: subsection not found

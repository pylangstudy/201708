print(str(b'ABC'.count(b'A')))
print(str(b'ABC'.count(b'AB')))
print(str(b'ABC'.count(b'AC')))
print(str(b'AbcA'.count(b'A')))
print(str(b'AbcAbcAbc'.count(b'A', 3)))
print(str(b'AbcAbcAbc'.count(b'A', 3, 5)))
print()
print(str(bytearray(b'ABC').count(b'A')))
print(str(bytearray(b'ABC').count(b'AB')))
print(str(bytearray(b'ABC').count(b'AC')))
print(str(bytearray(b'AbcA').count(b'A')))
print(str(bytearray(b'AbcAbcAbc').count(b'A', 3)))
print(str(bytearray(b'AbcAbcAbc').count(b'A', 3, 5)))
print()
print(str(bytearray(b'ABC').count(bytearray(b'A'))))
print(str(bytearray(b'ABC').count(bytearray(b'AB'))))
print(str(bytearray(b'ABC').count(bytearray(b'AC'))))
print(str(bytearray(b'AbcA').count(bytearray(b'A'))))
print(str(bytearray(b'AbcAbcAbc').count(bytearray(b'A'), 3)))
print(str(bytearray(b'AbcAbcAbc').count(bytearray(b'A'), 3, 5)))


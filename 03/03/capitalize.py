#最初の文字を大文字にし、残りを小文字に
print(b'abcdefg'.capitalize())
print(b'ABCDEFG'.capitalize())
print(b'abcdefg'.upper())
print(b'ABCDEFG'.lower())

print(bytearray(b'abcdefg').capitalize())
print(bytearray(b'ABCDEFG').capitalize())
print(bytearray(b'abcdefg').upper())
print(bytearray(b'ABCDEFG').lower())

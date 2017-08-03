x = bytes.maketrans(b'abc', b'123')
print(x, type(x))
s = b'abcbaABC'; print(s, s.translate(x))

# 第 3 引数を指定する場合、文字列を指定する必要があり、それに含まれる文字が None に対応付けられます。
#x = bytes.maketrans(b'abc', b'123', b'-')
#print(x, type(x))
#s = None; print(s, s.translate(x)) #AttributeError: 'NoneType' object has no attribute 'translate'

x = bytearray.maketrans(bytearray(b'abc'), bytearray(b'123'))
print(x, type(x))
s = bytearray(b'abcbaABC'); print(s, s.translate(x))


s = b'abc'; print(s, s.swapcase())
s = b'ABC'; print(s, s.swapcase())
s = b'Abc'; print(s, s.swapcase())
s = b'aBc'; print(s, s.swapcase())
s = b'abC'; print(s, s.swapcase())

# > s.swapcase().swapcase() == s が真であるとは限りません。
# どういう場合に偽になるのか不明。相互変換できないということだと思う。使いづらい。
s = b'abc'; print(s == s.swapcase().swapcase())
s = b'ABC'; print(s == s.swapcase().swapcase())
s = b'Abc'; print(s == s.swapcase().swapcase())
s = b'aBc'; print(s == s.swapcase().swapcase())
s = b'abC'; print(s == s.swapcase().swapcase())

s = bytearray(b'abc'); print(s, s.swapcase())
s = bytearray(b'ABC'); print(s, s.swapcase())
s = bytearray(b'Abc'); print(s, s.swapcase())
s = bytearray(b'aBc'); print(s, s.swapcase())
s = bytearray(b'abC'); print(s, s.swapcase())

# > s.swapcase().swapcase() == s が真であるとは限りません。
# どういう場合に偽になるのか不明。相互変換できないということだと思う。使いづらい。
s = bytearray(b'abc'); print(s == s.swapcase().swapcase())
s = bytearray(b'ABC'); print(s == s.swapcase().swapcase())
s = bytearray(b'Abc'); print(s == s.swapcase().swapcase())
s = bytearray(b'aBc'); print(s == s.swapcase().swapcase())
s = bytearray(b'abC'); print(s == s.swapcase().swapcase())

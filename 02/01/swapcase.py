s = 'abc'; print(s, s.swapcase())
s = 'ABC'; print(s, s.swapcase())
s = 'Abc'; print(s, s.swapcase())
s = 'aBc'; print(s, s.swapcase())
s = 'abC'; print(s, s.swapcase())

# > s.swapcase().swapcase() == s が真であるとは限りません。
# どういう場合に偽になるのか不明。相互変換できないということだと思う。使いづらい。
s = 'abc'; print(s == s.swapcase().swapcase())
s = 'ABC'; print(s == s.swapcase().swapcase())
s = 'Abc'; print(s == s.swapcase().swapcase())
s = 'aBc'; print(s == s.swapcase().swapcase())
s = 'abC'; print(s == s.swapcase().swapcase())

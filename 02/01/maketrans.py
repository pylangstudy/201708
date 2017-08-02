x = str.maketrans('abc', '123')
print(x, type(x))
s = 'abcbaABC'; print(s, s.translate(x))

# 第 3 引数を指定する場合、文字列を指定する必要があり、それに含まれる文字が None に対応付けられます。
x = str.maketrans('abc', '123', '-')
print(x, type(x))
s = None; print(s, s.translate(x)) #AttributeError: 'NoneType' object has no attribute 'translate'


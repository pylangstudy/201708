s = 'abc'; print(s.isprintable(), s)
s = 'a-c'; print(s.isprintable(), s)
s = 'a c'; print(s.isprintable(), s)
s = 'a\tc'; print(s.isprintable(), s)
s = '   '; print(s.isprintable(), s)#半角スペースつ3
s = '\r\n'; print(s.isprintable(), s)
s = '　'; print(s.isprintable(), s)#全角スペース

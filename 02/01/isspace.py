s = 'abc'; print(s.isspace(), s)
s = 'a-c'; print(s.isspace(), s)
s = 'a c'; print(s.isspace(), s)
s = 'a\tc'; print(s.isspace(), s)
s = '   '; print(s.isspace(), s)#半角スペースつ3
s = '\r\n'; print(s.isspace(), s)
s = '　'; print(s.isspace(), s)#全角スペース

import string
import datetime
f = string.Formatter()
print(f.format('現在日時は{0:%Y-%m-%d %H:%M:%S.%f}です。', datetime.datetime.now()))

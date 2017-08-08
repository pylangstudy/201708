import string
import datetime
print(string.Formatter().format('現在日時は{0:%Y-%m-%d %H:%M:%S.%f}です。', datetime.datetime.now()))
print('現在日時は{0:%Y-%m-%d %H:%M:%S.%f}です。'.format(datetime.datetime.now()))
print(f'現在日時は{datetime.datetime.now():%Y-%m-%d %H:%M:%S.%f}です。')

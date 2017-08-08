import string
import datetime
class MyFormatter(string.Formatter):
    def format(self, format_string, *args, **kwargs):
        print('format()', 'format_string:', format_string, '*args', *args, '**kwargs', **kwargs)
        return super().format(format_string, *args, **kwargs)
    def vformat(self, format_string, args, kwargs):
        print('vformat()', 'format_string:', format_string, 'args', args, 'kwargs', kwargs)
        return super().vformat(format_string, args, kwargs)

f = MyFormatter()
print(f.format('現在日時は{0:%Y-%m-%d %H:%M:%S.%f}です。', datetime.datetime.now()))
print(f.format('name={} age={}', 'Yamada', 99))
#print(f.format('name={name} age={age}', name='Yamada', age=99))#TypeError: 'name' is an invalid keyword argument for this function

import string
import datetime
class MyFormatter(string.Formatter):
    def format(self, format_string, *args, **kwargs):
        print('format()', 'format_string:', format_string, '*args', *args, '**kwargs', **kwargs)
        return super().format(format_string, *args, **kwargs)
    def vformat(self, format_string, args, kwargs):
        print('vformat()', 'format_string:', format_string, 'args', args, 'kwargs', kwargs)
        return super().vformat(format_string, args, kwargs)
    def parse(self, format_string):
        print('parse()', 'format_string:', format_string)
        return super().parse(format_string)
    def get_field(self, field_name, args, kwargs):
        print('get_field()', 'format_string:', field_name, 'args:', args, 'kwargs:', kwargs)
        return super().get_field(field_name, args, kwargs)
    def get_value(self, key, args, kwargs):
        print('get_value()', 'key:', key, 'args:', args, 'kwargs:', kwargs)
        return super().get_value(key, args, kwargs)
    def check_unused_args(self, used_args, args, kwargs):
        print('check_unused_args()', 'used_args:', used_args, 'args:', args, 'kwargs:', kwargs)
        return super().check_unused_args(used_args, args, kwargs)
    def format_field(self, value, format_spec):
        print('format_field()', 'value:', value, 'format_spec:', format_spec)
        return super().format_field(value, format_spec)
    def convert_field(self, value, conversion):
        print('convert_field()', 'value:', value, 'conversion:', conversion)
        return super().convert_field(value, conversion)
        
f = MyFormatter()
#print(f.format('現在日時は{0:%Y-%m-%d %H:%M:%S.%f}です。', datetime.datetime.now()))
print(f.format('name={} age={}', 'Yamada', 99))
#print(f.format('name={name} age={age}', name='Yamada', age=99))#TypeError: 'name' is an invalid keyword argument for this function
print()
#print(f.format('name={name} age={age}', {'name':'Yamada', 'age':99}))#KeyError: 'name'



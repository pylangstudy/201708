#!python3.6
from string import Template
class MyTemplate(Template):
    delimiter = '%'

s = MyTemplate('%who likes %what')
print(s.substitute(who='tim', what='kung pao'))

d = dict(who='tim')
print(MyTemplate('%who likes %what').safe_substitute(d))


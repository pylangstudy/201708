#!python3.6
from string import Template
s = Template('$who likes $what')
print(s.substitute(who='tim', what='kung pao'))

d = dict(who='tim')
#print(Template('Give $who $100').substitute(d))#ValueError: Invalid placeholder in string: line 1, col 11
#print(Template('$who likes $what').substitute(d))#KeyError: 'what'
print(Template('$who likes $what').safe_substitute(d))


#!python3.6
from string import Template
class MyTemplate(Template):
    idpattern = '[a-z]+_[a-z]+' # 英字しか使えなくなる。デフォルトの値は [_a-z][_a-z0-9]*

s = Template('$who0 likes $what0')
print(s.substitute(who0='tim', what0='kung pao'))

#s = MyTemplate('$who likes $what')
#print(s.substitute(who='tim', what='kung pao'))#ValueError: Invalid placeholder in string: line 1, col 1
s = MyTemplate('$wh_o likes $wh_at')
print(s.substitute(wh_o='tim', wh_at='kung pao'))

d = dict(who='tim')
print(MyTemplate('$who likes $what').safe_substitute(d))


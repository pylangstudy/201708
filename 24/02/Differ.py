#!python3.6
import difflib
d = difflib.Differ(); print(d)
d = difflib.Differ(linejunk=lambda s: ' ' in s); print(d)#junk文字列
d = difflib.Differ(charjunk=lambda c: ' ' == c); print(d)#junk文字

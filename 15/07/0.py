#!python3.6
import re
print(re.match(r"\W(.)\1\W", " ff "))
print(re.match("\\W(.)\\1\\W", " ff "))
print()
print(re.match(r"\\", r"\\"))
print(re.match("\\\\", r"\\"))


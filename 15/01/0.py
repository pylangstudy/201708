#!python3.6
import re
valid = re.compile(r"(\S+) - (\d+) errors, (\d+) warnings")
match = valid.match("/usr/sbin/sendmail - 0 errors, 4 warnings")
print(match.groups())

#!python3.6
import re
import random
text = "He was carefully disguised but captured quickly by police."
print(re.findall(r"\w+ly", text))

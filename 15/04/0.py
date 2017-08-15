#!python3.6
import re
import random
def repl(m):
#    print(m.groups())
    inner_word = list(m.group(2))
    random.shuffle(inner_word)
    return m.group(1) + "".join(inner_word) + m.group(3)
text = "Professor Abdolmalek, please report your absences promptly."
print(text)
print(re.sub(r"(\w)(\w+)(\w)", repl, text))
print(re.sub(r"(\w)(\w+)(\w)", repl, text))

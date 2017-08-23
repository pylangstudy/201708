#!python3.6
import difflib
s = difflib.SequenceMatcher(lambda x: x == " ",
                    "private Thread currentThread;",
                    "private volatile Thread currentThread;")
print(round(s.ratio(), 3))

for block in s.get_matching_blocks():
    print("a[%d] and b[%d] match for %d elements" % block)

for opcode in s.get_opcodes():
    print("%6s a[%d:%d] b[%d:%d]" % opcode)

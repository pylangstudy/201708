#!python3.6
import difflib
s = difflib.SequenceMatcher(None, "abxcd", "abcd")
print(s.get_matching_blocks())



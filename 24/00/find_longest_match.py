#!python3.6
import difflib
sm = difflib.SequenceMatcher(); print(sm);
print(sm.ratio())
sm.set_seqs('abc', 'abcd')
print(sm.ratio())
print(sm.find_longest_match(0, 3, 0, 3))
print(sm.ratio())

s = difflib.SequenceMatcher(None, " abcd", "abcd abcd")
match = s.find_longest_match(0, 5, 0, 9)
print(match)

s = difflib.SequenceMatcher(lambda x: x==" ", " abcd", "abcd abcd")
match = s.find_longest_match(0, 5, 0, 9)
print(match)

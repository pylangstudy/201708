#!python3.6
import difflib
sm = difflib.SequenceMatcher(); print(sm);
print(sm.ratio())
sm.set_seqs('abc', 'abcd')
print(sm.ratio())
sm.set_seqs('abc', 'abc')
print(sm.ratio())

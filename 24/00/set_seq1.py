#!python3.6
import difflib
sm = difflib.SequenceMatcher(); print(sm);
print(sm.ratio())
sm.set_seqs('abc', 'abcd')
print(sm.ratio())
sm.set_seq1('abcd')
print(sm.ratio())

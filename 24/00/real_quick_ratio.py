#!python3.6
import difflib
sm = difflib.SequenceMatcher(); print(sm);
sm = difflib.SequenceMatcher(a='abc', b='abc')
print('ratio:', sm.ratio());
print('quick_ratio:', sm.quick_ratio());
print('real_quick_ratio:', sm.real_quick_ratio());
sm = difflib.SequenceMatcher(a='abc', b='a b	c')
print('ratio:', sm.ratio());
print('quick_ratio:', sm.quick_ratio());
print('real_quick_ratio:', sm.real_quick_ratio());
sm = difflib.SequenceMatcher(isjunk=lambda x: x in " \t", a='abc', b='a b	c'); print(sm, sm.ratio());
print('ratio:', sm.ratio());
print('quick_ratio:', sm.quick_ratio());
print('real_quick_ratio:', sm.real_quick_ratio());

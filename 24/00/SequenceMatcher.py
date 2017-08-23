#!python3.6
import difflib
sm = difflib.SequenceMatcher(); print(sm);
sm = difflib.SequenceMatcher(a='abc', b='abc'); print(sm, sm.ratio());
sm = difflib.SequenceMatcher(a='abc', b='a b	c'); print(sm, sm.ratio());
sm = difflib.SequenceMatcher(isjunk=lambda x: x in " \t", a='abc', b='a b	c'); print(sm, sm.ratio());


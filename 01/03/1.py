import collections
#collections.namedtuple(typename, field_names, *, verbose=False, rename=False, module=None)
Point = collections.namedtuple('Point', ['x','y'])
p = Point(x=11, y=22)
print(p)
print(p.x, p.y)
print(p[0], p[1])

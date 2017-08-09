#!python3.6
c = 3-5j
print(('The complex number {0} is formed from the real part {0.real} '
 'and the imaginary part {0.imag}.').format(c))
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)
print(str(Point(4, 2)))

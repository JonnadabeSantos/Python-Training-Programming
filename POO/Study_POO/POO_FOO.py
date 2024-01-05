class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        print( 'x' )
        return self._x or 1

    @x.setter
    def x(self, value):
        print( 'z' )
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0


foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)
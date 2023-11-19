
class TransportTableCell:
    def __init__(self, c, x):
        self._c = c
        self._x = x

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, c):
        self._c = c

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

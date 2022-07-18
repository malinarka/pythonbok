class Rektangel: 
    def __init__(self, x, y, h, b):
        self.x = x
        self.y = y
        self.h = h
        self.b = b

    
    @property
    def h(self):
        return self._h


    @h.setter
    def h(self, h):
        assert h >= 0, ("Negativt värde", h)
        self._h = h


    @property
    def b(self):
        return self._b


    @b.setter
    def b(self, b):
        assert b >= 0, ("Negativt värde", b)
        self._b = b


    def area(self):
        return self.h * self.b


    def omkrets(self):
        return self.h * 2 + self.b * 2
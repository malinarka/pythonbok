class Rektangel: 
    def __init__(self, x, y, h, b):
        self.x = x
        self.y = y
        self.set_h(h)
        self.set_b(b)

    
    def get_h(self):
        return self._h


    def set_h(self, h):
        assert h >= 0, ("Negativt värde", h)
        self._h = h


    def get_b(self):
        return self._b


    def set_b(self, b):
        assert b >= 0, ("Negativt värde", b)
        self._b = b


    def area(self):
        return self._h * self._b


    def omkrets(self):
        return self._h * 2 + self._b * 2
class Rektangel: 
    def __init__(self, x, y, h, b):
        self.x = x
        self.y = y
        self.set_h(h)
        self.set_b(b)


    def set_h(self, h):
        assert h >= 0, ("Negativt värde", h)
        self.h = h


    def set_b(self, b):
        assert b >= 0, ("Negativt värde", b)
        self.b = b


    def area(self):
        return self.h * self.b


    def omkrets(self):
        return self.h * 2 + self.b * 2
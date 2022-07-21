class Hus:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def kvadratisk(self):
        return self.l == self.b

    def yta(self):
        return self.l * self.b


class Flervåningshus(Hus):
    def __init__(self, l, b, v):
        super().__init__(l, b)
        self.antal_våningar = v

    def höghus(self):
        return self.antal_våningar >= 10

    def yta(self):
        return self.l * self.b * self.antal_våningar


class Skola(Flervåningshus):
    def __init__(self, l, b, v, n):
        super().__init__(l, b, v)
        self.antal_klassrum = n

    def klassrum_per_våning(self):
        return self.antal_klassrum / self.antal_våningar


f1 = Flervåningshus(10, 15, 4)
s1 = Skola(10, 15, 4, 8)

print(s1.klassrum_per_våning())
print(s1.antal_klassrum)
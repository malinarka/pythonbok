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
        return self.antal_klassrum /self.antal_våningar
    def yta(self):
        return self.antal_klassrum * 50


lista = [Hus(10, 2), Skola(10, 2, 3, 9)]
for e in lista:
    print(type(e).__name__, "har ytan", e.yta)

class Datum:
    def __init__(self, åååå, mm, dd):
        self.åååå = åååå
        self.mm = mm
        self.dd = dd


    def __str__(self):
        return f"{self.åååå:04}-{self.mm:02}-{self.dd:02}"

    
d1 = Datum(1990, 3, 28)
print(d1)
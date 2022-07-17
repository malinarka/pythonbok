from rektangel import Rektangel


while True:
    b = float(input("Skriv in rektangelns bas: "))
    h = float(input("Skriv in rektangelns höjd: "))
    r = Rektangel(x=0, y=0, h=h, b=b) # Kan även skriva endast 0 för x och y och då behöver man inte skriva h=h och b=b.
    print(f"Arean av rektangeln är {r.area()} och omkretsen är {r.omkrets()}.")
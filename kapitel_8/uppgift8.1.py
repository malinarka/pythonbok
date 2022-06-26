import math

def omkrets(r):
    """Den här funktionen räknar ut en cirkels omkrets med radien r."""
    return(2 * r * math.pi)

def area(r): 
    """Den här funktionen räknar ut en cirkels area med radien r."""
    return(math.pi * r * r)

r = float(input("Ange cirkels radie: "))
omkretsen = omkrets(r)
arean = area(r)
print(f"Cirkelns omkrets är {omkretsen:.2f} och arean är {arean:.2f}.")
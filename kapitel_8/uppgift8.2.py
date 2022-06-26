import math

def omkrets_area(r):
    """Den här funktionen räknar ut en cirkels omkrets och area med radien r."""
    return 2 * r * math.pi, math.pi * r * r

o, a = omkrets_area(5)
print(f"Cirkelns omkrets är {o:.2f} och arean är {a:.2f}.")
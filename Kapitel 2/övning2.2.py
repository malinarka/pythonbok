angiven_radie = float(input("Ange sfärens radie i cm "))
print("Sfärens radie i cm är:", angiven_radie)

from math import pi

sfärens_volym = (4 * pi * angiven_radie ** 3) / 3
sfärens_area = 4 * pi * angiven_radie ** 2

print(f"Sfärens volym är {sfärens_volym:.2f} cm³ och dess area är {sfärens_area:.2f} cm²")

# Hur man räknar ut volymen och arean på en sfär. Om man bara vill skriva 
# "import math" så räcker det inte att använda "pi" utan måste skriva "math.pi".
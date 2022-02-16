from math import pi

radien = input("Skriv in cirelns radie: ")
cirkelns_radie = float(radien)

if cirkelns_radie > 0:
    print(f"Cirkelns omkrets är {cirkelns_radie * 2 * pi}")
    print(f"Och dess area är {cirkelns_radie ** 2 * pi}")
else:
    print("Felaktigt värde på radien")
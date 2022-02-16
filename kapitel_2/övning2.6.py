import math

t = float(input("Antal år: "))

andel_C14_kvar = math.e ** (0 - math.log(2) / 5730 * t)

print("Andel C14 kvar efter", t, "år, är:", andel_C14_kvar * 100, "%")

# Svåraste uppgiften hittills. 

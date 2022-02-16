sträcka_mile = float(input("Ange sträckan i miles: "))
bränsle_gallon = float(input("Ange bränsleförbrukning i gallons: "))

print(f"Miles per gallon: {sträcka_mile / bränsle_gallon:.2f}")

sträcka_mil = sträcka_mile * 1.609
bränsle_liter = bränsle_gallon * 3.785

print(f"Liter per mil: {bränsle_liter / sträcka_mil:.2f}")

# Omvandling av amerikanska enheter till svenska. 
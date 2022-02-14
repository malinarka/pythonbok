# Värdet av x ska räknas ut med hjälp av en for-sats. 

for x in range(-10, 11):
    resultat = 2 * x ** 2 - 5 * x + 1

    print(f"{x:3} {resultat:6.0f}")
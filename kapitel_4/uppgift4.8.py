# Samma som föregående uppgift men steget minskas till 0,1
# och intervallet till -1 och 1.

for v in range(-10, 11):
    x = v / 10
    resultat = 2 * x ** 2 - 5 * x + 1

    print(f"{x:3} {resultat:6.2f}")
# För förståelse:
# x = float(input("x? "))
# n = int(input("n? "))
# r = 1
# for i in range (0, n, 1):
# r = r * x
# print("Resultat:", r)

# Uppgiften är att räkna x ^ n med en for-sats
# Säg att man har följande:
# x = 4
# n = 2
# r = 1
# I intervallet 0 - 4 görs beräkningen r = r * x, alltså i det här fallet 1 = 1 * 4 = 4, 4 = 4 * 4 = 16
# Efter 4 är intervallet slut varför det inte görs några fler beräkningar.
# Mkt dåligt exempel som man inte använde rent programmeringsmässigt och det är
# svårt att förstå.


# Själva uppgiften:
# Skriv ett program som läser in ett heltal n och som beräknar summan, dvs 1 + 4 + 9 + 16...n². k² = k * k
# Använd nu for-satsen istället för while-satsen

n = int(input("Skriv in värdet för n här(obs endast heltal): "))

summa = 0
for k in range(1, n + 1):
    summa = summa + k * k

print("Resultat:", summa)

# Om n = 4 kommer intervallet vara 1 - 4 och hoppet bli 1.
# summa = 0 + 1 * 1 = 1
# summa2 = 1 + 2 * 2 = 5
# summa3 = 5 + 3 * 3 = 14
# summa4 = 14 + 4 * 4 = 30
# Eftersom n = 4 stoppas därefter och summan blir 30

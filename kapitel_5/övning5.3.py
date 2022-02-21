personnummer = input("Skriv in ditt personnummer enligt ååmmddxxxx: ")

if int(personnummer[8]) % 2 == 1:
    print("Personen är en man.")
else: 
    print("Personen är en kvinna.")


# Försökte göra denna med OR men det gick inte så bra. Erik tipsade att man även
# kan göra om de nummer som man vill jämföra med till en lista och sedan använda
# en if-sats med in. Kommer lära sig i nästa kapitel. 
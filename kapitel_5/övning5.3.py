personnummer = input("Skriv in ditt personnummer enligt ååmmddxxxx: ")

print(personnummer[8])

if personnummer[8] == 1 or 3 or 5 or 7 or 9:
    print("Personen är en man.")
else: 
    print("Personen är en kvinna.")

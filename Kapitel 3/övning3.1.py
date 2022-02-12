antal_minuter = int(input("Antal förväntade samtalsminuter: "))

if antal_minuter <= 33:
    print("Abonnemanget kontant är billigast")
elif 33 < antal_minuter <= 66: 
    print("Abonnemanget normal är billigast")
else:
    print("Abonnemanget plus är billigast")

    
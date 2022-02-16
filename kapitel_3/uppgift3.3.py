# Prov i matematik: max 50p. E 25p, D 30 p, C 35p, B 40p och A 45p. 

elevens_poäng = int(input("Ange elevens poäng: "))

if elevens_poäng >= 45:
    print("Betyg: A")
elif 45 > elevens_poäng >= 40:
    print("Betyg: B")
elif 40 > elevens_poäng >= 35:
    print("Betyg: C")
elif 35 > elevens_poäng >= 30:
    print("Betyg: D")
elif 30 > elevens_poäng >= 25:
    print("Betyg: E")
else:
    print("Ej godkänd")


while True:
    höjd = float(input("Från vilken höjd bollen släpps (m): (skriv ett tal < 0 för att avsluta beräkning)"))

    if höjd <= 0:
        break

    antal_studsar = 0
    while höjd > 0.01:
        höjd = höjd * 0.66
        antal_studsar = antal_studsar + 1

    print("Antal studsar:", antal_studsar)

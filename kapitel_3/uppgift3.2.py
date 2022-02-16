pris_årskort = float(input("Pris årskort: "))
pris_besök = float(input("Pris dagskort: "))
antal_planerade_besök = int(input("Antal planerade gymbesök per år: "))

if pris_årskort >= pris_besök * antal_planerade_besök:
    print("Årskort lönar sig inte.")
else:
    print("Årskort lönar sig.")

antal_minuter = float(input("Antal minuter per månad: "))
kostnad_per_minut = float(input("Kostnad per minut: "))

kostnad = antal_minuter * kostnad_per_minut

if kostnad >= 300:
    kostnad = kostnad * 0.9

print("Månadens konstnad för telefonen är:", kostnad)


# Hur man lägger till ett villkor för koden. 

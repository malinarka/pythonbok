höjd = float(input("Från vilken höjd bollen släpps (m): "))

# Om man släpper bollen från 2 m höjd, hur många ggr kommer den studsa innan 
# den kommer max 1 cm från golvet? 

# Vid varje studs minskas bollens höjd med 30 %. 

antal_studsar = 0

while höjd >= 0.01:
    höjd = höjd * 0.66
    antal_studsar = antal_studsar + 1 
print("Antal studsar:", antal_studsar)

# "Antal studsar" kallas för "i", i facit.  
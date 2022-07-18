class Bil:
    skatt_per_kg = 4.0


    def __init__(self, reg_nr="", fabrikat="", årsmodell=0, tjänstevikt=0.0, motoreffekt=0.0): 
        self.registeringsnummer = reg_nr
        self.fabrikat = fabrikat
        self.årsmodell = årsmodell
        self.tjänstevikt = tjänstevikt
        self.motoreffekt = motoreffekt
# Måste inte ange standardvärde för mina parametrar, här kommer man att få ett värde även om man
# inte anger alla parametrar. Kan dock vara missvisande och då kan det vara bättre att få ett error. 


    def skatt(self):
        return self.tjänstevikt * Bil.skatt_per_kg


bil_1 = Bil("WWT705", "Skoda", 2005, 1500.0, 90.0)
bil_2 = Bil("PNF588", "BMW", 2003, 2500.0, 250.0)


print(f"{bil_1.registeringsnummer} är en {bil_1.fabrikat} från {bil_1.årsmodell} som väger {bil_1.tjänstevikt} kg och har en effekt på {bil_1.motoreffekt}.")
print(f"{bil_2.registeringsnummer} är en {bil_2.fabrikat} från {bil_2.årsmodell} som väger {bil_2.tjänstevikt} kg och har en effekt på {bil_2.motoreffekt}.")


print({bil_1.skatt()})
print({bil_2.skatt()})
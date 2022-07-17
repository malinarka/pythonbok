class Bil:
    def __init__(self): 
        self.registeringsnummer = ""
        self.fabrikat = ""
        self.årsmodell = 0
        self.tjänstevikt = 0.0
        self.motoreffekt = 0.0

bil_1 = Bil()
bil_2 = Bil()

bil_1.registeringsnummer = "WWT705"
bil_1.fabrikat = "Skoda"
bil_1.årsmodell = 2005
bil_1.tjänstevikt = 1500.0
bil_1.motoreffekt = 90.0

bil_2.registeringsnummer = "PNF588"
bil_2.fabrikat = "BMW"
bil_2.årsmodell = 2003
bil_2.tjänstevikt = 2500.0
bil_2.motoreffekt = 250.0

print(f"{bil_1.registeringsnummer} är en {bil_1.fabrikat} från {bil_1.årsmodell} som väger {bil_1.tjänstevikt} kg och har en effekt på {bil_1.motoreffekt}.")
print(f"{bil_2.registeringsnummer} är en {bil_2.fabrikat} från {bil_2.årsmodell} som väger {bil_2.tjänstevikt} kg och har en effekt på {bil_2.motoreffekt}.")
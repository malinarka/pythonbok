# Skriv ett program som beräknar kommunens uppskattade 
# invånarantal i början av ett visst år. Vilket år som 
# gäller ska läsas in som indata till programmet. 

# I början av 2019 var befolkningsmängden 26 000 invånare. 
# Antal födda per år: 0,7 %
# Antal avlidna per år: 0,6 %
# Antal inflyttade per år: 300 personer
# Antal utflyttade per år: 325 personer

from __future__ import annotations


aktuellt_år = int(input("Ange det aktuella året: "))
if aktuellt_år < 2019:
    print("Ej giltig uträkning")
    exit()

antal_invånare = 26000
for _ in range(2019, aktuellt_år):
    antal_invånare = antal_invånare + antal_invånare * 0.007 - antal_invånare * 0.006 + 300 - 325
print(f"Antal invånare i början av {aktuellt_år} var {antal_invånare}")

# Lärdom: om man ska ha regler för en kod ska detta köras först. 
# För att avsluta innan man får ogiltigt input i koden. 

# Lärdom #2: ett ensamt "_" kan användas för att beskriva en variabel som man 
# inte kommer använda sig av. Till exempel här byttes "i" ut mot understreck då 
# "i" inte behövdes vidare. 


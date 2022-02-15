# På en mycket farlig arbetsplats erbjuds man följande lön: 
# första dagen tjänar man 1 öre och sedan fördubblas lönen varje dag. 
# Skriv ett program som räknar ut hur länge man behöver arbeta för att 
# tjäna ihop 10 miljoner kronor.

dagslön = 0.01
intjänad_lön = 0
slutlig_ackumulerad_lön = 10000000
dagar = 0

while intjänad_lön < slutlig_ackumulerad_lön:
    intjänad_lön = intjänad_lön + dagslön
    dagslön = dagslön * 2
    dagar = dagar + 1
    
print(f"För att tjäna ihop 10 miljoner måste man arbeta i {dagar} dagar.")

#Lärdom: ta ett trivialt tal och starta med det, så att man i huvudet kan 
# räkna ut vad som är fel. I det här fallet kan man byta ut 10 miljoner mot 
# ursprungsvärdet 0,01 för att loopen endast ska köras en gång. Detta gör det 
# enkelt att kontrollera sin kod. 

# Lärdom #2: kasta inte uträkningar i sjön. OBS: intjänad_lön = intjänad_lön + dagslön
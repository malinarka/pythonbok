personnummer = input("Skriv in ditt personnummer(10 siffror): ")

import datetime
dt = datetime.datetime.now()
datum = str(dt.date())

if  datum[5:7] == personnummer[2:4] and datum[8:10] == personnummer[4:6]:
    print("Grattis!")
else:
    print("Det är inte din födelsedag idag.")
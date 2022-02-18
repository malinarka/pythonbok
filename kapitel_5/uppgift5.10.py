import datetime

dt = datetime.datetime.now()

# Skriv ut dagens datum. 
d = dt.date()
dtext = str(d)
print(dtext)

# Skriv ut tiden. 
t = dt.time()
ttext= str(t)[:8]
print(ttext)
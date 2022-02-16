# Skriv ett program som läser in ett godtyckligt antal positiva tal. 
# När användaren skriver in ett negativt tal ska programmet skriva ut det 
# största och det minsta av de positiva talen. 

största = 0
minsta = 1.e300

while True: 
    tal = float(input("Skriv in ett tal: "))
    if tal < 0:
        break
    if tal > största:
        största = tal
    if tal < minsta: 
        minsta = tal
print("Största talet:", största)
print("Minsta talet:", minsta)

# # Skriv ett program som läser in ett godtyckligt antal positiva tal. 
# # När användaren skriver in ett negativt tal ska programmet skriva ut det 
# # största och det minsta av de positiva talen. 

# alla_tal = []
# while True: 
#     tal = float(input("Skriv in ett tal: "))
#     if tal < 0:
#         break
#     alla_tal.append(tal)

# if len(alla_tal) >= 1:
#     print("Största talet:", max(alla_tal))
#     print("Minsta talet:", min(alla_tal))
# else:
#     print("Knasboll!! Du skrev inte in ett enda tal större än noll!")

# Skriv ett program som läser in ett godtyckligt antal positiva tal. 
# När användaren skriver in ett negativt tal ska programmet skriva ut det 
# största och det minsta av de positiva talen. 

största = None
minsta = None

while True: 
    tal = float(input("Skriv in ett tal: "))
    if tal < 0:
        break

    if största == None:
        största = tal
        minsta = tal
    else:
        if tal > största:
            största = tal
        elif tal < minsta:
            minsta = tal
print("Största talet:", största)
print("Minsta talet:", minsta)

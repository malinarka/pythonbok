# Skriv ett program som läser in en text. Programmet ska undersöka om textens första och 
# sista bokstav är samma. 
# I den här uppgiften ska man lära sig att använda indexering. 

t = "här kommer min text" # OBS: programmet särskiljer små och stora bokstäver.

print(len(t))  # t innehåller 19 element

första_elementet = t[0]
sista_elemetet = t[18]

if första_elementet == sista_elemetet:
    print("Första och sista bokstaven är likadana.")
else: 
    print("Första och sista bokstaven är inte likadana.")

# Man kan även skriva enklare: 
# t = input("Skriv en text: ")
# if t[0] == t[len(t)-1]:
#   print("Lika")
# else: 
#   print("Inte lika")
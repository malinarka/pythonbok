# Skriv ett program som läser in en text som sedan översätts till rövarspråket. 
# Alla konsonanter dubbleras samt ett "o" placeras mellan de dubblerade
# konsonanterna. Vokaler och övriga tecken ändras ej. 

text = input("Skriv in en text som ska översättas till rövarspråk: ")
rövarspråket = " "
konsonanter = "bcdfghjklmnpqrstvwxyz"

for e in text:
    text_små_bokstäver = e.lower()
    if text_små_bokstäver in konsonanter:
        rövarspråket += text_små_bokstäver + "o" + text_små_bokstäver
else:
    rövarspråket += text_små_bokstäver

print(rövarspråket)

# Kod fungerar ej. Vet ej varför och vet egentligen inte 
# varför man skrivit denna kod. Kollat facit + Google.
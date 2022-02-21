text = input("Skriv in en medning men minst två ord: ")

lista_text = text.split(" ")

print(lista_text)
lista_text = filter(lista_text)

if len(lista_text) > 1:
    print(len(text))
    första_ordet = 
    print("Första ordet är")
else: 
    print("Meningen behöver fler ord.")

# eriks algoritm:
# 1. läs in en mening
# 2. dela upp strängen i en lista av strängar separerade av mellanslag
# 3. filtrera bort tomma sträng-element i listan med en filter funktion
#    - använd dig av en "är strängen inte tom" funktion som returnerar True/False (en predikatfunktion) utifrån om den är det
#    - använd dig av "filter" funktionen som tar predikatfunktionen och listan av strängar
# 4. tvinga resultatet av filter att bli en lista genom "list(<resultatet>)" (detta beövs p.g.a så kallad "lazy evaluation" - något du får lära dig om i fortsättningskurser)
# 5. räkna antalet ord i listan med len funktionen


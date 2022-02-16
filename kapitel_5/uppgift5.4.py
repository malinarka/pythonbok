# Undersök var sista vita tecknet finns i en text. 

s = input("Skriv in en text: ")
i = -1

for c in s[::-1]: 
    if c == " " or c == "\t":
        print(f"Sista vita tecknet på indexplats {i}.")
        break
    i = i - 1
else:
    print("Det finns inget vitt tecken i texten.")

    # Tänk på att man kan behöva googla fram sådant som man inte vet eller som man glömt. 
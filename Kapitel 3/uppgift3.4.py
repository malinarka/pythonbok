# Nästlade if-satser.

t = float(input("Temp? "))

if t <= 18:
    print("Det är kallt")
    print("Sätt på värmen")
    if t < 12:
        print("Sätt på jackan")
        if t < 5:
            print("Det är askallt, stanna alltid inomhus")
            if t < -2:
                print("Megakallt")
else:
    print("Det är varmt")
    if t >= 22:
        print("Stäng av värmen")
        if t >= 45:
            print("Stanna vid AC:n")
print("Det är", t, "grader")




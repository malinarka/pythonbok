# Skriv ett program som skriver ut en tabell för talen 1 till 12. 
# På varje rad i tabellen ska talet visas liksom talet i kvadrat
# och talet i kubik.

for i in range(1, 13):
    i_kvadrat = i ** 2
    i_kubik = i ** 3
    print(f"{i:6} {i_kvadrat:6} {i_kubik:6}")
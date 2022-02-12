user_provided_input = input("Skriv in ett tal: ")
print(f"Det här är talet du skrev in: {user_provided_input}")
square_length = float(user_provided_input)

square_area = square_length**2
square_circumference = 4 * square_length

print(f"Om vi låtsas att talet var sidlängden på en kvadrat, så blev arean: {square_area}, och omkretsen: {square_circumference}")

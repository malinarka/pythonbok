user_provided_info = input("Vad är priset på en vara ink moms? ")
print(f"Varans pris ink moms är (kr): {user_provided_info}")
varans_pris_ink_moms = float(user_provided_info)

given_momssats = input("Vilken momssats har den valda varan, svara i procent: ")
print(f"Varans momssats är {given_momssats}%")
momssats = float(given_momssats) / 100

varans_pris_exkl_moms = varans_pris_ink_moms / (1 + momssats)

print(f"Varans pris exkl moms är: {varans_pris_exkl_moms}")

momsens_värde = varans_pris_ink_moms - varans_pris_exkl_moms

print(f"Momsen är i detta fall: {momsens_värde}")


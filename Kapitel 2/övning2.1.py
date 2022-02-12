mätaren_idag = float(input("Mätarställning idag? "))
mätaren_för_1_år_sedan = float(input("Mätarställning för ett år sedan? "))

antal_körda_mil = mätaren_idag - mätaren_för_1_år_sedan

print("Antal körda mil:", antal_körda_mil)

antal_liter_bensin = float(input("Antal liter bensin? "))

förbrukning_per_mil = antal_liter_bensin / antal_körda_mil

print(f"Förbrukning per mil: {förbrukning_per_mil:.2f}")


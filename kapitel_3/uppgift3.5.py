# Satser och radstruktur

brevets_längd = float(input("Längd (mm): "))
brevets_bredd = float(input("Bredd (mm): "))
brevets_tjocklek = float(input("Tjocklek (mm): "))

if 140 <= brevets_längd <= 600 and brevets_tjocklek <= 100 and \
brevets_bredd >= 90 and brevets_bredd + brevets_tjocklek + brevets_längd <= 900:
    print("Brevet är tillåtet.")
else:
    print("Brevet är inte tillåtet.")

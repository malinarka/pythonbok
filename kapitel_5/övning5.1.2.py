mening = input("Skriv en mening med minst två ord: ")

antal_tecken = len(mening)
print(f"I texten finns {antal_tecken} tecken.")

mening_stripped = mening.strip()
första = mening_stripped.find(" ")
sista = mening_stripped.rfind(" ") + 1

första_ordet = mening[:första]
print(f"Första ordet är {första_ordet}.")

sista_ordet = mening[sista::]
print(f"Sista ordet är {sista_ordet}.")

from random import randint

tärning_1 = randint(1,6)
tärning_2 = randint(1,6)

print(f"Tärningarna gav värdena {tärning_1} och {tärning_2} ")

print("Summan av tärningarna är", tärning_1 + tärning_2)

# För att slippa importera hela modulen: "import random" 
# och sedan behöva skriva random.randint(a,b), 
# kan man endast imporera ent kommandot som man är ute efter. Alltså i
# det här fallet så kan man importera randint från modulen random 
# (from random import randint).
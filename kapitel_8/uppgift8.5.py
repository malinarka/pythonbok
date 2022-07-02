def primtal_eller_ej(pt):
    for i in range(2, pt):
        if pt % i == 0:
            return False
    return True


pt = int(input("Skriv in ett tal: "))
primtal = primtal_eller_ej(pt)
if primtal:
    print("Primtal")
else:
    print("Inte primtal")

# mål: primatal eller ej?
# algoritm, för talet 6
# 1. loopa över alla tal mellan 2-5
# 2. ifall något tal mellan 2-5 delade 6, returnera falskt
# 3. annars, returnera sant
# 6 => [2, 3] => 2 + 3 + 1 == 6?
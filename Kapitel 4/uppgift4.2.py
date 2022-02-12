n = int(input("n? "))

# n = 4 (tänk på ett konkret fall för att göra det mer förståbart)

summa = 0 # det här ska bli resultat och man bygger upp resultatet med varje loop
k = 1 # fyller funktionen att hålla index i loopen, alltså var i loopen man är


# 1 2 3 4 ...? (detta blir vad k har för värden)
# 1 4 9 16 ...? vad är detta? detta är k^2 (k**2, eller k*k)
# 1 + 4 + 9 + 16 ...? blir 30...?

while k <= n:
    summa = summa + k * k
    k = k + 1
print(summa)


# Man brukar använda i (står för index) istället för k. Om man har 
# flera sådana variabler brukar nästa kallas j..k...





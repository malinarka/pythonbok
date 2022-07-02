def nfak(n):
    """Skriver en funktion som ger fakulteten av n."""
    prod = 1
    for i in range(2, n+1):
        prod = prod * i
    return prod


n = int(input("Skriv in talet n: "))
fakulteten = nfak(n)
print(f"Svaret är {fakulteten}.")
# Prova lite hur en while-sats fungerar med olika värden
# på varibeln eller om man gör fel med intendering.

print("[", end="")
k = -4

while k < 10:
    print(f"{k:2}", end="")
    k = k + 2 # Om denna rad inte är indenderad kommer programmet köras i all evighet. k kommer då aldrig ta något annat värde än det första värdet.
print("]") # Om man intenderar denna rad kommer alla talen haman på egen rad med egan slutklamrar men endast den första komemr ha en startklammer. 


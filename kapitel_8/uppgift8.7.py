def beräkna_medelvärde(lista):
    medelvärde = sum(lista) / len(lista)
    return medelvärde

def beräkna_medelvärde_args(*args):
    medelvärde = sum(args) / len(args)
    return medelvärde


medelvärde_lista = beräkna_medelvärde([3, 5, 8, 10])
medelvärde_tupel = beräkna_medelvärde((4, 6, 2))
medelvärde_args_1 = beräkna_medelvärde_args(4, 6, 2)
medelvärde_args_2 = beräkna_medelvärde_args(4, 6, 2, 5)

print(f"Medelvärde lista = {medelvärde_lista}, medelvärde tupel = {medelvärde_tupel}")
print(f"Medelvärde lista = {medelvärde_args_1}, medelvärde tupel = {medelvärde_args_2}")

# Erik la till *args för att beskriva skillnader/likheter med vad jag gjort.
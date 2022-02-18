# Skriv ett program som läser in en text. 
# Programmet ska sedan ta bort alla blanka tecken (mellanslag) från texten och skriva ut resultatet. 

text = input("Skriv in en text: ")

text_utan_mellanslag = text.replace(" ", "")

print(text_utan_mellanslag)
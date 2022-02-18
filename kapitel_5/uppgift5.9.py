# Testa om texten är en palindrom. 

text = input("Skriv in en text: ")

text_utan_mellanslag = text.replace(" ", "")
text_baklänges = text_utan_mellanslag[::-1]

if text_utan_mellanslag == text_baklänges:
    print("palindrom")
else: 
    print("icke palindrom")
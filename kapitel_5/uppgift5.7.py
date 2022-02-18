# Gör om exemplet så att b kommer att innehålla födelsedagen enligt modellen dd/mm, dvs "14/03".

a = "   Erik Andersson 990314-2714   "

a = a.strip() # Tar bort de inledande och avslutande mellanslagen. 
m1 = a.rfind(" ") + 3 # Letar upp tredje indexet efter sista mellanslaget, alltså första månadstalettalet.
m2 = a.rfind(" ") + 5 # Letar upp andra månadstalet.
d1 = a.find("-") - 2 # Letar upp första dagstalet. Hoppar bakåt från "-". 
d2 = a.find("-") # Letar upp andra dagstalet. 
mm = a[m1:m2] 
dd = a[d1:d2]

print(dd + "/" + mm)

# Facit gjorde på helt annat sätt. 
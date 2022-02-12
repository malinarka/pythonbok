import math

a = float(input("Längd sida a: "))
b = float(input("Längd sida b: "))
V_grader = float(input("Vinkel i grader: "))

V_radianer = math.radians(V_grader)

c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(V_radianer))
e = 1e-10 # ett litet tal

if abs(a-b) < e and abs(a-c) < e and abs(b-c) < e:
    print("Triangeln är liksidig")
elif abs(a-b) < e or abs(a-c) < e or abs(b-c) < e:
    print("Triangeln är likbent")
else: 
    print("Triangeln är oliksidig")

# Svårare övning. Tog hjälp av facit för att lösa uppgiften.
# Det svåra var att jämföra med ett litet tal. 
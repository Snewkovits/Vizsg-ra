a = int(input("Adj meg egy számot! "))
b = int(input("Add meg a második számot! "))
uzenet = ""

if a >= 0 and b >= 0:
   uzenet = "A két szám közül egyik sem negatív"
elif a < 0 and b < 0:
   uzenet = "Mind a két szám negatív"
elif a < 0:
   uzenet = "A két szám közül az első negatív"
elif b < 0:
   uzenet = "A két szám közül a második negatív"

print(uzenet)
def hosszusag(oldalak):
   oldalak = int(oldalak)
   if oldalak > 150: return True
   else: return False

konyv_neve = input("Add meg a könyv címét! ")
while konyv_neve != "":
   könyv_oldalak = input("Add meg az oldalainak a számát! ")
   if hosszusag(könyv_oldalak): print(f"A(z) {konyv_neve} hosszú terjedelmű könyv")
   else: print(f"A(z) {konyv_neve} rövid terjedelmű könyv")
   konyv_neve = input("Add meg a könyv címét! ")
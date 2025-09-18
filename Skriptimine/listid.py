places = [] # Tühi list

places.append('Kehtna') #Lisa lõppu
places.append('Rapla') # Lisa lõppu
places[1:1] = ['Tallinn', 'Pärnu'] # Lisa Kehtna ja Rapla vahele
places.extend(['Viljandi', 'Tartu', 'Rapla']) # Lisab lõppu
places.insert(2, 'Are') #Lisab Tallinna ja Pärnu vahele

print(places)

# Kustutamine
places.remove('Rapla') # Esimene leitud
places.pop(6)   # Viimase kusutamine (7kokku!)
del places [2]  # Are kustutamine

print (places)

# Ülesanne : Lisa Rapla lõppu ja peale Pärnut
places.insert(3, 'Rapla') # peale Pärnut
places.extend(['Rapla'])  # Lõppu
print (places)

place = places[-1] # Muutuja saab väärtuseks listi viimase elemendi
index = places.index(place) # Mitmes element on Rapla (ainult üks!)
count = places.count(place) # Mitu Raplat on listis
print(index, count) # Väljund: 3 2
# Kas Rapla on nimekirjas?
if place in places:
    print(f'{place} on nimekirjas.')
# Koopia nimekirjast
list_copy = places.copy()
list_list = list(places)

print (places)
print (list_copy)
print (list_list)

list_copy.sort() # sorteerib A -> Z
list_list.sort(reverse=True ) # sorteerib Z -> A

print() # Tühi rida
print (list_copy)
print (list_list)

new_sorted_list = sorted(places, reverse=False) # sorteerib A -> Z
print(new_sorted_list)

# Tühjenda listi sisu
new_sorted_list.clear()
list_copy.clear()
list_list.clear()

print (new_sorted_list)
print (list_copy)
print (list_list)
print (places)

# Ülesanne: Väljasta listi places viimane element ilma [-1] kasutamata
print (places[len(places)-1])
print (places)

# Väljasta konsooli elemendi Pärnu keskmine täht trükitähena
print(places[2][2].upper())
city = places[2] #Element
char = city[2].upper() # Täht
print(char)

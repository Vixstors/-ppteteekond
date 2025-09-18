
import random

names = ['Mari', 'Anna', 'Villem', 'Jüri']

# Väljasta listis olevad nimed nime kaupa eraldi real.
for name in names:
    print(name)

print()
# Teist moodi väljastus
for x in range(len(names)):
    print(names[x], random.randint(1,122)) # Valib suvalise numbri nimede järgi


# Lihtsalt numbrid
for x in range(1, 5): #1, 2, 3, 4
    print(x, end= ' ')
print('\n') # Kaks reavahetust!

for x in range(0, 10, 2): # Paarisarvud
    print(x, end=' | ')
print('\n')

x = 0
while x < len(names):
    print(names[x])
    x += 1 # x = x + 1
print()
"""""

"""""
Väljasta listi nimed konsooli iga nimi eraldi real, kuid iga nime ees on järjekorra number. Järjekorra number algab ühega. Korrektne rida on järgnev:
1. Mari
2. Anna
3. Villem
4. Jüri


names = ['Mari', 'Anna', 'Villem', 'Jüri']
ages = [] # vanused

nr = 1
for name in names:
    age = random.randint(18, 65)
    ages.append(age) # lisab vanused listi
    print(nr, ".", name, "-", age, "aastat") # väljastus
    nr = nr + 1 # liidab järjekorrale juurde
print ("names:" , names)
print ("ages:", ages)



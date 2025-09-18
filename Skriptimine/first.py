# Import
from datetime import datetime

name = 'regnar heinsalu' # String ehk sõne
age = 25 # Täisarv (integer)
height = 1.79 #Ujukomaarv (Float)

print(name, age, height) # Väljastab kolm vääratust
# Kasutaja regnar heinsalu vanuses 25 aastat ja pikkusega 1.79 meetrit pikk
print(f'Kasutaja {name.title()} vanuses  {age} aastat ja pikkusega {height} meetrit pikk.')
print('kasutaja ' + name + ' vanuses ' + str(age)+ ' ja pikkusega ' + str(height))

# Arvutamine
birth_year = datetime.now().year - age # Jooksev aasta - vanus
print(birth_year)

name = name.title() # Korrasta nimi ja kasuta sama muutujat
print(name[1])      # Väljund nimelt 2 täht, loeb pärast [] olevat numbrit
print(name[1:5])    # Väljund: egna
print(name[7:])     # Väljund: Heinsalu (võtab tühiku arvesse samuti)
print(name[:6])     # Väljund: Regnar (võtab enne tühikut seda)
print(name[::-1])   # Väljund: ulasnieH rangeR

age = input('Sisesta vanus: ')
age = int(age)
if age < 1 or age > 122: # Kontrollib kas vanus on 1-122 vahemikus ja elif annab siis tingimuse teatud vanustele, ja väljas väljundi
        print ('Vanus on vales vahemikus (Lubatud on 1-122)')
elif age < 18:
    print('Alaealine')
elif age < 65:
    print('Tööealine')
elif age < 100:
    print('Pensionär')
else:
    print('Pikaealine')

place =input('Sisesta elukoht: ')
print(f'Sisestati: {place}')

if len (place) > 1 and len(place) <=7:
    print(f'Lühikese nimega koht {place.title()}')
elif len (place) >7:
    print (f'Pika nimega koht {place.title()}')
else:
     print('Nimi liiga lühike.')

# Väljasta muutujate andmetüübid
print(type(name))
print(type(age))
print(type(height))
print(type(place))

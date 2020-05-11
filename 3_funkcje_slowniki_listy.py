print('Hello')
a = round(3.1415, 2)
print(a)
x, y = 10, -7
greater_number = max(x, y)
lesser_number = min(x, y)
print(greater_number)
print(lesser_number)

print(abs(-121))

"""
Mając dane:
a, b, c = 12.4, 3, -50
oraz funkcje min(), abs(), print() wydrukuj wartość bezwzględną najmniejszej z nich. Czy potrafisz zrobić to w jednej linijce?
"""
a, b, c = 12.4, 3, -50

min_number = min(a, b, c)
abs_min_num = abs(min_number)
print(abs_min_num)

print(abs(min(a, b, c)))


first_name = 'adrian'
print(first_name.upper())
print(first_name.capitalize())


"""
Używając zmiennych
name, company = 'ricardo', 'fbi'
oraz method upper() i capitalize() wydrukuj zdanie:
"Officer Ricardo works for FBI"
"""
name, company = 'ricardo', 'fbi'
name_capitalized = name.capitalize()
company_upper = company.upper()
print(f"Officer {name_capitalized} works for {company_upper}")

print(f"Officer {name.capitalize()} works for {company.upper()}")

print('burek'.upper())


### LISTY ###
friends = ['Janek', 'Tomek', 'Kasia', 'Marta']
print(friends[0])
print(friends[2])
friends.append('Kazik')
print(friends[4])

print(len(friends))
print('Last element', friends[-1])
print('The one before last element', friends[-2])

friends[0] = 'Mirek'
print('My best friend:', friends[0])

print(friends[0:2])

"""
Stwórz listę swoich 5 ulubionych filmów
Wydrukuj długość listy
Wydrukuj 3 element tej listy
Dodaj na koniec listy element “Joker”
Wydrukuj ostatni element na liście
Wydrukuj dwa pierwsze elementy listy
"""

movies = ['Joker', 'LoTR', 'Inception', 'Godfather', 'Dexter']
print(len(movies))
print(movies[2])
movies.append('Dżoker')
print(movies[-1])
print(movies[0:2])


### SŁOWNIKI
friend = {
    'email': 'janek@example.com',
    'city': 'Warszawa',
    'age': 22,
    'has_pets': False,
    'favourite_bands': ['Slayer', 'Metallica'],
}
print(friend['age'])
friend['has_pets'] = True
friend['favourite_bands'].append('Anthrax')
friend['company'] = 'Fake Co.'

del friend['city']

print(friend)
print(type(friend['has_pets']))

friend['favourite_bands'].pop(1)
print(friend)

country = {
    'country_name': 'Italy',
    'language': 'Italian',
    'population': 60_360_000,
    'capital': 'Rome',
    'famous_people': ['Roberto Benigni', 'Leonardo da Vinci']
}

poland = {
    'country_name': 'Poland',
    'language': 'Polish',
    'population': 38_500_000,
    'capital': 'Kraków',
    'famous_people': ['Stefan Banach', 'Stanisław Lem',]
}
print(poland['famous_people'][-1])

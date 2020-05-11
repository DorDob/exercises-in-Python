import random
import uuid

# Zadanie 1
laws_of_robotics = [
    'A robot may not injure a human being or, through inaction, allow a human being to come to harm.',
    'A robot must obey the orders given it by human beings except where such orders would conflict with the First Law.',
    'A robot must protect its own existence as long as such protection does not conflict with the First or Second Laws.',
]
new_first_law = 'No machine may harm humanity; or, through inaction, allow humanity to come to harm.'
zeroth_law = 'A robot may not injure humanity, or, by inaction, allow humanity to come to harm.'

laws_of_robotics[0] = new_first_law
laws_of_robotics.insert(0, zeroth_law)
print('Four Laws Of Robotics')
for i, law in enumerate(laws_of_robotics):
    print(f'{i}. {law}')

# Zadanie 2
places = {
    'Aurora': {
        'age': 20_000,
        'description': 'Originally named New Earth, in later millennia the planet would be renamed "Aurora", which means "dawn", to signify the dawning of a new age for the Spacer culture.'
    },
    'Dahl': {
        'age': 1000,
        'description': 'Dahl is a district of Trantor. It is a small and rather down-trodden sector, which does not necessarily seem politically ambitious.'
    },
    'Cinna': {
        'age': 2000,
        'description': 'Cinna is the native planet of Dors Venabili.'
    },
    'Helicon': {
        'age': 10_000,
        'description': 'Helicon is the native planet of Hari Seldon. As the character says, Helicon is characterized by her Fight Abilities.'
    }
}

max_age = 0
oldest_name = None

for place, place_detail_dict in places.items():
    if place_detail_dict['age'] > max_age:
        max_age = place_detail_dict['age']
        pldest_place = place

print(
    f"The oldest place we know {oldest_name}. It's descrinption according to encyclopedia: {places[pldest_place]['description']}")

# Zadanie 3
# •	Znajdź z którego miejsca (origin) pochodzi najwięcej bohaterów
# •	Który z bohaterów ma największą średnią wiedzy z matematyki i historii (średnia kluczy math i history)
# •	Utwórz dwie nowe listy: robots i humans, które zawierać będą nazwy bohaterów z kluczami robot: True i False (odpowiednio)

heroes = [
    {
        'name': 'Hari Seldon',
        'robot': True,
        'math': 10,
        'history': 4,
        'origin': 'Helicon'
    },
    {
        'name': 'Yugo Amaryl',
        'robot': False,
        'math': 10,
        'history': 1,
        'origin': 'Dahl'
    },
    {
        'name': 'Dors Venabili',
        'robot': True,
        'math': 3,
        'history': 9,
        'origin': 'Cinna'
    },
    {
        'name': 'R. Daneel Olivaw',
        'robot': True,
        'math': 8,
        'history': 10,
        'origin': 'Aurora'
    },
    {
        'name': 'Raych Seldon',
        'robot': False,
        'math': 3,
        'history': 5,
        'origin': 'Dahl'
    },
]


# 	Znajdź z którego miejsca (origin) pochodzi najwięcej bohaterów
origin_count_dict = {}
for hero in heroes:
    if hero['origin'] in origin_count_dict.keys():
        origin_count_dict[hero['origin']] += 1
    else:
        origin_count_dict[hero['origin']] = 1
print(origin_count_dict)

sorted_origins_count = sorted(origin_count_dict, key=origin_count_dict.get, reverse=True)
print(sorted_origins_count[0])
# •	Który z bohaterów ma największą średnią wiedzy z matematyki i historii (średnia kluczy math i history)

# •	Utwórz dwie nowe listy: robots i humans, które zawierać będą nazwy bohaterów z kluczami robot: True i False (odpowiednio)

humans = [hero['name'] for hero in heroes if not hero['robot']]
robots = [hero['name'] for hero in heroes if hero['robot']]
print(humans, robots)



# Zadanie 4

# Używając w pokazany sposób funkcji random_planet(), która zwraca słownik opisujący szukaj tak długo, aż znajdziesz planetę spełniającą następujące warunki:
# •	has_water o wartości True
# •	oxygen_percentage większe od 20 a maksymalnie 25
# •	Is_solid o wartości True
# TIP: https://www.w3schools.com/python/python_while_loops.asp

def random_planet():
    return {
        'name': f'planet{uuid.uuid4()}',
        'has_water': random.choice((True, False,)),
        'oxygen_percentage': random.randint(0, 100),
        'is_solid': random.choice((True, False,)),
    }


perfect_planet, my_planet = False, {}
while not perfect_planet:
    my_planet = random_planet()
#    print(f'Random planet:{my_planet}')
    perfect_planet = my_planet['has_water'] and my_planet['is_solid'] and (20 < my_planet['oxygen_percentage'] <= 25)
print(my_planet)

# INACZEJ
my_planet = random_planet()
while not (my_planet['has_water'] and my_planet['is_solid'] and (20 <= my_planet['oxygen_percentage'] <= 25)):
    my_planet = random_planet()
print(my_planet)
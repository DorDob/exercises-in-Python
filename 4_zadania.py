import random
import datetime

# Listy zawierające dane do losowania
female_fnames = ['Kate', 'Agnieszka', 'Anna', 'Maria', 'Joss', 'Eryka']
male_fnames = ['James', 'Bob', 'Jan', 'Hans', 'Orestes', 'Saturnin']
surnames = ['Smith', 'Kowalski', 'Yu', 'Bona', 'Muster', 'Skinner', 'Cox', 'Brick', 'Malina']
countries = ['Poland', 'United Kingdom', 'Germany', 'France', 'Other']

# Przykład jak można losować imię z listy

people_list = []

current_year = datetime.datetime.now().year

for p in range(0, 10):
    firstname = random.choice(female_fnames) if p > 5 else random.choice(male_fnames)
    lastname = random.choice(surnames)
    country = random.choice(countries)
    age = random.randint(5, 45)
    people_list.append(
        {
            'firstname': firstname,
            'lastname': lastname,
            'country': country,
            'mail': f'{firstname}.{lastname}@example.com'.lower,
            'age': age,
            'adult': age > 17,
            'birth_year': current_year - age
        }
    )

for b in people_list:
    print(f"Hi! I'm {b['firstname']} {b['lastname']}. I come from {b['country']} and I was born in {b['birth_year']}")


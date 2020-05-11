# Zadanie 1

print('-' * 10, 'Exercise 1', '-' * 10)
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print(len(primes))
primes.append(31)
primes_four = primes[0:4]

print(sum(primes))
print(sum(primes_four))
print(sum(primes) / sum(primes_four))

# Zadanie 2

print('\n', '-' * 10, 'Exercise 2', '-' * 10)
random_numbers = [22, 3.3, -2, 5, 701, 42, -120, 35, 69.9, 123, -444, 0.0, 0]
print(sorted(random_numbers))

# lub:
sorted_numbers = sorted(random_numbers)
print(sorted_numbers)

# Zadanie 3

print('\n', '-' * 10, 'Exercise 2', '-' * 10)
band = {
    'name': 'The Mars Volta',
    'country': 'USA',
    'albums': ['De-Loused In Comatorium', 'Frances The Mute'],
    'start_year': 1999,
    'albums_sold': 10_000_000
}
band['activ'] = False
band['albums'].append('Bedlam in Goliath')
print(band['albums'])
band['activ'] = True
band['albums_sold'] += 1
print(band['albums_sold'])
print(band['activ'])

# Zadanie 4

print('\n', '-' * 10, 'Exercise 2', '-' * 10)

band2 = {
    'name': 'Opeth',
    'country': 'Sweden',
    'albums': ['Blackwater Park', 'Watershed'],
    'start_year': 1989,
    'albums_sold': 30_000_000
}
band3 = {
    'name': 'Porcupine Tree',
    'country': 'UK',
    'albums': ['In Absentia', 'Deadwing'],
    'start_year': 1990,
    'albums_sold': 50_000_000
}
print(band3['country'])
print(band2['albums'][0])
print(band['activ'])

#lub
# bands = [band, band2, band3]
# print(bands[-1]['country'])
# print(bands[1]['albums'][0])
# print(bands[0]['active'])

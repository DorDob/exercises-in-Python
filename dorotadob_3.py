# Zadanie 1
# 1.	Zdefiniuj listę “primes” zawierającą 10 kolejnych liczb pierwszych zaczynając od 2 (https://www.matemaks.pl/liczby-pierwsze.html)
# 2.	Wydrukuj długość tej listy
# 3.	Dodaj na koniec listy 11tą liczbę pierwszą
# 4.	Stwórz drugą listę “primes_four” zawierającą pierwsze 4 elementy “primes”
# 5.	Wydrukuj ostatni z elementów “primes_four”
# 6.	Używając funkcji sum() (https://docs.python.org/3/library/functions.html#sum) policz sumę “primes” i “primes_four”. Ile razy większa jest suma “primes” od “primes_four”?

print('-' * 10, 'Exercise 1', '-' * 10)
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print(len(primes))
primes.append(31)
primes_four = primes[0:4]

print(sum(primes))
print(sum(primes_four))
print(sum(primes) / sum(primes_four))

# Zadanie 2
# 1.	Zapisz do zmiennej listę
# [22, 3.3, -2, 5, 701, 42, -120, 35, 69.9, 123, -444, 0.0, 0]
# 2.	Używając funkcji sorted() (https://docs.python.org/3/library/functions.html#sorted) przypisz do innej zmiennej posortowaną listę z pierwszego punktu
# 3.	Wydrukuj pierwszy i ostatni element nowej listy

print('\n', '-' * 10, 'Exercise 2', '-' * 10)
random_numbers = [22, 3.3, -2, 5, 701, 42, -120, 35, 69.9, 123, -444, 0.0, 0]
print(sorted(random_numbers))
# Adriana :
sorted_numbers = sorted(random_numbers)
print(sorted_numbers)

# Zadanie 3
# 1.	Stwórz słownik opisujący ulubiony zespół (albo jakikolwiek zespół), który zawiera następujące klucze:
# a.	name - nazwa zespołu
# b.	country – kraj pochodzenia
# c.	albums – lista tytułów albumów
# d.	start_year - rok rozpoczęcia działalności
# e.	albums_sold – liczba sprzedanych albumów
# 2.	Dodaj do słownika nowy klucz: active – opisujący czy zespol jest aktywny (prawda/fałsz)
# 3.	Dodaj do klucza albums nowy album na koniec listy
# 4.	Wydrukuj wszystkie albumy
# 5.	Zmien wartość active na przeciwną
# 6.	Zwiększ wartość sprzedanych albumów o 1 (gratuluję zakupu!)

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
# 1.	W zmiennej “bands” stwórz listę 3 zespołów opisanych słownikami z zadania 3
# 2.	Wydrukuj kraj pochodzenia ostatniego zespołu
# 3.	Wydrukuj pierwszy album drugiego zespołu
# 4.	Wydrukuj stan aktywności (klucz “active”) pierwszego zespołu

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

#Adriana
bands = [band, band2, band3]
print(bands[-1]['country'])
print(bands[1]['albums'][0])
print(bands[0]['active'])

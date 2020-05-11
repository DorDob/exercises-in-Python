print('Today is friday')

is_day = False
if is_day:
    print('Sun is shining')
else:
    print('Have a good night!')

print('Let\'s have a beer')

temp_celsius = 0
pressure_hpa = 1013
if temp_celsius == 0 and pressure_hpa == 1013:
    print('In water freezing point')
else:
    print('Not in water freezing point')

performance = 115.0

if performance >= 115:
    print('Excellent!')
elif performance >= 105:
    print('Very good!')
elif performance >= 95:
    print('So So :(')
else:
    print('Not enough! Work harder!')

price = 100
cash_amount = 80
free_product = False

if free_product:
    print('You get the product for free!')
elif cash_amount >= price:
    print('You can buy this product.')
else:
    N = price - cash_amount
    print('You need', N, 'more cash buy this product')


# Pętle
for i in range(0, 100):
    print(i ** 2)

for k in range(1, 101):
    print(k ** 2)

for x in range(11, 28):
    print(x ** 3)

for i in range(0, 10):
    print('Python jest super!')

for _ in range(10):
    print('Python jest super!')

my_list = [1, 3, 5, 7, 9, 11]

for l in my_list:
    print(l, l * 4)

numbers = [3, 12, 55, 178, 1300, 6789, 19200]
for n in numbers:
    print(n * 3)

names = ['adam', 'monika', 'janek']
for name in names:
    print(name.capitalize())

login = 'admin1234super567'
for c in login:
    if c.isdigit():
        print(c)
    else:
        print(c.upper())

for n in numbers:
    if n % 3 == 0:
        print(n)
